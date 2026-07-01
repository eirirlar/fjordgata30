# SAAHA Timeliste – aggregert oversikt

**Periode:** 12.01.2026 – 19.06.2026
**Prosjekt:** 2601 Fjordgata_Minilager
**Prosjektleder:** Adnan Harambasic
**Totalt:** 44,0 timer (57 200 kr eks. mva ved timepris 1 300)
**Kilde:** `timer/2026-06-27_saaha_timeoversikt.pdf` (utstedt 27.06.2026)
**Generert:** 2026-07-01 (via `scripts/parse_saaha_timeliste.py`)

## Sammendrag per person

| Person | Fagdisiplin | jan | feb | mar | apr | mai | jun | Totalt |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Adnan Harambasic | Prosjektledelse / arkitekt |  |  | 2,0 | 4,0 | 7,0 | 1,0 | **14,0** |
| Dalibor Baran | Arkitekt | 24,0 |  |  |  |  |  | **24,0** |
| Elizaveta Marchenko | Arkitekt |  |  |  |  | 6,0 |  | **6,0** |
| **Sum** |  | **24,0** | – | **2,0** | **4,0** | **13,0** | **1,0** | **44,0** |

## Aktivitetsoversikt

Alle timer er registrert som «Fakturerbart arbeid» med timepris 1 300 kr. Arbeidet omfatter:

- **Januar (Dalibor Baran, 24 t):** Planarbeid og modellering av etasjer for rammesøknad; fasader og situasjonsplan; interne møter.
- **Mars (Adnan Harambasic, 2 t):** Statusmøter med Eirik, Ole Morten og Kristian.
- **April (Adnan Harambasic, 4 t):** Koordinering; oppfølging av tegninger og korrespondanse.
- **Mai (Adnan 7 t, Elizaveta 6 t):** Møter med kommunen; revidering av tegninger, kvalitetssikring og innsending av rammesøknad; snitt- og fasadeoppdateringer.
- **Juni (Adnan 1 t):** Statusmøte før sommer.

## Fakturaer

Se `timer/saaha_fakturaer.csv`. Utstedte fakturaer på prosjekt 2601 Fjordgata_Minilager per 27.06.2026:

| Fakturanr. | Fakturadato | Forfall | Eks. mva | Inkl. mva | Restbeløp | Status |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1621 | 2026-01-31 | 2026-03-01 | 105 192 | 131 490 | 131 490 | Sendt som EHF-faktura 2026-02-03 |
| 1646 | 2026-02-27 | 2026-03-29 | 24 700 | 30 875 | 30 875 | Sendt som EHF-faktura 2026-03-02 |
| 1697 | 2026-03-31 | 2026-04-30 | 2 988 | 3 735 | 3 735 | Sendt som EHF-faktura 2026-04-08 |
| **Sum** |  |  | **132 880** | **166 100** | **166 100** | Alle forfalt, ubetalt |

**Merknad om timeavvik:** Fakturasummen 132 880 eks. mva tilsvarer ca. 102 timer ved timeprisen 1 300 kr, mens timelisten viser 44 timer for perioden 2026-01-01 til 2026-06-30. Differansen stammer sannsynligvis fra arbeid utført i 2025 som er fakturert i januar 2026. Timelisten dekker kun 2026.

## Regenerering

```bash
uv run --with pdfplumber python scripts/parse_saaha_timeliste.py \
  --pdf timer/2026-06-27_saaha_timeoversikt.pdf \
  --out timer/saaha_timer_2026H1.csv
```

Aggregert oversikt (denne fila) og fakturaer-CSV vedlikeholdes manuelt inntil et tilsvarende aggregeringsscript foreligger.
