#!/usr/bin/env python3
"""
Bildeprosessering for Fjordgata 30.

Pakker ut .zip-arkiver fra ../temp/bilder/ til ../temp/bilder/extracted/,
konverterer bilder til JPEG med ~500kB målstørrelse, og lagrer med
dato-basert filnavn (YYYYMMDD_HHMMSS.jpg) i ../temp/bilder/processed/.

Kjøres fra prosjektmappen:
    python3 scripts/process_images.py
"""

import hashlib
import json
import math
import os
import subprocess
import sys
import zipfile
from collections import defaultdict
from datetime import datetime
from pathlib import Path

try:
    from PIL import Image
    from PIL.ExifTags import TAGS
except ImportError:
    print("FEIL: Pillow er ikke installert. Kjør: pip install Pillow")
    sys.exit(1)

BILDER_DIR   = Path(__file__).resolve().parent.parent.parent / "temp" / "bilder"
EXTRACTED_DIR = BILDER_DIR / "extracted"
PROCESSED_DIR = BILDER_DIR / "processed"

IMAGE_SUFFIXES = {".jpg", ".jpeg", ".png", ".heic", ".tiff", ".tif", ".bmp", ".webp", ".raw", ".cr2", ".nef", ".arw"}
JPEG_QUALITY = 85
TARGET_BYTES = 500 * 1024
HASH_CACHE   = EXTRACTED_DIR / ".zip_hashes.json"


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def _load_hash_cache() -> dict[str, str]:
    if HASH_CACHE.exists():
        return json.loads(HASH_CACHE.read_text(encoding="utf-8"))
    return {}


def _save_hash_cache(cache: dict[str, str]) -> None:
    HASH_CACHE.write_text(json.dumps(cache, indent=2), encoding="utf-8")


def extract_zips() -> dict[Path, datetime]:
    """
    Pakker ut alle zip-filer til EXTRACTED_DIR.
    Hopper over arkiver med uendret SHA256 (cachet i .zip_hashes.json).
    Returnerer et oppslagsverk filbane → dato fra zip-metadata (ZipInfo.date_time).
    """
    zip_dates: dict[Path, datetime] = {}
    zips = list(BILDER_DIR.glob("*.zip"))
    if not zips:
        print("  Ingen .zip-filer funnet.")
        return zip_dates
    EXTRACTED_DIR.mkdir(parents=True, exist_ok=True)
    cache = _load_hash_cache()
    cache_updated = False

    for zf in zips:
        current_hash = _sha256(zf)
        with zipfile.ZipFile(zf, "r") as z:
            infos = z.infolist()
            if cache.get(zf.name) == current_hash:
                print(f"  SKIP  {zf.name}  (uendret)")
            else:
                print(f"  Pakker ut: {zf.name}")
                for info in infos:
                    z.extract(info, EXTRACTED_DIR)
                cache[zf.name] = current_hash
                cache_updated = True
            for info in infos:
                if info.date_time and info.date_time[0] > 1980:
                    zip_dates[EXTRACTED_DIR / info.filename] = datetime(*info.date_time)

    if cache_updated:
        _save_hash_cache(cache)
    print(f"  {len(zips)} arkiv(er) behandlet.")
    return zip_dates


def collect_images() -> list[Path]:
    images = []
    for root, _dirs, files in os.walk(EXTRACTED_DIR):
        for fname in files:
            if Path(fname).suffix.lower() in IMAGE_SUFFIXES:
                images.append(Path(root) / fname)
    return images


def get_exif_datetime(path: Path) -> datetime | None:
    try:
        img = Image.open(path)
        exif_data = img._getexif()
        if not exif_data:
            return None
        for tag_id, value in exif_data.items():
            if TAGS.get(tag_id) == "DateTimeOriginal":
                return datetime.strptime(value, "%Y:%m:%d %H:%M:%S")
        return None
    except Exception:
        return None


def get_image_datetime(path: Path, zip_dates: dict[Path, datetime]) -> datetime | None:
    """Prioritet: EXIF → ZipInfo-dato. Returnerer None hvis ingen kilde finnes."""
    return get_exif_datetime(path) or zip_dates.get(path)


def build_filename_map(images: list[Path], zip_dates: dict[Path, datetime]) -> dict[Path, str]:
    """
    Tildel destinasjonsfilnavn.
    - Med dato: YYYYMMDD_HHMMSS.jpg (kollisjon: _001, _002 osv.)
    - Uten dato: UNPARSABLE_DATE_001.jpg, _002.jpg osv.
    Sorteres nyeste først; filer uten dato havner til slutt.
    """
    images_sorted = sorted(
        images,
        key=lambda p: get_image_datetime(p, zip_dates) or datetime.min,
        reverse=True,
    )

    used: defaultdict[str, int] = defaultdict(int)
    result: dict[Path, str] = {}
    unparsable = 0
    for path in images_sorted:
        dt = get_image_datetime(path, zip_dates)
        if dt is None:
            unparsable += 1
            result[path] = f"UNPARSABLE_DATE_{unparsable:03d}.jpg"
        else:
            base = dt.strftime("%Y%m%d_%H%M%S")
            n = used[base]
            used[base] += 1
            result[path] = f"{base}.jpg" if n == 0 else f"{base}_{n:03d}.jpg"
    return result


def convert_to_jpeg(src: Path, dst: Path) -> bool:
    """
    Konverter til JPEG med fast kvalitet (JPEG_QUALITY).
    Hvis resulterende fil overstiger TARGET_BYTES, skaleres dimensjonene ned
    med sqrt(TARGET_BYTES / faktisk_størrelse) og konverteres på nytt.
    Bildene forstørres aldri.
    """
    def run_convert(extra_args: list[str]) -> bool:
        cmd = ["convert", str(src), "-auto-orient"] + extra_args + ["-quality", str(JPEG_QUALITY), str(dst)]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"    FEIL: {result.stderr.strip()}")
            return False
        return True

    if not run_convert([]):
        return False

    actual = dst.stat().st_size
    if actual > TARGET_BYTES:
        scale_pct = math.sqrt(TARGET_BYTES / actual) * 100
        dst.unlink()
        if not run_convert(["-resize", f"{scale_pct:.1f}%"]):
            return False

    return True


def main() -> None:
    if not BILDER_DIR.exists():
        print(f"FEIL: Mappen finnes ikke: {BILDER_DIR}")
        print("Legg .zip-filer i ../temp/bilder/ og prøv igjen.")
        sys.exit(1)

    print(f"Inndata:   {BILDER_DIR}")
    print(f"Utpakket:  {EXTRACTED_DIR}")
    print(f"Resultat:  {PROCESSED_DIR}")
    print()

    print("=== Steg 1: Pakk ut zip-arkiver ===")
    zip_dates = extract_zips()
    print()

    print("=== Steg 2: Finn bildefiler ===")
    images = collect_images()
    if not images:
        print("  Ingen bildefiler funnet i extracted/.")
        sys.exit(0)
    print(f"  {len(images)} bilde(r) funnet.")
    print()

    print("=== Steg 3: Konverter til JPEG (~500kB) ===")
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    ok = skipped = fail = 0
    for src, dst_name in build_filename_map(images, zip_dates).items():
        dst = PROCESSED_DIR / dst_name
        if dst.exists():
            print(f"  SKIP  {dst_name}")
            skipped += 1
            continue
        print(f"  {src.name}  →  {dst_name}")
        if convert_to_jpeg(src, dst):
            ok += 1
        else:
            fail += 1
    print()

    print("=== Ferdig ===")
    print(f"  Konvertert:   {ok}")
    if skipped:
        print(f"  Hoppet over:  {skipped}  (fantes allerede i processed/)")
    if fail:
        print(f"  Feilet:       {fail}")
    print(f"\nOriginaler i extracted/ beholdes for manuell verifisering.")


if __name__ == "__main__":
    main()
