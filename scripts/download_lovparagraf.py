"""
Last ned en lovparagraf fra lovdata.no og lagre som .md i bakgrunn/lovverk/.
Bruker curl via subprocess + BeautifulSoup for parsing.
Dependencies: beautifulsoup4, lxml (installeres via uv run --with).
"""
import re
import subprocess
import sys
from pathlib import Path
from bs4 import BeautifulSoup


def download(url: str) -> str:
    result = subprocess.run(
        ["curl", "-s", "-L", "-A", "Mozilla/5.0 (fjordgata30-prosjekt)", url],
        capture_output=True,
        text=False,
        check=True,
    )
    return result.stdout.decode("utf-8")


def extract_paragraf(html: str, paragraf_id: str) -> tuple[str, str, list[tuple[str, str]]]:
    soup = BeautifulSoup(html, "lxml")
    sec = soup.find(id=f"PARAGRAF_{paragraf_id}")
    if sec is None:
        raise ValueError(f"Fant ikke PARAGRAF_{paragraf_id}")

    heading = sec.find(["h3", "h4", "h2"])
    heading_text = heading.get_text(" ", strip=True) if heading else ""

    # Split § number from title: "§ 9-3.Overføring av..." or "§ 9-3. Overføring av..."
    m = re.match(r"(§\s*[\d\-a-z]+)\.?\s*(.+)", heading_text)
    if m:
        paragraf_label = m.group(1).strip()
        title = m.group(2).strip()
    else:
        paragraf_label = heading_text
        title = ""

    # Collect leddene — each is in a <p> or similar; use (N) markers
    # Simpler: get entire section text, then clean up
    full_text = sec.get_text("\n", strip=True)
    lines = [ln.strip() for ln in full_text.split("\n") if ln.strip()]

    # Drop heading lines (first 2) and trailing "Del paragraf"/🔗
    body_lines = []
    i = 0
    # skip heading tokens
    while i < len(lines) and (lines[i].startswith("§") or lines[i] == title):
        i += 1

    # Group ledd: pattern is "(N)" line followed by content lines until next "(N+1)"
    # Lovdata marks endringsnoter med en linje "0" etterfulgt av "Endret ved ..." eller "Opphevet ..."
    ledd: list[tuple[str, list[str]]] = []
    current_num: str | None = None
    current_lines: list[str] = []
    in_endringsnotat = False
    unnumbered_lines: list[str] = []
    while i < len(lines):
        ln = lines[i]
        if ln in ("🔗", "Del paragraf"):
            i += 1
            continue
        if ln == "0":
            # Markør for endringsnoter — alt etter dette ignoreres
            in_endringsnotat = True
            i += 1
            continue
        if in_endringsnotat:
            i += 1
            continue
        m2 = re.match(r"^\((\d+)\)$", ln)
        if m2:
            if current_num is not None:
                ledd.append((current_num, current_lines))
            current_num = m2.group(1)
            current_lines = []
            i += 1
            continue
        if current_num is None:
            unnumbered_lines.append(ln)
        else:
            current_lines.append(ln)
        i += 1
    if current_num is not None:
        ledd.append((current_num, current_lines))

    # Hvis paragrafen ikke har (N)-markører: samle hele teksten som ett ledd uten nummer
    if not ledd and unnumbered_lines:
        ledd = [("", unnumbered_lines)]

    ledd_text: list[tuple[str, str]] = []
    for num, parts in ledd:
        text = " ".join(parts)
        text = re.sub(r"\s+", " ", text).strip()
        ledd_text.append((num, text))

    return paragraf_label, title, ledd_text


def format_md(
    paragraf_label: str,
    title: str,
    ledd_text: list[tuple[str, str]],
    lov_tittel: str,
    lov_dato_nr: str,
    url: str,
    hentedato: str,
) -> str:
    body = []
    body.append(f"# {lov_tittel.split('(')[0].strip()} {paragraf_label} – {title}")
    body.append("")
    body.append(f"**Lov:** {lov_tittel}\\")
    body.append(f"**Kilde:** <{url}>\\")
    body.append(f"**Hentet:** {hentedato} (via curl + Python-parsing)")
    body.append("")
    body.append("---")
    body.append("")
    body.append("## Lovtekst (verbatim)")
    body.append("")
    body.append(f"**{paragraf_label}. {title}**")
    body.append("")
    for num, text in ledd_text:
        if num:
            body.append(f"({num}) {text}")
        else:
            body.append(text)
        body.append("")
    return "\n".join(body).rstrip() + "\n"


LOVER = {
    "mval": {
        "tittel": "Lov om merverdiavgift (merverdiavgiftsloven) av 19. juni 2009 nr. 58",
        "dato_nr": "2009-06-19-58",
    },
    "asl": {
        "tittel": "Lov om aksjeselskaper (aksjeloven) av 13. juni 1997 nr. 44",
        "dato_nr": "1997-06-13-44",
    },
    "sktl": {
        "tittel": "Lov om skatt av formue og inntekt (skatteloven) av 26. mars 1999 nr. 14",
        "dato_nr": "1999-03-26-14",
    },
}


def main():
    if len(sys.argv) != 4:
        print("Bruk: download_lovparagraf.py <lov_kortnavn> <paragraf_nr> <output_filename>")
        print("  f.eks: download_lovparagraf.py mval 9-3 mval_9-3_overforing_rett_plikt_justering.md")
        sys.exit(1)

    lov = sys.argv[1]
    paragraf_nr = sys.argv[2]
    out_name = sys.argv[3]

    if lov not in LOVER:
        print(f"Ukjent lov: {lov}. Tilgjengelige: {list(LOVER)}")
        sys.exit(1)

    lov_info = LOVER[lov]
    url = f"https://lovdata.no/lov/{lov_info['dato_nr']}/%C2%A7{paragraf_nr}"

    print(f"Laster ned {lov} § {paragraf_nr} fra {url}")
    html = download(url)

    paragraf_label, title, ledd = extract_paragraf(html, paragraf_nr)
    print(f"Parsed: {paragraf_label} — {title} ({len(ledd)} ledd)")

    md = format_md(
        paragraf_label,
        title,
        ledd,
        lov_info["tittel"],
        lov_info["dato_nr"],
        url,
        "13. oktober 2026",
    )

    out_path = Path("bakgrunn/lovverk") / out_name
    out_path.write_text(md, encoding="utf-8")
    print(f"Lagret: {out_path}")


if __name__ == "__main__":
    main()
