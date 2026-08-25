"""
T46 – Score tags per bilde med CLIP og skriv data/scores_clip.csv.

Long format, append-only – én rad per bilde per tag.
Inkrementell: håndterer både nye bilder og nye tags automatisk.

Ved kjøring:
  1. Nye bilder scores mot HELE vokabularet (alle tags).
  2. Eksisterende bilder scores mot BARE tags de mangler (backfill).

Ingen manuell inngripen kreves når nye bilder introduserer nye tags via
score_ram.py. Bruk --force kun hvis du vil re-score alt fra scratch
(f.eks. hvis CLIP-modellen endres).

Bruk:
    python scripts/score_clip.py
    python scripts/score_clip.py --limit 10   # begrens til 10 nye + 10 backfill
    python scripts/score_clip.py --force      # slett og re-score alt
"""

from __future__ import annotations

import warnings
warnings.filterwarnings("ignore", category=FutureWarning, module="transformers")

import argparse
import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from config import PROCESSED_DIR

DATA_DIR      = Path(__file__).resolve().parents[1] / "data"
SCORES_RAM    = DATA_DIR / "scores_ram.csv"
SCORES_CLIP   = DATA_DIR / "scores_clip.csv"
COLUMNS       = ["filnavn", "tag", "clip_score"]


def _read_all_tags() -> list[str]:
    tags: set[str] = set()
    with SCORES_RAM.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            tags.add(row["tag"])
    return sorted(tags)


def _read_existing() -> dict[str, set[str]]:
    """Returner filnavn → sett av tags som allerede er scoret for det bildet."""
    if not SCORES_CLIP.exists():
        return {}
    per_image: dict[str, set[str]] = {}
    with SCORES_CLIP.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            per_image.setdefault(row["filnavn"], set()).add(row["tag"])
    return per_image


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
    parser.add_argument("--limit", type=int, default=None,
                        help="Begrens antall nye bilder og antall backfill-bilder til N hver")
    parser.add_argument("--force", action="store_true",
                        help="Slett scores_clip.csv og re-score alt fra scratch")
    args = parser.parse_args()

    if args.force and SCORES_CLIP.exists():
        print("--force: Sletter scores_clip.csv og re-scorer alt.")
        SCORES_CLIP.unlink()

    all_tags = _read_all_tags()
    print(f"Vokabular (scores_ram.csv): {len(all_tags)} unike tags")

    existing = _read_existing()
    existing_vocab = set().union(*existing.values()) if existing else set()

    new_tags = [t for t in all_tags if t not in existing_vocab]
    if new_tags and existing:
        preview = new_tags[:8]
        more = "…" if len(new_tags) > 8 else ""
        print(f"Detektert {len(new_tags)} nye tags "
              f"({len(existing_vocab)} → {len(all_tags)}): {preview}{more}")
        print(f"  {len(existing)} eksisterende bilder må backfilles mot disse.")

    images = sorted(PROCESSED_DIR.glob("*.jpg"), reverse=True)
    new_images = [img for img in images if img.name not in existing]

    # Backfill: bilder som allerede er scoret, men mangler nye tags.
    # Bruk per-bilde tag-sett så vi tåler crash midt i backfill (idempotent).
    backfill: list[tuple[Path, list[str]]] = []
    if new_tags:
        for img in images:
            if img.name in existing:
                missing = [t for t in new_tags if t not in existing[img.name]]
                if missing:
                    backfill.append((img, missing))

    if args.limit:
        new_images = new_images[:args.limit]
        backfill = backfill[:args.limit]

    print(f"{len(images)} bilder totalt: {len(existing)} allerede scoret, "
          f"{len(new_images)} nye å score, {len(backfill)} å backfille mot nye tags.")

    if not new_images and not backfill:
        print("Ingenting å gjøre.")
        return

    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Laster CLIP-modell (device={device}) …")
    model, _, preprocess = open_clip.create_model_and_transforms("ViT-B-32", pretrained="openai")
    model.eval()
    model = model.to(device)
    tokenizer = open_clip.get_tokenizer("ViT-B-32")

    with torch.no_grad():
        text_features_all = model.encode_text(tokenizer(all_tags).to(device))
        text_features_all /= text_features_all.norm(dim=-1, keepdim=True)

    # Pre-encode nye tags én gang for backfill; indekser inn i den per bilde
    if backfill:
        with torch.no_grad():
            text_features_new = model.encode_text(tokenizer(new_tags).to(device))
            text_features_new /= text_features_new.norm(dim=-1, keepdim=True)
        new_tag_index = {tag: i for i, tag in enumerate(new_tags)}

    # 1. Score nye bilder mot HELE vokabularet
    for i, img_path in enumerate(new_images, 1):
        image = preprocess(Image.open(img_path).convert("RGB")).unsqueeze(0).to(device)
        with torch.no_grad():
            img_features = model.encode_image(image)
            img_features /= img_features.norm(dim=-1, keepdim=True)
            scores = (img_features @ text_features_all.T).squeeze(0).cpu().tolist()
        _append_scores(img_path.name, dict(zip(all_tags, scores)))
        print(f"  [ny {i}/{len(new_images)}] {img_path.name}")

    # 2. Backfill: score eksisterende bilder mot BARE de nye taggene de mangler
    for i, (img_path, missing_tags) in enumerate(backfill, 1):
        indices = torch.tensor([new_tag_index[t] for t in missing_tags], device=device)
        text_features_missing = text_features_new[indices]
        image = preprocess(Image.open(img_path).convert("RGB")).unsqueeze(0).to(device)
        with torch.no_grad():
            img_features = model.encode_image(image)
            img_features /= img_features.norm(dim=-1, keepdim=True)
            scores = (img_features @ text_features_missing.T).squeeze(0).cpu().tolist()
        _append_scores(img_path.name, dict(zip(missing_tags, scores)))
        print(f"  [backfill {i}/{len(backfill)}] {img_path.name} (+{len(missing_tags)} tags)")

    print(f"\nFerdig. Kjør calibrate_tags.py og build_scores.py for oppdatert total.")


if __name__ == "__main__":
    main()
