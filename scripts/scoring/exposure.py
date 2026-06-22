"""
Eksponeringsvurdering via histogramanalyse (T38).

Eksporterer exposure_score(path) for bruk i score_auto.py (T42).
Returnerer total clipping-andel (0.0–1.0). Høyere = dårligere eksponering.
Normalisering til 1–10 gjøres av T42 på tvers av hele datasettet.

Standalone – ett bilde:
    python3 scripts/scoring/exposure.py <bildefil>
"""

from __future__ import annotations

import sys
from pathlib import Path

try:
    import cv2
    import numpy as np
except ImportError:
    print("FEIL: opencv-contrib-python er ikke installert. Kjør: uv pip install opencv-contrib-python")
    sys.exit(1)

# Pikselverdier under/over disse grensene regnes som clippet
SHADOW_THRESHOLD    = 15
HIGHLIGHT_THRESHOLD = 240


def exposure_normalized(path: Path) -> float | None:
    """Returnerer normalisert eksponeringsscore (1–10) fra scores_total.csv, eller None."""
    from . import _lookup
    return _lookup(path.name, "exposure")


def exposure_score(path: Path) -> float | None:
    """
    Returner total clipping-andel (0.0–1.0) for ett bilde, eller None hvis bildet ikke kan leses.
    0.0 = perfekt eksponering, ingen clipping.
    Høyere verdi = mer under- og/eller overeksponering.
    Normalisering til 1–10 gjøres av T42.
    """
    img = cv2.imread(str(path), cv2.IMREAD_GRAYSCALE)
    if img is None:
        return None
    total = img.size
    shadow    = float(np.sum(img < SHADOW_THRESHOLD))    / total
    highlight = float(np.sum(img > HIGHLIGHT_THRESHOLD)) / total
    return shadow + highlight


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Bruk: python3 exposure.py <bildefil>")
        sys.exit(1)

    path = Path(sys.argv[1])
    raw = exposure_score(path)
    if raw is None:
        print(f"Kunne ikke lese: {path}")
        sys.exit(1)
    norm = exposure_normalized(path)
    norm_str = f"{norm:.2f}" if norm is not None else "ikke i scores_total.csv"
    print(f"{path.name}: clipping={raw:.3f}  normalisert={norm_str}")
