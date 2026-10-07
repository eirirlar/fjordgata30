"""T160 verifier for `forretningsplan/lover/`.

Same pipeline as T158 (curl + pup + html2text + diff) targeting the parallel
mval-paragraph collection used by the MVA-strategy. Reuses shared normalize /
pup_extract / html2md / fetch functions from `t158_verify_lovverk`.

The forretningsplan/lover/ files use a slightly different format than
bakgrunn/lovverk/:
  - Bold ledd-markers: `**(1)**` instead of `(1)`
  - Letter list items with closing paren: `a)` instead of `a.`
  - Trailing "## Relevans for FG30" section with project commentary

Normalization strips bold-emphasis and the Relevans-section; a letter-with-
paren rule is added below to canonicalize `a)` -> `a.`.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import t158_verify_lovverk as t158

ROOT = Path(__file__).resolve().parent.parent
TARGET_DIR = ROOT / "forretningsplan" / "lover"
TMP = ROOT / "tmp_lovdata"
TMP.mkdir(exist_ok=True)

SPEC = [
    ("mval", "2-1", "https://lovdata.no/lov/2009-06-19-58/%C2%A72-1", "mval_2-1_registreringsplikt.md"),
    ("mval", "2-3", "https://lovdata.no/lov/2009-06-19-58/%C2%A72-3", "mval_2-3_frivillig_registrering.md"),
    ("mval", "3-11", "https://lovdata.no/lov/2009-06-19-58/%C2%A73-11", "mval_3-11_fast_eiendom.md"),
    ("mval", "8-1", "https://lovdata.no/lov/2009-06-19-58/%C2%A78-1", "mval_8-1_fradragsrett.md"),
    ("mval", "8-2", "https://lovdata.no/lov/2009-06-19-58/%C2%A78-2", "mval_8-2_forholdsvis_fradrag.md"),
    ("mval", "8-6", "https://lovdata.no/lov/2009-06-19-58/%C2%A78-6", "mval_8-6_tilbakegaende_avgiftsoppgjor.md"),
    ("mval", "9-1", "https://lovdata.no/lov/2009-06-19-58/%C2%A79-1", "mval_9-1_kapitalvarer.md"),
    ("mval", "9-4", "https://lovdata.no/lov/2009-06-19-58/%C2%A79-4", "mval_9-4_justeringsperiode.md"),
]


# Canonicalize letter list items with closing paren -> period.
RE_LETTER_PAREN = re.compile(r"(^|\n)([a-z])\)([ \t]+)", re.MULTILINE)


def normalize_fp(text: str) -> str:
    """Normalize to the same canonical form T158 uses, plus `a)` -> `a.`."""
    text = RE_LETTER_PAREN.sub(r"\1\2.\3", text)
    return t158.normalize(text)


def process(lov: str, nr: str, url: str, fname: str, html_cache: dict):
    existing = TARGET_DIR / fname
    html_path = TMP / f"{lov}_{nr}.html"
    md_path = TMP / f"fp_{lov}_{nr}.md"
    expected_path = TMP / f"fp_{lov}_{nr}.expected.md"

    if url in html_cache:
        html_path = html_cache[url]
    else:
        t158.fetch(url, html_path)
        html_cache[url] = html_path

    selector = f"div#PARAGRAF_{nr}"
    block = t158.pup_extract(html_path, selector)
    if not block.strip():
        return {"status": "ERROR", "note": f"pup returned empty for {selector}", "url": url}

    md = t158.html2md(block)
    md_path.write_text(md, encoding="utf-8")

    if not existing.exists():
        return {"status": "MISSING_FILE", "note": "existing file not found", "url": url}

    existing_body = t158.extract_lovtext_from_file(existing)
    norm_lovdata = normalize_fp(md)
    norm_existing = normalize_fp(existing_body)
    expected_path.write_text(norm_lovdata, encoding="utf-8")
    existing_norm_path = TMP / f"fp_{lov}_{nr}.existing.norm.md"
    existing_norm_path.write_text(norm_existing, encoding="utf-8")

    if norm_lovdata == norm_existing:
        return {"status": "MATCH", "url": url}

    diff = subprocess.run(
        ["diff", "-u", str(existing_norm_path), str(expected_path)],
        capture_output=True, text=True, encoding="utf-8",
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

    (TMP / "t160_results.json").write_text(
        json.dumps(results, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    stats = {}
    for r in results:
        stats[r["status"]] = stats.get(r["status"], 0) + 1
    sys.stderr.write(f"\nSummary: {stats}\n")


if __name__ == "__main__":
    main()
