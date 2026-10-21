# Arkivering av dokumenter

Utdyping av kjerneregelen fra `CLAUDE.md`: lukkede saker og avsluttede serier flyttes til `arkiv/`-undermappe etter samme prinsipp som TASKS→ARCHIVE, men kun på eksplisitt bruker-beslutning per sak.

## To typer "gammelhet"

Materiale blir mindre relevant over tid av to grunner som krever ulik håndtering:

### Type 1 – Lukket sak eller avsluttet serie

Noe skjedde ferdig. Vedtaket er fattet, saken er forkastet, tilsagnet er utbetalt, tilsynssyklusen er avsluttet.

**Håndtering:** Arkiveres. Flyttes til `<domene>/arkiv/<sak_eller_serie_navn>/` eller `saker/arkiv/<sak>/`.

**Eksempler:**

- TBRT-tilsynssyklusen 2018-2022 (serie med aksepterte tiltaksplaner uten tvangsmulkt-oppfølging; serien er avsluttet)
- Kontor-rammesøknaden 2023 (forkastet 30.12.2025)
- Et utbetalt tilskudd når hele saken er avsluttet
- En klage som har fått endelig vedtak uten muligheter for videre oppfølging

### Type 2 – Permanent referanse som brukes sjelden

Materialet er fortsatt gyldig og kan trenges, men daglig arbeid rører det ikke.

**Håndtering:** Arkiveres IKKE. Blir værende i vanlig domenemappe.

**Eksempler:**

- Eiendomsmatrikkel, kjøpekontrakt, grunnbok
- Lovtekster (`bakgrunn/lovverk/*`, `forretningsplan/lover/*`)
- Historisk tilstandsrapport
- Rammesøknad som er godkjent og fortsatt styrer bygget

Når man er i tvil: hvis materialet potensielt kan refereres i et framtidig vedtak eller leveranse, er det Type 2 og skal ikke arkiveres.

## Mønster speilet av TASKS→ARCHIVE

| | Oppgaver | Dokumenter |
|---|---|---|
| Aktive/levende | `TASKS.md` | `bakgrunn/<domene>/`, `leveranser/`, `saker/<sak>/` |
| Lukket/arkivert | `ARCHIVE.md` | `bakgrunn/<domene>/arkiv/<sak>/`, `saker/arkiv/<sak>/` |
| Trigger for flytting | Brukeren ber eksplisitt | Brukeren ber eksplisitt |
| Søkeregel | Søk i både ved behov | Søk i både ved behov |

## Konkrete regler

- **Arkivering kun på eksplisitt bruker-beslutning per sak.** Aldri arkiver på eget initiativ, selv om en sak virker lukket. Samme prinsipp som TASKS→ARCHIVE.
- **Navnekonvensjon på arkiv-undermapper:** `<sak_eller_serie_navn>_<tidsrom>/` eller `<sak_eller_serie_navn>/`. Eksempler: `tbrt_tilsynssyklus_2018-2022/`, `kontor_rammesoknad_2023/`, `kmf_tilsagn_240126_utbetalt/`.
- **Hvor arkivet ligger:**
  - For materiale knyttet til et spesifikt domene: `bakgrunn/<domene>/arkiv/<sak>/`
  - For hele saker (ofte krysser domener): `saker/arkiv/<sak>/`
  - Valget avhenger av hvor hovedmassen av filene naturlig hører hjemme.
- **Søk-regel:** Når du leter etter noe i et domene, inkluder `arkiv/`-undermappen i søket. Både aktiv og arkiv er pålitelig innhold.
- **Oppdater referanser etter flytting:** Alle pekere i `historikk.md`, `TASKS.md`, `ARCHIVE.md`, sak-indekser og dokumenter som refererer til arkivert materiale må oppdateres.

## Hva som IKKE arkiveres

- Permanent referanse (Type 2): matrikkel, kjøpekontrakt, lovtekster, grunnlagsrapporter som fortsatt styrer bygget
- Aktive saker, selv om de har ligget stille lenge – stille betyr ikke lukket
- Materiale som refereres aktivt fra pågående saker (f.eks. 2018-2022 TBRT-historikk refereres i tvangsmulkt-saken 2026; dette materialet BLE arkivert fordi serien er avsluttet, men indeksen `saker/tvangsmulkt/OVERSIKT.md` peker fortsatt inn i arkivet)

## Når brukeren signaliserer at noe er lukket

Vanlige formuleringer som indikerer at bruker er klar for arkivering:

- "Arkiver [sak]"
- "Denne saken er over, flytt den vekk"
- "Dette er historisk nå"

Alltid: bekreft hvilke filer som flyttes før du gjør det, slik at ambisiøs tolkning ikke tar med for mye.
