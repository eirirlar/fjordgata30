# Aktivering (per nytt terminalvindu)

Aktiver miljøet før du kjører scripts. Dette gjøres i hvert nytt terminalvindu.

For førstegangsoppsett, se [oppsett.md](oppsett.md).

## 2.1 Bildescoring

Aktiver **`.venv-win`** hvis du er på Windows, **`.venv-linux`** hvis du er i WSL2/Linux. Se [1.2 b](oppsett.md#12-bildescoring) for opprettelse.

**Windows-venv (`.venv-win`):**

> **Kjør i:** Git Bash (Windows)

```bash
source .venv-win/Scripts/activate
```

> **Kjør i:** PowerShell (Windows) – alternativ til Git Bash

```powershell
.\.venv-win\Scripts\Activate.ps1
```

**Linux-venv (`.venv-linux`):**

> **Kjør i:** WSL2 Ubuntu (eller native Linux)

```bash
source .venv-linux/bin/activate
```

## 2.2 Transkribering

> **Kjør i:** WSL2 Ubuntu (eller native Linux)

```bash
source whisper-env/bin/activate
export HF_TOKEN=hf_xxxxxxxxxxxxxxxxxxxx   # kun hvis ikke i ~/.bashrc
```

## 2.3 Dokumentkonvertering

Pandoc trenger ikke aktivering – kommandoene er systeminstallert. Ved behov for spesifikk Node-versjon:

> **Kjør i:** Vilkårlig skall (Windows PowerShell/Git Bash eller Linux bash) – syntaks varierer

```bash
# nvm-sh (Linux/WSL2 og Git Bash med nvm-sh):
nvm use --lts

# nvm-windows (choco-installasjonen på Windows):
nvm use lts
```

## 2.4 Analyseverktøy

Ingen aktivering nødvendig – scriptene kjøres via `uv run python`, som henter riktige avhengigheter ad hoc.
