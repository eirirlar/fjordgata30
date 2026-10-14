"""
Fjerner manuell hard-wrap i markdown-brødtekst. Bevarer tabeller, lister,
kodeblokker, blockquotes, headere og YAML frontmatter.
"""
import re
import sys
from pathlib import Path


def is_list_start(line):
    stripped = line.lstrip()
    if stripped.startswith(("- ", "* ", "+ ")):
        return True
    if re.match(r"^\d+\.\s", stripped):
        return True
    return False


def is_table_row(line):
    return line.lstrip().startswith("|")


def is_header(line):
    return line.lstrip().startswith("#")


def is_hr(line):
    stripped = line.strip()
    return stripped in ("---", "***", "___")


def is_blockquote(line):
    return line.lstrip().startswith(">")


def process_markdown(text):
    # Trekk ut YAML frontmatter
    yaml_match = re.match(r"^(---\n.*?\n---\n)", text, re.DOTALL)
    if yaml_match:
        yaml = yaml_match.group(1)
        rest = text[yaml_match.end():]
    else:
        yaml = ""
        rest = text

    lines = rest.split("\n")
    out = []
    i = 0
    in_fence = False
    fence_marker = None

    while i < len(lines):
        line = lines[i]

        # Håndter kodeblokker
        if line.lstrip().startswith("```") or line.lstrip().startswith("~~~"):
            marker = "```" if line.lstrip().startswith("```") else "~~~"
            if not in_fence:
                in_fence = True
                fence_marker = marker
            elif marker == fence_marker:
                in_fence = False
                fence_marker = None
            out.append(line)
            i += 1
            continue

        if in_fence:
            out.append(line)
            i += 1
            continue

        # Tom linje: bevares som avsnittsskiller
        if line.strip() == "":
            out.append("")
            i += 1
            continue

        # Headere, HR, tabellrader, blockquotes: bevares som egne linjer
        if (
            is_header(line)
            or is_hr(line)
            or is_table_row(line)
            or is_blockquote(line)
        ):
            out.append(line)
            i += 1
            continue

        # List-items: finn hele list-item (kan ha fortsettelseslinjer)
        if is_list_start(line):
            # Finn alle linjer som er del av dette list-item
            # (fortsetter til tom linje eller nytt list-item på samme nivå/høyere)
            indent = len(line) - len(line.lstrip())
            buffer = [line.strip()]
            i += 1
            while i < len(lines):
                nxt = lines[i]
                if nxt.strip() == "":
                    break
                nxt_indent = len(nxt) - len(nxt.lstrip())
                # Hvis neste er list-start på samme eller lavere indent, nytt item
                if is_list_start(nxt) and nxt_indent <= indent:
                    break
                # Hvis neste er header, tabell, blockquote, hr: avbryt
                if (
                    is_header(nxt)
                    or is_hr(nxt)
                    or is_table_row(nxt)
                    or is_blockquote(nxt)
                ):
                    break
                # Hvis neste er list-start med dypere indent (nested list), ta det med
                if is_list_start(nxt) and nxt_indent > indent:
                    # Dette er et nested list-item; behandle som egen linje
                    # Slå ikke sammen; avslutt denne itemen og la neste iterasjon
                    # håndtere nested item
                    break
                # Ellers: fortsettelseslinje — slå sammen
                buffer.append(nxt.strip())
                i += 1
            # Bevar prefix fra originallinjen (indent + list-marker)
            prefix_match = re.match(r"^(\s*(?:[-*+]|\d+\.)\s+)", line)
            if prefix_match:
                prefix = prefix_match.group(1)
                body = line[len(prefix):].strip()
                tail = " ".join(buffer[1:]) if len(buffer) > 1 else ""
                merged = prefix + body + (" " + tail if tail else "")
                out.append(merged)
            else:
                out.append(" ".join(buffer))
            continue

        # Vanlig brødtekst-avsnitt: slå sammen flere linjer
        buffer = [line.strip()]
        i += 1
        while i < len(lines):
            nxt = lines[i]
            if nxt.strip() == "":
                break
            if (
                is_header(nxt)
                or is_hr(nxt)
                or is_table_row(nxt)
                or is_blockquote(nxt)
                or is_list_start(nxt)
                or nxt.lstrip().startswith("```")
                or nxt.lstrip().startswith("~~~")
            ):
                break
            buffer.append(nxt.strip())
            i += 1
        out.append(" ".join(buffer))

    return yaml + "\n".join(out)


def main():
    if len(sys.argv) != 2:
        print("Usage: python unwrap_markdown.py <file>")
        sys.exit(1)
    path = Path(sys.argv[1])
    text = path.read_text(encoding="utf-8")
    new_text = process_markdown(text)
    path.write_text(new_text, encoding="utf-8")
    print(f"Unwrapped {path}")


if __name__ == "__main__":
    main()
