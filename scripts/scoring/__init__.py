from __future__ import annotations

import csv
from pathlib import Path

_SCORES_TOTAL = Path(__file__).resolve().parents[2] / "data" / "scores_total.csv"
_cache: dict[str, dict] | None = None


def _lookup(filnavn: str, col: str) -> float | None:
    global _cache
    if _cache is None:
        if not _SCORES_TOTAL.exists():
            return None
        with _SCORES_TOTAL.open(newline="", encoding="utf-8") as f:
            _cache = {row["filnavn"]: row for row in csv.DictReader(f)}
    row = _cache.get(Path(filnavn).name)
    if row is None:
        return None
    v = row.get(col, "")
    return float(v) if v else None
