#!/usr/bin/env python3
"""Transcribe all new audio files in referat/nye/ with WhisperX.

Scans referat/nye/ for supported audio/video files and runs whisperx on each.
Idempotent: files that already have a sibling .srt are skipped.
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path

AUDIO_DIR = Path("referat/nye")
EXTENSIONS = {".m4a", ".mp3", ".wav", ".mp4"}
WHISPERX_ARGS = [
    "--model", "large-v2",
    "--language", "no",
    "--compute_type", "float32",
    "--diarize",
    "--batch_size", "4",
    "--output_format", "srt",
]


def main() -> int:
    hf_token = os.environ.get("HF_TOKEN")
    if not hf_token:
        print("FEIL: HF_TOKEN mangler. Sett med: export HF_TOKEN=hf_...", file=sys.stderr)
        return 1

    if shutil.which("whisperx") is None:
        print("FEIL: whisperx ikke funnet i PATH. Aktiver whisper-env først:", file=sys.stderr)
        print("  source whisper-env/bin/activate", file=sys.stderr)
        return 1

    if not AUDIO_DIR.exists():
        print(f"FEIL: {AUDIO_DIR}/ finnes ikke.", file=sys.stderr)
        return 1

    audio_files = sorted(
        p for p in AUDIO_DIR.iterdir()
        if p.is_file() and p.suffix.lower() in EXTENSIONS
    )

    if not audio_files:
        exts = ", ".join(sorted(EXTENSIONS))
        print(f"Ingen lydfiler i {AUDIO_DIR}/ (formater: {exts})")
        return 0

    pending = []
    for audio in audio_files:
        srt = audio.with_suffix(".srt")
        if srt.exists():
            print(f"[hopper over] {audio.name} – {srt.name} finnes allerede")
        else:
            pending.append(audio)

    if not pending:
        print("Alle lydfiler er allerede transkribert.")
        return 0

    print(f"Transkriberer {len(pending)} fil(er): {[p.name for p in pending]}")

    failures = []
    for audio in pending:
        print(f"\n=== {audio.name} ===")
        cmd = [
            "whisperx",
            str(audio),
            *WHISPERX_ARGS,
            "--hf_token", hf_token,
            "--output_dir", str(audio.parent),
        ]
        result = subprocess.run(cmd)
        if result.returncode != 0:
            print(f"FEIL: {audio.name} feilet (exit {result.returncode})", file=sys.stderr)
            failures.append(audio.name)

    if failures:
        print(f"\n{len(failures)} fil(er) feilet: {failures}", file=sys.stderr)
        return 1

    print(f"\nFerdig – transkriberte {len(pending)} fil(er).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
