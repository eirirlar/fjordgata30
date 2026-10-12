"""Integrate iter 02 agent reports into iteration 02 report."""

from pathlib import Path
import re
import sys

ITER_DIR = Path("bakgrunn/brann/strategi_tvangsmulkt_2026-10-11")
AGENTS = [
    ("Del 1 — Formelle rettsmidler", "agent_01_maksimalistjurist_v2.md", "Agent 1 — Maksimalistjurist (iter 02)"),
    ("Del 2 — Prosessuelle forsinkelser og saksbehandlingsfeil", "agent_02_prosessguerilla_v2.md", "Agent 2 — Prosessguerilla (iter 02)"),
    ("Del 3 — Selskapsrettslige grep", "agent_03_selskapsrett_v2.md", "Agent 3 — Selskapsrettslig arkitekt (iter 02)"),
    ("Del 4 — Mediestrategi og politisk mobilisering", "agent_04_politisk_v2.md", "Agent 4 — Politisk strateg (iter 02)"),
    ("Del 5 — Kreative/ukonvensjonelle manøvre", "agent_05_djevelen_v2.md", "Agent 5 — Djevelens advokat (iter 02)"),
]


def strip_frontmatter(text: str) -> str:
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[end + 4:].lstrip("\n")
    return text


def demote_headers(text: str) -> str:
    return re.sub(r"^(#{1,5})(?= )", lambda m: "#" + m.group(0), text, flags=re.MULTILINE)


def strip_top_header(text: str) -> str:
    lines = text.splitlines()
    out, skipped = [], False
    for line in lines:
        if not skipped and line.startswith("## ") and not line.startswith("## Del"):
            skipped = True
            continue
        out.append(line)
    return "\n".join(out)


def process(path: Path) -> str:
    raw = path.read_text(encoding="utf-8")
    return strip_top_header(demote_headers(strip_frontmatter(raw)))


def main() -> None:
    out_path = ITER_DIR / "iteration_02_body_del1_5.md"
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
