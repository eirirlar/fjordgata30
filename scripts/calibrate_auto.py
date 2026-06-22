"""
T41 steg B – Lineær regresjon for å finne vekter til auto-score.

Les scores_manual.csv og scores_total.csv, join på filnavn, kjør LinearRegression,
og lagre koeffisienter i weights_auto.json.

Bruk:
    .venv/Scripts/python scripts/calibrate_auto.py           # skriv weights_auto.json
    .venv/Scripts/python scripts/calibrate_auto.py --dry-run # skriv ingenting
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

import numpy as np
from sklearn.linear_model import LinearRegression

SCORES_TOTAL = Path(__file__).resolve().parent / "scoring" / "scores_total.csv"
SCORES_MANUAL = Path(__file__).resolve().parent / "scoring" / "scores_manual.csv"
WEIGHTS_JSON = Path(__file__).resolve().parent / "scoring" / "weights_auto.json"

FEATURES = ["sharpness", "exposure", "brisque", "musiq"]


def read_manual() -> dict[str, float]:
    manual: dict[str, float] = {}
    with SCORES_MANUAL.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            try:
                manual[row["filnavn"]] = float(row["score"])
            except (ValueError, KeyError):
                pass
    return manual


def main() -> None:
    parser = argparse.ArgumentParser(description="Kalibrer vekter via lineær regresjon (T41 steg B)")
    parser.add_argument("--dry-run", action="store_true", help="Ikke skriv til weights_auto.json")
    args = parser.parse_args()

    if not SCORES_TOTAL.exists():
        print(f"FEIL: {SCORES_TOTAL.name} finnes ikke – kjør build_scores.py (T48) først.")
        sys.exit(1)
    scores: dict[str, dict] = {}
    with SCORES_TOTAL.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            scores[row["filnavn"]] = row

    manual = read_manual()

    joined = [
        (scores[fn], manual[fn])
        for fn in manual
        if fn in scores and all(scores[fn].get(f) for f in FEATURES)
    ]

    if len(joined) < 10:
        print(f"FEIL: Bare {len(joined)} bilder i join – for få til regresjon.")
        sys.exit(1)

    X = np.array([[float(row[f]) for f in FEATURES] for row, _ in joined])
    y = np.array([score for _, score in joined])

    model = LinearRegression(fit_intercept=True)
    model.fit(X, y)
    r2 = model.score(X, y)

    print(f"\n{'='*50}")
    print(f"Treningssett: {len(joined)} bilder")
    print(f"R²:           {r2:.4f}")
    print(f"\nKoeffisienter:")
    for feat, coef in zip(FEATURES, model.coef_):
        print(f"  {feat:12s}  {coef:+.4f}")
    print(f"  {'intercept':12s}  {model.intercept_:+.4f}")

    residuals = y - model.predict(X)
    print(f"\nResiduals – std: {residuals.std():.3f}  max|e|: {np.abs(residuals).max():.3f}")
    print(f"{'='*50}\n")

    weights = {
        "intercept": float(model.intercept_),
        **{feat: float(coef) for feat, coef in zip(FEATURES, model.coef_)},
    }

    if not args.dry_run:
        WEIGHTS_JSON.write_text(json.dumps(weights, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"Vekter lagret: {WEIGHTS_JSON}")
        print(f"Kjør nå: .venv/Scripts/python scripts/build_scores.py")
    else:
        print("Dry-run – ingen filer skrevet.")


if __name__ == "__main__":
    main()
