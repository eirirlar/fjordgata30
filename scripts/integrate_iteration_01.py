"""Integrate agent reports into iteration 01 report.

Reads the five agent markdown files, demotes their header hierarchy by one level,
strips frontmatter, and writes a combined Del 1..5 section. The orchestrator's
own integration content (metadata, prioriteringer, kombinasjoner, matrise,
utkast, kildeliste) is written separately as parts A and C.
"""

from pathlib import Path
import re
import sys

ITER_DIR = Path("bakgrunn/brann/strategi_tvangsmulkt_2026-10-11")
AGENTS = [
    ("Del 1 — Formelle rettsmidler", "agent_01_maksimalistjurist.md", "Agent 1 — Maksimalistjurist"),
    ("Del 2 — Prosessuelle forsinkelser og saksbehandlingsfeil", "agent_02_prosessguerilla.md", "Agent 2 — Prosessguerilla"),
    ("Del 3 — Selskapsrettslige grep", "agent_03_selskapsrett.md", "Agent 3 — Selskapsrettslig arkitekt"),
    ("Del 4 — Mediestrategi og politisk mobilisering", "agent_04_politisk.md", "Agent 4 — Politisk strateg"),
    ("Del 5 — Kreative/ukonvensjonelle manøvre", "agent_05_djevelen.md", "Agent 5 — Djevelens advokat"),
]


def strip_frontmatter(text: str) -> str:
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[end + 4:].lstrip("\n")
    return text


def demote_headers(text: str) -> str:
    """Add a '#' to every ATX header, so top-level becomes level 2 etc."""
    def repl(m: re.Match) -> str:
        return "#" + m.group(0)
    return re.sub(r"^(#{1,5})(?= )", repl, text, flags=re.MULTILINE)


def strip_top_header(text: str) -> str:
    """Drop the first H1 (now H2 after demotion) because we add our own Del heading."""
    lines = text.splitlines()
    out = []
    skipped = False
    for line in lines:
        if not skipped and line.startswith("## ") and not line.startswith("## Del"):
            skipped = True
            continue
        out.append(line)
    return "\n".join(out)


def process(path: Path) -> str:
    raw = path.read_text(encoding="utf-8")
    stripped = strip_frontmatter(raw)
    demoted = demote_headers(stripped)
    return strip_top_header(demoted)


def main() -> None:
    out_path = ITER_DIR / "iteration_01_body_del1_5.md"
    chunks: list[str] = []
    for del_title, filename, agent_label in AGENTS:
        p = ITER_DIR / filename
        if not p.exists():
            print(f"MISSING: {p}", file=sys.stderr)
            continue
        chunks.append(f"## {del_title}\n\n*({agent_label} — bevart i sin fulle dybde.)*\n")
        chunks.append(process(p))
        chunks.append("\n---\n")
    out_path.write_text("\n".join(chunks), encoding="utf-8")
    print(f"Wrote {out_path} ({sum(len(c.splitlines()) for c in chunks)} lines)")


if __name__ == "__main__":
    main()
