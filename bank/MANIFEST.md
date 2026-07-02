# Bankpakke – Fjordgata 30

Materialgrunnlag for prinsippforespørsel til bank: om innvilget offentlig støtte (2,25 MNOK) kan vektes som egenkapitallignende finansiering / reduksjon i nettoeksponering i kredittvurderingen.

Pakka er materialgrunnlag for prinsippspørsmål, ikke endelig kredittsøknad. Førsteversjon — oppdateres etter hvert som BFU, LOI, detaljprosjektering og revidert energikartlegging foreligger.

## Filer i pakka

| Nr | docx-fil i `bank/` | Markdown-kilde | Tema |
|---|---|---|---|
| 00 | `00_bankhenvendelse.docx` | `leveranser/2026-06-28_bankhenvendelse.md` | Bankhenvendelse med prinsippforespørsel |
| 01 | `01_forretningsplan.docx` | `forretningsplan/forretningsplan.md` | Forretningsplan (konsept, marked, økonomi, bankargumentasjon) |
| 02 | `02_finansieringsplan.docx` | `leveranser/2026-06-28_finansieringsplan.md` | Finansieringsplan med kontantstrøm og sensitivitetsanalyse |
| 03 | `03_mva_strategi.docx` | `forretningsplan/mva_strategi.md` | MVA-strategi og juridisk analyse |
| 04 | `04_konkurrentanalyse_og_markedsdata.docx` | `forretningsplan/konkurrentanalyse_og_markedsdata.md` | Konkurrentanalyse og markedsdata |
| 05 | `05_stoetteoversikt.docx` | `leveranser/2026-06-26_stoetteoversikt.md` | Oversikt over innvilgede tilskudd og finansieringskilder |
| 06 | `06_tilskudd_som_egenkapital.docx` | `leveranser/2026-06-26_tilskudd_som_egenkapital.md` | Juridisk utredning – tilskudd som egenkapitallignende finansiering |
| 07 | `07_groent_laan.docx` | `leveranser/2026-06-26_groent_laan.md` | Grønt lån – kriteriedokument |
| 08 | *(leveres separat)* | – | Energikartleggingsrapport, HRP AS, 05.05.2026 – originalrapport fra HRP legges inn i pakka som PDF direkte, ikke regenerert fra `bakgrunn/stotte/enova_kl/energikartleggingsrapport.md` (Markdown-versjonen er kildesporing, ikke leveranse) |

## Reviews

`bank/reviews/` – iterativ multi-agent rolle-review av pakka (T104). Siste: `2026-06-30_bank_review_007.md` (iter 10, snitt 7,9/10).

## Regenerering

Fra prosjektrot:

**Nr. 08 (energikartleggingsrapport) genereres ikke** — HRPs original PDF legges inn i pakka manuelt. Alle andre 8 dokumenter genereres slik:

Forutsetninger og forklaring av flaggene er dokumentert i [README.md → Dokumentkonvertering (Pandoc)](../README.md#dokumentkonvertering-pandoc). Kommandoene under kjøres fra **Git Bash på Windows** og bruker `-F mermaid-filter.cmd` (Windows-varianten av npm-bin). På Linux/macOS: erstatt med `-F mermaid-filter` (ingen `.cmd`).

### DOCX

```bash
cd bank
DOCXOPT="-F mermaid-filter.cmd"
pandoc ../leveranser/2026-06-28_bankhenvendelse.md                 -o 00_bankhenvendelse.docx                 $DOCXOPT
pandoc ../forretningsplan/forretningsplan.md                       -o 01_forretningsplan.docx                 $DOCXOPT
pandoc ../leveranser/2026-06-28_finansieringsplan.md               -o 02_finansieringsplan.docx               $DOCXOPT
pandoc ../forretningsplan/mva_strategi.md                          -o 03_mva_strategi.docx                    $DOCXOPT
pandoc ../forretningsplan/konkurrentanalyse_og_markedsdata.md      -o 04_konkurrentanalyse_og_markedsdata.docx $DOCXOPT
pandoc ../leveranser/2026-06-26_stoetteoversikt.md                 -o 05_stoetteoversikt.docx                 $DOCXOPT
pandoc ../leveranser/2026-06-26_tilskudd_som_egenkapital.md        -o 06_tilskudd_som_egenkapital.docx        $DOCXOPT
pandoc ../leveranser/2026-06-26_groent_laan.md                     -o 07_groent_laan.docx                     $DOCXOPT
cd ..
uv run --with python-docx python scripts/format_docx.py bank/01_forretningsplan.docx
```

`format_docx.py` kjøres kun på forretningsplanen (legger til tynne grå tabellrammer + faste kolonnebredder). Andre 7 dokumenter får ren pandoc-output uten ekstra formatering.

### PDF

Krever xelatex (TeX Live). Samme løkke med PDF-flagg:

```bash
cd bank
PDFOPT="-F mermaid-filter.cmd --pdf-engine=xelatex -V documentclass=scrartcl -V geometry:margin=1in -V mainfont=\"Times New Roman\" -V monofont=\"Consolas\" --number-sections=false"
pandoc ../leveranser/2026-06-28_bankhenvendelse.md                 -o 00_bankhenvendelse.pdf                 $PDFOPT
pandoc ../forretningsplan/forretningsplan.md                       -o 01_forretningsplan.pdf                 $PDFOPT
pandoc ../leveranser/2026-06-28_finansieringsplan.md               -o 02_finansieringsplan.pdf               $PDFOPT
pandoc ../forretningsplan/mva_strategi.md                          -o 03_mva_strategi.pdf                    $PDFOPT
pandoc ../forretningsplan/konkurrentanalyse_og_markedsdata.md      -o 04_konkurrentanalyse_og_markedsdata.pdf $PDFOPT
pandoc ../leveranser/2026-06-26_stoetteoversikt.md                 -o 05_stoetteoversikt.pdf                 $PDFOPT
pandoc ../leveranser/2026-06-26_tilskudd_som_egenkapital.md        -o 06_tilskudd_som_egenkapital.pdf        $PDFOPT
pandoc ../leveranser/2026-06-26_groent_laan.md                     -o 07_groent_laan.pdf                     $PDFOPT
```

## Siste regenerering

30.06.2026 — etter T104 iter 10, T133–T136, og T-ingen-nummer (bankhenvendelse «førsteversjon»-mykning).
