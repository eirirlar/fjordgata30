"""
T46 – Score tags per bilde med CLIP og skriv scripts/scoring/scores_clip.csv.

Leser alle unike tags fra scores_ram.csv, scorer hvert bilde mot alle tags.
Long format, append-only – én rad per bilde per tag.
Idempotent – bilder som allerede har rader hoppes over.

Bruk:
    .venv/Scripts/python scripts/score_clip.py
    .venv/Scripts/python scripts/score_clip.py --limit 10
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

PROCESSED_DIR = Path(__file__).resolve().parents[2] / "temp" / "bilder" / "processed"
SCORING_DIR   = Path(__file__).resolve().parent / "scoring"
SCORES_RAM    = SCORING_DIR / "scores_ram.csv"
SCORES_CLIP   = SCORING_DIR / "scores_clip.csv"
COLUMNS       = ["filnavn", "tag", "clip_score"]


def _read_all_tags() -> list[str]:
    tags: set[str] = set()
    with SCORES_RAM.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            tags.add(row["tag"])
    return sorted(tags)


def _read_existing() -> set[str]:
    if not SCORES_CLIP.exists():
        return set()
    with SCORES_CLIP.open(newline="", encoding="utf-8") as f:
        return {row["filnavn"] for row in csv.DictReader(f)}


def _append_scores(filnavn: str, tag_scores: dict[str, float]) -> None:
    SCORES_CLIP.parent.mkdir(parents=True, exist_ok=True)
    write_header = not SCORES_CLIP.exists()
    with SCORES_CLIP.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS)
        if write_header:
            writer.writeheader()
        for tag, score in tag_scores.items():
            writer.writerow({"filnavn": filnavn, "tag": tag, "clip_score": f"{score:.4f}"})


def main() -> None:
    try:
        import open_clip
        import torch
        from PIL import Image
    except ImportError:
        print("FEIL: open-clip-torch ikke installert. Kjør: pip install open-clip-torch")
        sys.exit(1)

    if not SCORES_RAM.exists():
        print(f"FEIL: {SCORES_RAM.name} finnes ikke – kjør score_ram.py (T45) først.")
        sys.exit(1)

    parser = argparse.ArgumentParser(description="CLIP-score tags per bilde (T46)")
    parser.add_argument("--limit", type=int, default=None)
    args = parser.parse_args()

    all_tags = _read_all_tags()
    print(f"Vokabular: {len(all_tags)} unike tags")

    existing = _read_existing()
    images = sorted(PROCESSED_DIR.glob("*.jpg"), reverse=True)
    if args.limit:
        images = images[:args.limit]
    new_images = [img for img in images if img.name not in existing]
    print(f"{len(images)} bilder, {len(existing)} allerede scoret, {len(new_images)} nye.")

    if not new_images:
        print("Ingenting å gjøre.")
        return

    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Laster CLIP-modell (device={device}) …")
    model, _, preprocess = open_clip.create_model_and_transforms("ViT-B-32", pretrained="openai")
    model.eval()
    model = model.to(device)
    tokenizer = open_clip.get_tokenizer("ViT-B-32")

    text_tokens = tokenizer(all_tags).to(device)
    with torch.no_grad():
        text_features = model.encode_text(text_tokens)
        text_features /= text_features.norm(dim=-1, keepdim=True)

    for i, img_path in enumerate(new_images, 1):
        image = preprocess(Image.open(img_path).convert("RGB")).unsqueeze(0).to(device)
        with torch.no_grad():
            img_features = model.encode_image(image)
            img_features /= img_features.norm(dim=-1, keepdim=True)
            scores = (img_features @ text_features.T).squeeze(0).cpu().tolist()

        _append_scores(img_path.name, dict(zip(all_tags, scores)))
        print(f"  [{i}/{len(new_images)}] {img_path.name}")

    print(f"\nFerdig. Kjør calibrate_tags.py og build_scores.py for oppdatert total.")


if __name__ == "__main__":
    main()
