"""
Skarphetsmåling via Laplacian-varians (T37).

Eksporterer sharpness_score(path) for bruk i score_images.py (T42).
Returnerer råscore (Laplacian-varians). Normalisering til 1–10 gjøres av T42.

Standalone – ett bilde:
    python3 scripts/scoring/sharpness.py <bildefil>
"""

from __future__ import annotations

import sys
from pathlib import Path

try:
    import cv2
except ImportError:
    print("FEIL: opencv-contrib-python er ikke installert. Kjør: uv pip install opencv-contrib-python")
    sys.exit(1)


def sharpness_normalized(path: Path) -> float | None:
    """Returnerer normalisert skarphetsscore (1–10) fra scores_total.csv, eller None."""
    from . import _lookup
    return _lookup(path.name, "sharpness")


def sharpness_score(path: Path) -> float | None:
    """
    Returner Laplacian-varians for ett bilde, eller None hvis bildet ikke kan leses.
    Høy verdi = skarpt bilde. Skala 0 til ubegrenset.
    Normalisering til 1–10 gjøres av T42 på tvers av hele datasettet.
    """
    img = cv2.imread(str(path), cv2.IMREAD_GRAYSCALE)
    if img is None:
        return None
    return float(cv2.Laplacian(img, cv2.CV_64F).var())


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Bruk: python3 sharpness.py <bildefil>")
        sys.exit(1)
    path = Path(sys.argv[1])
    score = sharpness_score(path)
    if score is None:
        print(f"Kunne ikke lese: {path}")
        sys.exit(1)
    norm = sharpness_normalized(path)
    norm_str = f"{norm:.2f}" if norm is not None else "ikke i scores_total.csv"
    print(f"{path.name}: rå={score:.1f}  normalisert={norm_str}")
