"""
T57 – Select the best images within a date range.

Reads scores_total.csv and picks the top N images by effective score.
Manual rating always takes priority over model score.

Usage:
    .venv/bin/python scripts/select_images.py --from 2026-01-01 --to 2026-06-30
    .venv/bin/python scripts/select_images.py --from 2026-01-01 --to 2026-06-30 --count 20
    .venv/bin/python scripts/select_images.py --from 2026-01-01 --to 2026-06-30 --output /tmp/selected
"""

from __future__ import annotations

import argparse
import csv
import shutil
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from config import PROCESSED_DIR

DATA_DIR      = Path(__file__).resolve().parents[1] / "data"
SCORES_TOTAL  = DATA_DIR / "scores_total.csv"


def _parse_date(s: str) -> date:
    try:
        return date.fromisoformat(s)
    except ValueError:
        raise argparse.ArgumentTypeError(f"Invalid date '{s}' — expected YYYY-MM-DD")


def _image_date(filename: str) -> date | None:
    """Extract date from filename like 20260620_080001.jpg."""
    stem = Path(filename).stem
    if len(stem) >= 8 and stem[:8].isdigit():
        try:
            return date(int(stem[0:4]), int(stem[4:6]), int(stem[6:8]))
        except ValueError:
            pass
    return None


def main() -> None:
    parser = argparse.ArgumentParser(description="Select best images within a date range (T57)")
    parser.add_argument("--from", dest="date_from", required=True, type=_parse_date,
                        metavar="YYYY-MM-DD", help="Start date (inclusive)")
    parser.add_argument("--to",   dest="date_to",   required=True, type=_parse_date,
                        metavar="YYYY-MM-DD", help="End date (inclusive)")
    parser.add_argument("--count", type=int, default=10,
                        help="Number of images to select (default: 10)")
    parser.add_argument("--output", type=Path, default=None,
                        help="Copy selected images to this directory")
    args = parser.parse_args()

    if not SCORES_TOTAL.exists():
        print(f"ERROR: {SCORES_TOTAL} not found — run build_scores.py first.")
        raise SystemExit(1)

    candidates: list[tuple[float, str, str]] = []  # (effective_score, filename, source)

    with SCORES_TOTAL.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            filename = row["filnavn"]
            img_date = _image_date(filename)
            if img_date is None or not (args.date_from <= img_date <= args.date_to):
                continue

            manual = row.get("manual", "").strip()
            if manual:
                score, source = float(manual), "manual"
            elif row.get("total", "").strip():
                score, source = float(row["total"]), "model"
            else:
                continue

            candidates.append((score, filename, source))

    candidates.sort(key=lambda x: x[0], reverse=True)
    selected = candidates[: args.count]

    period = f"{args.date_from} – {args.date_to}"
    print(f"Period: {period}  |  {len(candidates)} images found  |  top {len(selected)} selected\n")
    print(f"{'#':<4} {'Score':<7} {'Source':<8} Filename")
    print("-" * 50)
    for i, (score, filename, source) in enumerate(selected, 1):
        print(f"{i:<4} {score:<7.2f} {source:<8} {filename}")

    if args.output is not None:
        args.output.mkdir(parents=True, exist_ok=True)
        missing = 0
        for _, filename, _ in selected:
            src = PROCESSED_DIR / filename
            if src.exists():
                shutil.copy2(src, args.output / filename)
            else:
                print(f"  WARNING: {filename} not found in processed dir — skipped")
                missing += 1
        copied = len(selected) - missing
        print(f"\nCopied {copied}/{len(selected)} images to {args.output}")


if __name__ == "__main__":
    main()
