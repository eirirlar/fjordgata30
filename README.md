# Fjordgata 30

## Forutsetninger

```
Python >= 3.10
ImageMagick              (systemverktøy – ikke pip)
Pillow                   (EXIF-lesing i process_images.py)
opencv-contrib-python    (T37, T38 – ikke installer opencv-python i samme venv, de kolliderer)
pyiqa                    (T39 BRISQUE + T40 MUSIQ – laster ned modellvekter ved første kjøring)
torch                    (kreves av pyiqa, RAM og CLIP)
scikit-learn             (vektfinding – T41, T47)
numpy                    (normalisering)
recognize-anything       (RAM – T45, installeres fra GitHub)
open-clip-torch          (CLIP – T46)
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
pip install git+https://github.com/xinyu1205/recognize-anything.git
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

Aktiver miljøet før du kjører scripts:

```bash
# Windows (Git Bash)
source .venv/Scripts/activate
# Linux/macOS
source .venv/bin/activate
```

Eller kjør direkte uten aktivering:

```bash
# Windows (Git Bash)
.venv/Scripts/python scripts/process_images.py
# Linux/macOS
.venv/Scripts/python scripts/process_images.py
```

---

## Scripts

### 1. Prosessere bilder

Legg `.zip`-arkiver fra Google Drive i `../temp/bilder/`, kjør så:

```bash
.venv/Scripts/python scripts/process_images.py
```

Utpakkede originaler lagres i `../temp/bilder/extracted/`.
Prosesserte bilder (JPEG ~500 kB) lagres i `../temp/bilder/processed/`.
Hopper automatisk over bilder som allerede er prosessert.

### 2. Råscore alle bilder – sharpness, exposure, BRISQUE, MUSIQ (T42)

```bash
.venv/Scripts/python scripts/score_images.py
.venv/Scripts/python scripts/score_images.py --limit 10  # test
```

Skriver råscorer til `scripts/scoring/scores_auto.csv`. Append-only og idempotent –
bilder som allerede er scoret hoppes over. MUSIQ tar 1–3 sek/bilde.

### 3. Bygg scores_total.csv med normaliserte scorer og total (T48)

```bash
.venv/Scripts/python scripts/build_scores.py
```

Leser `scores_auto.csv`, normaliserer råscorer til 1–10 og beregner `total`.
Bruker `weights.json` og `tag_weights.json` automatisk hvis de finnes.
Regenereres fullt ut hver gang – kildefilene røres ikke.

### 4. Tag alle bilder med RAM (T45)

```bash
.venv/Scripts/python scripts/tag_images.py
.venv/Scripts/python scripts/tag_images.py --limit 10  # test
```

Kjører RAM+ (Recognize Anything Model) på hvert bilde og skriver tags til
`scripts/scoring/scores_ram.csv` (long format: én rad per bilde per tag).
Første kjøring laster ned modellvekter (~400 MB). Idempotent.

### 5. Score tags med CLIP (T46)

```bash
.venv/Scripts/python scripts/clip_score.py
.venv/Scripts/python scripts/clip_score.py --limit 10  # test
```

Leser alle unike tags fra `scores_ram.csv`, scorer hvert bilde mot alle tags
med CLIP og skriver til `scripts/scoring/scores_clip.csv`. Idempotent.

### 6. Kalibrer vekter – auto-metrikker (T41)

```bash
.venv/Scripts/python scripts/calibrate_weights.py --dry-run  # se resultat
.venv/Scripts/python scripts/calibrate_weights.py             # skriv weights.json
.venv/Scripts/python scripts/build_scores.py                  # oppdater total
```

Lineær regresjon på normaliserte auto-metrikker mot manuelle ratings i
`scripts/scoring/scores_manual.csv`. Skriver `scripts/scoring/weights.json`.

### 7. Kalibrer vekter – tags (T47)

```bash
.venv/Scripts/python scripts/calibrate_tags.py --dry-run  # se topp/bunn-tags
.venv/Scripts/python scripts/calibrate_tags.py             # skriv tag_weights.json
.venv/Scripts/python scripts/build_scores.py               # oppdater total
```

Ridge-regresjon på CLIP-scorer mot manuelle ratings. Viser hvilke tags som
korrelerer positivt (interessant innhold) og negativt. Skriver
`scripts/scoring/tag_weights.json`.

### Enkeltbilde-debug (T37–T40)

```bash
.venv/Scripts/python scripts/scoring/sharpness.py <bildefil>
.venv/Scripts/python scripts/scoring/exposure.py <bildefil>
.venv/Scripts/python scripts/scoring/brisque.py <bildefil>
.venv/Scripts/python scripts/scoring/musiq.py <bildefil>
```

Viser råscore og normalisert score (fra `scores_total.csv`) for ett bilde.

---

## Datafiler

Alle datafiler ligger i `scripts/scoring/`:

| Fil | Produseres av | Innhold |
|---|---|---|
| `scores_auto.csv` | `score_images.py` | Råscorer – append-only |
| `scores_manual.csv` | bruker | Manuelle ratings 1–10 |
| `scores_ram.csv` | `tag_images.py` | RAM-tags – long format, append-only |
| `scores_clip.csv` | `clip_score.py` | CLIP-scorer per tag – long format, append-only |
| `scores_total.csv` | `build_scores.py` | Normaliserte scorer + total – regenereres fullt |
| `weights.json` | `calibrate_weights.py` | Regresjonskoeffisienter, auto-metrikker |
| `tag_weights.json` | `calibrate_tags.py` | Regresjonskoeffisienter, tags |

---

## Mappestruktur

```
fjordgata30/
├── CLAUDE.md              – prosjektkontekst for AI
├── TASKS.md               – oppgaveliste med status
├── README.md              – dette dokumentet
├── scripts/
│   ├── process_images.py  – bildeprosessering (zip → JPEG)
│   ├── score_images.py    – råscoring (T42)
│   ├── build_scores.py    – normalisering og total (T48)
│   ├── tag_images.py      – RAM-tagging (T45)
│   ├── clip_score.py      – CLIP-scoring (T46)
│   ├── calibrate_weights.py – vekter for auto-metrikker (T41)
│   ├── calibrate_tags.py  – vekter for tags (T47)
│   └── scoring/           – moduler per metrikk + datafiler
├── bakgrunn/              – søknader, lovverk, bakgrunnsdokumenter
├── brann/                 – branndokumentasjon og TBRT-korrespondanse
└── referat/               – møtereferater
```

Bildemapper (utenfor prosjektet):

```
../temp/bilder/
├── *.zip                  – nedlastede arkiver fra Google Drive (input)
├── extracted/             – utpakkede originaler
└── processed/             – prosesserte bilder (output fra process_images.py)
```
