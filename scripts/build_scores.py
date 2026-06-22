"""
T48 – Bygg scores_total.csv fra alle kildefiler.

Les scores_auto.csv, normaliser råscorer, beregn total per bilde.
Dette er den eneste filen som regenereres fullt ut – alle kildefiler forblir urørt.

Valgfrie kildefiler (brukes automatisk hvis de finnes):
  weights_combined.json – kombinert modell, auto + tags (T50) – prioriteres
  weights_auto.json     – regresjonskoeffisienter for auto-metrikker (T41)
  scores_clip.csv       – CLIP-scorer per tag per bilde (T46)
  weights_tags.json     – regresjonskoeffisienter per tag (T47)

Bruk:
    .venv/Scripts/python scripts/build_scores.py
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

import numpy as np

SCORING_DIR  = Path(__file__).resolve().parent / "scoring"
SCORES_AUTO  = SCORING_DIR / "scores_auto.csv"
SCORES_CLIP  = SCORING_DIR / "scores_clip.csv"
SCORES_TOTAL = SCORING_DIR / "scores_total.csv"
WEIGHTS_JSON     = SCORING_DIR / "weights_auto.json"
TAG_WEIGHTS_JSON = SCORING_DIR / "weights_tags.json"
WEIGHTS_COMBINED = SCORING_DIR / "weights_combined.json"

P_LOW, P_HIGH = 5, 95

AUTO_METRICS = {
    "sharpness": ("sharpness_raw", False),
    "exposure":  ("exposure_raw",  True),
    "brisque":   ("brisque_raw",   True),
    "musiq":     ("musiq_raw",     False),
}

OUT_COLS = ["filnavn", "sharpness", "exposure", "brisque", "musiq", "tag_score", "total"]


def _normalize(raw: float, p5: float, p95: float, invert: bool) -> float:
    if p95 == p5:
        return 5.0
    score = (10.0 - 9.0 * (raw - p5) / (p95 - p5)) if invert \
        else (1.0 + 9.0 * (raw - p5) / (p95 - p5))
    return max(1.0, min(10.0, score))


def _read_auto() -> dict[str, dict]:
    rows = {}
    with SCORES_AUTO.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            rows[row["filnavn"]] = row
    return rows


def _read_clip() -> dict[str, dict[str, float]]:
    if not SCORES_CLIP.exists():
        return {}
    clip: dict[str, dict[str, float]] = {}
    with SCORES_CLIP.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            clip.setdefault(row["filnavn"], {})[row["tag"]] = float(row["clip_score"])
    return clip


def main() -> None:
    print(f"Leser {SCORES_AUTO.name} …")
    rows = _read_auto()
    print(f"  {len(rows)} bilder")

    # Beregn p5/p95 per metrikk
    percentiles: dict[str, tuple[float, float]] = {}
    for col, (raw_col, _) in AUTO_METRICS.items():
        vals = [float(r[raw_col]) for r in rows.values() if r.get(raw_col)]
        if len(vals) < 2:
            print(f"FEIL: For få verdier for {col} ({len(vals)}).")
            return
        p5  = float(np.percentile(vals, P_LOW))
        p95 = float(np.percentile(vals, P_HIGH))
        percentiles[col] = (p5, p95)
        print(f"  {col}: p{P_LOW}={p5:.3f}  p{P_HIGH}={p95:.3f}")

    # Last combined-modell (prioriteres hvis den finnes)
    combined_weights = None
    if WEIGHTS_COMBINED.exists():
        combined_weights = json.loads(WEIGHTS_COMBINED.read_text(encoding="utf-8"))
        print(f"Kombinert modell lastet fra {WEIGHTS_COMBINED.name}")

    # Last separate vekter (fallback)
    weights = None
    if WEIGHTS_JSON.exists():
        weights = json.loads(WEIGHTS_JSON.read_text(encoding="utf-8"))
        if not combined_weights:
            print(f"Vekter lastet fra {WEIGHTS_JSON.name}")

    # Last CLIP og tag-vekter
    clip_rows = _read_clip()
    tag_weights = None
    if TAG_WEIGHTS_JSON.exists() and clip_rows:
        tag_weights = json.loads(TAG_WEIGHTS_JSON.read_text(encoding="utf-8"))
        if not combined_weights:
            print(f"Tag-vekter lastet fra {TAG_WEIGHTS_JSON.name} ({len(tag_weights)-1} tags)")

    out_rows = []
    for fn, row in rows.items():
        norm: dict[str, float] = {}
        for col, (raw_col, invert) in AUTO_METRICS.items():
            v = row.get(raw_col)
            if v:
                p5, p95 = percentiles[col]
                norm[col] = _normalize(float(v), p5, p95, invert)

        if not norm:
            continue

        # Auto-score (alltid beregnet for kolonner i output)
        if weights:
            auto_score = weights["intercept"] + sum(
                weights.get(c, 0) * v for c, v in norm.items()
            )
            auto_score = max(1.0, min(10.0, auto_score))
        else:
            auto_score = sum(norm.values()) / len(norm)

        # Tag-score (alltid beregnet for kolonner i output)
        tag_score_str = ""
        if tag_weights and fn in clip_rows:
            ts = tag_weights.get("intercept", 0) + sum(
                tag_weights.get(tag, 0) * score
                for tag, score in clip_rows[fn].items()
            )
            tag_score_str = f"{max(1.0, min(10.0, ts)):.2f}"

        # Total – combined-modell hvis tilgjengelig, ellers 50/50
        if combined_weights and fn in clip_rows:
            feats = combined_weights["features"]
            raw_total = combined_weights["intercept"] + sum(
                ((norm.get(name) or clip_rows[fn].get(name, 0)) - feats[name]["mean"])
                / feats[name]["std"] * feats[name]["coef"]
                for name in feats
                if feats[name]["std"] > 0
            )
            total = max(1.0, min(10.0, raw_total))
        elif tag_score_str:
            total = (auto_score + float(tag_score_str)) / 2
        else:
            total = auto_score

        out_rows.append({
            "filnavn":   fn,
            **{col: f"{norm[col]:.2f}" if col in norm else "" for col in AUTO_METRICS},
            "tag_score": tag_score_str,
            "total":     f"{total:.2f}",
        })

    with SCORES_TOTAL.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=OUT_COLS)
        writer.writeheader()
        writer.writerows(out_rows)

    print(f"\nFerdig. {SCORES_TOTAL.name}: {len(out_rows)} rader.")


if __name__ == "__main__":
    main()
