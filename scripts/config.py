"""
Read project config from config.json at project root.

Scripts import paths from here instead of hardcoding them:

    from config import PROCESSED_DIR, BILDER_DIR, EXTRACTED_DIR
"""

from __future__ import annotations

import json
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parent.parent
_CONFIG_FILE  = _PROJECT_ROOT / "config.json"
_DEFAULTS     = {"bilder_dir": "../temp/bilder"}


def _load() -> dict:
    if _CONFIG_FILE.exists():
        return {**_DEFAULTS, **json.loads(_CONFIG_FILE.read_text(encoding="utf-8"))}
    return _DEFAULTS


def _resolve(rel: str) -> Path:
    p = Path(rel)
    return p if p.is_absolute() else (_PROJECT_ROOT / p).resolve()


_cfg = _load()

BILDER_DIR    = _resolve(_cfg["bilder_dir"])
PROCESSED_DIR = BILDER_DIR / "processed"
EXTRACTED_DIR = BILDER_DIR / "extracted"
