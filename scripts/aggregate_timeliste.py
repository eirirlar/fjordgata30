"""
Aggregates HRP timeliste from XledgerData Excel export.

Usage:
    uv run python timer/aggregate_timeliste.py [--input FILE] [--output FILE]

Defaults:
    --input  timer/HRP - Timeliste 26.06.2026.xlsx
    --output timer/hrp_timeliste_aggregert.md
"""

import argparse
import openpyxl
from collections import defaultdict
from datetime import datetime


KNOWN_ACTIVITY_LABELS = {
    "Prosjektleder":     "PGL – Prosjektledelse",
    "Energikartlegging": "RiEn – Energikartlegging",
    "Rib HRP":           "RiB – Konstruksjon",
    "RIE":               "RIE – Elektrisk",
    "RIVa":              "RIVa – VA/VVS",
    "RiVent":            "RiVent – Ventilasjon",
}

MONTHS_NO = {
    "2026-01": "jan",
    "2026-02": "feb",
    "2026-03": "mar",
    "2026-04": "apr",
    "2026-05": "mai",
    "2026-06": "jun",
    "2026-07": "jul",
    "2026-08": "aug",
    "2026-09": "sep",
    "2026-10": "okt",
    "2026-11": "nov",
    "2026-12": "des",
}


def fix_encoding(s):
    """Repair mojibake caused by latin-1/utf-8 mismatch in xlsx export."""
    if isinstance(s, str):
        try:
            return s.encode("latin-1").decode("utf-8")
        except (UnicodeDecodeError, UnicodeEncodeError):
            return s
    return s


def load_data(path):
    wb = openpyxl.load_workbook(path)
    ws = wb.active
    rows = list(ws.iter_rows(values_only=True))
    header = rows[0]
    records = []
    for row in rows[1:]:
        r = {h: fix_encoding(v) for h, v in zip(header, row)}
        if not any(r.values()):
            continue
        records.append(r)
    return records


def parse_person(raw):
    """Return (emp_id, name) from '1172 - Ole Morten Lagmannssveen'."""
    if " - " in str(raw):
        emp_id, name = raw.split(" - ", 1)
        return emp_id.strip(), name.strip()
    return str(raw), str(raw)


def normalize_person(name):
    """Merge duplicate employee registrations for same person."""
    return name.strip()


def month_key(dt):
    if isinstance(dt, datetime):
        return dt.strftime("%Y-%m")
    return str(dt)[:7]


def build_summary(records):
    """Return nested dict: person -> month -> activity -> hours."""
    summary = defaultdict(lambda: defaultdict(lambda: defaultdict(float)))
    descriptions = defaultdict(lambda: defaultdict(list))

    for r in records:
        emp_id, person = parse_person(r["Ansatt"])
        month = month_key(r["Dato"])
        activity = (r["Aktivitet"] or "").strip().rstrip()
        hours = float(r["Timer"]) if r["Timer"] else 0.0
        text = (r["Tekst"] or "").strip()

        summary[person][month][activity] += hours
        if text and text.lower() not in (
            "fjordgata 30, minilager",
            "fjordgata 30, minilager, befaring, møte",
            "beskrivelse",
        ):
            descriptions[person][month].append((r["Dato"], activity, hours, text))

    return summary, descriptions


def all_months(summary):
    months = set()
    for person_data in summary.values():
        months.update(person_data.keys())
    return sorted(months)


def fmt_hours(h):
    return f"{h:.1f}" if h else ""


def generate_markdown(records, summary, descriptions, source_file):
    months = all_months(summary)
    month_labels = [MONTHS_NO.get(m, m) for m in months]

    lines = []
    lines.append("# HRP Timeliste – aggregert oversikt")
    lines.append("")
    if records:
        dates = [r["Dato"] for r in records if r["Dato"]]
        if dates:
            d_min = min(d for d in dates if isinstance(d, datetime))
            d_max = max(d for d in dates if isinstance(d, datetime))
            lines.append(
                f"**Periode:** {d_min.strftime('%d.%m.%Y')} – {d_max.strftime('%d.%m.%Y')}  "
            )
    total_hours = sum(
        h
        for pd in summary.values()
        for md in pd.values()
        for h in md.values()
    )
    lines.append(f"**Totalt:** {total_hours:.1f} timer  ")
    lines.append(f"**Kilde:** {source_file}  ")
    lines.append(f"**Generert:** {datetime.today().strftime('%Y-%m-%d')}")
    lines.append("")

    # --- Summary table: person x month ---
    lines.append("## Sammendrag per person")
    lines.append("")
    header_cols = ["Person", "Fagdisiplin"] + month_labels + ["Totalt"]
    lines.append("| " + " | ".join(header_cols) + " |")
    lines.append("|" + "|".join([" --- "] * len(header_cols)) + "|")

    for person in sorted(summary.keys()):
        person_data = summary[person]
        # Infer discipline from activity types used
        all_acts = set()
        for md in person_data.values():
            all_acts.update(md.keys())
        discipline = " / ".join(
            KNOWN_ACTIVITY_LABELS.get(a, a) for a in sorted(all_acts)
        )

        month_totals = []
        for m in months:
            h = sum(person_data.get(m, {}).values())
            month_totals.append(fmt_hours(h))

        grand_total = sum(
            h for md in person_data.values() for h in md.values()
        )
        row = [person, discipline] + month_totals + [f"**{grand_total:.1f}**"]
        lines.append("| " + " | ".join(row) + " |")

    # Total row
    month_grand = []
    for m in months:
        h = sum(
            sum(md.get(m, {}).values())
            for md in summary.values()
        )
        month_grand.append(fmt_hours(h) if h else "")
    lines.append(
        "| **Totalt** | | "
        + " | ".join(month_grand)
        + f" | **{total_hours:.1f}** |"
    )
    lines.append("")

    # --- Summary table: activity x month ---
    lines.append("## Sammendrag per aktivitet")
    lines.append("")
    all_acts = set()
    for pd in summary.values():
        for md in pd.values():
            all_acts.update(md.keys())
    all_acts = sorted(all_acts)

    act_header = ["Aktivitet"] + month_labels + ["Totalt", "Utøvere"]
    lines.append("| " + " | ".join(act_header) + " |")
    lines.append("|" + "|".join([" --- "] * len(act_header)) + "|")

    for act in all_acts:
        month_vals = []
        for m in months:
            h = sum(
                pd.get(m, {}).get(act, 0)
                for pd in summary.values()
            )
            month_vals.append(fmt_hours(h) if h else "")
        act_total = sum(
            pd.get(m, {}).get(act, 0)
            for pd in summary.values()
            for m in months
        )
        performers = sorted(
            p for p, pd in summary.items()
            if any(act in md for md in pd.values())
        )
        performers_str = ", ".join(p.split()[0] for p in performers)
        label = KNOWN_ACTIVITY_LABELS.get(act, act)
        row = [label] + month_vals + [f"**{act_total:.1f}**", performers_str]
        lines.append("| " + " | ".join(row) + " |")

    lines.append("")

    # --- Per-person detail ---
    lines.append("## Detaljert logg per person")
    lines.append("")

    for person in sorted(summary.keys()):
        person_data = summary[person]
        grand_total = sum(h for md in person_data.values() for h in md.values())
        all_acts_p = set()
        for md in person_data.values():
            all_acts_p.update(md.keys())
        discipline = " / ".join(
            KNOWN_ACTIVITY_LABELS.get(a, a) for a in sorted(all_acts_p)
        )

        lines.append(f"### {person}")
        lines.append(f"**Disiplin:** {discipline}  ")
        lines.append(f"**Totalt:** {grand_total:.1f} timer")
        lines.append("")

        # Activity breakdown for this person
        if len(all_acts_p) > 1:
            lines.append("**Timer per aktivitet:**")
            for act in sorted(all_acts_p):
                act_h = sum(
                    person_data.get(m, {}).get(act, 0) for m in months
                )
                if act_h:
                    label = KNOWN_ACTIVITY_LABELS.get(act, act)
                    lines.append(f"- {label}: {act_h:.1f} t")
            lines.append("")

        # Monthly log with concatenated descriptions
        desc_data = descriptions.get(person, {})
        for m in sorted(person_data.keys()):
            m_total = sum(person_data[m].values())
            lines.append(f"**{MONTHS_NO.get(m, m).capitalize()} {m[:4]} – {m_total:.1f} t**")
            entries = sorted(desc_data.get(m, []), key=lambda x: x[0] or datetime.min)
            if entries:
                for dt, act, hrs, txt in entries:
                    date_str = dt.strftime("%d.%m") if isinstance(dt, datetime) else str(dt)
                    act_short = act.strip().replace("Rib HRP", "RiB")
                    lines.append(f"- {date_str} [{act_short}] {hrs:.1f}t – {txt}")
            else:
                lines.append("_(ingen beskrivelse registrert)_")
            lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Aggregate HRP timeliste to Markdown")
    parser.add_argument(
        "--input",
        default="timer/HRP - Timeliste 26.06.2026.xlsx",
        help="Path to input .xlsx file",
    )
    parser.add_argument(
        "--output",
        default="timer/hrp_timeliste_aggregert.md",
        help="Path to output .md file",
    )
    args = parser.parse_args()

    records = load_data(args.input)
    summary, descriptions = build_summary(records)
    md = generate_markdown(records, summary, descriptions, args.input)

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(md)

    print(f"Skrevet til {args.output}")
    persons = len(summary)
    total = sum(h for pd in summary.values() for md in pd.values() for h in md.values())
    print(f"  {len(records)} rader, {persons} personer, {total:.1f} timer totalt")


if __name__ == "__main__":
    main()
