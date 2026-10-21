---
name: pdf-til-md
description: Konverter PDF til Markdown med pdftotext -layout, dato-prefix og kilde-metadata. Brukes når et nytt PDF-dokument skal legges inn i bakgrunn/. Bevarer originalt filnavn i metadata-header slik at kildesporing fungerer selv etter rename. Aldri bruk Read-verktøyet side for side på PDF — det er dyrt og mister struktur.
---

# PDF til Markdown med metadata-sporing

## Når skill-en skal brukes

Når brukeren vil:

- Legge inn en PDF-fil i `bakgrunn/` eller en av undermappene
- Konvertere et mottatt brev, pålegg, vedtak, tilsagn eller rapport
- Innsynsmateriale (eInnsyn, Fylkesmannen, DSB, osv.)

Trigger-fraser: «konverter denne PDF-en», «legg til dette dokumentet», «lag md av <fil>.pdf», «arkiver denne».

## Trinn-for-trinn

### 1. Konverter PDF til tekst med pdftotext

```bash
pdftotext -layout "<original-navn>.pdf" - > /tmp/raw.txt
```

**Hvorfor -layout:** Bevarer kolonneoppsett, tabeller og innrykk tilnærmet som i PDF-en. Uten -layout får du én sammenhengende tekstblokk.

**Alternativer når pdftotext ikke er installert:** `uv run --with pymupdf python` med PyMuPDF-ekstraksjon er fallback. Flagg til brukeren hvis pdftotext mangler.

### 2. Identifiser dato fra innholdet

Prioriterte dato-kilder i rekkefølge:

1. **Brevdato / vedtaksdato** – datoen dokumentet er stemplet med
2. **Mottaksdato** – hvis brevdato mangler
3. **Sakens dato** – som siste utvei

Hvis flere datoer finnes: velg den som er mest relevant for arkivering (vedtaksdato for pålegg, mottaksdato for innkomne brev der brevdato ikke står).

### 3. Normaliser filnavnet

Målformat: `YYYY-MM-DD_<beskrivelse>.md`

- Kun snake_case med små bokstaver
- Beskrivelsen er kort og tematisk (f.eks. `tbrt_tilsynsrapport_varsel_paalegg`, ikke `brev_fra_tbrt_av_15_januar_2018`)
- Fjern spesialtegn (æøå → ae/oe/aa eller behold hvis URL-sikkerhet ikke er et problem; vi beholder dem i dette prosjektet)

### 4. Legg til YAML-frontmatter med kilde-metadata

**Format:**

```markdown
---
kilde: "<Original PDF-filnavn med utvidelse>"
---

# <Dokumentets tittel>

<Dokumentets innhold>
```

**Hvorfor:** Konverterte filer renames nesten alltid ved innsjekk (dato-prefiks, normalisering, forkorting). Uten lagret originalnavn er det ikke mulig å finne tilbake til kilde-PDF-en.

**Særlig kritisk** når leveransen skal ha original-PDF-en som vedlegg i stedet for den konverterte avskriften — originalen er beviset, avskriften er lesbarhetshjelp.

**Hvis frontmatter ikke er aktuelt** (ren `.txt` uten metadata-blokk): legg originalnavnet som første linje med prefikset `Original PDF: ...`.

### 5. Rydd opp i teksten etter behov

Vanlige problemer fra pdftotext:

- Sammenkjørte ord ved kolonneskift
- Ødelagte tabeller (bruk pipe-tabeller hvis gjenopprettbart)
- Side- og linjeskift midt i avsnitt
- Fotnoter som havner i løpende tekst

**Når teksten er svært ødelagt** (OCR av dårlig skan): behold som-er med en kommentar i frontmatter om kvaliteten (`kvalitet: "ocr-korrupt, bruk originalen som kilde"`), eller noter i chat at originalfilen bør brukes direkte.

### 6. Foreslå målmappe

**Hoved-mappen:** `bakgrunn/`

**Undermapper:**

- `bakgrunn/brann/` – brannkonsept, brannteknisk vurdering, TBRT-pålegg og saksdokumenter
- `bakgrunn/brann/arkiv/<sak>/` – avsluttede brann-serier
- `bakgrunn/stotte/<giver>/` – tilsagn, vilkår, originalt søknadsgrunnlag fra støttegiver
- `bakgrunn/eiendom/` – permanente eiendomsdokumenter (matrikkel, grunnbok, kjøpekontrakt)
- `bakgrunn/okonomi/` – regnskapsrapporter
- `bakgrunn/mva/` – skatteetaten-korrespondanse, MVA-vurderinger
- `bakgrunn/enova/` – Enova-søknader
- `bakgrunn/fisjon/` – fisjonsarbeid
- `bakgrunn/lovverk/` – lovtekster (men bruk `last-ned-paragraf`-skill, ikke pdf-konvertering)

Bekreft målmappe med brukeren hvis valget er usikkert.

## Regler som gjelder

- **Aldri bruk Read-verktøyet side for side på PDF.** Det er svært kostbart og mister strukturert tekst. Bruk pdftotext.
- **Dato-prefix** er påkrevd for alle filer i `bakgrunn/` (CLAUDE.md). Unntak: `bakgrunn/stotte/` (følger prosjektmappestruktur) og `bakgrunn/lovverk/` (keyes på lov og paragraf).
- **Kilde-metadata er påkrevd** – uten den mister vi sporingen når filer renames.
- **Alt skrives på norsk** (bokmål) – konverteringer av norske brev blir norsk.

## Historisk referanse

- T17, T27 (ARCHIVE.md) – bulk-konvertering av tidligere `bakgrunn/`-innhold
- T82, T84 (ARCHIVE.md) – rydding av ødelagte konverteringer og trofastighets-sjekk
- T168 (ARCHIVE.md) – eInnsyn-bestilling for Oppdal-saken
- Mønsteret med `kilde:`-frontmatter er etablert i tvangsmulkt-konverteringen i `bakgrunn/brann/` (se OVERSIKT.md der)

## Kjente feil å unngå

- **Mistet originalnavn** – uten `kilde:`-frontmatter er det umulig å finne tilbake til kilde-PDF-en etter rename
- **Feil dato-prioritering** – ikke bruk «dato jeg konverterte» (dagens dato) som filnavn-prefix; bruk dokumentets egen dato
- **Flat lagring i `bakgrunn/`** når det passer bedre i undermappe – f.eks. TBRT-dokument fra 2018-2022 skal direkte til `bakgrunn/brann/arkiv/tbrt_tilsynssyklus_2018-2022/`, ikke `bakgrunn/`
- **Hallusinert innhold** når teksten er svært ødelagt – ikke «fiks» ved å improvisere; be bruker peke på originalen i stedet
- Konvertering av lovparagrafer med denne skill-en – bruk `last-ned-paragraf` for det
