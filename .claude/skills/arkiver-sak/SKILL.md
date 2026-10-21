---
name: arkiver-sak
description: Arkiver lukket sak eller avsluttet serie til bakgrunn/<domene>/arkiv/<sak>/ eller saker/arkiv/<sak>/. Oppdater alle referanser via Python-script med eksplisitt lookup-tabell. Mønsteret er speilet av TASKS→ARCHIVE. Krever eksplisitt bruker-tillatelse per sak — aldri arkiver på eget initiativ.
---

# Arkiver lukket sak eller avsluttet serie

## Når skill-en skal brukes

Når brukeren eksplisitt ber om arkivering av en sak eller serie. Trigger-fraser:

- «arkiver <sak>»
- «denne saken er over, flytt den vekk»
- «dette er historisk nå»
- «flytt kontor-rammesøknad 2023 til arkiv»

**Aldri start på eget initiativ.** Dette er samme prinsipp som TASKS→ARCHIVE-regelen i CLAUDE.md.

## Når skill-en IKKE skal brukes (Type 2 – permanent referanse)

Permanent referanse arkiveres aldri, selv om materialet brukes sjelden:

- Eiendomsmatrikkel, grunnbok, kjøpekontrakt
- Lovtekster (`bakgrunn/lovverk/`, `forretningsplan/lover/`)
- Historisk tilstandsrapport
- Rammesøknad som er godkjent og fortsatt styrer bygget
- Grunnlagsrapporter som potensielt refereres i framtidige vedtak

**Når man er i tvil:** hvis materialet potensielt kan refereres i en framtidig leveranse eller vedtak, er det Type 2 og skal ikke arkiveres.

Les `docs/arbeidsregler/arkivering.md` for full regelsett.

## Trinn-for-trinn

### 1. Avklar hva som skal arkiveres

- Hvilken sak? Hvis sakens navn ikke er entydig: bekreft med bruker.
- Hvor hovedmassen av filene ligger (styrer plassering av arkivet):
  - Hovedsakelig innenfor ett domene (f.eks. brann): `bakgrunn/<domene>/arkiv/<sak>/`
  - Krysser mange domener: `saker/arkiv/<sak>/`

### 2. Finn alle filer som hører til saken

Bruk Glob/Grep for å identifisere kandidater. Typisk å sjekke:

- Dato-rekkevidde: f.eks. «alle 2023-filer om kontorbygg»
- Nøkkelord: «rammesøknad kontor», «BYGG-23/82364»
- Krysser-mappe (`bakgrunn/`, `leveranser/`, `bakgrunn/<domene>/`)

**Vis listen til bruker og få eksplisitt bekreftelse før flytting.** Ambisiøs tolkning tar med for mye.

### 3. Opprett arkiv-undermappen

**Navnekonvensjon:** `<sak_eller_serie_navn>_<tidsrom>/` eller `<sak_eller_serie_navn>/`

Eksempler:

- `bakgrunn/brann/arkiv/tbrt_tilsynssyklus_2018-2022/`
- `bakgrunn/brann/arkiv/kontor_rammesoknad_2023/`
- `saker/arkiv/kontor_rammesoknad_2023/`
- `bakgrunn/arkiv/hrp_intrum_2026/`
- `bakgrunn/stotte/<giver>/arkiv/tilsagn_<ref>_utbetalt/` (hvis et tilsagn er helt avsluttet)

```bash
mkdir -p <target-path>
```

### 4. Flytt filene

```bash
mv <fil1> <fil2> ... <target-path>/
```

For mange filer: bruk flerlinje `mv`-kommando eller en enkel for-løkke.

### 5. Oppdater alle referanser

**Via Python-script med eksplisitt lookup-tabell.** Dette er trygt mønster — ingen regex-magi, bare rene strengerstatninger per unikt filnavn/sti.

```python
import pathlib

replacements = {
    'bakgrunn/<gammel-sti>/': 'bakgrunn/<domene>/arkiv/<sak>/',
    # Legg til én linje per unik sti som endres.
    # Hvis mange filer, generer lookup-tabellen fra fillisten.
}

targets = [
    pathlib.Path('historikk.md'),
    pathlib.Path('TASKS.md'),
    pathlib.Path('ARCHIVE.md'),
    pathlib.Path('docs/mappestruktur.md'),
    # Pluss relevante saker/*/OVERSIKT.md
    # Pluss evt. interne self-referanser i de arkiverte filene selv
]

for path in targets:
    if not path.exists():
        continue
    text = path.read_text(encoding='utf-8')
    orig = text
    for old, new in replacements.items():
        text = text.replace(old, new)
    if text != orig:
        path.write_text(text, encoding='utf-8')
        print(f'  {path}: oppdatert')
```

**Hvorfor Python og ikke sed:** Prosjektets regel er Edit-tool for strukturerte endringer; for mange identiske-mønster erstatninger på tvers av flere filer er Python med eksplisitt lookup-tabell den klareste, auditbare løsningen.

### 6. Verifiser med grep

```bash
```

Erstatt `<gammelt-mønster>` med gamle paths. Alle treff må være forventede (f.eks. inne i løsningsnotater for tidligere tasks, som er historisk dokumentasjon og OK å beholde).

### 7. Oppdater struktur-dokumentasjon

- `docs/mappestruktur.md` – legg inn den nye `arkiv/<sak>/`-mappen
- Hvis saken har sin egen sak-indeks (`saker/<sak>/OVERSIKT.md`): oppdater alle filpekere og vurder om indeksen selv skal flyttes til `saker/arkiv/<sak>/`

### 8. Dokumenter arkiveringen

- Under tasken som ba om arkiveringen: notér hva som ble flyttet, hvor, og hvilke referanser som ble oppdatert
- Vurder om det er grunn til egen T-task (f.eks. T185 for innføring av mønsteret var det)

## Regler som gjelder

- **Arkivering kun på eksplisitt bruker-beslutning per sak.** Aldri på eget initiativ (CLAUDE.md: «Arkivering av dokumenter»).
- **Bekreft fillisten med bruker** før flytting. Ambisiøs tolkning tar med for mye.
- **Grep for stale paths** etter oppdatering. Null overraskelser.
- **Les `docs/arbeidsregler/arkivering.md`** for Type 1 vs Type 2-skillet.

## Historisk referanse

- T184 (TASKS.md) – rydding av `bakgrunn/`-rot inkl. opprettelse av `bakgrunn/tbrt/` (feilplassert, flyttet senere)
- T185 (TASKS.md) – innføring av arkiverings-mønsteret og flytting av TBRT 2018-2022 til `bakgrunn/brann/arkiv/`

Kandidater for framtidig arkivering (ikke utført — krever eksplisitt tillatelse per sak):

- Kontor-rammesøknad 2023 (forkastet 30.12.2025)
- HRP-Intrum-saken (avsluttet 15.09.2026)
- Utbetalte tilsagn når sluttrapport er levert

## Kjente feil å unngå

- Arkivering på eget initiativ uten eksplisitt bruker-tillatelse
- Arkivering av Type 2-materiale (permanent referanse) — matrikkel, lovtekster, grunnlagsrapporter som fortsatt styrer bygget
- Ambisiøs filliste som tar med dokumenter som fortsatt refereres fra aktive saker
- Glemte referanser etter flytting (sjekk alltid historikk.md fotnoter, sak-indekser, OVERSIKT.md-pekere)
- Opprettelse av «arkiv»-mappe på feil nivå — f.eks. `bakgrunn/arkiv/<sak>/` når det bør være `bakgrunn/<domene>/arkiv/<sak>/`
- Avvikende navnekonvensjon (eks. dato i mappenavn: `bakgrunn/fisjon_2026-10-12/` var en slik tabbe som ble korrigert i T184)
