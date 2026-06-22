"""
T47 – Regresjon på CLIP-tags + manuelle ratings → weights_tags.json.

Ridge-regresjon pga mange features (tags) og begrenset antall manuelle ratings.
Kjør build_scores.py etterpå for å regenerere scores_total.csv.

Bruk:
    .venv/Scripts/python scripts/calibrate_tags.py --dry-run
    .venv/Scripts/python scripts/calibrate_tags.py
    .venv/Scripts/python scripts/calibrate_tags.py --alpha 0.5
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

import numpy as np
from sklearn.linear_model import Ridge

DATA_DIR         = Path(__file__).resolve().parents[1] / "data"
SCORES_CLIP      = DATA_DIR / "scores_clip.csv"
SCORES_MANUAL    = DATA_DIR / "scores_manual.csv"
TAG_WEIGHTS_JSON = DATA_DIR / "weights_tags.json"


def _read_clip() -> dict[str, dict[str, float]]:
    clip: dict[str, dict[str, float]] = {}
    with SCORES_CLIP.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            clip.setdefault(row["filnavn"], {})[row["tag"]] = float(row["clip_score"])
    return clip


def _read_manual() -> dict[str, float]:
    manual: dict[str, float] = {}
    with SCORES_MANUAL.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            try:
                if row["score"].strip():
                    manual[row["filnavn"]] = float(row["score"])
            except (ValueError, KeyError):
                pass
    return manual


def main() -> None:
    parser = argparse.ArgumentParser(description="Regresjon på CLIP-tags (T47)")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--alpha", type=float, default=1.0,
                        help="Ridge regularisering (default 1.0)")
    args = parser.parse_args()

    if not SCORES_CLIP.exists():
        print(f"FEIL: {SCORES_CLIP.name} finnes ikke – kjør score_clip.py (T46) først.")
        sys.exit(1)

    clip   = _read_clip()
    manual = _read_manual()

    all_tags   = sorted({tag for tags in clip.values() for tag in tags})
    tag_index  = {tag: i for i, tag in enumerate(all_tags)}

    joined = [(fn, clip[fn], manual[fn]) for fn in manual if fn in clip]
    if len(joined) < 10:
        print(f"FEIL: Bare {len(joined)} bilder i join – for få til regresjon.")
        sys.exit(1)

    X = np.zeros((len(joined), len(all_tags)))
    y = np.array([score for _, _, score in joined])
    for i, (_, tag_scores, _) in enumerate(joined):
        for tag, score in tag_scores.items():
            if tag in tag_index:
                X[i, tag_index[tag]] = score

    model = Ridge(alpha=args.alpha, fit_intercept=True)
    model.fit(X, y)
    r2 = model.score(X, y)

    coefs = sorted(zip(all_tags, model.coef_), key=lambda x: x[1], reverse=True)
    residuals = y - model.predict(X)

    print(f"\n{'='*55}")
    print(f"Treningssett: {len(joined)} bilder, {len(all_tags)} tags")
    print(f"R²:           {r2:.4f}  (alpha={args.alpha})")
    print(f"\nTopp 15 positive tags (interessant innhold):")
    for tag, coef in coefs[:15]:
        print(f"  {tag:35s}  {coef:+.4f}")
    print(f"\nTopp 15 negative tags (uinteressant innhold):")
    for tag, coef in coefs[-15:]:
        print(f"  {tag:35s}  {coef:+.4f}")
    print(f"\nResiduals – std: {residuals.std():.3f}  max|e|: {np.abs(residuals).max():.3f}")
    print(f"{'='*55}\n")

    if not args.dry_run:
        weights = {
            "intercept": float(model.intercept_),
            **{tag: float(coef) for tag, coef in zip(all_tags, model.coef_)},
        }
        TAG_WEIGHTS_JSON.write_text(
            json.dumps(weights, indent=2, ensure_ascii=False), encoding="utf-8"
        )
        print(f"Tag-vekter lagret: {TAG_WEIGHTS_JSON}")
        print(f"Kjør nå: .venv/Scripts/python scripts/build_scores.py")
    else:
        print("Dry-run – ingen filer skrevet.")


if __name__ == "__main__":
    main()
