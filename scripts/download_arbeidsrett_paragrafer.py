"""Last ned arbeidsretts-paragrafer fra Lovdata verbatim.

Følger samme format som eksisterende filer i bakgrunn/lovverk/ (T158).
Bruker curl via subprocess, parser med BeautifulSoup.
"""
import subprocess
import re
import tempfile
from pathlib import Path
from bs4 import BeautifulSoup

OUTPUT_DIR = Path("bakgrunn/lovverk")
TODAY_NOR = "5. november 2026"

AML = {
    "short": "Arbeidsmiljøloven",
    "full": "Lov om arbeidsmiljø, arbeidstid og stillingsvern mv. (arbeidsmiljøloven) av 17. juni 2005 nr. 62",
    "lov_date": "2005-06-17-62",
}
FERIELOVEN = {
    "short": "Ferieloven",
    "full": "Lov om ferie (ferieloven) av 29. april 1988 nr. 21",
    "lov_date": "1988-04-29-21",
}
FTRL = {
    "short": "Folketrygdloven",
    "full": "Lov om folketrygd (folketrygdloven) av 28. februar 1997 nr. 19",
    "lov_date": "1997-02-28-19",
}
YSKL = {
    "short": "Yrkesskadeforsikringsloven",
    "full": "Lov om yrkesskadeforsikring av 16. juni 1989 nr. 65",
    "lov_date": "1989-06-16-65",
}
OTPL = {
    "short": "OTP-loven",
    "full": "Lov om obligatorisk tjenestepensjon av 21. desember 2005 nr. 124",
    "lov_date": "2005-12-21-124",
}

# (meta, paragraf-i-URL, PARAGRAF-id-i-HTML, filnavn, kort_beskrivelse_for_tittel)
PARAGRAFER = [
    (AML, "6-1", "6-1", "aml_6-1_verneombud.md", "Verneombud"),
    (AML, "10-6", "10-6", "aml_10-6_overtidstillegg.md", "Overtid"),
    (AML, "10-9", "10-9", "aml_10-9_pauser.md", "Pauser"),
    (AML, "14-4a", "14-4a", "aml_14-4a_rett_til_faktisk_stilling.md", "Rett til stilling for deltidsansatte tilsvarende faktisk arbeidstid"),
    (AML, "14-5", "14-5", "aml_14-5_krav_skriftlig_arbeidsavtale.md", "Krav om skriftlig arbeidsavtale"),
    (AML, "14-6", "14-6", "aml_14-6_minimumskrav_arbeidsavtale.md", "Minimumskrav til innholdet i den skriftlige arbeidsavtalen"),
    (AML, "14-8a", "14-8a", "aml_14-8a_forutsigbare_arbeidsvilkar.md", "Forespørsel om mer forutsigbare og trygge arbeidsvilkår"),
    (AML, "14-9", "14-9", "aml_14-9_midlertidig_ansettelse.md", "Fast og midlertidig ansettelse"),
    (AML, "14-11", "14-11", "aml_14-11_konsekvens_ulovlig_midlertidighet.md", "Virkninger av brudd på reglene om fast og midlertidig ansettelse"),
    (AML, "15-3", "15-3", "aml_15-3_oppsigelsesfrister.md", "Oppsigelsesfrister"),
    (AML, "15-7", "15-7", "aml_15-7_saklig_grunn.md", "Vern mot usaklig oppsigelse"),
    (FERIELOVEN, "10", "10", "ferieloven_10_feriepengegrunnlag.md", "Feriepengenes størrelse"),
    (FTRL, "8-19", "8-19", "folketrygdloven_8-19_arbeidsgiverperiode.md", "Arbeidsgiverperioden"),
    (FTRL, "8-30", "8-30", "folketrygdloven_8-30_sykepengegrunnlag.md", "Fastsetting av sykepengegrunnlaget"),
    (YSKL, "3", "3", "yrkesskadeforsikringsloven_3_forsikringsplikt.md", "Hvem som har forsikringsplikt"),
    (OTPL, "1", "1", "otp_loven_1_formal.md", "Formål"),
]


def fetch_html(url: str) -> str:
    """Last ned URL med curl, følg redirects."""
    with tempfile.NamedTemporaryFile(suffix=".html", delete=False) as tmp:
        tmp_path = tmp.name
    try:
        result = subprocess.run(
            ["curl", "-s", "-L", "-A", "Mozilla/5.0", url, "-o", tmp_path],
            capture_output=True,
            timeout=60,
        )
        if result.returncode != 0:
            raise RuntimeError(f"curl exit {result.returncode}: {result.stderr.decode()}")
        with open(tmp_path, "r", encoding="utf-8") as f:
            return f.read()
    finally:
        Path(tmp_path).unlink(missing_ok=True)


def extract_paragraph(html: str, para_id: str):
    """Ekstraher paragraf fra Lovdata-HTML.

    Lovdata-struktur:
      <div id="PARAGRAF_X-Y" class="paragraf">
        <h3 class="paragrafHeader">§ X-Y.Tittel</h3>
        <table class="... avsnitt">(1) Ledd-tekst</table>
        <table class="... avsnitt">(2) Ledd-tekst</table>
        ...
        <table class="textList fotnote avsnitt liste">Endret ved...</table>
      </div>

    Returnerer (overskrift, [(ledd-nr, ledd-tekst), ...])
    """
    soup = BeautifulSoup(html, "html.parser")
    div = soup.find("div", id=f"PARAGRAF_{para_id}")
    if div is None:
        return None

    # Overskrift
    h = div.find(["h2", "h3", "h4"], class_="paragrafHeader")
    if h is None:
        h = div.find(["h2", "h3", "h4"])
    heading = h.get_text(" ", strip=True) if h else f"§ {para_id}"
    # Normaliser mellomrom: "§ 10-6.Overtid" -> "§ 10-6. Overtid"
    heading = re.sub(r"\.(\S)", r". \1", heading)

    # Ledd — både <table class="avsnitt"> (aml, mval) og <p class="avsnitt"> (folketrygdloven)
    ledd_list = []
    for el in div.find_all(["table", "p"]):
        classes = el.get("class", [])
        if "avsnitt" not in classes:
            continue
        # Skip fotnote-tabeller
        if "fotnote" in classes or "liste" in classes:
            continue
        text = el.get_text(" ", strip=True)
        text = re.sub(r"\s+", " ", text)
        if not text:
            continue
        # Hent ledd-nummer hvis det starter med (N)
        m = re.match(r"^\((\d+)\)\s*(.*)", text)
        if m:
            ledd_num = int(m.group(1))
            ledd_text = m.group(2).strip()
        else:
            ledd_num = None
            ledd_text = text
        ledd_list.append((ledd_num, ledd_text))

    return heading, ledd_list


def format_md(meta, para_num_display, para_id, filename, description, heading, ledd_list):
    url = f"https://lovdata.no/lov/{meta['lov_date']}/%C2%A7{para_id}"
    body_lines = []
    for ledd_num, ledd_text in ledd_list:
        if ledd_num is not None:
            body_lines.append(f"({ledd_num}) {ledd_text}")
        else:
            body_lines.append(ledd_text)
    body = "\n\n".join(body_lines)

    return f"""# {meta['short']} § {para_num_display} – {description}

**Lov:** {meta['full']}\\
**Kilde:** <{url}>\\
**Hentet:** {TODAY_NOR}

---

## Lovtekst (verbatim)

**{heading}**

{body}
"""


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    results = []

    for meta, para_url, para_id, filename, description in PARAGRAFER:
        url = f"https://lovdata.no/lov/{meta['lov_date']}/%C2%A7{para_url}"
        print(f"\n[{filename}]")
        print(f"  URL: {url}")

        try:
            html = fetch_html(url)
        except Exception as e:
            print(f"  FEIL ved nedlasting: {e}")
            results.append((filename, False, f"download: {e}"))
            continue

        if len(html) < 500:
            print(f"  FEIL: HTML for liten ({len(html)} bytes)")
            results.append((filename, False, "html too small"))
            continue

        result = extract_paragraph(html, para_id)
        if result is None:
            print(f"  FEIL: fant ikke PARAGRAF_{para_id} i HTML")
            debug_path = OUTPUT_DIR / f"DEBUG_{filename}.html"
            debug_path.write_text(html, encoding="utf-8")
            print(f"  (lagret debug-HTML til {debug_path})")
            results.append((filename, False, "extract failed"))
            continue

        heading, ledd_list = result
        if not ledd_list:
            print(f"  ADVARSEL: fant ingen ledd")
        md = format_md(meta, para_url.replace("a", " a").replace("b", " b"), para_id, filename, description, heading, ledd_list)
        out_path = OUTPUT_DIR / filename
        out_path.write_text(md, encoding="utf-8")
        print(f"  OK: {len(ledd_list)} ledd, {len(md)} tegn")
        results.append((filename, True, f"{len(ledd_list)} ledd"))

    print("\n\n=== SAMMENDRAG ===")
    ok_count = sum(1 for _, ok, _ in results if ok)
    print(f"OK: {ok_count}/{len(results)}")
    for fn, ok, info in results:
        status = "OK " if ok else "FEIL"
        print(f"  [{status}] {fn}  ({info})")


if __name__ == "__main__":
    main()
