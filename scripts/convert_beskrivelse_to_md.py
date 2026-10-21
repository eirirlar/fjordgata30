"""
Convert the HRP ISY NS 3420 beskrivelse PDF to Markdown.

Strategy: strip repeating page headers/footers, split by chapter and post,
and emit each post as a fenced code block that preserves the original
column layout from pdftotext. The verbatim content wins over fancy
formatting since the source is a tender document where exact wording
matters.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

PDF = Path("bakgrunn/nye/kjeller/FG30. Beskrivelse for kjeller. 19.10.2026.pdf")
OUT_MD = Path("bakgrunn/kjeller/2026-10-19_fg30_beskrivelse_kjeller.md")

HEADER_HRP = re.compile(r"^\s*HRP AS\s+19\.10\.2026\s*$")
HEADER_PROSJEKT = re.compile(r"^\s*Prosjekt: Beskrivelse kjeller")
HEADER_SIDE = re.compile(r"^\s*Side \d{2}-\d+\s*$")
HEADER_SUM_COL = re.compile(r"^\s*Sum\s*$")
HEADER_POSTNR_COL = re.compile(r"^\s*Postnr:::\s+NS-kode")
HEADER_KAPITTEL = re.compile(r"^\s*Kapittel:\s*(\d{2})\s+(.+?)\s*$")
FOOTER_SUM_SIDE = re.compile(r"^\s*Sum denne side\s*:")
FOOTER_AKKUM = re.compile(r"^\s*Akkumulert Kapittel\s+\d{2}")

POSTNR_WITH_NSCODE = re.compile(r"^(\d{2}\.\d+(?:/\d+)?)\s+([A-Z]{2}\d[A-Z0-9.]+)(?:\s+.*)?$")
POSTNR_ONLY = re.compile(r"^(\d{2}\.\d+(?:/\d+)?)\s*$")
NSCODE_ONLY = re.compile(r"^\s{5,}([A-Z]{2}\d[A-Z0-9.]+)(?:\s+.*)?$")
CHAPTER_INTRO = re.compile(r"^(\d{2})\s{5,}([A-Z][a-zæøåA-ZÆØÅ].+)\s*$")


def extract_pdf_text(pdf_path: Path) -> list[str]:
    result = subprocess.run(
        ["pdftotext", "-layout", "-enc", "UTF-8", str(pdf_path), "-"],
        check=True, capture_output=True,
    )
    return result.stdout.decode("utf-8").splitlines()


def strip_boilerplate(lines: list[str]) -> list[str]:
    out: list[str] = []
    for line in lines:
        if HEADER_HRP.match(line): continue
        if HEADER_PROSJEKT.match(line): continue
        if HEADER_SIDE.match(line): continue
        if HEADER_SUM_COL.match(line): continue
        if HEADER_POSTNR_COL.match(line): continue
        if FOOTER_SUM_SIDE.match(line): continue
        if FOOTER_AKKUM.match(line): continue
        m = HEADER_KAPITTEL.match(line)
        if m:
            out.append(f"@@CHAPTER@@{m.group(1)}@@{m.group(2)}")
            continue
        out.append(line)
    cleaned: list[str] = []
    prev_blank = False
    for line in out:
        is_blank = not line.strip()
        if is_blank and prev_blank:
            continue
        cleaned.append(line.rstrip())
        prev_blank = is_blank
    while cleaned and not cleaned[0].strip():
        cleaned.pop(0)
    while cleaned and not cleaned[-1].strip():
        cleaned.pop()
    return cleaned


def dedent_lines(lines: list[str]) -> list[str]:
    non_empty = [l for l in lines if l.strip()]
    if not non_empty:
        return lines
    min_indent = min(len(l) - len(l.lstrip()) for l in non_empty)
    return [l[min_indent:] if l.strip() else "" for l in lines]


def split_into_posts(lines: list[str]) -> list[dict]:
    """Walk the stripped text. Emit a list of segments:
       {kind: 'chapter', num, name}
       {kind: 'prose', text: str}  (chapter-level introductory text)
       {kind: 'post', postnr, nscode, body: str}
    """
    segments: list[dict] = []
    current_chapter: str | None = None
    i = 0
    n = len(lines)
    pending_prose: list[str] = []

    def flush_prose():
        if any(l.strip() for l in pending_prose):
            text = "\n".join(pending_prose).strip("\n")
            segments.append({"kind": "prose", "text": text})
        pending_prose.clear()

    while i < n:
        line = lines[i]
        if line.startswith("@@CHAPTER@@"):
            flush_prose()
            _, _, rest = line.partition("@@CHAPTER@@")
            num, name = rest.split("@@", 1)
            if current_chapter != num:
                segments.append({"kind": "chapter", "num": num, "name": name})
                current_chapter = num
            i += 1
            continue
        # Chapter intro line like "03         Grunnarbeider" — skip, we already emitted header
        cm = CHAPTER_INTRO.match(line)
        if cm and current_chapter == cm.group(1):
            i += 1
            continue
        # Post header patterns
        pwn = POSTNR_WITH_NSCODE.match(line)
        po = POSTNR_ONLY.match(line)
        nso = NSCODE_ONLY.match(line) if not pwn and not po else None

        if pwn:
            flush_prose()
            postnr, nscode = pwn.group(1), pwn.group(2)
            # Peek: if the very next non-blank line is a bare postnr, we are in the
            # "stacked header" ISY layout where two posts share column space.
            # The next body chunk belongs to THIS post; the stacked postnr marks the
            # following post, whose NS code appears later as an ns-code-only line.
            stacked_postnr: str | None = None
            k = i + 1
            while k < n and not lines[k].strip():
                k += 1
            if k < n and POSTNR_ONLY.match(lines[k]):
                stacked_postnr = POSTNR_ONLY.match(lines[k]).group(1)
                i = k + 1
            else:
                i = i + 1
            # Collect body until we hit an ns-code-only line (which belongs to the
            # stacked post) or a new postnr-with-nscode / chapter.
            body_lines: list[str] = []
            while i < n:
                nxt = lines[i]
                if nxt.startswith("@@CHAPTER@@"): break
                if POSTNR_WITH_NSCODE.match(nxt): break
                if POSTNR_ONLY.match(nxt): break
                if stacked_postnr and NSCODE_ONLY.match(nxt): break
                body_lines.append(nxt)
                i += 1
            body = "\n".join(dedent_lines(body_lines)).strip("\n")
            segments.append({"kind": "post", "postnr": postnr, "nscode": nscode, "body": body})
            # If we have a stacked postnr pending, start its post now using the
            # upcoming ns-code line (if any) as its NS code.
            if stacked_postnr is not None:
                nscode2: str = ""
                body2: list[str] = []
                if i < n:
                    nsm = NSCODE_ONLY.match(lines[i])
                    if nsm:
                        nscode2 = nsm.group(1)
                        body2.append(lines[i])
                        i += 1
                while i < n:
                    nxt = lines[i]
                    if nxt.startswith("@@CHAPTER@@"): break
                    if POSTNR_WITH_NSCODE.match(nxt): break
                    if POSTNR_ONLY.match(nxt): break
                    if NSCODE_ONLY.match(nxt): break
                    body2.append(nxt)
                    i += 1
                body2_s = "\n".join(dedent_lines(body2)).strip("\n")
                segments.append({"kind": "post", "postnr": stacked_postnr, "nscode": nscode2, "body": body2_s})
            continue

        if po:
            # Postnr on its own line; next lines may contain NS code
            flush_prose()
            postnr = po.group(1)
            body_lines: list[str] = []
            nscode: str | None = None
            j = i + 1
            while j < n:
                nxt = lines[j]
                if nxt.startswith("@@CHAPTER@@"): break
                if POSTNR_WITH_NSCODE.match(nxt): break
                if POSTNR_ONLY.match(nxt): break
                nsm = NSCODE_ONLY.match(nxt)
                if nsm and nscode is None:
                    nscode = nsm.group(1)
                    # include the ns-code line raw in the body for context
                    body_lines.append(nxt)
                    j += 1
                    continue
                body_lines.append(nxt)
                j += 1
            body = "\n".join(dedent_lines(body_lines)).strip("\n")
            segments.append({"kind": "post", "postnr": postnr, "nscode": nscode or "", "body": body})
            i = j
            continue

        if nso:
            # NS code on its own line without a postnr — treat as a post with no postnr
            flush_prose()
            nscode = nso.group(1)
            body_lines: list[str] = [line]
            j = i + 1
            while j < n:
                nxt = lines[j]
                if nxt.startswith("@@CHAPTER@@"): break
                if POSTNR_WITH_NSCODE.match(nxt): break
                if POSTNR_ONLY.match(nxt): break
                if NSCODE_ONLY.match(nxt): break
                body_lines.append(nxt)
                j += 1
            body = "\n".join(dedent_lines(body_lines)).strip("\n")
            segments.append({"kind": "post", "postnr": "", "nscode": nscode, "body": body})
            i = j
            continue

        pending_prose.append(line)
        i += 1

    flush_prose()
    return segments


FRONTMATTER = """---
kilde: "FG30. Beskrivelse for kjeller. 19.10.2026.pdf"
dokumenttype: anbudsbeskrivelse
dato: 2026-10-19
avsender: HRP AS
mottaker: Kodeworks Eiendom AS
tema: ISY-beskrivelse for kjellerarbeider (NS 3420)
standard: NS 3420
antall_sider: 28
status_i_pdf: utkast med alternative tekstforslag og tomme felt
---

# Beskrivelse kjeller — Fjordgata 30 Minilager

**HRP AS**, 19.10.2026\\
**Byggherre:** Kodeworks Eiendom AS

Teknisk beskrivelse basert på NS 3420 (4. utgave) for arbeidene i kjelleren.

> **Status i PDF-en:** Dokumentet er levert som utkast fra HRP. Flere seksjoner inneholder HRP sine egne arbeidsnotater («Dette er å betrakte som alternative forslag til tekst samt ulike sideoppsett .... bearbeid derfor selv innholdet og fjern det du ikke trenger!») og duplikater av «Teknisk beskrivelse». Innbydelsen og flere felt i Kapittel 00 er tomme («<dato>», «<antall>», «............................»). Innholdet er tatt verbatim med fra PDF-en.

> **Hovedprinsipp (fra Kapittel 00):** Betongarbeider i kjeller må påregnes delvis under vannspeil — både graving, gjenfylling, forskaling og støping. Ekstrakostnader for dette skal medtas i alle prisbærende poster som omhandler kjellerarbeider.

> **Konvertering:** Produsert med `scripts/convert_beskrivelse_to_md.py` fra `pdftotext -layout`. Hver post gjengis verbatim i et kodeblokk under sitt `postnr/NS-kode`-underkapittel for å bevare NS 3420-strukturen og unngå tolkningstap.

"""


def build_markdown(segments: list[dict]) -> str:
    out: list[str] = [FRONTMATTER]
    for seg in segments:
        if seg["kind"] == "chapter":
            out.append(f"\n## Kapittel {seg['num']} — {seg['name']}\n")
        elif seg["kind"] == "prose":
            out.append(seg["text"] + "\n")
        elif seg["kind"] == "post":
            postnr = seg["postnr"]
            nscode = seg["nscode"]
            if postnr and nscode:
                out.append(f"\n### {postnr} — `{nscode}`\n")
            elif postnr:
                out.append(f"\n### {postnr}\n")
            else:
                out.append(f"\n### `{nscode}`\n")
            body = seg["body"]
            if body.strip():
                out.append("```\n" + body + "\n```\n")
    md = "\n".join(out)
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md


def main() -> None:
    if not PDF.exists():
        sys.exit(f"PDF not found: {PDF}")
    lines = extract_pdf_text(PDF)
    cleaned = strip_boilerplate(lines)
    segments = split_into_posts(cleaned)
    md = build_markdown(segments)
    OUT_MD.write_text(md, encoding="utf-8")
    chapters = sum(1 for s in segments if s["kind"] == "chapter")
    posts = sum(1 for s in segments if s["kind"] == "post")
    print(f"Wrote {OUT_MD}: {chapters} chapters, {posts} posts, {len(md)} chars, {md.count(chr(10))} lines")


if __name__ == "__main__":
    main()
