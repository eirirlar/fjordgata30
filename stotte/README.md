# stotte/ – Fjordgata 30 tilskuddsdata

Denne mappen inneholder tilskuddsdata for Fjordgata 30 i `project_cards.json`-format, basert på malen i `../stotte/project_cards_template.json`.

## Filer

| Fil | Innhold |
|-----|---------|
| `project_cards.json` | Alle aktive tilskuddsprosjekter for KodeWorks Eiendom AS / Fjordgata 30 |
| `fg30_skattefunn_vurdering.md` | Intern vurdering av Skattefunn-egnethet |
| `fg30_innovasjon_norge_vurdering.md` | Intern vurdering av IN-egnethet |

## Prosjekter i project_cards.json

| ProjectID | Ordning | Tilskudd | Status |
|-----------|---------|----------|--------|
| KMF-FG30 | Kulturminnefondet | 750 000 NOK | active |
| BYA-FG30 | Byantikvaren | 500 000 NOK | active |
| UNI-FG30 | Stiftelsen UNI | 100 000 NOK | active |
| ENOVA-KL-FG30 | Enova – Energikartlegging | 400 000 NOK | active |
| ENOVA-OM-FG30 | Enova – Mulighetsstudie ombruk | 500 000 NOK | active |

---

## Avvik fra malen (`../stotte/project_cards_template.json`)

### Tillegg (i vår fil, ikke i malen)

| Felt | Berørte prosjekter | Notat |
|------|-------------------|-------|
| `UsageConstraints` (objekt med `eligible`/`ineligible`) | Alle 5 | FG30-spesifikt tillegg — dokumenterer hva som er støtteberettiget per tilskuddsordning. Beholdes. |
| `ConsortiumPartners[*].Role` | ENOVA-KL-FG30, ENOVA-OM-FG30 | Ikke i malen; beskriver leverandørrollen. Beholdes som nyttig tillegg, men malen bruker `Comments`-feltet til dette. |

### Manglende felt (malen har, vi mangler)

**`ConsortiumPartners`-oppføringer** — ENOVA-KL-FG30 og ENOVA-OM-FG30:

| Felt (mal) | Status i vår fil |
|-----------|-----------------|
| `PartnerBudget` | Mangler — null/ukjent for disse leverandørene |
| `PartnerGrantAmount` | Mangler — ikke relevant (underleverandører, ikke tilskuddsmottakere) |
| `Comments` | Mangler per partner — bør vurderes |

**`workpackages`-oppføringer** — alle prosjekter med WP-er (KMF-FG30, ENOVA-OM-FG30):

| Felt (mal) | Status i vår fil |
|-----------|-----------------|
| `DurationFromDate` | Mangler — ikke fastsatt per WP |
| `DurationToDate` | Mangler — ikke fastsatt per WP |
| `DurationFromMonth` | Mangler — ikke relevant (ikke Horizon-prosjekt) |
| `DurationToMonth` | Mangler — ikke relevant (ikke Horizon-prosjekt) |
| `BudgetValue` | Mangler — budsjett ikke fordelt per WP |
| `BudgetUnit` | Mangler (henger sammen med BudgetValue) |
| `IntensityOverride` | Mangler — uniform intensitet i alle prosjekter |
| `Participants` | Mangler — bare EL er involvert i alle |
| `Comments` | Mangler per WP |

### Navnefeil (bør rettes)

| Prosjekt | Feil | Korrekt (mal) |
|---------|------|---------------|
| ENOVA-OM-FG30 | `ConsortiumPartners[*].Name` | `PartnerName` |

### WPID-format

Malen sier WPID skal følge mønsteret `{ProjectID}-WP{n}` (f.eks. `KMF-FG30-WP1`). Vi bruker `AP1`, `AP2` etc. (arbeidspaккebetegnelse fra tilskuddsbrevet). Avviket er bevisst — `AP`-betegnelsene samsvarer med ordlyden i tilskuddsavtalene og gjør det enklere å referere til dem i rapporter.

### SchemeID-verdier

Malen nevner eksempler `HORIZON | ENOVA | SF | IN`. Våre SchemeIDs:

| SchemeID | Ordning |
|----------|---------|
| `KMF` | Kulturminnefondet |
| `BYA` | Byantikvaren Trondheim |
| `UNI` | Stiftelsen UNI |
| `ENOVA_KART` | Enova – Energikartlegging og mulighetsstudie |

Ingen `schemes.csv` brukes i dette prosjektet — SchemeID er kun en intern nøkkel i `project_cards.json`.
