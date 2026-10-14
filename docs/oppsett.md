# Førstegangsoppsett (per maskin)

Stegene under gjøres én gang per ny maskin. Hopp over blokker for verktøy du ikke trenger.

For aktivering per terminalvindu, se [aktivering.md](aktivering.md).

## 1.1 Felles: `uv` og `pipx`

`uv` brukes til å styre Python-versjoner og virtuelle miljøer.

**Linux / WSL2:** På Ubuntu 24.04+ / Debian er system-Python «externally-managed», så `pip install uv` direkte fungerer ikke – bruk `pipx`:

> **Kjør i:** WSL2 Ubuntu (eller native Linux)

```bash
sudo apt install pipx        # hvis pipx ikke er installert
pipx install uv
pipx ensurepath              # legger ~/.local/bin på PATH
```

Restart shellet etter `pipx ensurepath` første gang.

**Windows:**

> **Kjør i:** PowerShell / CMD (Windows)

```powershell
winget install --id=astral-sh.uv
```

Alternativt: last ned fra <https://docs.astral.sh/uv/getting-started/installation/>.

**Oppgradering av `uv`:** `pipx install uv` og `winget install` er idempotente på "finnes/finnes ikke" – de oppgraderer *ikke* en eksisterende installasjon (`pipx install uv` melder `'uv' already seems to be installed. Not modifying...`). Bruk en av:

> **Kjør i:** Vilkårlig skall – forutsetter at `uv` finnes på PATH

```bash
uv self update                       # anbefalt – uv sin egen updater, plattform-agnostisk
```

Alternativt, hvis `uv self update` av en eller annen grunn feiler:

```bash
pipx upgrade uv                      # Linux/WSL2 (pipx-installasjon)
pipx install uv --force              # Linux/WSL2 (full reinstall)
winget upgrade --id=astral-sh.uv     # Windows (winget-installasjon)
```

## 1.2 Bildescoring

**a) ImageMagick (systemverktøy):**

- **Windows:** Last ned installer fra <https://imagemagick.org/script/download.php#windows>
- **Linux / WSL2:**

> **Kjør i:** WSL2 Ubuntu (eller native Linux)

```bash
sudo apt install imagemagick
```

**b) Python 3.11-venv med bildescoring-avhengigheter:**

Bruk Python 3.11 – `pyiqa` trekker inn `numba`/`llvmlite` som pinner seg til Python 3.6–3.9 transitive, så uv kan ikke løse avhengighetstreet på nyere Python (3.12+). uv laster automatisk ned Python 3.11 hvis det ikke er installert.

**Prosjektkonvensjon:** Venven heter `.venv-win` på Windows og `.venv-linux` i WSL2/Linux. Navnet gjør det tydelig når man kommer tilbake til prosjektet hvilken plattform venven tilhører, og gjør sameksistens mulig (mange utviklere veksler mellom Git Bash og WSL2 på samme maskin). Kommandoene er identiske – bare navnet skiller.

**Windows-venv:**

> **Kjør i:** Git Bash (Windows) eller PowerShell (Windows) – fra prosjektroten

```bash
uv venv .venv-win --python 3.11
uv pip install --python .venv-win Pillow opencv-contrib-python pyiqa torch scikit-learn numpy requests open-clip-torch
uv pip install --python .venv-win "transformers<4.41" fairscale
uv pip install --python .venv-win git+https://github.com/xinyu1205/recognize-anything.git
```

**Linux/WSL2-venv:**

> **Kjør i:** WSL2 Ubuntu (eller native Linux) – fra prosjektroten

```bash
uv venv .venv-linux --python 3.11
uv pip install --python .venv-linux Pillow opencv-contrib-python pyiqa torch scikit-learn numpy requests open-clip-torch
uv pip install --python .venv-linux "transformers<4.41" fairscale
uv pip install --python .venv-linux git+https://github.com/xinyu1205/recognize-anything.git
```

Trenger du bare én plattform, kjør bare den ene blokken. Trenger du begge, kjør begge – de forstyrrer ikke hverandre siden mappenavnene er ulike.

**NB:** Ikke installer `opencv-python` eller `opencv-python-headless` i samme venv – de kolliderer med `opencv-contrib-python` og bryter `cv2`-importen.

Fullstendig avhengighetsliste:

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
python-docx              (post-prosessering av docx – tabellrammer og kolonnebredder)
```

**c) Modellvekter (lastes ned ved første kjøring):**

- **RAM+ (~2 GB):** `score_ram.py` laster ned automatisk til `~/.cache/ram/` ved første kjøring via `requests`.
- **MUSIQ (104 MB):** På Windows må denne lastes ned manuelt første gang – se [Kjente feil og fallbacks](referanse.md#kjente-feil-og-fallbacks).

## 1.3 Dokumentkonvertering

Pandoc er valgt konverteringsverktøy for docx/pptx/pdf. Alle PDF-konverteringer må støtte mermaid-diagrammer inline i Markdown; DOCX bør. Det krever tre systempakker: `pandoc`, **Node via nvm** + `mermaid-filter`, og TeX Live med xelatex (bare for PDF).

Node installeres via `nvm` (Node Version Manager) slik at Node-versjonen er eksplisitt versjonsstyrt og user-lokal – ikke bundet til systemets pakkebehandler.

**Windows (Chocolatey):**

> **Kjør i:** PowerShell (Windows, som administrator) – kjør `choco`-kommandoene her

```powershell
choco install pandoc
choco install nvm
```

Åpne deretter et **nytt** PowerShell- eller CMD-vindu (ikke admin) for at nvm skal være på PATH:

> **Kjør i:** PowerShell / CMD (Windows) – nytt vindu, uten admin

```powershell
nvm install lts
nvm use lts
npm install -g mermaid-filter
```

**For PDF-generering:** Installer TeX Live 2026 fra <https://tug.org/texlive/> (egen installer, ikke via choco).

**Linux / WSL2 (Ubuntu/Debian):**

> **Kjør i:** WSL2 Ubuntu (eller native Linux)

```bash
sudo apt install pandoc
sudo apt install texlive-xetex texlive-fonts-extra   # for PDF
```

Installer nvm ved å følge kommandoen fra README-en på <https://github.com/nvm-sh/nvm> (installskript-URL-en har versjonsnummer som endres – bruk den offisielle). Etter nvm-install, start nytt shell eller kjør `source ~/.bashrc`, deretter:

> **Kjør i:** WSL2 Ubuntu (eller native Linux) – nytt shell etter nvm-install

```bash
nvm install --lts
nvm use --lts
npm install -g mermaid-filter    # NB: ingen sudo – nvm er user-lokal
```

**NB nvm og `npm -g`:** Med nvm installeres alt user-lokalt under `~/.nvm/versions/node/<versjon>/`. Bruk aldri `sudo npm install -g` – det bryter PATH og lager skrive-tilgang-rot. `nvm use <versjon>` skifter aktiv Node globalt for terminalen.

**Chromium for mermaid-filter (kritisk på Node 24+):** `mermaid-filter` drar inn puppeteer 19, og install-hooken som skulle lastet ned Chromium hopper stille over på moderne Node. Uten Chromium feiler filteret med `spawn … chrome.exe ENOENT`. Se [Kjente feil og fallbacks](referanse.md#kjente-feil-og-fallbacks) for manuell nedlasting eller fallback til systeminstallert Chrome/Edge.

## 1.4 Transkribering (WSL2/Linux)

WhisperX kombinerer OpenAI Whisper med automatisk taler-separasjon (pyannote). Kjøres i **WSL2/Linux** – ikke Windows direkte. Alle kommandoer i denne seksjonen kjøres i WSL2-terminalen (eller native Linux).

**a) Installer WhisperX i en Python 3.12-venv:**

> **Kjør i:** WSL2 Ubuntu (eller native Linux)

```bash
python3.12 -m venv whisper-env
source whisper-env/bin/activate
python -m pip install whisperx
```

WhisperX krever Python 3.12.

**b) HuggingFace-konto og token:**

- Opprett konto på [huggingface.co](https://huggingface.co)
- Gå til [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens) og generer et **read**-token
- Legg tokenet i miljøvariabelen (helst i `~/.bashrc` for permanent effekt):

> **Kjør i:** WSL2 Ubuntu (eller native Linux)

```bash
export HF_TOKEN=hf_xxxxxxxxxxxxxxxxxxxx
```

**c) Godta brukervilkår for tre pyannote-modeller:**

Logg inn på HuggingFace og klikk **"Agree and access repository"** på disse tre sidene:

| Modell | URL |
|---|---|
| `pyannote/segmentation-3.0` | <https://huggingface.co/pyannote/segmentation-3.0> |
| `pyannote/speaker-diarization-3.1` | <https://huggingface.co/pyannote/speaker-diarization-3.1> |
| `pyannote/embedding` | <https://huggingface.co/pyannote/embedding> |

Uten disse tillatelsene feiler diariseringssteget med en autentiseringsfeil.
