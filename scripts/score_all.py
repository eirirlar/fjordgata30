"""
Kjør hele bildescoring-pipelinen i sekvens.

Stegene kjøres med samme Python-executable som dette scriptet selv,
slik at riktig venv alltid brukes.

Bruk:
    .venv/bin/python scripts/score_all.py
"""

import subprocess
import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent

STEPS = [
    "process_images.py",
    "score_auto.py",
    "score_ram.py",
    "score_clip.py",
    "calibrate_combined.py",
    "build_scores.py",
]


def main() -> None:
    for step in STEPS:
        script = SCRIPTS_DIR / step
        print(f"\n{'='*55}")
        print(f"  {step}")
        print(f"{'='*55}")
        result = subprocess.run([sys.executable, str(script)])
        if result.returncode != 0:
            print(f"\nFEIL: {step} avsluttet med kode {result.returncode}. Stopper.")
            sys.exit(result.returncode)

    print(f"\n{'='*55}")
    print("  Pipeline ferdig.")
    print(f"{'='*55}")


if __name__ == "__main__":
    main()
