"""Update all project references from leveranser/dsb/ to leveranser/brann/dsb/."""

from pathlib import Path

OLD = "leveranser/dsb/"
NEW = "leveranser/brann/dsb/"

FILES = [
    "bakgrunn/brann/strategi_tvangsmulkt_2026-10-11/rapport_final.md",
    "bakgrunn/brann/strategi_tvangsmulkt_2026-10-11/faktaark.md",
    "TASKS.md",
    "bakgrunn/brann/strategi_tvangsmulkt_2026-10-11/final_tail.md",
    "bakgrunn/brann/strategi_tvangsmulkt_2026-10-11/final_head.md",
    "bakgrunn/brann/strategi_tvangsmulkt_2026-10-11/iteration_03_body_del1_5.md",
    "bakgrunn/brann/strategi_tvangsmulkt_2026-10-11/iterasjon_02_1245.md",
    "bakgrunn/brann/strategi_tvangsmulkt_2026-10-11/iteration_02_body_del1_5.md",
    "bakgrunn/brann/strategi_tvangsmulkt_2026-10-11/agent_01_maksimalistjurist_v2.md",
    "bakgrunn/brann/strategi_tvangsmulkt_2026-10-11/iterasjon_01_1200.md",
    "bakgrunn/brann/strategi_tvangsmulkt_2026-10-11/iteration_01_tail.md",
    "bakgrunn/brann/strategi_tvangsmulkt_2026-10-11/iteration_01_body_del1_5.md",
    "bakgrunn/brann/strategi_tvangsmulkt_2026-10-11/agent_01_maksimalistjurist.md",
    "historikk.md",
    "leveranser/brann/dsb/2026-10-08_dsb_soknad_frafall/README.md",
    "bakgrunn/brann/2026-10-08_dsb_soknad_gapanalyse.md",
    "bakgrunn/brann/2026-10-08_dsb_frafall_screening/OVERSIKT.md",
    "bakgrunn/lovverk/plan_bygningsloven.md",
    "bakgrunn/lovverk/forvaltningsloven.md",
    "bakgrunn/lovverk/forskrift_brannforebygging.md",
    "leveranser/T159_lovsitater_rapport.md",
    "leveranser/brann/2026-06-17_tbrt_klage_innkrevinger_2026.md",
]

changed = 0
for rel in FILES:
    p = Path(rel)
    if not p.exists():
        print(f"MISSING: {rel}")
        continue
    txt = p.read_text(encoding="utf-8")
    if OLD not in txt:
        continue
    n = txt.count(OLD)
    p.write_text(txt.replace(OLD, NEW), encoding="utf-8")
    print(f"  {rel}: {n} replacements")
    changed += n
print(f"Total: {changed} replacements")
