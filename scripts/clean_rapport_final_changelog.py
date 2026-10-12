"""Remove changelog residue from rapport_final.md.

Scope:
- Strip "(iter 02)", "(iter 03)", "v2", "v3" tags from inline references
- Remove "Endringslogg iterasjon XX" paragraph blocks inside agent sections
- Remove "Faktaavvik oppdaget" / "Avvik N — ..." blocks inside agent sections
  (these are per-agent findings notes, not strategy content)
- Clean up the per-section agent attribution line

The script preserves all strategy content.
"""

from pathlib import Path
import re

PATH = Path("bakgrunn/brann/strategi_tvangsmulkt_2026-10-11/rapport_final.md")
text = PATH.read_text(encoding="utf-8")

# 1. Drop per-section agent attribution one-liner (immediately below "## Del N — ..." heading).
text = re.sub(
    r"^\*\(Agent \d — [^)]+ — bevart i sin fulle dybde\.\)\*\n+",
    "",
    text,
    flags=re.MULTILINE,
)

# 2. Remove inline "(iter 0X)" / "iter 0X" tags on cross-references.
text = re.sub(r"\s*\(iter 0\d( pkt\. \d+)?\)", r"\1", text)
text = re.sub(r"\s*iter 0\d( pkt\. \d+)", r"\1", text)
text = re.sub(r"\s*iter 0\d\b", "", text)

# 3. Strip version suffixes v1/v2/v3 near agent names.
text = re.sub(r"\s*v[1-3]\b", "", text)

# 4. Remove per-agent "Endringslogg iterasjon ..." italic blocks (whole paragraph).
text = re.sub(
    r"\n\*Endringslogg[^*]+\*\n",
    "\n",
    text,
)

# 5. Remove per-agent "## Faktaavvik oppdaget" blocks (until next ## header).
#    These exist inside the agent sections now flattened to ### depth.
#    Match "### Faktaavvik oppdaget" through to the next "###" or "## " heading.
text = re.sub(
    r"\n###+ Faktaavvik oppdaget\n[\s\S]*?(?=\n### |\n## )",
    "\n",
    text,
)

# 6. Collapse resulting double blank lines down to one.
text = re.sub(r"\n{3,}", "\n\n", text)

PATH.write_text(text, encoding="utf-8")
print(f"Wrote {PATH} ({len(text.splitlines())} lines)")
