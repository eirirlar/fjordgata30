# Bankpakke – Fjordgata 30

Materialgrunnlag for prinsippforespørsel til bank: om innvilget offentlig støtte (2,25 MNOK) kan vektes som egenkapitallignende finansiering / reduksjon i nettoeksponering i kredittvurderingen.

Pakka er materialgrunnlag for prinsippspørsmål, ikke endelig kredittsøknad. Førsteversjon — oppdateres etter hvert som BFU, LOI, detaljprosjektering og revidert energikartlegging foreligger.

## Filer i pakka

| Nr | docx-fil i `bank/` | Markdown-kilde | Tema |
|---|---|---|---|
| 00 | `00_bankhenvendelse.docx` | `leveranser/2026-06-28_fg30_bankhenvendelse.md` | Bankhenvendelse med prinsippforespørsel |
| 01 | `01_forretningsplan.docx` | `forretningsplan/fg30_forretningsplan.md` | Forretningsplan (konsept, marked, økonomi, bankargumentasjon) |
| 02 | `02_finansieringsplan.docx` | `leveranser/2026-06-28_fg30_finansieringsplan.md` | Finansieringsplan med kontantstrøm og sensitivitetsanalyse |
| 03 | `03_mva_strategi.docx` | `forretningsplan/fg30_vurderinger_mva.md` | MVA-strategi og juridisk analyse |
| 04 | `04_konkurrentanalyse_og_markedsdata.docx` | `forretningsplan/kilde_markedsdata.md` | Konkurrentanalyse og markedsdata |
| 05 | `05_stoetteoversikt.docx` | `leveranser/2026-06-26_fg30_stoetteoversikt_bank.md` | Oversikt over innvilgede tilskudd og finansieringskilder |
| 06 | `06_tilskudd_som_egenkapital.docx` | `leveranser/2026-06-26_tilskudd_som_egenkapital.md` | Juridisk utredning – tilskudd som egenkapitallignende finansiering |
| 07 | `07_groent_laan.docx` | `leveranser/2026-06-26_groenne_laan_kriterier.md` | Grønt lån – kriteriedokument |
| 08 | `08_energikartleggingsrapport.docx` | `bakgrunn/stotte/enova_kl/hrp_energikartlegging_rapport.md` | Energikartleggingsrapport, HRP AS, 05.05.2026 |

## Originalrapport (PDF)

`Energikartlegging Fjordgt 30.pdf` – HRPs originalrapport, ikke regenerert (PDF-original fra HRP).

## Reviews

`bank/reviews/` – iterativ multi-agent rolle-review av pakka (T104). Siste: `2026-06-30_bank_review_007.md` (iter 10, snitt 7,9/10).

## Regenerering

Fra prosjektrot:

```bash
cd bank
pandoc ../leveranser/2026-06-28_fg30_bankhenvendelse.md       -o 00_bankhenvendelse.docx
pandoc ../forretningsplan/fg30_forretningsplan.md             -o 01_forretningsplan.docx
pandoc ../leveranser/2026-06-28_fg30_finansieringsplan.md     -o 02_finansieringsplan.docx
pandoc ../forretningsplan/fg30_vurderinger_mva.md             -o 03_mva_strategi.docx
pandoc ../forretningsplan/kilde_markedsdata.md                -o 04_konkurrentanalyse_og_markedsdata.docx
pandoc ../leveranser/2026-06-26_fg30_stoetteoversikt_bank.md  -o 05_stoetteoversikt.docx
pandoc ../leveranser/2026-06-26_tilskudd_som_egenkapital.md   -o 06_tilskudd_som_egenkapital.docx
pandoc ../leveranser/2026-06-26_groenne_laan_kriterier.md     -o 07_groent_laan.docx
pandoc ../bakgrunn/stotte/enova_kl/hrp_energikartlegging_rapport.md -o 08_energikartleggingsrapport.docx
cd ..
uv run --with python-docx python scripts/format_docx.py bank/01_forretningsplan.docx
```

`format_docx.py` kjøres kun på forretningsplanen (legger til tynne grå tabellrammer + faste kolonnebredder). Andre 8 dokumenter får ren pandoc-output uten ekstra formatering.

## PDF-konvertering

PDF leveres ved at bruker åpner hver `.docx` i Word/Office og «Lagre som PDF». Pandoc-PDF-generering krever en separat engine (pdflatex/xelatex/wkhtmltopdf) som per nå ikke er installert på dette systemet.

## Siste regenerering

30.06.2026 — etter T104 iter 10, T133–T136, og T-ingen-nummer (bankhenvendelse «førsteversjon»-mykning).
