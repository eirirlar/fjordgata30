"""Extract per-page PNG images from architect PDFs in tegninger/.

Each PDF contains a cover page (omslag) followed by E-numbered drawings.
Output files are named with the rammesoeknad date prefix and a slugified
title derived from the drawing's title text.

Run from project root:
    uv run --with pymupdf python scripts/extract_tegninger.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import fitz  # PyMuPDF

TEGNINGER_DIR = Path("tegninger")
DATE_PREFIX = "2026-05-12"
DPI = 200

# Cover (page 1) naming uses file category and E-range — page 1's title text
# is inconsistent (e.g., Snitt planlagt.pdf side 1 has wrong title).
PDF_META: dict[str, tuple[str, str]] = {
    "E-1 - E-4_ Fasade eksisterende.pdf": ("E-01-E-04", "fasade_eksisterende"),
    "E-5 - E-8_ Fasade planlagt.pdf": ("E-05-E-08", "fasade_planlagt"),
    "E-9 - E-15_Planer-eksisterende.pdf": ("E-09-E-15", "planer_eksisterende"),
    "E-16 - E-22_Planer planlagt.pdf": ("E-16-E-22", "planer_planlagt"),
    "E-23 - E-24_ Snitt eksisterende.pdf": ("E-23-E-24", "snitt_eksisterende"),
    "E-25 - E-26_ Snitt planlagt.pdf": ("E-25-E-26", "snitt_planlagt"),
}


def slugify(text: str) -> str:
    text = text.lower()
    text = (
        text.replace("ø", "oe")
        .replace("æ", "ae")
        .replace("å", "aa")
        .replace("ö", "oe")
        .replace("ä", "ae")
    )
    # Preserve negative-number prefix (e.g. "-1. etasje" = kjeller) before
    # stripping punctuation — otherwise "Plan -1" collapses to "Plan 1".
    text = re.sub(r"-(\d)", r"minus_\1", text)
    text = re.sub(r"[^a-z0-9]+", "_", text)
    text = re.sub(r"_+", "_", text)
    return text.strip("_")


def find_e_number(text: str) -> str | None:
    m = re.search(r"\bE-(\d+)\b", text)
    return f"E-{int(m.group(1)):02d}" if m else None


def first_nonempty_line(text: str) -> str:
    for line in text.splitlines():
        line = line.strip()
        if line:
            return line
    return ""


def render_page(page: fitz.Page, out_path: Path) -> None:
    matrix = fitz.Matrix(DPI / 72, DPI / 72)
    pix = page.get_pixmap(matrix=matrix)
    pix.save(out_path)


def main() -> int:
    if not TEGNINGER_DIR.exists():
        print(f"ERROR: {TEGNINGER_DIR} not found (run from project root)")
        return 1

    pdfs = sorted(TEGNINGER_DIR.glob("*.pdf"))
    if not pdfs:
        print(f"No PDFs in {TEGNINGER_DIR}")
        return 1

    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]

    written: list[Path] = []
    warnings: list[str] = []

    for pdf_path in pdfs:
        meta = PDF_META.get(pdf_path.name)
        if meta is None:
            warnings.append(f"No metadata for {pdf_path.name} — skipping cover naming")
            e_range, category = "unknown", slugify(pdf_path.stem)
        else:
            e_range, category = meta

        print(f"\n=== {pdf_path.name} ===")
        doc = fitz.open(pdf_path)

        for page_idx, page in enumerate(doc):
            text = page.get_text("text")
            title = first_nonempty_line(text)

            if page_idx == 0:
                filename = f"{DATE_PREFIX}_{e_range}_omslag_{category}.png"
            else:
                e_num = find_e_number(text)
                if e_num is None:
                    warnings.append(
                        f"{pdf_path.name} side {page_idx + 1}: no E-number found"
                    )
                    e_num = f"E-unknown-{page_idx + 1}"
                desc = slugify(title) if title else category
                filename = f"{DATE_PREFIX}_{e_num}_{desc}.png"

            out_path = TEGNINGER_DIR / filename
            render_page(page, out_path)
            written.append(out_path)
            print(f"  side {page_idx + 1}: {filename}")

        doc.close()

    print(f"\nWrote {len(written)} files to {TEGNINGER_DIR}/")
    if warnings:
        print("\nWarnings:")
        for w in warnings:
            print(f"  - {w}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
