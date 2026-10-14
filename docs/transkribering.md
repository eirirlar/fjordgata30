# Transkribering av lydopptak

**Manuelt steg:** Legg én eller flere lydfiler i `referat/nye/` (formater: `.m4a`, `.mp3`, `.wav`, `.mp4`). Filnavn er fritt – f.eks. `2026-08-25_statusmote.m4a`. Filene kan legges dit fra hvilken som helst plattform (også Windows Explorer / File Explorer i WSL2 via `\\wsl$\Ubuntu\...`).

**Kjør transkripsjon:**

> **Kjør i:** WSL2 Ubuntu (eller native Linux) – med `whisper-env` aktivert og `HF_TOKEN` satt (se [aktivering.md § 2.2](aktivering.md#22-transkribering))

```bash
python scripts/transcribe_audio.py
```

Scriptet iterer alle lydfiler i `referat/nye/`, hopper over de som allerede har `<stem>.srt` ved siden av, og kjører WhisperX på resten med prosjektets standardflagg (`--model large-v2 --language no --compute_type float32 --diarize --batch_size 4`).

`--batch_size 4` er trygt på de fleste maskiner. Endre i `scripts/transcribe_audio.py` (`WHISPERX_ARGS`) hvis du har mer GPU-minne.

**Utdata:** For hver lydfil `<stem>.m4a` skrives `<stem>.srt` i samme mappe – undertekster med tidskoder og taler-ID per segment.

**Fra transkripsjon til referat:** Talerne i utdata er merket `SPEAKER_00`, `SPEAKER_01` osv. Identifiser hvem som er hvem ut fra sammenhengen og skriv referatet i `referat/YYYY-MM-DD_statusmote_XX.md` etter det etablerte formatet.
