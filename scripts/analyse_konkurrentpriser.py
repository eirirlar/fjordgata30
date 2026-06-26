"""
Weighted competitive price analysis for Fjordgata 30 Minilager.

FG30 units: Micro ~1.7 m2 (22 units), Standard ~2.1 m2 (432 units), Medium+ ~2.9 m2 (51 units).
Weights competitor data by proximity to FG30's typical unit size using a Gaussian function.

Usage: uv run python scripts/analyse_konkurrentpriser.py
Output: data/konkurrent_analyse.md
Config: data/comp_weights.conf
"""

import csv
import json
import math
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).parent.parent
CSV_PATH = ROOT / "data" / "konkurrent_priser.csv"
OUT_PATH = ROOT / "data" / "konkurrent_analyse.md"
CONF_PATH = ROOT / "data" / "comp_weights.conf"

_conf = json.loads(CONF_PATH.read_text(encoding="utf-8"))

FG30_CENTER = _conf["fg30_center_m2"]
FG30_SIGMA = _conf["fg30_sigma_m2"]
FG30_HEIGHT = _conf["fg30_height_m"]
SKRATAK_PENALTY = _conf["skratak_penalty"]
ESTIMATE_PENALTY = _conf["estimate_penalty"]


def gauss(x: float) -> float:
    return math.exp(-((x - FG30_CENTER) ** 2) / (2 * FG30_SIGMA ** 2))


def load_csv() -> list[dict]:
    with open(CSV_PATH, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def should_exclude(row: dict) -> bool:
    """Drop unreliable or duplicate rows."""
    n = row["notater"]
    if "USIKKERT" in n and "ikke bruk i analyse" in n:
        return True
    return False


def effective(row: dict) -> tuple[float, float, str]:
    """
    Return (effective_m2, effective_kr_kvm_mnd, correction_note).

    Correction applied only for skratak: recalculate effective floor area from m3 volume.
    High ceiling gives no price adjustment — extra height above TEK17 standard adds no value.
    """
    m2 = float(row["storrelse_m2"])
    kr_kvm = float(row["kr_kvm_mnd"])
    unit_type = row["type"]
    m3_raw = row["storrelse_m3"].strip()

    if unit_type == "skratak" and m3_raw:
        m3 = float(m3_raw)
        eff_m2 = m3 / FG30_HEIGHT
        eff_kr_kvm = float(row["kr_mnd"]) / eff_m2
        return eff_m2, eff_kr_kvm, f"skratak → {eff_m2:.1f} m² eff. ({m3:.1f} m³ ÷ {FG30_HEIGHT} m)"

    return m2, kr_kvm, ""


def run():
    rows = [r for r in load_csv() if not should_exclude(r)]

    indoor, containers = [], []
    for r in rows:
        (containers if r["type"] == "container" else indoor).append(r)

    actor_points: dict[str, list[dict]] = defaultdict(list)
    for r in indoor:
        eff_m2, eff_kr_kvm, note = effective(r)
        size_w = gauss(eff_m2)
        type_penalty = SKRATAK_PENALTY if r["type"] == "skratak" else 1.0
        if r["kilde_type"] == "visuelt_estimat_screenshot":
            type_penalty *= ESTIMATE_PENALTY
        total_w = size_w * type_penalty

        actor_points[r["aktor"]].append({
            "bod": r["bod_id"],
            "eff_m2": eff_m2,
            "eff_kr_kvm": eff_kr_kvm,
            "size_w": size_w,
            "type_p": type_penalty,
            "total_w": total_w,
            "type": r["type"],
            "kilde": r["kilde_type"],
            "note": note,
            "avstand": float(r["avstand_sentrum_km"]),
        })

    results = []
    for actor, pts in sorted(actor_points.items()):
        tw = sum(p["total_w"] for p in pts)
        wkr = sum(p["eff_kr_kvm"] * p["total_w"] for p in pts) / tw if tw > 1e-9 else None
        meaningful = sum(1 for p in pts if p["size_w"] > 0.05)
        results.append({
            "actor": actor,
            "wkr": wkr,
            "n": len(pts),
            "meaningful": meaningful,
            "avstand": pts[0]["avstand"],
            "is_estimate": any(p["kilde"] == "visuelt_estimat_screenshot" for p in pts),
            "no_range_data": meaningful == 0,
            "pts": pts,
        })

    results.sort(key=lambda r: r["wkr"] if r["wkr"] is not None else 9999)
    return results, containers


def render_md(results: list[dict], containers: list[dict]) -> str:
    lines = []

    lines += [
        "# Konkurranseanalyse – Fjordgata 30 Minilager",
        "",
        "*Generert av `scripts/analyse_konkurrentpriser.py`. Data: `data/konkurrent_priser.csv`.*",
        "",
        "## Analysemetode",
        "",
        "**FG30-boder:**",
        "| Kategori | Størrelse | Antall |",
        "|---|---|---|",
        "| Micro | ~1,7 m² | 22 |",
        "| Standard | ~2,1 m² | 432 |",
        "| Medium+ | ~2,9 m² | 51 |",
        "",
        f"**Størrelsesvekting:** Gaussisk forfall sentrert på {FG30_CENTER} m² (σ = {FG30_SIGMA} m²).",
        "Enheter på 2,1 m² får vekt 1,0; vekten faller raskt med avstand fra FG30s typiske bodstørrelse.",
        "",
        "| Størrelse (m²) | Gaussvekt |",
        "|---|---|",
    ]
    for s in [1.0, 1.7, 2.1, 2.9, 4.0, 5.0, 7.0]:
        lines.append(f"| {s:.1f} | {gauss(s):.3f} |")

    lines += [
        "",
        "**Arealkorreksjoner:**",
        f"- *Skrå tak* (skratak): Effektiv m² = m³ ÷ {FG30_HEIGHT} m; vekt ganges med {SKRATAK_PENALTY} (lavere brukervennlighet)",
        f"- *Høy takhøyde*: ingen korreksjon – ekstra høyde over TEK17-standard (2,4 m) gir ikke mer verdi",
        f"- *Visuelle estimater* (Extra Minilager): ingen vektstraf – usikkerhet i areal er ikke systematisk skjevhet",
        "",
        "**Ekskludert fra analyse:**",
        "- Gammelt Green Storage-datapunkt (1,5 m²/919 kr – inkonsistent, merket USIKKERT)",
        "- Containere behandles separat (annen produkttype)",
        "",
    ]

    # Main results table
    lines += [
        "## Innendørs enheter – vektet kr/kvm/mnd",
        "",
        "| Aktør | Vektet kr/kvm/mnd | Dp totalt | Dp med vekt > 5 % | Avstand sentrum | Merknad |",
        "|---|---|---|---|---|---|",
    ]
    for r in results:
        wkr = f"**{r['wkr']:.0f}**" if r["wkr"] is not None else "–"
        note = ""
        if r["no_range_data"]:
            note = "⚠️ ingen enheter i FG30-størrelsesrange – resultat ikke representativt"
        elif r["is_estimate"]:
            note = "⚠️ størrelse estimert fra bilde (±40 %)"
        lines.append(
            f"| {r['actor']} | {wkr} | {r['n']} | {r['meaningful']} | {r['avstand']:.1f} km | {note} |"
        )
    lines += [""]

    # Per-actor detail tables
    lines += ["## Detaljer per aktør", ""]
    for r in results:
        lines.append(f"### {r['actor']}")
        lines += [
            "",
            "| Bod | Eff. m² | Eff. kr/kvm/mnd | Størrelsesvekt | Typefaktor | Totalvekt | Korreksjon |",
            "|---|---|---|---|---|---|---|",
        ]
        for p in sorted(r["pts"], key=lambda x: x["eff_m2"]):
            lines.append(
                f"| {p['bod']} | {p['eff_m2']:.2f} | {p['eff_kr_kvm']:.0f} |"
                f" {p['size_w']:.3f} | {p['type_p']:.2f} | {p['total_w']:.3f} |"
                f" {p['note'] or '–'} |"
            )
        lines.append("")

    # Container section
    lines += [
        "## Containere (separat analyse)",
        "",
        "Utemperert drive-in-container – ikke direkte sammenlignbart med FG30s innendørs boder.",
        "",
        "| Aktør | Størrelse (m²) | Kr/kvm/mnd | Kilde |",
        "|---|---|---|---|",
    ]
    for r in sorted(containers, key=lambda x: (x["aktor"], float(x["storrelse_m2"]))):
        lines.append(
            f"| {r['aktor']} | {r['storrelse_m2']} | {r['kr_kvm_mnd']} | {r['kilde_type']} |"
        )
    lines.append("")

    # Conclusion
    no_data = [r for r in results if r["no_range_data"]]

    lines += ["## Konklusjon", ""]
    if no_data:
        lines.append(
            "**Ingen data i FG30-størrelsesspenn (1,7–2,9 m²):** "
            + ", ".join(r["actor"] for r in no_data)
            + " – kan ikke sammenlignes direkte."
        )
        lines.append("")
    lines.append(
        "Aktører med periferi-lokasjon (>5 km) konkurrerer ikke med FG30 på sentralitet, "
        "men definerer markedets prisgulv for sammenlignbare enheter."
    )
    lines.append("")

    return "\n".join(lines)


if __name__ == "__main__":
    results, containers = run()

    print("\n=== VEKTET KONKURRANSEANALYSE - INNENDORS ===\n")
    print(f"{'Aktor':<32} {'Vektet kr/kvm/mnd':>20} {'Dp':>4} {'I range':>8} {'Avstand':>10}")
    print("-" * 80)
    for r in results:
        wkr = f"{r['wkr']:.0f}" if r["wkr"] is not None else "n/a"
        flag = " [NB]" if r["no_range_data"] or r["is_estimate"] else ""
        print(
            f"{r['actor']:<32} {wkr:>20} {r['n']:>4} {r['meaningful']:>8}"
            f" {str(r['avstand'])+'km':>10}{flag}"
        )
    print("\n=== CONTAINERE ===\n")
    for r in sorted(containers, key=lambda x: (x["aktor"], float(x["storrelse_m2"]))):
        print(f"  {r['aktor']} {r['bod_id']}: {r['storrelse_m2']} m2 -> {r['kr_kvm_mnd']} kr/kvm/mnd")

    md = render_md(results, containers)
    OUT_PATH.write_text(md, encoding="utf-8")
    print(f"\nSkrevet: {OUT_PATH}")
