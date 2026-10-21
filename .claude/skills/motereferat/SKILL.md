---
name: motereferat
description: Fra lydopptak i referat/nye/ til ferdig møtereferat. Kjører WhisperX-transkripsjon via scripts/transcribe_audio.py, identifiserer talere (SPEAKER_00..N → navn fra sammenhengen), strukturerer i etablert referatformat basert på statusmøter 01-05, lagrer som referat/YYYY-MM-DD_statusmote_XX.md.
---

# Møtereferat fra lydopptak

## Når skill-en skal brukes

Når brukeren:

- Har lagt lydfil(er) i `referat/nye/` og vil ha ferdig referat
- Ber om å «transkribere opptaket» eller «lag referat fra møtet»
- Trigger-fraser: «lag referat», «transkriber møtet», «fra lyd til referat»

**Krever:** WSL2/Linux (ikke Windows-native) med `whisper-env`-venv aktivert og `HF_TOKEN` satt. Se `docs/transkribering.md`.

## Trinn-for-trinn

### 1. Verifiser oppsett og lydfiler

```bash
ls referat/nye/
```

Lydformater som støttes: `.m4a`, `.mp3`, `.wav`, `.mp4`.

Hvis WSL2/Linux-miljøet ikke er klart (venv ikke aktivert, HF_TOKEN mangler), flagg til bruker. Transkripsjon fungerer ikke i Windows-native shell.

### 2. Kjør transkripsjon

```bash
python scripts/transcribe_audio.py
```

Scriptet:

- Iterer alle lydfiler i `referat/nye/`
- Hopper over filer som allerede har `<stem>.srt`
- Kjører WhisperX med `--model large-v2 --language no --compute_type float32 --diarize --batch_size 4`
- Produserer `<stem>.srt` ved siden av lydfilen

Transkripsjon tar typisk 1–3 ganger lydens lengde på CPU, raskere med GPU.

### 3. Les .srt-filen og identifiser talere

Talerne er merket `SPEAKER_00`, `SPEAKER_01` osv. Identifiser hvem som er hvem ved å:

- Lytte etter navn som blir nevnt («Eirik, hva mener du?»)
- Se på rolleinformasjon i teksten (hvem styrer møtet, hvem presenterer status)
- Krysse mot kjent deltakerliste fra møtekonteksten
- Sjekk `data/team.json` for autoritativt register av personer og roller

Hvis identifisering er usikker, flagg til bruker (f.eks. «SPEAKER_02 kan være Kristian eller Ole Morten — bekreft»).

### 4. Les tidligere referater som mal

- `referat/2026-03-02_statusmote_01.md`
- `referat/2026-03-06_statusmote_02.md`
- `referat/2026-03-13_statusmote_03.md`
- `referat/2026-04-14_statusmote_04.md`
- `referat/2026-04-17_statusmote_05.md`
- `referat/2026-06-11_referat_statusmote_tbrt.md` (annen type møte: med TBRT)

Studer formatet: deltakerliste med rolle, agenda, kronologisk gjennomgang per tema, aksjonspunkter med ansvarlig og frist.

### 5. Strukturer referatet

**Grunnstruktur:**

```markdown
# Statusmøte XX — DD.MM.YYYY

**Sted:** <sted eller «Teams»>
**Tid:** <tidspunkt>

**Deltakere:**

- Navn (rolle/organisasjon) \
- Navn (rolle/organisasjon) \
- ...

## Agenda

1. ...
2. ...

## Gjennomgang

### <Tema 1>

<Kort oppsummering av diskusjonen. Sitér når det er en konkret beslutning eller kommentar. Ikke lim inn transkripsjon ord for ord — bearbeidet referat.>

### <Tema 2>

...

## Aksjonspunkter

| Aksjon | Ansvarlig | Frist |
|---|---|---|
| ... | ... | ... |
```

**Markdown hard linebreak** (`\`) på hver deltaker-linje slik at listen ikke kollapser i pandoc/docx-rendering (CLAUDE.md-regel).

### 6. Lagre og flytt lydfila ut av `nye/`

**Målfil:** `referat/YYYY-MM-DD_statusmote_XX.md`

- `XX` = fortløpende nummer. Finn høyeste `statusmote_XX` i `referat/` og bruk neste.
- Hvis møtet ikke er et vanlig statusmøte (f.eks. TBRT-møte, bank-møte): bruk `referat/YYYY-MM-DD_<type>mote_<kort>.md`

Når referatet er lagret: flytt lydfila og .srt-fila ut av `referat/nye/` (opp til `referat/` eller slett `nye/`-innholdet hvis det ikke er behov for å bevare dem).

## Regler som gjelder

- **Alle referater skrives på norsk** (bokmål)
- **Ikke navngi brukeren** i rolle-bestemmende prosa — bruk «prosjektleder» hvis det er mer passende enn fornavn. Deltakerlisten og sitater er unntak (CLAUDE.md).
- **Markdown hard linebreak** på deltakerlisten og i andre korte-linje-blokker
- **Krysssjekk mot `data/team.json`** for riktig navn, rolle, organisasjon

## Historisk referanse

- Statusmøter 01-05 i mars-april 2026 er etablert format
- `scripts/transcribe_audio.py` er WhisperX-pipeline (T-nummer finnes i ARCHIVE)
- `data/team.json` er autoritativ person-/organisasjon-register (T128)

## Kjente feil å unngå

- Transkripsjon kjøres på Windows direkte — WhisperX trenger WSL2/Linux
- Ferdig referat uten identifisering av SPEAKER_00..N — gjør det umulig å lese
- Ordrett transkripsjon limt inn — bruk bearbeidet referat
- Lydfil blir værende i `referat/nye/` etter at referat er levert — pipelinen tolker den som nyinnkommende neste gang
- Feil nummerering (`statusmote_06` når det egentlig er møte med annet organ) — bruk type-navn i stedet for `statusmote_XX`
