# Fjordgata 30

Prosjektrepo for rehabilitering av Fjordgata 30 til minilager. Se `CLAUDE.md` for prosjektkontekst og `TASKS.md` for oppgaveliste.

Denne README-en er en lenkeindeks til dokumentasjonen under `docs/` + en rask oppstart. Detaljer per verktøy ligger i egne tematiske filer.

## Dokumentasjon

| Dokument | Innhold |
|---|---|
| [`docs/oppsett.md`](docs/oppsett.md) | Førstegangsoppsett per maskin: `uv`, bildescoring-venv, Pandoc, WhisperX |
| [`docs/aktivering.md`](docs/aktivering.md) | Aktivering per nytt terminalvindu |
| [`docs/bildescoring.md`](docs/bildescoring.md) | Bruk av bildescoring-pipelinen |
| [`docs/transkribering.md`](docs/transkribering.md) | Transkribering av lydopptak med WhisperX |
| [`docs/dokumentkonvertering.md`](docs/dokumentkonvertering.md) | Pandoc → docx/pdf med mermaid-diagrammer |
| [`docs/analyseverktoy.md`](docs/analyseverktoy.md) | Arealoversikt, konkurranseanalyse, PDF-tegninger |
| [`docs/referanse.md`](docs/referanse.md) | Dataflyt, datafiler, kode-mappestruktur, kjente feil |
| [`docs/mappestruktur.md`](docs/mappestruktur.md) | Prosjektets dokument-/leveransemapper |
| [`docs/interessenter.md`](docs/interessenter.md) | Stakeholder-oversikt |

## Rask oppstart

Prosjektet dekker fire arbeidsverktøy:

| Verktøy | Formål | Miljø |
|---|---|---|
| Bildescoring | Automatisk kvalitetsscoring av arbeidsbilder | Windows (Git Bash / PowerShell) eller Linux |
| Dokumentkonvertering | Markdown → docx/pdf med mermaid-diagrammer | Windows (Git Bash anbefalt) eller Linux |
| Transkribering | Lydopptak → tidsstemplet undertekst med taler-ID | **WSL2/Linux** (ikke Windows direkte) |
| Analyseverktøy | Arealoversikt, konkurransepriser, PDF-tegninger | Windows eller Linux (`uv run`) |

**NB om venvs:** Prosjektet bruker to separate Python-venvs for bildescoring: `.venv-win` (opprettet på Windows i Git Bash/PowerShell) og `.venv-linux` (opprettet i WSL2 eller native Linux). Grunnen er at Python-venvs ikke er portable mellom OS – Windows-binærer og Linux-binærer kan ikke deles. Bruk kun én av dem hvis du kun jobber på én plattform. Se [`docs/oppsett.md § 1.2`](docs/oppsett.md#12-bildescoring). WhisperX bruker sin egen venv `whisper-env` (kun WSL2/Linux).

## Miljøer og valg av skall

Prosjektet må fungere på tvers av flere miljøer. Standardvalg per verktøy:

| Verktøy | Anbefalt skall | Alternativ | Begrensning |
|---|---|---|---|
| Bildescoring | Git Bash på Windows | PowerShell, Linux bash | – |
| Pandoc + mermaid-filter | **Git Bash på Windows** (må ha `.cmd`-endelse på filter) | PowerShell/CMD (uten `.cmd`), Linux bash | – |
| WhisperX | WSL2 med Ubuntu | Native Linux | **Fungerer ikke i Windows-native shell** (Git Bash/PowerShell/CMD) |
| Analyseverktøy | Vilkårlig – kjøres via `uv run python` | – | – |

Cygwin frarådes – stier som `/cygdrive/c/...` er inkompatible med resten av oppsettet. Bruk Git Bash for Windows-arbeid.

### Skall-markører brukt i dokumentasjonen

Kodeblokker i `docs/`-filene er merket med **hvilket skall de skal kjøres i** på linjen rett over. Betydningen:

| Markør | Skall |
|---|---|
| `Kjør i: PowerShell (Windows, som administrator)` | PowerShell startet med «Kjør som administrator» |
| `Kjør i: PowerShell / CMD (Windows)` | Vanlig PowerShell- eller CMD-vindu på Windows |
| `Kjør i: Git Bash (Windows)` | MINGW64-terminal fra Git for Windows |
| `Kjør i: WSL2 Ubuntu (eller native Linux)` | Linux-shell – enten WSL2 på Windows eller native Linux |
| `Kjør i: Git Bash (Windows) eller bash (Linux/WSL2)` | Cross-platform bash-kommando – begge fungerer |
| `Kjør i: Vilkårlig skall` | Kjører uendret i alle skall på begge plattformer (typisk `uv run …`) |
