---
name: last-ned-paragraf
description: Last ned lovparagraf verbatim fra Lovdata via curl, parse HTML, lagre som .md med metadata-header i bakgrunn/lovverk/ eller forretningsplan/lover/. Bruk ALLTID før en leveranse eller chat-utkast refererer en konkret paragraf, ledd eller punktum. Forbudt å bruke WebFetch — den returnerer AI-prosessert parafrase.
---

# Last ned lovparagraf verbatim fra Lovdata

## Når skill-en skal brukes

**Alltid** før du navngir en konkret paragraf, ledd eller punktum (eks. «fvl § 29», «mval § 3-11 første ledd», «brann- og eksplosjonsvernloven § 39 tredje punktum») i:

- Leveranser (klager, søknader, notater, rapporter)
- Utkast og forslag
- Chat-svar

**Unntak:** Hvis paragrafen allerede finnes som verifisert .md-fil i `bakgrunn/lovverk/` eller `forretningsplan/lover/` med metadata-header og hentedato, kan den brukes som kilde direkte. Re-verifisér sitatet mot filen før utsending.

## Trinn-for-trinn

### 1. Identifisér paragrafen

- Lov: full navn og kortnavn (fvl, mval, pbl, offl, kml, osv.)
- Paragrafnummer (og evt. ledd/punktum)
- Hva paragrafen regulerer (brukes i filnavn-beskrivelsen)

### 2. Konstruer Lovdata-URL

Grunnmønster for en paragraf:

```
https://lovdata.no/dokument/NL/lov/<yyyy-mm-dd>-<nr>/§<n>
```

For forskrifter:

```
https://lovdata.no/dokument/SF/forskrift/<yyyy-mm-dd>-<nr>/§<n>
```

### 3. Last ned med curl via Bash — ALDRI WebFetch

```bash
curl -s -A "Mozilla/5.0" "<lovdata-url>" -o /tmp/paragraf.html
```

**Hvorfor curl, ikke WebFetch:** WebFetch returnerer AI-prosessert innhold (parafrase/sammendrag). Audit (T157 i ARCHIVE.md) avdekket at parafrase systematisk gled inn i leveranser til forvaltningsorganer. Dette er den enkeltregelen i prosjektet som har gått mest galt — bruk alltid curl.

### 4. Parse HTML og ekstraher §-tekst verbatim

Enten via regex eller BeautifulSoup via `uv run python`:

```bash
uv run --with beautifulsoup4 python - <<'PY'
from bs4 import BeautifulSoup
html = open('/tmp/paragraf.html').read()
soup = BeautifulSoup(html, 'html.parser')
# Finn relevante element — Lovdata bruker typisk <div class="paragraf"> eller <section>
# Ekstraher tekst og bevare paragrafens struktur
PY
```

Verifiser visuelt at parsingen fanget hele paragrafen inkludert alle ledd og bokstavpunkter.

### 5. Lagre som .md med metadata-header

**Filnavn:** `<lov_kortnavn>_<para>_<beskrivelse>.md`

- `fvl_17_utredningsplikt.md`
- `mval_3-11_fast_eiendom.md`
- `sivilombudsloven_8_vilkar_klage.md`
- `brann_eksplosjonsvernloven_39_tvangsmulkt.md`

**Målmappe:**

- MVA-paragrafer: `forretningsplan/lover/`
- Alt annet: `bakgrunn/lovverk/`

**Metadata-header + verbatim tekst:**

```markdown
---
kilde: "<Lovens fulle tittel, slik Lovdata presenterer den>"
lovnr: "YYYY-MM-DD nr. X"
url: https://lovdata.no/dokument/NL/lov/YYYY-MM-DD-X/§<n>
hentet: YYYY-MM-DD
---

# § <n>. <paragrafens overskrift>

<Verbatim paragraftekst, inkludert alle ledd og bokstavpunkter, slik det står på Lovdata.>
```

### 6. Verifisering før bruk som kilde

Når en leveranse refererer paragrafen:

- Re-les filen og bekreft at sitatet som brukes i leveransen er ordrett
- Sjekk at paragrafnummer, ledd og evt. punktum stemmer
- Oppdater `hentet`-feltet hvis det er lenge siden sist nedlasting

## Regler som gjelder

- **WebFetch er forbudt** for lovsitater — bruk kun curl.
- Hvis brukeren sier «bruk curl», «ikke bruk webfetch» e.l. i samtalen, er WebFetch forbudt for ALT i resten av samtalen (ikke bare paragrafer).
- Ved tvil om paragraf-nummer eller ledd: omformulér uten paragrafnavn («etter forvaltningsloven», ikke «etter fvl § 29»).
- Full referanse til regelverket: `docs/arbeidsregler/lovparagrafer.md` og `docs/arbeidsregler/webfetch.md`.

## Historisk referanse

- T157 (ARCHIVE.md) — audit som avdekket systematisk parafrase fra WebFetch
- T158 (ARCHIVE.md) — re-opprettelse av alle verbatim paragraf-filer med curl
- T159 (ARCHIVE.md) — gjennomgang av lovsitater i leveranser mot verifiserte filer
- T160 (ARCHIVE.md) — verifisering av lovfiler i `forretningsplan/lover/`

Allerede verifiserte lovfiler ligger i `bakgrunn/lovverk/` (120+ filer) og `forretningsplan/lover/` (MVA-paragrafer og prinsipputtalelser). Sjekk alltid om paragrafen allerede finnes før du laster ned på nytt.

## Kjente feil å unngå

- Bruk av WebFetch — gir parafrase, ikke verbatim
- Siterte lovparagrafer fra hukommelsen uten verifikasjon — ledd og punktum feiles oftest
- Lagring uten `hentet`-dato — fil kan bli stale uten at det oppdages
- Lagring i feil mappe (MVA i `bakgrunn/lovverk/` når det skal i `forretningsplan/lover/`)
- Ekstrahering som kutter paragrafens siste ledd eller bokstavpunkt (sjekk alltid at hele teksten er med)
