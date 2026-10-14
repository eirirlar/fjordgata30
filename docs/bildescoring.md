# Bildescoring

Pipelinen tar .zip-arkiver fra `../temp/bilder/`, prosesserer bildene, scorer dem med flere modeller, kalibrerer mot manuelle ratings, og produserer en samlet score per bilde. Se [Dataflyt](referanse.md#dataflyt) for oversikt.

**Manuelt steg:** Legg .zip-arkiver fra Google Drive i `../temp/bilder/` før du kjører pipelinen.

Alle scriptene i denne seksjonen forutsetter at riktig venv er **aktivert** (se [aktivering.md § 2.1](aktivering.md#21-bildescoring)): `.venv-win` på Windows, `.venv-linux` i WSL2/Linux. Etter aktivering er `python`-kommandoen den samme uansett plattform.

## Kjør hele pipelinen

> **Kjør i:** Samme skall som venv-aktiveringen (Git Bash / PowerShell med `.venv-win`, eller WSL2/Linux bash med `.venv-linux`)

```bash
python scripts/score_all.py
```

Kjører alle steg i sekvens. Stopper ved feil. Bruker samme Python-executable som scriptet ble startet med, slik at riktig venv alltid er aktiv.

Stegene er: `process_images.py` → `score_auto.py` → `score_ram.py` → `score_clip.py` → `calibrate_combined.py` → `build_scores.py`.

## Enkeltsteg

Alle enkeltsteg-kommandoer forutsetter aktivert venv (`.venv-win` eller `.venv-linux`) og kjøres i samme skall som pipeline-kommandoen over.

**1. Prosessere bilder**

```bash
python scripts/process_images.py
```

Pakker ut `.zip`-arkiver fra `../temp/bilder/` og konverterer til prosesserte JPEG (~500 kB). Utpakkede originaler: `../temp/bilder/extracted/`. Prosesserte bilder: `../temp/bilder/processed/`. Idempotent – hopper over bilder som allerede er prosessert.

**2. Råscore bilder – sharpness, exposure, BRISQUE, MUSIQ**

```bash
python scripts/score_auto.py
python scripts/score_auto.py --limit 10  # test
```

Skriver råscorer til `scores_auto.csv`. Append-only og idempotent. MUSIQ tar 1–3 sek/bilde.

**3. Tag bilder med RAM**

```bash
python scripts/score_ram.py
python scripts/score_ram.py --limit 10  # test
```

Kjører RAM+ på hvert bilde og skriver tags til `scores_ram.csv`. Første kjøring laster ned modellvekter (~2 GB) til `~/.cache/ram/`. Idempotent.

**4. Score tags med CLIP**

```bash
python scripts/score_clip.py
python scripts/score_clip.py --limit 10  # test
python scripts/score_clip.py --force     # slett og re-score alt (sjeldent)
```

Leser alle unike tags fra `scores_ram.csv`, scorer hvert bilde mot alle tags med CLIP. Skriver til `scores_clip.csv`. Inkrementell og idempotent: nye bilder scores mot hele vokabularet, eksisterende bilder backfilles automatisk mot tags de mangler (typisk pga. nye tags som dukker opp når nye bilder tags-es av RAM). Ingen manuell inngripen kreves når vokabularet vokser – `--force` trengs bare hvis du vil scrap-e alt (f.eks. bytte CLIP-modell).

**5. Kalibrer kombinert modell (anbefalt)**

```bash
python scripts/calibrate_combined.py --dry-run  # se R² uten å skrive
python scripts/calibrate_combined.py             # skriv weights_combined.json
python scripts/build_scores.py                   # oppdater scores_total.csv
```

Ridge-regresjon på alle 723 features (4 auto-metrikker + 719 CLIP-tags) mot manuelle ratings. Krever `scores_manual.csv`. Skriver `weights_combined.json`. R²≈0.68 (alpha=100).

**6. Kalibrer separate vekter (alternativ)**

```bash
# Auto-metrikker
python scripts/calibrate_auto.py --dry-run
python scripts/calibrate_auto.py

# Tags
python scripts/calibrate_tags.py --dry-run
python scripts/calibrate_tags.py

# Oppdater total
python scripts/build_scores.py
```

Brukes hvis `weights_combined.json` ikke finnes. `build_scores.py` faller tilbake på 50/50-snitt av `auto_score` og `tag_score`.

**7. Bygg `scores_total.csv`**

```bash
python scripts/build_scores.py
```

Leser alle kildefiler, normaliserer råscorer til 1–10, beregner `total`. Hvis `weights_combined.json` finnes brukes den. Ellers 50/50-snitt av auto og tag. Eneste fil som regenereres fullt – alle kildefiler røres ikke.

## Velg beste bilder for en periode

> **Kjør i:** Samme skall som venv-aktiveringen (Git Bash / PowerShell med `.venv-win`, eller WSL2/Linux bash med `.venv-linux`)

```bash
python scripts/select_images.py --from 2026-01-01 --to 2026-06-30
python scripts/select_images.py --from 2026-01-01 --to 2026-06-30 --count 20
python scripts/select_images.py --from 2026-01-01 --to 2026-06-30 --output /tmp/utvalg
```

Henter de N beste bildene innenfor en dato-periode basert på `scores_total.csv`. Manuell rating (`manual`-kolonnen) overstyrer alltid modellscoren (`total`). `--output` kopierer de valgte bildene til angitt mappe.

## Enkeltbilde-debug

> **Kjør i:** Samme skall som venv-aktiveringen (Git Bash / PowerShell med `.venv-win`, eller WSL2/Linux bash med `.venv-linux`)

```bash
python scripts/scoring/sharpness.py <bildefil>
python scripts/scoring/exposure.py <bildefil>
python scripts/scoring/brisque.py <bildefil>
python scripts/scoring/musiq.py <bildefil>
```

Viser råscore og normalisert score (fra `scores_total.csv`) for ett bilde.
