"""
Fjerner markdown-bold (**...**) i brødtekst. Bevarer bold i:
- Tabellrader (linjer som starter med |)
- Overskrifter (linjer som starter med #)
- Linjer i eksplisitt forkortelses-/begreps-liste (seksjon mellom
  'Forkortelser og sentrale begreper' og 'Innholdsfortegnelse')

Alle andre forekomster av **tekst** erstattes med tekst.
"""
import re
import sys
from pathlib import Path


def strip_bold(line: str) -> str:
    return re.sub(r"\*\*([^*]+?)\*\*", r"\1", line)


def main():
    path = Path(sys.argv[1])
    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")

    in_abbrev_section = False
    out = []
    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith("## Forkortelser og sentrale begreper"):
            in_abbrev_section = True
            out.append(line)
            continue
        if in_abbrev_section and stripped.startswith("## "):
            in_abbrev_section = False
            # fall through — denne overskrifta skal også prosesseres
        if in_abbrev_section:
            out.append(line)
            continue
        if stripped.startswith("|"):
            out.append(line)
            continue
        if stripped.startswith("#"):
            out.append(line)
            continue
        out.append(strip_bold(line))

    path.write_text("\n".join(out), encoding="utf-8")
    print(f"Processed {path}")


if __name__ == "__main__":
    main()
