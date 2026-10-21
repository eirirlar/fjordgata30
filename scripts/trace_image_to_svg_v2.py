#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "potracer",
#   "Pillow",
#   "numpy",
# ]
# ///
"""Vectorize a hand-drawn sketch to SVG, with corrections requested after v1.

Corrections applied vs trace_image_to_svg.py:
- Deskew via ImageMagick -deskew (fixes small rotation from scanning)
- Trim via ImageMagick -trim (removes dark scan edges that caused evenodd inversion)
- Explicit white <rect> background + black <path> (black-on-white regardless of fill-rule)
- Transcribed printed and handwritten text overlaid as <text> elements
  Text content and positions are HARDCODED for side-1.png — not generalized.
  Positions are in post-trim pixel coordinates and will need manual tuning.

NOT applied (per user: can be done later):
- Line straightening — hand-drawn wobble is preserved as traced curves.
- Automatic OCR — text was transcribed by hand from the image.
"""
from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

import numpy as np
import potrace
from PIL import Image

# Transcribed text for side-1.png. Positions are approximate (post-trim px).
# fs = font size (px); anc = text-anchor; fam = font-family; w = font-weight.
TEXT_ANNOTATIONS = [
    # --- Printed title block ---
    {"x": 620, "y": 30, "text": "Sivilingeniørene Harboe og Leganger AS",
     "fs": 20, "anc": "middle", "w": "bold"},
    {"x": 620, "y": 55, "text": "Telefon: 73 99 28 30    firmapost@h-l.no",
     "fs": 13, "anc": "middle"},
    # Printed labels, second row
    {"x": 50, "y": 90, "text": "Prosjekt:", "fs": 14},
    {"x": 540, "y": 90, "text": "Tegning:", "fs": 14},
    # Handwritten values, second row
    {"x": 160, "y": 90, "text": "FJORDGT 30", "fs": 22, "fam": "cursive"},
    {"x": 640, "y": 90, "text": "SNITT BUNNPUTE / SØYLE",
     "fs": 22, "fam": "cursive"},
    # Printed labels, third row
    {"x": 50, "y": 120, "text": "Dato:", "fs": 14},
    {"x": 260, "y": 120, "text": "Mål:", "fs": 14},
    {"x": 540, "y": 120, "text": "Sign:", "fs": 14},
    # Handwritten values, third row
    {"x": 120, "y": 120, "text": "24/4-26", "fs": 22, "fam": "cursive"},
    {"x": 320, "y": 120, "text": "1:20", "fs": 22, "fam": "cursive"},
    {"x": 605, "y": 120, "text": "OAS", "fs": 22, "fam": "cursive"},
    # --- Drawing area labels (all handwritten) ---
    {"x": 690, "y": 300, "text": "SØYLE", "fs": 26, "fam": "cursive"},
    {"x": 75, "y": 360, "text": "410", "fs": 26, "fam": "cursive"},
    {"x": 75, "y": 510, "text": "400", "fs": 26, "fam": "cursive"},
    {"x": 460, "y": 495, "text": "FUNDAMENT", "fs": 26, "fam": "cursive"},
    {"x": 460, "y": 530, "text": "STØPES FØRST", "fs": 26, "fam": "cursive"},
    {"x": 875, "y": 525, "text": "FUGEBLIKK +", "fs": 26, "fam": "cursive"},
    {"x": 875, "y": 560, "text": "SVELLEBÅND", "fs": 26, "fam": "cursive"},
    {"x": 550, "y": 630, "text": "2000 × 2000", "fs": 26, "fam": "cursive"},
    # --- Bottom specifications (handwritten) ---
    {"x": 90, "y": 820, "text": "BETONG  B45  MF40 — VANNTETT",
     "fs": 30, "fam": "cursive"},
    {"x": 90, "y": 870, "text": "ARMERING  150 kg/m³",
     "fs": 30, "fam": "cursive"},
]


def deskew_and_trim(src: Path, dst: Path) -> None:
    """Flatten to white, deskew, trim, then pad with white.

    The trailing -border is critical: without it, potrace treats the paper
    edge as a dark region and traces the entire canvas as filled, inverting
    the whole image. White padding guarantees the outermost boundary is
    pure white so the printed form border is traced correctly as a frame.
    """
    subprocess.run(
        [
            "magick", str(src),
            "-background", "white", "-alpha", "remove", "-alpha", "off",
            "-deskew", "40%",
            "-fuzz", "15%",
            "-trim", "+repage",
            "-bordercolor", "white", "-border", "20",
            str(dst),
        ],
        check=True,
    )


def trace_bitmap(png_path: Path, threshold: int = 128):
    img = Image.open(png_path).convert("L")
    width, height = img.size
    arr = np.array(img) < threshold
    bitmap = potrace.Bitmap(arr)
    path = bitmap.trace()
    return width, height, path


def path_to_svg_d(path) -> str:
    parts: list[str] = []
    # potracer emits the full image bounding rectangle as the first curve;
    # with evenodd fill-rule this inverts the whole canvas. Skip it.
    for curve in path.curves[1:]:
        start = curve.start_point
        parts.append(f"M{start.x:.2f},{start.y:.2f}")
        for segment in curve.segments:
            end = segment.end_point
            if segment.is_corner:
                c = segment.c
                parts.append(f"L{c.x:.2f},{c.y:.2f}L{end.x:.2f},{end.y:.2f}")
            else:
                c1 = segment.c1
                c2 = segment.c2
                parts.append(
                    f"C{c1.x:.2f},{c1.y:.2f} "
                    f"{c2.x:.2f},{c2.y:.2f} "
                    f"{end.x:.2f},{end.y:.2f}"
                )
        parts.append("z")
    return "".join(parts)


def escape_xml(s: str) -> str:
    return (s.replace("&", "&amp;")
             .replace("<", "&lt;")
             .replace(">", "&gt;"))


def text_elements_svg(annotations) -> str:
    lines = []
    for a in annotations:
        anc = a.get("anc", "start")
        fam = a.get("fam", "sans-serif")
        w = a.get("w", "normal")
        fs = a.get("fs", 14)
        txt = escape_xml(a["text"])
        lines.append(
            f'<text x="{a["x"]}" y="{a["y"]}" '
            f'font-family="{fam}" font-size="{fs}" '
            f'text-anchor="{anc}" font-weight="{w}" fill="black">'
            f'{txt}</text>'
        )
    return "\n  ".join(lines)


def build_svg(width: int, height: int, path_d: str, text_svg: str) -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'viewBox="0 0 {width} {height}" width="{width}" height="{height}">\n'
        f'  <rect width="{width}" height="{height}" fill="white"/>\n'
        f'  <path fill="black" fill-rule="evenodd" d="{path_d}"/>\n'
        f'  {text_svg}\n'
        f'</svg>\n'
    )


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: trace_image_to_svg_v2.py <image-path>", file=sys.stderr)
        return 2
    src = Path(sys.argv[1])
    if not src.is_file():
        print(f"not found: {src}", file=sys.stderr)
        return 1
    dst = src.with_name(src.stem + "-v2.svg")

    tmp_fd, tmp_name = tempfile.mkstemp(suffix=".png")
    tmp_path = Path(tmp_name)
    import os
    os.close(tmp_fd)
    try:
        deskew_and_trim(src, tmp_path)
        width, height, path = trace_bitmap(tmp_path)
    finally:
        tmp_path.unlink(missing_ok=True)

    path_d = path_to_svg_d(path)
    text_svg = text_elements_svg(TEXT_ANNOTATIONS)
    svg = build_svg(width, height, path_d, text_svg)
    dst.write_text(svg, encoding="utf-8")
    print(f"wrote {dst} ({dst.stat().st_size} bytes, {width}x{height} px)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
