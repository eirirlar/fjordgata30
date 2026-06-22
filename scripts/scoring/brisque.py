"""
Teknisk bildekvalitet via BRISQUE (T39).

Bruker PyIQA sin BRISQUE-implementasjon. Modellvekter (~112 kB) lastes ned
automatisk første gang og caches i ~/.cache/torch/hub/pyiqa/.

Eksporterer brisque_score(path) for bruk i score_auto.py (T42).

Standalone – ett bilde:
    python3 scripts/scoring/brisque.py <bildefil>

Rekalibrering:
    find ../temp/bilder/processed -name "*.jpg" | \
        python3 scripts/scoring/brisque.py --recalibrate
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

try:
    import pyiqa
    import torch
    import numpy as np
except ImportError:
    print("FEIL: pyiqa er ikke installert. Kjør: uv pip install pyiqa torch")
    sys.exit(1)

CALIBRATION_FILE = Path(__file__).resolve().parent / "brisque_calibration.json"
PERCENTILE_LOW  = 5
PERCENTILE_HIGH = 95

_metric = None

def _get_metric() -> pyiqa.InferenceModel:
    global _metric
    if _metric is None:
        _metric = pyiqa.create_metric("brisque", device=torch.device("cpu"))
    return _metric


def brisque_normalized(path: Path) -> float | None:
    """Returnerer normalisert BRISQUE-score (1–10) fra scores_total.csv, eller None."""
    from . import _lookup
    return _lookup(path.name, "brisque")


def _raw_brisque(path: Path) -> float | None:
    try:
        result = _get_metric()(str(path))
        return float(result)
    except Exception:
        return None


def _load_calibration() -> tuple[float, float]:
    if not CALIBRATION_FILE.exists():
        raise FileNotFoundError(
            f"Kalibreringsfil mangler: {CALIBRATION_FILE}\n"
            "Kjør rekalibrering først (se --recalibrate i docstring)."
        )
    data = json.loads(CALIBRATION_FILE.read_text())
    return data["p_low"], data["p_high"]


def _normalize(raw: float, p_low: float, p_high: float) -> float:
    # Lav rå BRISQUE = god kvalitet → inverter skalaen
    if p_high == p_low:
        return 5.0
    score = 10.0 - 9.0 * (raw - p_low) / (p_high - p_low)
    return max(1.0, min(10.0, score))


def brisque_score(path: Path) -> float | None:
    """
    Returner BRISQUE-basert kvalitetsscore 1–10 for ett bilde, eller None hvis bildet ikke kan leses.
    Score 10 = høy teknisk kvalitet. Score 1 = støy/blur/artefakter.
    Normalisering baseres på kalibreringsfil (brisque_calibration.json).
    """
    raw = _raw_brisque(path)
    if raw is None:
        return None
    p_low, p_high = _load_calibration()
    return _normalize(raw, p_low, p_high)


def recalibrate(paths: list[Path]) -> None:
    raw_values = [v for p in paths if (v := _raw_brisque(p)) is not None]
    if not raw_values:
        print("Ingen bilder å kalibrere mot.")
        return
    p_low  = float(np.percentile(raw_values, PERCENTILE_LOW))
    p_high = float(np.percentile(raw_values, PERCENTILE_HIGH))
    CALIBRATION_FILE.write_text(json.dumps({"p_low": p_low, "p_high": p_high}, indent=2))
    print(f"Kalibrering lagret ({len(raw_values)} bilder): p{PERCENTILE_LOW}={p_low:.1f}, p{PERCENTILE_HIGH}={p_high:.1f}")


if __name__ == "__main__":
    if "--recalibrate" in sys.argv:
        paths = [Path(line.strip()) for line in sys.stdin if line.strip()]
        recalibrate(paths)
    elif len(sys.argv) == 2:
        path = Path(sys.argv[1])
        raw = _raw_brisque(path)
        if raw is None:
            print(f"Kunne ikke lese: {path}")
            sys.exit(1)
        norm = brisque_normalized(path)
        norm_str = f"{norm:.2f}" if norm is not None else "ikke i scores_total.csv"
        print(f"{path.name}: rå BRISQUE={raw:.1f}  normalisert={norm_str}")
    else:
        print("Bruk: python3 brisque.py <bildefil>")
        print("      find ... | python3 brisque.py --recalibrate")
        sys.exit(1)
