"""
T45 – Tag alle bilder med RAM og skriv scripts/scoring/scores_ram.csv.

Long format, append-only – én rad per bilde per tag.
Idempotent – bilder som allerede har rader hoppes over.

Bruk:
    .venv/Scripts/python scripts/tag_images.py
    .venv/Scripts/python scripts/tag_images.py --limit 10
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

PROCESSED_DIR = Path(__file__).resolve().parents[2] / "temp" / "bilder" / "processed"
SCORES_RAM    = Path(__file__).resolve().parent / "scoring" / "scores_ram.csv"
COLUMNS       = ["filnavn", "tag"]


def _read_existing() -> set[str]:
    if not SCORES_RAM.exists():
        return set()
    with SCORES_RAM.open(newline="", encoding="utf-8") as f:
        return {row["filnavn"] for row in csv.DictReader(f)}


def _append_tags(filnavn: str, tags: list[str]) -> None:
    SCORES_RAM.parent.mkdir(parents=True, exist_ok=True)
    write_header = not SCORES_RAM.exists()
    with SCORES_RAM.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS)
        if write_header:
            writer.writeheader()
        for tag in tags:
            writer.writerow({"filnavn": filnavn, "tag": tag})


def main() -> None:
    try:
        from ram import get_transform
        from ram.models import ram_plus
        import torch
        from PIL import Image
    except ImportError as e:
        print(f"FEIL: {e}")
        print("Kjør: uv pip install git+https://github.com/xinyu1205/recognize-anything.git")
        sys.exit(1)

    parser = argparse.ArgumentParser(description="Tag bilder med RAM (T45)")
    parser.add_argument("--limit", type=int, default=None)
    args = parser.parse_args()

    if not PROCESSED_DIR.exists():
        print(f"FEIL: Bildemapp finnes ikke: {PROCESSED_DIR}")
        sys.exit(1)

    existing = _read_existing()
    images = sorted(PROCESSED_DIR.glob("*.jpg"), reverse=True)
    if args.limit:
        images = images[:args.limit]
    new_images = [img for img in images if img.name not in existing]
    print(f"{len(images)} bilder funnet, {len(existing)} allerede tagget, {len(new_images)} nye.")

    if not new_images:
        print("Ingenting å gjøre.")
        return

    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Laster RAM+-modell (device={device}) …")
    transform = get_transform(image_size=384)

    weights_url = "https://huggingface.co/xinyu1205/recognize-anything-plus-model/resolve/main/ram_plus_swin_large_14m.pth"
    weights_path = Path.home() / ".cache" / "ram" / "ram_plus_swin_large_14m.pth"
    if not weights_path.exists():
        import requests
        print(f"Laster ned modellvekter (~2 GB) til {weights_path} …")
        weights_path.parent.mkdir(parents=True, exist_ok=True)
        r = requests.get(weights_url, stream=True, timeout=300)
        r.raise_for_status()
        with open(weights_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
        print("Nedlasting ferdig.")

    model = ram_plus(pretrained=str(weights_path), image_size=384, vit="swin_l")
    model.eval()
    model = model.to(device)
    print("Modell klar. Starter tagging …")

    for i, img_path in enumerate(new_images, 1):
        image = transform(Image.open(img_path).convert("RGB")).unsqueeze(0).to(device)
        with torch.no_grad():
            result = model.generate_tag(image)
        tags = [t.strip() for t in result[0][0].split("|") if t.strip()]
        _append_tags(img_path.name, tags)
        print(f"  [{i}/{len(new_images)}] {img_path.name}: {tags}")

    print(f"\nFerdig. Kjør clip_score.py for å score tags med CLIP.")


if __name__ == "__main__":
    main()
