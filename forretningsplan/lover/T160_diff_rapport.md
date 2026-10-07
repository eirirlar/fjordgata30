# T160 diff-rapport — 2026-10-06

## Metode

Samme pipeline som T158 (curl → pup → html2text → diff), kjørt mot `forretningsplan/lover/`-filene via `scripts/t160_verify_forretningsplan_lover.py`. Scriptet gjenbruker normaliserings- og pipeline-funksjonene fra `scripts/t158_verify_lovverk.py` og legger kun til en regel for å kanonisere `a)` → `a.` (forretningsplan-filene brukte lukkende parentes på bokstavlistene).

**Normaliseringen fra T158 ble utvidet med to patch-er** (gjelder også T158 — alle 51 paragrafer re-verifisert MATCH etter patch):

1. `RE_ENDRINGSHIST` gjort case-insensitive og mer tolerant mot innhold mellom pipe-skille og endringshistorikk-verbet (mval § 9-1 har en fotnote som starter med «0 | Tredje ledd er opphevet…» i stedet for «0 | Endret ved…»).
2. `RE_SPACE_BEFORE_PUNCT` endret fra `[ \t]+` til `\s+` (fanger også newline-innsmett før punktum når html2text wrap'et et link rett før en setningsslutt — f.eks. `§ 3-26\n.`).

**Verktøyversjoner:** `pup 0.4.0` · `html2text 2025.4.15` · `curl 8.18.0`.

## Oversikt

- **Totalt verifisert:** 8 mval-paragraf-filer
- **MATCH ved første gjennomkjøring:** 3 (mval §§ 2-1, 2-3, 3-11)
- **DIFF ved første gjennomkjøring:** 5 (mval §§ 8-1, 8-2, 8-6, 9-1, 9-4) — regenerert
- **MATCH etter regenerering:** 8/8

## Alvorlighetsvurdering av funnene

De fem DIFF-funnene var **ikke** harmløse format-forskjeller — fire av fem filer hadde substansielt feil eller forkortet lovtekst, og den femte hadde strukturell formateringsfeil som skjulte innholdet. Oppsummering:

| Fil | Avvikstype | Beskrivelse |
|---|---|---|
| `mval_8-1_fradragsrett.md` | **Oppdiktet lovtekst** | Eksisterende fil hadde 3 ledd (1–3). Lovdata § 8-1 er én enkelt setning uten ledd-nummerering. Hele innholdet var konstruert. |
| `mval_8-2_forholdsvis_fradrag.md` | **Kraftig forkortet** | Eksisterende fil hadde én setning. Lovdata § 8-2 har 5 ledd, inkludert viktige fem-prosent-regler (ledd 3 og 4) og 5-5-unntak for tjenester (ledd 1 andre punktum). Hele det materielle innholdet manglet. |
| `mval_8-6_tilbakegaende_avgiftsoppgjor.md` | Format-feil | Lovteksten var korrekt verbatim, men ett sammenhengende ledd (1) var strukturert som 5 separate paragrafer, hvilket skjuler at det er samme ledd. Mindre alvorlig, men misvisende. |
| `mval_9-1_kapitalvarer.md` | **Parafrasert + feil struktur** | Ledd (1) forenklet («endring i fradragsretten» uten dato-referanse og §§-henvisninger). Ledd (2)a manglet unntak for kjøretøyer etter § 6-7. Ledd (3)/(4) markert «(Opphevet)» i stedet for Lovdatas «– – –». Ledd (5) oppdiktet (Lovdatas (4) er om forskriftsadgang for byggetiltak). |
| `mval_9-4_justeringsperiode.md` | **Parafrasert + ledd mangler** | Ledd (1) parafrasert med feil formulering («Slik kapitalvare anses anskaffet i det regnskapsåret kapitalvaren tas i bruk» finnes ikke i Lovdata; faktisk er regelen om «fem første regnskapsårene etter anskaffelsen eller framstillingen»). Ledd (3) om re-innrulling ved gjenopptatt MVA-pliktig virksomhet manglet helt. |

**Konklusjon:** Filen `forretningsplan/lover/`-samlingen fra 23.06.2026 var ikke lastet ned verbatim fra Lovdata — den var åpenbart parafrasert eller gjengitt fra hukommelsen/håndboken, slik som hele-loven-filene T157 avdekket. Dette er det samme mønsteret T157 fant, kun i en annen katalog.

## Konsekvens for leveranser

Alle leveranser som siterer §§ 8-1, 8-2, 8-6, 9-1 eller 9-4 fra MVA-strategien må gjennomgås mot de regenererte paragraf-filene. Dette dekker:

- `forretningsplan/mva_strategi.md` (24 §-sitater totalt)
- `forretningsplan/fg30_selskapsstruktur_mva.md` (32 §-sitater)
- `forretningsplan/kilde_mva_regelverk.md` (43 §-sitater — høyest tetthet)
- `forretningsplan/forretningsplan.md` (7 §-sitater)
- `leveranser/2026-08-05_driftsbeskrivelse_fjordgata30.md` (sendt til Skatteetaten — mval-sitater må verifiseres mot nye filer)
- Bank-pakka 00/02/03/05/06/07 (regenereres via pandoc etter kildeoppdatering)

T159 delleveranse 2 (bank-/forretningsplan-sporet) må nå inkludere eksplisitt sjekk mot de regenererte §§ 8-1, 8-2, 8-6, 9-1, 9-4-filene — særlig for:

- **§ 8-1-sitater:** sjekk at eldre sitater om «Avgiftssubjektet har rett til fradrag … ved anskaffelse av varer og tjenester som skal brukes ved omsetning som er omfattet av loven» byttes mot korrekt verbatim «Et registrert avgiftssubjekt har rett til fradrag for inngående merverdiavgift på anskaffelser av varer og tjenester som er til bruk i den registrerte virksomheten.»
- **§ 8-2-sitater:** 5-prosent-reglene (ledd 3 og 4) var ikke dokumentert i den gamle fila. Hvis MVA-strategien bygger på disse, må de nå siteres korrekt.
- **§ 9-1-sitater:** «annet ledd bokstav b»-definisjonen av «fast eiendom» inneholder nå en spesifikk 31.12.2007-grense som den gamle fila manglet. Også kjøretøy-unntaket under bokstav a.
- **§ 9-4-sitater:** 10-årsperioden stod korrekt, men formuleringen må nå tilpasses Lovdatas eksakte ordlyd. Nye ledd (3) om re-innrulling er en potensielt verdifull fallback.

## Per-fil-resultat

### mval_2-1_registreringsplikt.md
- Status: MATCH (ingen endring)
- Kilde: <https://lovdata.no/lov/2009-06-19-58/%C2%A72-1>

### mval_2-3_frivillig_registrering.md
- Status: MATCH (ingen endring)
- Kilde: <https://lovdata.no/lov/2009-06-19-58/%C2%A72-3>

### mval_3-11_fast_eiendom.md
- Status: MATCH (ingen endring)
- Kilde: <https://lovdata.no/lov/2009-06-19-58/%C2%A73-11>

### mval_8-1_fradragsrett.md
- Status: **REGENERERT** (oppdiktet lovtekst byttet mot verbatim Lovdata)
- Kilde: <https://lovdata.no/lov/2009-06-19-58/%C2%A78-1>
- Gammel versjon: 3 oppdiktede ledd om omsetning/uttak/forskrift
- Ny versjon: Lovdatas ett-setnings-paragraf «Et registrert avgiftssubjekt har rett til fradrag for inngående merverdiavgift på anskaffelser av varer og tjenester som er til bruk i den registrerte virksomheten.»

### mval_8-2_forholdsvis_fradrag.md
- Status: **REGENERERT** (kraftig forkortet versjon byttet mot full verbatim)
- Kilde: <https://lovdata.no/lov/2009-06-19-58/%C2%A78-2>
- Gammel versjon: én kort setning
- Ny versjon: 5 ledd inkludert fem-prosent-reglene

### mval_8-6_tilbakegaende_avgiftsoppgjor.md
- Status: **REGENERERT** (korrekt tekst, feil struktur — ledd (1) var splittet i 5 paragrafer)
- Kilde: <https://lovdata.no/lov/2009-06-19-58/%C2%A78-6>
- Gammel versjon: Fem separate paragrafer under ledd (1)
- Ny versjon: Ett sammenhengende ledd (1) med fem setninger, som i Lovdata

### mval_9-1_kapitalvarer.md
- Status: **REGENERERT** (parafrasert + feil struktur)
- Kilde: <https://lovdata.no/lov/2009-06-19-58/%C2%A79-1>
- Gammel versjon: Parafrasert ledd (1), unøyaktig bokstavliste, feil ledd-nummerering på opphevede ledd
- Ny versjon: Verbatim fra Lovdata, inkludert 31.12.2007-grense og § 6-7-unntak

### mval_9-4_justeringsperiode.md
- Status: **REGENERERT** (parafrasert + ledd (3) manglet)
- Kilde: <https://lovdata.no/lov/2009-06-19-58/%C2%A79-4>
- Gammel versjon: 2 parafraserte ledd, manglet ledd (3)
- Ny versjon: 3 ledd verbatim, inkludert ny ledd (3) om re-innrulling

## Ikke-lov-dokumenter (verifiseres mot primærkilde ved tvil)

Følgende filer er ikke lovparagrafer og er ikke i scope for T160-automatikken. De bør verifiseres manuelt mot primærkilde når de siteres i leveranser:

- `prinsipputtalelse_2014_minilager.md` — SKD-prinsipputtalelse 18.11.2014. Primærkilde: skatteetaten.no eller original PDF.
- `prinsipputtalelse_2014_minilager_tekst.txt` — råtekst som underlag for forrige fil.
- `skatteklagenemnda_datasenter_2020.md` — SKNS1-2020-134. Primærkilde: skatteetaten.no (Skatteklagenemnda sine vedtak) eller Rettsdata.

Disse flagges som uverifiserte i denne audit-runden.

## Script

Verifiseringen er automatisert i `scripts/t160_verify_forretningsplan_lover.py`. Kjøres på nytt med `uv run python scripts/t160_verify_forretningsplan_lover.py`. Scriptet importerer shared pipeline fra `scripts/t158_verify_lovverk.py`.

## Beslutning om overlappende filer

Mval §§ 2-3, 3-11 og 8-6 finnes nå i både `forretningsplan/lover/` og `bakgrunn/lovverk/`. Begge versjonene er verifisert verbatim-korrekte mot Lovdata, men har små format-forskjeller (`a)` vs. `a.`, bold vs. plain ledd-markers, pluss «Relevans for FG30»-seksjon i forretningsplan-versjonen). **Beslutning: beholder begge** — forretningsplan-versjonen inneholder prosjektspesifikk kontekstuell drøfting og brukes direkte i pandoc-renderingen av bankpakka. `bakgrunn/lovverk/` er den rene paragraf-samlingen som brukes som kilde av andre leveranser. Ingen duplikasjon av risiko så lenge begge peker på samme Lovdata-URL og dateringen er lik.
