#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "potracer",
#   "Pillow",
#   "numpy",
# ]
# ///
"""Vectorize a single raster image to SVG using the pure-Python potracer port.

Usage:
    uv run --script scripts/trace_image_to_svg.py <image-path>

Writes <image-path with .svg suffix> next to the input (e.g. side-1.png -> side-1.svg).
No tuning options are exposed — this is a minimum viable pipeline.
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import potrace
from PIL import Image


def trace_to_svg(image_path: Path, svg_path: Path, threshold: int = 128) -> None:
    img = Image.open(image_path).convert("L")
    width, height = img.size
    arr = np.array(img) < threshold  # True where ink
    bitmap = potrace.Bitmap(arr)
    path = bitmap.trace()

    parts: list[str] = [
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
        '<path fill="black" stroke="none" fill-rule="evenodd" d="',
    ]
    for curve in path:
        start = curve.start_point
        parts.append(f"M{start.x:.3f},{start.y:.3f}")
        for segment in curve.segments:
            end = segment.end_point
            if segment.is_corner:
                c = segment.c
                parts.append(
                    f"L{c.x:.3f},{c.y:.3f}L{end.x:.3f},{end.y:.3f}"
                )
            else:
                c1 = segment.c1
                c2 = segment.c2
                parts.append(
                    f"C{c1.x:.3f},{c1.y:.3f} "
                    f"{c2.x:.3f},{c2.y:.3f} "
                    f"{end.x:.3f},{end.y:.3f}"
                )
        parts.append("z")
    parts.append('"/>')
    parts.append("</svg>")

    svg_path.write_text("\n".join(parts), encoding="utf-8")


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: trace_image_to_svg.py <image-path>", file=sys.stderr)
        return 2
    src = Path(sys.argv[1])
    if not src.is_file():
        print(f"not found: {src}", file=sys.stderr)
        return 1
    dst = src.with_suffix(".svg")
    trace_to_svg(src, dst)
    print(f"wrote {dst} ({dst.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
