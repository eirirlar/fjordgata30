"""
T42 – Score alle bilder og skriv scripts/scoring/scores.csv.

To pass:
  Pass 1 (råscoring):     kall sharpness_score, exposure_score, _raw_brisque,
                           _raw_musiq for hvert bilde uten råscore i CSV.
                           Idempotent – bilder med eksisterende råscore hoppes over.
  Pass 2 (normalisering):  beregn p5/p95 per metrikk, normaliser til 1–10,
                           skriv normaliserte kolonner tilbake til CSV.

Bruk:
    .venv/bin/python3 scripts/score_images.py             # alle bilder
    .venv/bin/python3 scripts/score_images.py --limit 10  # test med 10 bilder
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))

from scoring.sharpness import sharpness_score
from scoring.exposure import exposure_score
from scoring.brisque import _raw_brisque
from scoring.musiq import _raw_musiq

PROCESSED_DIR = Path(__file__).resolve().parents[2] / "temp" / "bilder" / "processed"
SCORES_CSV = Path(__file__).resolve().parent / "scoring" / "scores.csv"

COLUMNS = [
    "filnavn",
    "sharpness_raw", "exposure_raw", "brisque_raw", "musiq_raw",
    "sharpness", "exposure", "brisque", "musiq",
    "total",
]

P_LOW = 5
P_HIGH = 95


def _read_csv() -> dict[str, dict]:
    rows: dict[str, dict] = {}
    if not SCORES_CSV.exists():
        return rows
    with SCORES_CSV.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            rows[row["filnavn"]] = row
    return rows


def _write_csv(rows: dict[str, dict]) -> None:
    SCORES_CSV.parent.mkdir(parents=True, exist_ok=True)
    with SCORES_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS, extrasaction="ignore")
        writer.writeheader()
        for row in rows.values():
            writer.writerow(row)


def _pass1(images: list[Path], existing: dict[str, dict]) -> dict[str, dict]:
    rows = dict(existing)
    new_count = sum(1 for img in images
                    if img.name not in rows or not rows[img.name].get("sharpness_raw"))
    n = len(images)
    if new_count == 0:
        for i, img in enumerate(images, 1):
            print(f"  [{i}/{n}] {img.name} SKIPPED")
        print(f"Pass 1: alle {n} bilder allerede scoret – ingenting å gjøre.")
        return rows

    print(f"Pass 1: {n} bilder ({new_count} nye, {n - new_count} hoppes over) …")

    # Nye rader invaliderer tidligere normalisering – nullstill for alle
    had_normalized = sum(1 for row in rows.values() if row.get("sharpness"))
    for row in rows.values():
        row["sharpness"] = row["exposure"] = row["brisque"] = row["musiq"] = row["total"] = ""
    if had_normalized:
        print(f"  Fjerner normalisering fra {had_normalized} eksisterende rader (vil reberegnes i Pass 2).")
    _write_csv(rows)
    for i, img in enumerate(images, 1):
        if img.name in rows and rows[img.name].get("sharpness_raw"):
            print(f"  [{i}/{n}] {img.name} SKIPPED")
            continue

        sharp = sharpness_score(img)
        exp = exposure_score(img)
        brisq = _raw_brisque(img)
        musiq = _raw_musiq(img)

        row = {
            "filnavn": img.name,
            "sharpness_raw": "" if sharp is None else f"{sharp:.4f}",
            "exposure_raw":  "" if exp   is None else f"{exp:.6f}",
            "brisque_raw":   "" if brisq is None else f"{brisq:.4f}",
            "musiq_raw":     "" if musiq is None else f"{musiq:.4f}",
            "sharpness": "", "exposure": "", "brisque": "", "musiq": "", "total": "",
        }
        rows[img.name] = row

        print(f"  [{i}/{n}] {img.name}: "
              f"sharp={row['sharpness_raw']}  "
              f"exp={row['exposure_raw']}  "
              f"brisque={row['brisque_raw']}  "
              f"musiq={row['musiq_raw']}")

        _write_csv(rows)

    return rows


def _normalize(raw: float, p5: float, p95: float, invert: bool) -> float:
    if p95 == p5:
        return 5.0
    score = (10.0 - 9.0 * (raw - p5) / (p95 - p5)) if invert \
        else (1.0 + 9.0 * (raw - p5) / (p95 - p5))
    return max(1.0, min(10.0, score))


def _pass2(rows: dict[str, dict]) -> dict[str, dict]:
    metrics = {
        "sharpness": ("sharpness_raw", False),
        "exposure":  ("exposure_raw",  True),
        "brisque":   ("brisque_raw",   True),
        "musiq":     ("musiq_raw",     False),
    }

    percentiles: dict[str, tuple[float, float]] = {}
    for col, (raw_col, _) in metrics.items():
        vals = [float(row[raw_col]) for row in rows.values()
                if row.get(raw_col)]
        if len(vals) < 2:
            print(f"Pass 2: for få verdier for {col} ({len(vals)}) – normalisering utsatt.")
            return rows
        p5 = float(np.percentile(vals, P_LOW))
        p95 = float(np.percentile(vals, P_HIGH))
        percentiles[col] = (p5, p95)
        print(f"  {col}: p{P_LOW}={p5:.3f}  p{P_HIGH}={p95:.3f}  (n={len(vals)})")

    for row in rows.values():
        norm_vals = []
        for col, (raw_col, invert) in metrics.items():
            v = row.get(raw_col)
            if v:
                raw = float(v)
                p5, p95 = percentiles[col]
                n = _normalize(raw, p5, p95, invert)
                row[col] = f"{n:.2f}"
                norm_vals.append(n)
            else:
                row[col] = ""
        row["total"] = f"{sum(norm_vals)/len(norm_vals):.2f}" if norm_vals else ""

    _write_csv(rows)
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description="Score alle bilder (T42)")
    parser.add_argument("--limit", type=int, default=None,
                        help="Antall bilder å score (test-modus, kun Pass 1)")
    parser.add_argument("--pass", dest="only_pass", type=int, choices=[1, 2], default=None,
                        help="Kjør bare Pass 1 (råscoring) eller Pass 2 (normalisering). "
                             "Utelatt = kjør begge.")
    args = parser.parse_args()

    if not PROCESSED_DIR.exists():
        print(f"FEIL: Bildemapp finnes ikke: {PROCESSED_DIR}")
        sys.exit(1)

    existing = _read_csv()

    if args.only_pass != 2:
        images = sorted(PROCESSED_DIR.glob("*.jpg"), reverse=True)
        if args.limit:
            images = images[: args.limit]
            print(f"Test-modus: {len(images)} bilder (nyeste først)")
        existing = _pass1(images, existing)

    if args.only_pass != 1:
        print("\nPass 2: normaliserer alle rader …")
        existing = _pass2(existing)

    print(f"\nFerdig. {len(existing)} rader i {SCORES_CSV}")


if __name__ == "__main__":
    main()
