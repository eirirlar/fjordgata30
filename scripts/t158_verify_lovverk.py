"""T158 verifier.

Pipeline per paragraph:
  curl -sL -A "Mozilla/5.0" <url> | pup --charset utf-8 'div#PARAGRAF_<nr>' | html2text

Only text normalization is done in Python (strip header line, trailing
"Del paragraf", endringshistorikk row, markdown emphasis, table separators).
HTML extraction is delegated to pup + html2text only.
"""
import os
import re
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TMP = ROOT / "tmp_lovdata"
LOVVERK = ROOT / "bakgrunn" / "lovverk"
TMP.mkdir(exist_ok=True)

# (lov_label, paragraf_id, lovdata_url, existing_filename)
SPEC = [
    # Brann- og eksplosjonsvernloven
    ("brann-eksplosjonsvernloven", "1", "https://lovdata.no/lov/2002-06-14-20/%C2%A71", "brann_eksplosjonsvernloven_1_formaal.md"),
    ("brann-eksplosjonsvernloven", "6", "https://lovdata.no/lov/2002-06-14-20/%C2%A76", "brann_eksplosjonsvernloven_6_sikringstiltak.md"),
    ("brann-eksplosjonsvernloven", "37", "https://lovdata.no/lov/2002-06-14-20/%C2%A737", "brann_eksplosjonsvernloven_37_paalegg_bruksforbud.md"),
    ("brann-eksplosjonsvernloven", "39", "https://lovdata.no/lov/2002-06-14-20/%C2%A739", "brann_eksplosjonsvernloven_39_tvangsmulkt.md"),
    ("brann-eksplosjonsvernloven", "40", "https://lovdata.no/lov/2002-06-14-20/%C2%A740", "brann_eksplosjonsvernloven_40_tvangsgjennomforing.md"),
    ("brann-eksplosjonsvernloven", "41", "https://lovdata.no/lov/2002-06-14-20/%C2%A741", "brann_eksplosjonsvernloven_41_klage.md"),
    ("brann-eksplosjonsvernloven", "42", "https://lovdata.no/lov/2002-06-14-20/%C2%A742", "brann_eksplosjonsvernloven_42_straff.md"),
    # Forskrift brannforebygging
    ("forskrift-brannforebygging", "4", "https://lovdata.no/forskrift/2015-12-17-1710/%C2%A74", "forskrift_brannforebygging_4_kunnskap_brannsikkerhet.md"),
    ("forskrift-brannforebygging", "5", "https://lovdata.no/forskrift/2015-12-17-1710/%C2%A75", "forskrift_brannforebygging_5_kontroll_bygningsdeler.md"),
    ("forskrift-brannforebygging", "6", "https://lovdata.no/forskrift/2015-12-17-1710/%C2%A76", "forskrift_brannforebygging_6_fyringsanlegg.md"),
    ("forskrift-brannforebygging", "8", "https://lovdata.no/forskrift/2015-12-17-1710/%C2%A78", "forskrift_brannforebygging_8_oppgradering.md"),
    ("forskrift-brannforebygging", "9", "https://lovdata.no/forskrift/2015-12-17-1710/%C2%A79", "forskrift_brannforebygging_9_systematisk_sikkerhetsarbeid.md"),
    # Plan- og bygningsloven
    ("pbl", "29-4", "https://lovdata.no/lov/2008-06-27-71/%C2%A729-4", "pbl_29-4_byggverkets_plassering.md"),
    ("pbl", "31-2", "https://lovdata.no/lov/2008-06-27-71/%C2%A731-2", "pbl_31-2_tiltak_eksisterende_byggverk.md"),
    ("pbl", "31-3", "https://lovdata.no/lov/2008-06-27-71/%C2%A731-3", "pbl_31-3_tiltak_strid_med_plan.md"),
    ("pbl", "31-4", "https://lovdata.no/lov/2008-06-27-71/%C2%A731-4", "pbl_31-4_unntak_tekniske_krav.md"),
    # Forvaltningsloven
    ("fvl", "11", "https://lovdata.no/lov/1967-02-10/%C2%A711", "fvl_11_veiledningsplikt.md"),
    ("fvl", "17", "https://lovdata.no/lov/1967-02-10/%C2%A717", "fvl_17_utredningsplikt.md"),
    ("fvl", "24", "https://lovdata.no/lov/1967-02-10/%C2%A724", "fvl_24_naar_begrunnes.md"),
    ("fvl", "25", "https://lovdata.no/lov/1967-02-10/%C2%A725", "fvl_25_begrunnelsens_innhold.md"),
    ("fvl", "29", "https://lovdata.no/lov/1967-02-10/%C2%A729", "fvl_29_klagefrist.md"),
    ("fvl", "41", "https://lovdata.no/lov/1967-02-10/%C2%A741", "fvl_41_virkning_feil.md"),
    ("fvl", "42", "https://lovdata.no/lov/1967-02-10/%C2%A742", "fvl_42_utsatt_iverksetting.md"),
    ("fvl", "51", "https://lovdata.no/lov/1967-02-10/%C2%A751", "fvl_51_tvangsmulkt.md"),
    # Kulturminneloven
    ("kulturminneloven", "3", "https://lovdata.no/lov/1978-06-09-50/%C2%A73", "kulturminneloven_3_forbud_inngrep.md"),
    ("kulturminneloven", "4", "https://lovdata.no/lov/1978-06-09-50/%C2%A74", "kulturminneloven_4_automatisk_fredete.md"),
    ("kulturminneloven", "8", "https://lovdata.no/lov/1978-06-09-50/%C2%A78", "kulturminneloven_8_tillatelse_inngrep.md"),
    ("kulturminneloven", "15", "https://lovdata.no/lov/1978-06-09-50/%C2%A715", "kulturminneloven_15_fredning_nyere_tid.md"),
    ("kulturminneloven", "19", "https://lovdata.no/lov/1978-06-09-50/%C2%A719", "kulturminneloven_19_fredning_omrade.md"),
    ("kulturminneloven", "20", "https://lovdata.no/lov/1978-06-09-50/%C2%A720", "kulturminneloven_20_fredning_kulturmiljo.md"),
    # Tvangsfullbyrdelsesloven
    ("tvangsfullbyrdelsesloven", "7-2", "https://lovdata.no/lov/1992-06-26-86/%C2%A77-2", "tvangsfullbyrdelsesloven_7-2_tvangsgrunnlag_utlegg.md"),
    ("tvangsfullbyrdelsesloven", "13-14", "https://lovdata.no/lov/1992-06-26-86/%C2%A713-14", "tvangsfullbyrdelsesloven_13-14_fullbyrdelsesmaate.md"),
    # Skatteloven
    ("skatteloven", "5-30", "https://lovdata.no/lov/1999-03-26-14/%C2%A75-30", "skatteloven_5-30_virksomhetsinntekt.md"),
    ("skatteloven", "14-42", "https://lovdata.no/lov/1999-03-26-14/%C2%A714-42", "skatteloven_14-42_grunnlag_avskrivning.md"),
    ("skatteloven", "14-43", "https://lovdata.no/lov/1999-03-26-14/%C2%A714-43", "skatteloven_14-43_avskrivningssatser.md"),
    # Finansavtaleloven
    ("finansavtaleloven", "1-5", "https://lovdata.no/lov/2020-12-18-146/%C2%A71-5", "finansavtaleloven_1-5.md"),
    ("finansavtaleloven", "3-1", "https://lovdata.no/lov/2020-12-18-146/%C2%A73-1", "finansavtaleloven_3-1.md"),
    # Finansforetaksloven
    ("finansforetaksloven", "13-5", "https://lovdata.no/lov/2015-04-10-17/%C2%A713-5", "finansforetaksloven_13-5_forsvarlig_virksomhet.md"),
    # Grunnloven
    ("grunnloven", "97", "https://lovdata.no/lov/1814-05-17/%C2%A797", "grunnloven_97.md"),
    ("grunnloven", "98", "https://lovdata.no/lov/1814-05-17/%C2%A798", "grunnloven_98.md"),
    # Regnskapsloven
    ("regnskapsloven", "6-2", "https://lovdata.no/lov/1998-07-17-56/%C2%A76-2", "regnskapsloven_6-2_balanse.md"),
    # Sivilombudsloven
    ("sivilombudsloven", "4", "https://lovdata.no/lov/2021-06-18-121/%C2%A74", "sivilombudsloven_4_arbeidsomrade.md"),
    ("sivilombudsloven", "8", "https://lovdata.no/lov/2021-06-18-121/%C2%A78", "sivilombudsloven_8_vilkar_klage.md"),
    ("sivilombudsloven", "9", "https://lovdata.no/lov/2021-06-18-121/%C2%A79", "sivilombudsloven_9_klagefrist.md"),
    # TEK17
    ("tek17", "12-7", "https://lovdata.no/forskrift/2017-06-19-840/%C2%A712-7", "tek17_12-7_rom_oppholdsareal.md"),
    # Merverdiavgiftsloven
    ("mval", "2-3", "https://lovdata.no/lov/2009-06-19-58/%C2%A72-3", "mval_2-3_frivillig_registrering.md"),
    ("mval", "3-1", "https://lovdata.no/lov/2009-06-19-58/%C2%A73-1", "mval_3-1_avgiftsplikt_omsetning.md"),
    ("mval", "3-11", "https://lovdata.no/lov/2009-06-19-58/%C2%A73-11", "mval_3-11_fast_eiendom.md"),
    ("mval", "8-6", "https://lovdata.no/lov/2009-06-19-58/%C2%A78-6", "mval_8-6_tilbakegaende_avgiftsoppgjor.md"),
    ("mval", "9-2", "https://lovdata.no/lov/2009-06-19-58/%C2%A79-2", "mval_9-2_overgang_justeringsforpliktelse.md"),
    # EMK art. 6 — different anchor scheme (vedlegg to menneskerettsloven)
    ("emk", "6", "https://lovdata.no/dokument/NL/lov/1999-05-21-30/emkn/ARTIKKEL_6", "emk_art_6_rettferdig_rettergang.md"),
]

# Custom pup selector per (lov, nr). Default is `div#PARAGRAF_<nr>`.
CUSTOM_SELECTORS = {
    ("emk", "6"): 'div[id="emkn/ARTIKKEL_6"]',
}


def run(cmd, stdin=None, check=True):
    env = {**os.environ, "PYTHONIOENCODING": "utf-8", "PYTHONUTF8": "1"}
    return subprocess.run(cmd, input=stdin, capture_output=True, text=True, encoding="utf-8", env=env, check=check)


def fetch(url: str, path: Path):
    if path.exists() and path.stat().st_size > 1000:
        return
    r = run(["curl", "-sL", "-A", "Mozilla/5.0", url, "-o", str(path)])
    if path.stat().st_size < 500:
        raise RuntimeError(f"Fetch failed or empty: {url}")
    time.sleep(0.3)


def pup_extract(html_path: Path, selector: str) -> str:
    r = run(["pup", "--charset", "utf-8", selector, "-f", str(html_path)])
    return r.stdout


def html2md(html: str) -> str:
    r = run(["uv", "tool", "run", "html2text"], stdin=html)
    return r.stdout


# ------------- normalization ------------- #

RE_EMPH = re.compile(r"[*_]+(?P<x>[^*_\n]+?)[*_]+")
RE_LINK = re.compile(r"\[\s*(?P<text>[^\]]+?)\s*\]\([^)]+\)")
RE_WS = re.compile(r"[ \t]+")
RE_BLANKS = re.compile(r"\n{2,}")
# Headers may wrap across lines (html2text wraps long titles). Strip the
# header line AND any following non-blank lines up to the first blank line.
RE_HEAD_BLOCK = re.compile(r"^#{1,6}\s+.*(?:\n(?!\s*$).*)*", re.MULTILINE)
RE_EXPLICIT_HEAD = re.compile(r"^\s*\*\*\s*(?:§|Art\.?|Artikkel)\s*[0-9A-Za-z\-]+\.?.*?\*\*\s*$", re.MULTILINE)
RE_TABLE_SEP = re.compile(r"^\s*-{2,}(?:\s*\|\s*-{2,})*\s*$", re.MULTILINE)
RE_DEL_PARAGRAF = re.compile(r"^\s*(?:_?🔗_?)?\s*Del paragraf.*$", re.MULTILINE)
RE_ENDRINGSHIST = re.compile(
    r"^\s*\d+\s*\|\s*.*?(?:Endret|Rettet|Oppheva|Opphevet|Endra|Tilføyd|Lagt\s+til|Føyd|opphevet).*$",
    re.MULTILINE | re.IGNORECASE,
)
RE_PIPES = re.compile(r"\s*\|\s*")
RE_SOFTBREAK = re.compile(r"\\$", re.MULTILINE)
RE_LEADING_PIPE = re.compile(r"^\s*\|\s*", re.MULTILINE)
RE_ESCAPED_DOT = re.compile(r"(\d+)\\\.")
RE_SPACE_BEFORE_PUNCT = re.compile(r"\s+([.,:;!?])")
RE_ZERO_WIDTH_SPACES = re.compile(r"[\s​]*​[\s​]*")
SUPERSCRIPT_MAP = str.maketrans({"¹": "1", "²": "2", "³": "3", "⁴": "4", "⁵": "5", "⁶": "6", "⁷": "7", "⁸": "8", "⁹": "9", "⁰": "0"})


def normalize(text: str) -> str:
    """Normalize to canonical form for verbatim comparison."""
    # strip links -> keep link text only
    text = RE_LINK.sub(lambda m: m.group("text"), text)
    # drop header block (header line + any following wrapped lines up to blank)
    text = RE_HEAD_BLOCK.sub("", text)
    text = RE_EXPLICIT_HEAD.sub("", text)
    # drop "Del paragraf" trailer
    text = RE_DEL_PARAGRAF.sub("", text)
    # drop endringshistorikk / footnote rows (before pipe conversion)
    text = RE_ENDRINGSHIST.sub("", text)
    # drop table separator rows (`---` or `--- | ---`)
    text = RE_TABLE_SEP.sub("", text)
    # pipe-separated table rows → spaces (html2text uses `a. | text` for dl)
    text = RE_PIPES.sub(" ", text)
    text = RE_LEADING_PIPE.sub("", text)
    # unescape numbered list items `1\.` -> `1.`
    text = RE_ESCAPED_DOT.sub(r"\1.", text)
    # strip trailing `\` softbreaks
    text = RE_SOFTBREAK.sub("", text)
    # strip markdown emphasis
    for _ in range(3):
        text = RE_EMPH.sub(lambda m: m.group("x"), text)
    # normalize superscript digits (m² → m2, m³ → m3 etc.)
    text = text.translate(SUPERSCRIPT_MAP)
    # strip zero-width spaces plus surrounding whitespace
    text = re.sub(r"\s*​\s*", "", text)
    # drop space before punctuation (artifact of stripped link + trailing dot)
    text = RE_SPACE_BEFORE_PUNCT.sub(r"\1", text)
    # unify non-breaking spaces and various dashes
    text = text.replace(" ", " ").replace(" ", " ").replace(" ", " ")
    text = text.replace("–", "–").replace("—", "—")
    # collapse whitespace
    text = RE_WS.sub(" ", text)
    text = "\n".join(line.rstrip() for line in text.splitlines())
    text = RE_BLANKS.sub("\n\n", text)
    # unwrap: within a paragraph (block of non-blank lines), replace single
    # newlines with spaces. Paragraph break = blank line (preserved).
    paragraphs = re.split(r"\n\s*\n", text)
    paragraphs = [RE_WS.sub(" ", p.replace("\n", " ")).strip() for p in paragraphs]
    paragraphs = [p for p in paragraphs if p]
    text = "\n\n".join(paragraphs)
    text = text.strip()
    return text


def extract_lovtext_from_file(path: Path) -> str:
    content = path.read_text(encoding="utf-8")
    # Find "## Lovtekst (verbatim)" (fallback: after `---` horizontal rule).
    m = re.search(r"^##\s+Lovtekst.*$", content, re.MULTILINE)
    start = m.end() if m else None
    if start is None:
        m = re.search(r"^---\s*$", content, re.MULTILINE)
        start = m.end() if m else 0
    body = content[start:]
    # Stop at next "## " heading (e.g. "## Relevans for FG30") or at a
    # horizontal rule followed by a heading. First check for next "## " that
    # is NOT "## Lovtekst" header we just passed.
    m = re.search(r"\n##\s+", body)
    if m:
        body = body[: m.start()]
    return body


def process(lov: str, nr: str, url: str, fname: str, html_cache: dict):
    existing = LOVVERK / fname
    html_path = TMP / f"{lov}_{nr}.html"
    md_path = TMP / f"{lov}_{nr}.md"
    expected_path = TMP / f"{lov}_{nr}.expected.md"

    if url in html_cache:
        html_path = html_cache[url]
    else:
        fetch(url, html_path)
        html_cache[url] = html_path

    selector = CUSTOM_SELECTORS.get((lov, nr), f"div#PARAGRAF_{nr}")
    block = pup_extract(html_path, selector)
    if not block.strip():
        return {"status": "ERROR", "note": f"pup returned empty for {selector}", "url": url}

    md = html2md(block)
    md_path.write_text(md, encoding="utf-8")

    if not existing.exists():
        return {"status": "MISSING_FILE", "note": "existing file not found", "url": url, "md": md}

    existing_body = extract_lovtext_from_file(existing)
    norm_lovdata = normalize(md)
    norm_existing = normalize(existing_body)
    expected_path.write_text(norm_lovdata, encoding="utf-8")
    existing_norm_path = TMP / f"{lov}_{nr}.existing.norm.md"
    existing_norm_path.write_text(norm_existing, encoding="utf-8")

    if norm_lovdata == norm_existing:
        return {"status": "MATCH", "url": url}

    # Produce a short diff summary
    diff = subprocess.run(
        ["diff", "-u", str(existing_norm_path), str(expected_path)],
        capture_output=True, text=True, encoding="utf-8"
    )
    return {
        "status": "DIFF",
        "url": url,
        "diff": diff.stdout,
        "expected_path": str(expected_path),
        "existing_norm_path": str(existing_norm_path),
    }


def main():
    results = []
    cache = {}
    for i, (lov, nr, url, fname) in enumerate(SPEC):
        sys.stderr.write(f"[{i+1}/{len(SPEC)}] {lov} § {nr} ... ")
        sys.stderr.flush()
        try:
            r = process(lov, nr, url, fname, cache)
        except Exception as e:
            r = {"status": "ERROR", "note": str(e), "url": url}
        r["lov"] = lov
        r["nr"] = nr
        r["fname"] = fname
        results.append(r)
        sys.stderr.write(f"{r['status']}\n")

    # Write summary json for the reporter
    import json
    (TMP / "t158_results.json").write_text(
        json.dumps(results, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    stats = {}
    for r in results:
        stats[r["status"]] = stats.get(r["status"], 0) + 1
    sys.stderr.write(f"\nSummary: {stats}\n")


if __name__ == "__main__":
    main()
