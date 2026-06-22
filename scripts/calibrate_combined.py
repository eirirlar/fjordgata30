"""
T50 – Kombinert Ridge-regresjon på auto-metrikker + CLIP-tags → weights_combined.json.

Auto-metrikker normaliseres til 1–10 med p5/p95 (samme som build_scores.py).
Alle 723 features skaleres deretter med StandardScaler før Ridge, siden
auto-metrikker (1–10) og CLIP-scores (~0.1–0.4) er på ulike skalaer.

Bruk:
    .venv/Scripts/python scripts/calibrate_combined.py --dry-run
    .venv/Scripts/python scripts/calibrate_combined.py
    .venv/Scripts/python scripts/calibrate_combined.py --alpha 0.5
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

import numpy as np
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler

SCORING_DIR      = Path(__file__).resolve().parent / "scoring"
SCORES_AUTO      = SCORING_DIR / "scores_auto.csv"
SCORES_CLIP      = SCORING_DIR / "scores_clip.csv"
SCORES_MANUAL    = SCORING_DIR / "scores_manual.csv"
WEIGHTS_COMBINED = SCORING_DIR / "weights_combined.json"

P_LOW, P_HIGH = 5, 95

AUTO_METRICS = {
    "sharpness": ("sharpness_raw", False),
    "exposure":  ("exposure_raw",  True),
    "brisque":   ("brisque_raw",   True),
    "musiq":     ("musiq_raw",     False),
}


def _normalize(raw: float, p5: float, p95: float, invert: bool) -> float:
    if p95 == p5:
        return 5.0
    score = (10.0 - 9.0 * (raw - p5) / (p95 - p5)) if invert \
        else (1.0 + 9.0 * (raw - p5) / (p95 - p5))
    return max(1.0, min(10.0, score))


def _read_auto_normalized() -> dict[str, dict[str, float]]:
    rows: dict[str, dict] = {}
    with SCORES_AUTO.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            rows[row["filnavn"]] = row

    percentiles: dict[str, tuple[float, float]] = {}
    for col, (raw_col, _) in AUTO_METRICS.items():
        vals = [float(r[raw_col]) for r in rows.values() if r.get(raw_col)]
        percentiles[col] = (float(np.percentile(vals, P_LOW)),
                            float(np.percentile(vals, P_HIGH)))

    result: dict[str, dict[str, float]] = {}
    for fn, row in rows.items():
        norm = {}
        for col, (raw_col, invert) in AUTO_METRICS.items():
            v = row.get(raw_col)
            if v:
                p5, p95 = percentiles[col]
                norm[col] = _normalize(float(v), p5, p95, invert)
        if len(norm) == len(AUTO_METRICS):
            result[fn] = norm
    return result


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
    parser = argparse.ArgumentParser(description="Kombinert Ridge-regresjon (T50)")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--alpha", type=float, default=100.0)
    args = parser.parse_args()

    for f in (SCORES_AUTO, SCORES_CLIP, SCORES_MANUAL):
        if not f.exists():
            print(f"FEIL: {f.name} finnes ikke.")
            sys.exit(1)

    auto   = _read_auto_normalized()
    clip   = _read_clip()
    manual = _read_manual()

    all_tags = sorted({tag for tags in clip.values() for tag in tags})

    joined = [fn for fn in manual if fn in auto and fn in clip]
    if len(joined) < 10:
        print(f"FEIL: Bare {len(joined)} bilder i join – for få til regresjon.")
        sys.exit(1)

    auto_cols  = list(AUTO_METRICS.keys())
    feat_names = auto_cols + all_tags
    tag_index  = {tag: i for i, tag in enumerate(all_tags)}

    X = np.zeros((len(joined), len(feat_names)))
    y = np.array([manual[fn] for fn in joined])

    for i, fn in enumerate(joined):
        for j, col in enumerate(auto_cols):
            X[i, j] = auto[fn][col]
        for tag, score in clip[fn].items():
            if tag in tag_index:
                X[i, len(auto_cols) + tag_index[tag]] = score

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model = Ridge(alpha=args.alpha, fit_intercept=True)
    model.fit(X_scaled, y)
    r2 = model.score(X_scaled, y)
    residuals = y - model.predict(X_scaled)

    coefs = sorted(zip(feat_names, model.coef_), key=lambda x: x[1], reverse=True)

    print(f"\n{'='*55}")
    print(f"Treningssett: {len(joined)} bilder, {len(feat_names)} features")
    print(f"  herav: {len(auto_cols)} auto-metrikker + {len(all_tags)} CLIP-tags")
    print(f"R²:           {r2:.4f}  (alpha={args.alpha})")
    print(f"\nAuto-metrikker:")
    for col in auto_cols:
        coef = model.coef_[feat_names.index(col)]
        print(f"  {col:12s}  {coef:+.4f}")
    print(f"\nTopp 15 positive tags:")
    for tag, coef in coefs[:15]:
        if tag not in auto_cols:
            print(f"  {tag:35s}  {coef:+.4f}")
    print(f"\nTopp 15 negative tags:")
    for tag, coef in reversed(coefs[-15:]):
        if tag not in auto_cols:
            print(f"  {tag:35s}  {coef:+.4f}")
    print(f"\nResiduals – std: {residuals.std():.3f}  max|e|: {np.abs(residuals).max():.3f}")
    print(f"{'='*55}\n")

    if not args.dry_run:
        weights = {
            "intercept": float(model.intercept_),
            "features": {
                name: {
                    "mean": float(scaler.mean_[i]),
                    "std":  float(scaler.scale_[i]),
                    "coef": float(model.coef_[i]),
                }
                for i, name in enumerate(feat_names)
            },
        }
        WEIGHTS_COMBINED.write_text(
            json.dumps(weights, indent=2, ensure_ascii=False), encoding="utf-8"
        )
        print(f"Kombinerte vekter lagret: {WEIGHTS_COMBINED}")
        print(f"Kjør nå: .venv/Scripts/python scripts/build_scores.py")
    else:
        print("Dry-run – ingen filer skrevet.")


if __name__ == "__main__":
    main()
