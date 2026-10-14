# Dokumentkonvertering

Kjøremiljø: **Git Bash på Windows** (MINGW64) er standard. På Linux/macOS erstatt `mermaid-filter.cmd` med `mermaid-filter` – se [Plattform-note – filternavnet](#plattform-note--filternavnet) under.

## DOCX

> **Kjør i:** Git Bash (Windows) – bruker `mermaid-filter.cmd`

```bash
pandoc input.md -o output.docx -F mermaid-filter.cmd
```

## PDF (brukes for bankpakka og andre eksterne leveranser)

> **Kjør i:** Git Bash (Windows) – bruker `mermaid-filter.cmd` og Windows-fonter

```bash
pandoc input.md -o output.pdf \
  -F mermaid-filter.cmd \
  --pdf-engine=xelatex \
  -V documentclass=scrartcl \
  -V geometry:margin=1in \
  -V mainfont="Times New Roman" \
  -V monofont="Consolas"
```

Forklaring av flaggene:

| Flagg | Effekt |
|---|---|
| `-F mermaid-filter.cmd` | Pandoc-filter som pre-prosesserer AST og erstatter mermaid-blokker med rendrede PNG-bilder. Fungerer både på inline mermaid i .md-en og på blokker som er importert via `include`. Ingen effekt hvis .md-en ikke har mermaid – trygt å ha som standardflagg. |
| `--pdf-engine=xelatex` | Bruker xelatex fra TeX Live (nødvendig for unicode-tegn – «≥», «–», «€» – og for TrueType-fonter). |
| `-V documentclass=scrartcl` | KOMA-Script artikkel-klasse – renere typografi og bedre marg-håndtering enn standard `article`. |
| `-V geometry:margin=1in` | 1 tomme marg på alle sider. |
| `-V mainfont="Times New Roman"` | Hovedfont for brødtekst. Systemfont på Windows. På Linux: enten installer Microsoft core fonts (`sudo apt install ttf-mscorefonts-installer` — krever EULA-godkjenning), eller bytt til metric-kompatibel `Liberation Serif` (samme tegnbredder, identisk sideoppsett; kommer med `fonts-liberation` og er standard på Ubuntu/Debian). |
| `-V monofont="Consolas"` | Mono-font for kodeblokker. Standard-fonten (Latin Modern Mono) mangler Unicode box-drawing-tegn (├, ─, └, │) og gir «Missing character»-warnings på ASCII-tre-strukturer. Consolas følger *ikke* med `ttf-mscorefonts-installer` på Linux — bruk `DejaVu Sans Mono` som Linux-alternativ (kommer med `fonts-dejavu` og er standard på Ubuntu/Debian). |

**Autonummerering av overskrifter:** Pandoc autonummererer *ikke* overskrifter som standard, så vi trenger ingen flagg for å slå det av. Kildene i dette prosjektet har egen nummerering («01.01», «Post 03» osv.) som beholdes uendret. Hvis autonummerering skulle ønskes for et enkeltdokument, legg til `--number-sections` (eller `-N`).

**Plattform-note – filternavnet:** På Windows lager npm tre filer per bin (`mermaid-filter`, `mermaid-filter.cmd`, `mermaid-filter.ps1`). Pandoc slår opp *eksakt filnavn* og respekterer ikke Windows' `PATHEXT`-mekanisme, så fra **Git Bash / MINGW64** må endelsen `.cmd` med. Fra **PowerShell/CMD** virker `-F mermaid-filter` også. Fra **Linux/macOS** finnes bare `mermaid-filter` (ingen `.cmd`) – bruk det.

**Plattform-note – fonter på Linux:** Kommandoen over er skrevet for Windows/Git Bash. På Linux, bruk metric-/funksjonsalternativer:

> **Kjør i:** WSL2 Ubuntu (eller native Linux) – bruker `mermaid-filter` (uten `.cmd`) og Linux-native fonter

```bash
pandoc input.md -o output.pdf \
  -F mermaid-filter \
  --pdf-engine=xelatex \
  -V documentclass=scrartcl \
  -V geometry:margin=1in \
  -V mainfont="Liberation Serif" \
  -V monofont="DejaVu Sans Mono"
```

`Liberation Serif` er metric-kompatibel med Times New Roman, så sideoppsett og linjebrudd blir identiske. `DejaVu Sans Mono` støtter samme Unicode-omfang som Consolas (inkludert box-drawing).

## Generere forretningsplan som docx

> **Kjør i:** Git Bash (Windows) – bruker `mermaid-filter.cmd`

```bash
cd forretningsplan
pandoc forretningsplan.md -o fg30_forretningsplan.docx -F mermaid-filter.cmd
uv run --with python-docx python ../scripts/format_docx.py fg30_forretningsplan.docx
```

`format_docx.py` legger til tynn grå ramme (0,5pt, #BFBFBF) på alle tabellceller og setter faste kolonnebredder per tabell.

## Bankpakke

Bankpakka (9 dokumenter) ligger i `bank/`. Markdown → docx-mappingen og regenereringskommandoer er dokumentert i [`bank/MANIFEST.md`](../bank/MANIFEST.md). Standard-flaggene for DOCX og PDF er de samme som over – både `-F mermaid-filter` og xelatex-flaggene brukes i bankpakke-regenereringen.
