"""Compute area totals and unit distribution from fg30_arealoversikt.csv.

The CSV layout:
- Each floor starts with a label row (e.g. "Kjeller", "1. etg")
- Numeric rows list lager-enhet sizes in kvm
- Special areas (krypkjeller, kontor) appear as a single number with a text
  annotation in the next cell
- Blank rows separate floors

Usage:
    uv run python scripts/arealoversikt.py
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

CSV_PATH = Path("forretningsplan/fg30_arealoversikt.csv")

MICRO_MAX = 2.0          # < 2.0 kvm
STANDARD_MAX = 2.4       # 2.0 <= kvm <= 2.4


def parse_num(cell: str) -> float | None:
    cell = cell.strip().replace(",", ".")
    if not cell:
        return None
    try:
        return float(cell)
    except ValueError:
        return None


def category(kvm: float) -> str:
    if kvm < MICRO_MAX:
        return "Micro (<2,0)"
    if kvm <= STANDARD_MAX:
        return "Standard (2,0–2,4)"
    return "Medium+ (2,5+)"


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]

    if not CSV_PATH.exists():
        print(f"ERROR: {CSV_PATH} not found (run from project root)")
        return 1

    with CSV_PATH.open(encoding="utf-8") as f:
        rows = list(csv.reader(f))

    by_floor: dict[str, dict] = {}
    current = None

    for row in rows:
        if not any(c.strip() for c in row):
            continue

        first = row[0].strip()
        first_num = parse_num(first)

        if first_num is None:
            current = first
            by_floor[current] = {"enheter": [], "spesial": []}
            continue

        if current is None:
            print(f"WARN: numeric row before any floor header: {row}")
            continue

        annotation = ""
        for cell in row[1:]:
            txt = cell.strip()
            if txt and parse_num(cell) is None:
                annotation = txt
                break

        if annotation:
            by_floor[current]["spesial"].append((first_num, annotation))
        else:
            nums = [n for n in (parse_num(c) for c in row) if n is not None]
            by_floor[current]["enheter"].extend(nums)

    total_lager_kvm = 0.0
    total_enheter = 0
    total_spesial_kvm = 0.0
    all_enheter: list[float] = []

    print("=" * 70)
    print("Arealoversikt – Fjordgata 30")
    print("=" * 70)

    for floor, data in by_floor.items():
        lager_kvm = sum(data["enheter"])
        lager_n = len(data["enheter"])
        print(f"\n{floor}:")
        print(f"  Lager: {lager_n} enheter, {lager_kvm:.1f} kvm")
        for kvm, ann in data["spesial"]:
            print(f"  {ann}: {kvm:.1f} kvm")
        total_lager_kvm += lager_kvm
        total_enheter += lager_n
        total_spesial_kvm += sum(k for k, _ in data["spesial"])
        all_enheter.extend(data["enheter"])

    grand_total = total_lager_kvm + total_spesial_kvm

    print("\n" + "=" * 70)
    print("TOTAL")
    print("=" * 70)
    print(f"  Lager-enheter:               {total_enheter} stk")
    print(f"  Lager-areal:                 {total_lager_kvm:.1f} kvm")
    print(f"  Spesialareal (krypk./kont.): {total_spesial_kvm:.1f} kvm")
    print(f"  Totalt utleibart areal:      {grand_total:.1f} kvm")

    print("\nFordeling per størrelseskategori:")
    cats: dict[str, list[float]] = {
        "Micro (<2,0)": [],
        "Standard (2,0–2,4)": [],
        "Medium+ (2,5+)": [],
    }
    for kvm in all_enheter:
        cats[category(kvm)].append(kvm)

    for name, lst in cats.items():
        if not lst:
            continue
        total = sum(lst)
        avg = total / len(lst)
        share_kvm = total / total_lager_kvm * 100 if total_lager_kvm else 0
        share_n = len(lst) / total_enheter * 100 if total_enheter else 0
        print(
            f"  {name:22}  {len(lst):4d} stk ({share_n:4.1f} %)"
            f"   {total:6.1f} kvm ({share_kvm:4.1f} %)"
            f"   gj.snitt {avg:.2f} kvm"
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
