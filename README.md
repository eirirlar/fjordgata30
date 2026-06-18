# Fjordgata 30

## Forutsetninger

```
Python >= 3.10
ImageMagick              (systemverktøy – ikke pip)
Pillow                   (EXIF-lesing i process_images.py)
opencv-contrib-python    (T37, T38 – ikke installer opencv-python i samme venv, de kolliderer)
pyiqa                    (T39 BRISQUE + T40 MUSIQ – laster ned modellvekter ved første kjøring)
torch                    (kreves av pyiqa)
scikit-learn             (vektfinding – T41)
```

Installer ImageMagick via systemets pakkebehandler:

```bash
sudo apt install imagemagick        # Ubuntu/Debian
```

Installer Python-avhengigheter i et virtuelt miljø med `uv`:

```bash
uv venv .venv
uv pip install Pillow opencv-contrib-python pyiqa torch scikit-learn
```

**NB:** Ikke installer `opencv-python` eller `opencv-python-headless` i samme venv –
de kolliderer med `opencv-contrib-python` og bryter `cv2`-importen.

Aktiver miljøet før du kjører scripts:

```bash
source .venv/bin/activate
```

Eller kjør direkte uten aktivering:

```bash
.venv/bin/python3 scripts/process_images.py
```

---

## Scripts

### Prosessere bilder

Legg `.zip`-arkiver fra Google Drive i `../temp/bilder/`, kjør så:

```bash
python3 scripts/process_images.py
```

Utpakkede originaler lagres i `../temp/bilder/extracted/`.
Prosesserte bilder (JPEG ~500 kB) lagres i `../temp/bilder/processed/`.
Hopper automatisk over bilder som allerede er prosessert.

### Skarphetsscore – ett bilde (T37)

```bash
.venv/bin/python3 scripts/scoring/sharpness.py <bildefil>
```

Eksempel:

```bash
.venv/bin/python3 scripts/scoring/sharpness.py ../temp/bilder/processed/20250109_114732.jpg
# → 20250109_114732.jpg: 7.43
```

Returnerer en score fra 1–10 basert på Laplacian-varians, normalisert mot
kalibreringsfilen `scripts/scoring/sharpness_calibration.json`.

Rekalibrering (kjør etter at mange nye bilder er prosessert):

```bash
find ../temp/bilder/processed -name "*.jpg" | \
    .venv/bin/python3 scripts/scoring/sharpness.py --recalibrate
```

### Eksponeringsscore – ett bilde (T38)

```bash
.venv/bin/python3 scripts/scoring/exposure.py <bildefil>
```

Eksempel:

```bash
.venv/bin/python3 scripts/scoring/exposure.py ../temp/bilder/processed/20250109_114732.jpg
# → 20250109_114732.jpg: 8.75  (skygge 3.7%, lys 0.0%)
```

Returnerer clipping-andel (0.0–1.0): andel piksler som er for mørke (< 15) eller
for lyse (> 240). Lav verdi = god eksponering. Normalisering til 1–10 gjøres av score_images.py.

### BRISQUE teknisk kvalitet – ett bilde (T39)

```bash
.venv/bin/python3 scripts/scoring/brisque.py <bildefil>
```

Returnerer teknisk kvalitetsscore 1–10 basert på BRISQUE. Krever kalibreringsfil
(`scripts/scoring/brisque_calibration.json`) – uten den vises rå BRISQUE-score.
Første kjøring laster ned modellvekter (~112 kB) automatisk og caches i
`~/.cache/torch/hub/pyiqa/`. Påfølgende kjøringer bruker cache.

### MUSIQ estetisk kvalitet – ett bilde (T40)

```bash
python scripts/scoring/musiq.py <bildefil>
```

Første kjøring laster ned modellvekter (~104 MB) automatisk. Påfølgende kjøringer
bruker cache og starter umiddelbart. Viser rå MUSIQ-score inntil kalibrert.

### Score alle bilder (T42)

```bash
.venv/bin/python3 scripts/score_images.py
```

Kjører alle metrikker (skarphet, eksponering, BRISQUE, MUSIQ) på hvert bilde
og skriver resultater til `scripts/scoring/scores.csv`.

Test med 10 bilder først:

```bash
.venv/bin/python3 scripts/score_images.py --limit 10
```

Scriptet er idempotent – bilder som allerede er scoret hoppes over. MUSIQ tar
1–3 sek/bilde, så et fullt kjør på 1256 bilder tar ca. 30–60 min.

Kolonner i `scores.csv`:
`filnavn, sharpness_raw, exposure_raw, brisque_raw, musiq_raw, sharpness, exposure, brisque, musiq, total`

Normaliserte scorer (1–10) beregnes automatisk (Pass 2) etter at råscorene er samlet.

---

## Mappestruktur

```
fjordgata30/
├── CLAUDE.md              – prosjektkontekst for AI
├── TASKS.md               – oppgaveliste med status
├── README.md              – dette dokumentet
├── scripts/
│   ├── process_images.py  – bildeprosessering (zip → JPEG)
│   ├── score_images.py    – bildescoring (T42)
│   └── scoring/           – moduler for hver metrikk (T37–T40)
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
