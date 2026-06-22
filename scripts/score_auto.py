"""
T42 – Råscore alle bilder og skriv data/scores_auto.csv.

Append-only – én rad per bilde, aldri overskrevet.
Normalisering og total beregnes av build_scores.py (T48).

Bruk:
    .venv/Scripts/python scripts/score_images.py             # score nye bilder
    .venv/Scripts/python scripts/score_images.py --limit 10  # test med 10 bilder
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from scoring.sharpness import sharpness_score
from scoring.exposure import exposure_score
from scoring.brisque import _raw_brisque
from scoring.musiq import _raw_musiq

PROCESSED_DIR = Path(__file__).resolve().parents[2] / "temp" / "bilder" / "processed"
SCORES_AUTO = Path(__file__).resolve().parents[1] / "data" / "scores_auto.csv"

COLUMNS = ["filnavn", "sharpness_raw", "exposure_raw", "brisque_raw", "musiq_raw"]


def _read_existing() -> set[str]:
    if not SCORES_AUTO.exists():
        return set()
    with SCORES_AUTO.open(newline="", encoding="utf-8") as f:
        return {row["filnavn"] for row in csv.DictReader(f)}


def _append_row(row: dict) -> None:
    SCORES_AUTO.parent.mkdir(parents=True, exist_ok=True)
    write_header = not SCORES_AUTO.exists()
    with SCORES_AUTO.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS)
        if write_header:
            writer.writeheader()
        writer.writerow(row)


def main() -> None:
    parser = argparse.ArgumentParser(description="Råscore alle bilder (T42)")
    parser.add_argument("--limit", type=int, default=None,
                        help="Antall bilder å score (test-modus)")
    args = parser.parse_args()

    if not PROCESSED_DIR.exists():
        print(f"FEIL: Bildemapp finnes ikke: {PROCESSED_DIR}")
        sys.exit(1)

    existing = _read_existing()
    images = sorted(PROCESSED_DIR.glob("*.jpg"), reverse=True)
    if args.limit:
        images = images[:args.limit]

    new_images = [img for img in images if img.name not in existing]
    print(f"{len(images)} bilder funnet, {len(existing)} allerede scoret, {len(new_images)} nye.")

    if not new_images:
        print("Ingenting å gjøre. Kjør build_scores.py for å oppdatere scores_total.csv.")
        return

    for i, img in enumerate(new_images, 1):
        sharp = sharpness_score(img)
        exp   = exposure_score(img)
        brisq = _raw_brisque(img)
        musiq = _raw_musiq(img)

        row = {
            "filnavn":      img.name,
            "sharpness_raw": "" if sharp is None else f"{sharp:.4f}",
            "exposure_raw":  "" if exp   is None else f"{exp:.6f}",
            "brisque_raw":   "" if brisq is None else f"{brisq:.4f}",
            "musiq_raw":     "" if musiq is None else f"{musiq:.4f}",
        }
        _append_row(row)
        print(f"  [{i}/{len(new_images)}] {img.name}: "
              f"sharp={row['sharpness_raw']}  exp={row['exposure_raw']}  "
              f"brisque={row['brisque_raw']}  musiq={row['musiq_raw']}")

    print(f"\nFerdig. Kjør build_scores.py for å regenerere scores_total.csv.")


if __name__ == "__main__":
    main()
