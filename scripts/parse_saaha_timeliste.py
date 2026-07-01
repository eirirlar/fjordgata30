"""
Parse SAAHA timeliste PDF and write CSV.

The PDF (from SAAHA-portal) is grouped by employee, with time entries per row:
    <YYYY-MM-DD> <activity> <hours> <billable-hours> <rate> <amount> <comment>

Also emits per-employee sum rows for validation purposes.

Usage:
    uv run --with pdfplumber python scripts/parse_saaha_timeliste.py \
        --pdf timer/nye/<file>.pdf \
        --out timer/saaha_timer_2026H1.csv \
        [--project "2601 Fjordgata_Minilager"]
"""

import argparse
import csv
import re
from pathlib import Path

import pdfplumber

# Rows starting with a date look like:
#   2026-03-02 Fakturerbart arbeid 1,0 1,0 1 300 1 300,00 <comment>
# Number with optional thousands-separators (spaces): "1 300" or "12 345 678"
NUM = r"\d{1,3}(?:\s?\d{3})*"
DATE_RE = re.compile(
    r"^(?P<dato>\d{4}-\d{2}-\d{2})\s+"
    r"(?P<aktivitet>\S.*?)\s+"
    r"(?P<timer>\d+[.,]\d+)\s+"
    r"(?P<fakt_timer>\d+[.,]\d+)\s+"
    rf"(?P<timepris>{NUM})\s+"
    rf"(?P<fakt_belop>{NUM}[.,]\d{{2}})"
    r"(?:\s+(?P<kommentar>.*))?$"
)
# Skip these boilerplate lines
SKIP_PREFIXES = (
    "SAAHA AS",
    "NO ",
    "Timeoversikt",
    "Periode:",
    "Vis ",
    "Prosjektleder",
    "Prosjekt ",
    "Ansatt ",
    "Timer 2026",
    "Dato ",
    "Fakt.-",
    "timer bel",
    "Fakturerbart arbeid",
    "Aktivitetssammendrag",
    "Sum NOK",
    "Sum alle",
    "lørdag ",
    "søndag ",
    "mandag ",
    "tirsdag ",
    "onsdag ",
    "torsdag ",
    "fredag ",
    "Generert",
)


def norm_number(s: str) -> str:
    """Normalize '1 300,00' -> '1300.00'."""
    return s.replace(" ", "").replace(",", ".") if s else ""


def parse_pdf(pdf_path: Path) -> list[dict]:
    rows: list[dict] = []
    current_employee: str | None = None
    project: str | None = None

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text() or ""
            for raw_line in text.splitlines():
                line = raw_line.strip()
                if not line:
                    continue

                # Track project (first occurrence of pattern "NNNN Name")
                if project is None:
                    m = re.match(r"^Prosjekt\s+(\S+\s+\S.*)$", line)
                    if m:
                        project = m.group(1).strip()
                        continue

                # Skip boilerplate
                if any(line.startswith(p) for p in SKIP_PREFIXES):
                    continue
                if line == project:
                    continue

                # Time row?
                m = DATE_RE.match(line)
                if m:
                    if current_employee is None:
                        # Time row before employee name shouldn't happen; skip safely
                        continue
                    rows.append({
                        "dato": m.group("dato"),
                        "ansatt": current_employee,
                        "prosjekt": project or "",
                        "aktivitet": m.group("aktivitet").strip(),
                        "timer": norm_number(m.group("timer")),
                        "timepris": norm_number(m.group("timepris")),
                        "fakturert_belop": norm_number(m.group("fakt_belop")),
                        "kommentar": (m.group("kommentar") or "").strip(),
                    })
                    continue

                # Anything else that isn't a number-only summary → treat as employee name
                # Employee-name lines are typically "Fornavn Etternavn" (no digits)
                if re.match(r"^[A-ZÆØÅ][a-zæøå]+(?:\s+[A-ZÆØÅ][a-zæøå'-]+)+$", line):
                    current_employee = line
                    continue

    return rows


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--pdf", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    args = ap.parse_args()

    rows = parse_pdf(args.pdf)
    if not rows:
        print("No rows parsed", flush=True)
        return

    fieldnames = ["dato", "ansatt", "prosjekt", "aktivitet",
                  "timer", "timepris", "fakturert_belop", "kommentar"]
    with args.out.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)

    # Simple summary for stdout
    print(f"Wrote {len(rows)} rows to {args.out}")
    people: dict[str, float] = {}
    for r in rows:
        people[r["ansatt"]] = people.get(r["ansatt"], 0.0) + float(r["timer"])
    for p, t in sorted(people.items()):
        print(f"  {p}: {t:.1f} timer")
    total = sum(people.values())
    print(f"  Totalt: {total:.1f} timer")


if __name__ == "__main__":
    main()
