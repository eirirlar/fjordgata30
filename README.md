# Fjordgata 30

## Forutsetninger

```
Python >= 3.10
ImageMagick              (systemverktøy – ikke pip)
Pillow                   (EXIF-lesing i process_images.py)
opencv-contrib-python    (sharpness + exposure – ikke installer opencv-python i samme venv, de kolliderer)
pyiqa                    (BRISQUE + MUSIQ – laster ned modellvekter ved første kjøring)
torch                    (kreves av pyiqa, RAM og CLIP)
scikit-learn             (kalibrering)
numpy                    (normalisering)
recognize-anything       (RAM – installeres fra GitHub)
open-clip-torch          (CLIP)
requests                 (nedlasting av store modellvekter på Windows)
```

Installer ImageMagick:

```bash
# Windows – last ned installer fra https://imagemagick.org/script/download.php#windows
# Ubuntu/Debian
sudo apt install imagemagick
```

Installer Python-avhengigheter i et virtuelt miljø med `uv`:

```bash
uv venv .venv
uv pip install Pillow opencv-contrib-python pyiqa torch scikit-learn numpy requests open-clip-torch
uv pip install "transformers<4.41" fairscale
uv pip install git+https://github.com/xinyu1205/recognize-anything.git
```

**NB:** Ikke installer `opencv-python` eller `opencv-python-headless` i samme venv –
de kolliderer med `opencv-contrib-python` og bryter `cv2`-importen.

**NB Windows – MUSIQ-modellvekter (104 MB):** `pyiqa` sin interne nedlasting feiler på store filer via `urllib` på Windows. Last ned manuelt med `requests` første gang:

```bash
.venv/Scripts/python -c "
import requests, pathlib
url = 'https://huggingface.co/chaofengc/IQA-PyTorch-Weights/resolve/main/musiq_spaq_ckpt-358bb6af.pth'
dest = pathlib.Path.home() / '.cache/torch/hub/pyiqa/musiq_spaq_ckpt-358bb6af.pth'
dest.parent.mkdir(parents=True, exist_ok=True)
r = requests.get(url, stream=True, timeout=120)
r.raise_for_status()
open(dest, 'wb').write(b''.join(r.iter_content(8192)))
print('OK')
"
```

**NB Windows – RAM+-modellvekter (~2 GB):** `score_ram.py` laster ned vekter automatisk til `~/.cache/ram/` ved første kjøring via `requests`.

Aktiver miljøet før du kjører scripts:

```bash
# Windows (Git Bash / PowerShell)
source .venv/Scripts/activate
# Linux/macOS
source .venv/bin/activate
```

---

## Dataflyt

```
../temp/bilder/*.zip
        │
        ▼
  process_images.py
        │
        ▼
../temp/bilder/processed/*.jpg
        │
        ├──────────────────────────────┐
        ▼                              ▼
  score_auto.py                  score_ram.py
        │                              │
        ▼                              ▼
  scores_auto.csv            scores_ram.csv
        │                              │
        │                              ▼
        │                        score_clip.py
        │                              │
        │                              ▼
        │                        scores_clip.csv
        │                              │
        │            scores_manual.csv │
        │                   │          │
        │          ┌────────┴──────────┘
        │          ▼
        │   calibrate_combined.py   (også calibrate_auto.py / calibrate_tags.py
        │          │                 for separate vekter)
        │          ▼
        │   weights_combined.json
        │   weights_auto.json
        │   weights_tags.json
        │          │
        └──────────┤
                   ▼
             build_scores.py
                   │
                   ▼
            scores_total.csv
```

---

## Scripts

### 1. Prosessere bilder

```bash
.venv/Scripts/python scripts/process_images.py
```

Pakker ut `.zip`-arkiver fra `../temp/bilder/` og konverterer til prosesserte JPEG (~500 kB).
Utpakkede originaler: `../temp/bilder/extracted/`. Prosesserte bilder: `../temp/bilder/processed/`.
Idempotent – hopper over bilder som allerede er prosessert.

### 2. Råscore bilder – sharpness, exposure, BRISQUE, MUSIQ

```bash
.venv/Scripts/python scripts/score_auto.py
.venv/Scripts/python scripts/score_auto.py --limit 10  # test
```

Skriver råscorer til `scores_auto.csv`. Append-only og idempotent. MUSIQ tar 1–3 sek/bilde.

### 3. Tag bilder med RAM

```bash
.venv/Scripts/python scripts/score_ram.py
.venv/Scripts/python scripts/score_ram.py --limit 10  # test
```

Kjører RAM+ på hvert bilde og skriver tags til `scores_ram.csv`.
Første kjøring laster ned modellvekter (~2 GB) til `~/.cache/ram/`. Idempotent.

### 4. Score tags med CLIP

```bash
.venv/Scripts/python scripts/score_clip.py
.venv/Scripts/python scripts/score_clip.py --limit 10  # test
```

Leser alle unike tags fra `scores_ram.csv`, scorer hvert bilde mot alle tags med CLIP.
Skriver til `scores_clip.csv`. Idempotent.

### 5. Kalibrer kombinert modell (anbefalt)

```bash
.venv/Scripts/python scripts/calibrate_combined.py --dry-run  # se R² uten å skrive
.venv/Scripts/python scripts/calibrate_combined.py             # skriv weights_combined.json
.venv/Scripts/python scripts/build_scores.py                   # oppdater scores_total.csv
```

Ridge-regresjon på alle 723 features (4 auto-metrikker + 719 CLIP-tags) mot manuelle ratings.
Krever `scores_manual.csv`. Skriver `weights_combined.json`. R²≈0.68 (alpha=100).

### 6. Kalibrer separate vekter (alternativ)

```bash
# Auto-metrikker
.venv/Scripts/python scripts/calibrate_auto.py --dry-run
.venv/Scripts/python scripts/calibrate_auto.py

# Tags
.venv/Scripts/python scripts/calibrate_tags.py --dry-run
.venv/Scripts/python scripts/calibrate_tags.py

# Oppdater total
.venv/Scripts/python scripts/build_scores.py
```

Brukes hvis `weights_combined.json` ikke finnes. `build_scores.py` faller tilbake på
50/50-snitt av `auto_score` og `tag_score`.

### 7. Bygg scores_total.csv

```bash
.venv/Scripts/python scripts/build_scores.py
```

Leser alle kildefiler, normaliserer råscorer til 1–10, beregner `total`.
Hvis `weights_combined.json` finnes brukes den. Ellers 50/50-snitt av auto og tag.
Eneste fil som regenereres fullt – alle kildefiler røres ikke.

### Enkeltbilde-debug

```bash
.venv/Scripts/python scripts/scoring/sharpness.py <bildefil>
.venv/Scripts/python scripts/scoring/exposure.py <bildefil>
.venv/Scripts/python scripts/scoring/brisque.py <bildefil>
.venv/Scripts/python scripts/scoring/musiq.py <bildefil>
```

Viser råscore og normalisert score (fra `scores_total.csv`) for ett bilde.

---

## Datafiler

Alle datafiler ligger i `scripts/scoring/`.

### `scores_auto.csv` — append-only, skrives av `score_auto.py`

| Kolonne | Beskrivelse |
|---|---|
| `filnavn` | Bildefilnavn, f.eks. `20260620_080001.jpg` |
| `sharpness_raw` | Laplacian-varians (0–∞, høyere = skarpere) |
| `exposure_raw` | Clipping-andel (0.0–1.0, lavere = bedre eksponering) |
| `brisque_raw` | BRISQUE-score (0–100, lavere = bedre teknisk kvalitet) |
| `musiq_raw` | MUSIQ-SPAQ-score (0–100, høyere = bedre estetisk kvalitet) |

### `scores_manual.csv` — fylles ut manuelt

| Kolonne | Beskrivelse |
|---|---|
| `filnavn` | Bildefilnavn |
| `score` | Manuell rating 1–10 (tom = ikke ratet ennå) |

### `scores_ram.csv` — long format, append-only, skrives av `score_ram.py`

| Kolonne | Beskrivelse |
|---|---|
| `filnavn` | Bildefilnavn |
| `tag` | Ord RAM+ har gjenkjent i bildet, f.eks. `beam`, `debris`, `pipe` |

Én rad per bilde per tag. Et bilde kan ha 5–20 rader.

### `scores_clip.csv` — long format, append-only, skrives av `score_clip.py`

| Kolonne | Beskrivelse |
|---|---|
| `filnavn` | Bildefilnavn |
| `tag` | Tag fra vokabularet (alle unike tags fra `scores_ram.csv`) |
| `clip_score` | Cosine-similaritet mellom bilde og tag (ca. 0.1–0.4) |

Hvert bilde har én rad per tag i hele vokabularet (719 tags × 1258 bilder = 904 502 rader).

### `scores_total.csv` — regenereres fullt av `build_scores.py`

| Kolonne | Beskrivelse |
|---|---|
| `filnavn` | Bildefilnavn |
| `sharpness` | Normalisert sharpness 1–10 (p5/p95) |
| `exposure` | Normalisert exposure 1–10 (p5/p95, invertert) |
| `brisque` | Normalisert BRISQUE 1–10 (p5/p95, invertert) |
| `musiq` | Normalisert MUSIQ 1–10 (p5/p95) |
| `tag_score` | Score fra `weights_tags.json` (referanse, brukes ikke i total hvis combined finnes) |
| `total` | Endelig score 1–10 – fra combined-modell hvis `weights_combined.json` finnes, ellers 50/50 auto+tag |

### `weights_auto.json` — skrives av `calibrate_auto.py`

Lineære regresjonskoeffisienter for de 4 auto-metrikk-scorene + intercept.

### `weights_tags.json` — skrives av `calibrate_tags.py`

Ridge-regresjonskoeffisienter for alle 719 CLIP-tags + intercept.

### `weights_combined.json` — skrives av `calibrate_combined.py`

Ridge-regresjonskoeffisienter for alle 723 features (4 auto + 719 tags).
Inneholder scaler-parametrene (`mean`, `std`) per feature siden features StandardScales
før regresjon. Format:

```json
{
  "intercept": 5.42,
  "features": {
    "sharpness": {"mean": 5.1, "std": 2.3, "coef": 0.18},
    "debris":    {"mean": 0.21, "std": 0.04, "coef": 0.12}
  }
}
```

---

## Mappestruktur

```
fjordgata30/
├── CLAUDE.md                  – prosjektkontekst for AI
├── TASKS.md                   – oppgaveliste med status
├── README.md                  – dette dokumentet
├── scripts/
│   ├── process_images.py      – bildeprosessering (zip → JPEG)
│   ├── score_auto.py          – råscoring, skriver scores_auto.csv
│   ├── score_ram.py           – RAM-tagging, skriver scores_ram.csv
│   ├── score_clip.py          – CLIP-scoring, skriver scores_clip.csv
│   ├── calibrate_auto.py      – kalibrering auto-metrikker, skriver weights_auto.json
│   ├── calibrate_tags.py      – kalibrering tags, skriver weights_tags.json
│   ├── calibrate_combined.py  – kombinert kalibrering, skriver weights_combined.json
│   ├── build_scores.py        – beregner scores_total.csv
│   └── scoring/               – moduler per metrikk + alle datafiler
│       ├── sharpness.py
│       ├── exposure.py
│       ├── brisque.py
│       ├── musiq.py
│       ├── scores_auto.csv
│       ├── scores_manual.csv
│       ├── scores_ram.csv
│       ├── scores_clip.csv
│       ├── scores_total.csv
│       ├── weights_auto.json
│       ├── weights_tags.json
│       └── weights_combined.json
├── bakgrunn/                  – søknader, lovverk, bakgrunnsdokumenter
├── brann/                     – branndokumentasjon og TBRT-korrespondanse
└── referat/                   – møtereferater
```

Bildemapper (utenfor prosjektet):

```
../temp/bilder/
├── *.zip                  – nedlastede arkiver fra Google Drive (input)
├── extracted/             – utpakkede originaler
└── processed/             – prosesserte bilder (output fra process_images.py)
```
