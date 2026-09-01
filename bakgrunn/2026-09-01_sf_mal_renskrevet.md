---
title: "Mal — SkatteFUNN-søknad (Mitt SkatteFUNN / Forskningsrådet)"
date: "1. september 2026"
subtitle: "Renskrevet skjemastruktur. Kilde: rå utklipp i bakgrunn/2026-09-01_sf_mal.md"
---

# Om denne malen

Dette er søknadsskjemaet i Mitt SkatteFUNN, skrevet om til en utfyllbar Markdown-mal. Rekkefølgen følger skjemaet side for side.

Malen er **tom**. Den er ikke fylt ut med innhold fra noe konkret prosjekt.

## Tegnforklaring

| Merke | Betyr |
|---|---|
| ⭐ | Obligatorisk felt |
| 📏 | Tegngrense. Skjemaet teller og stopper deg |
| 🔁 | **Gjentakende blokk** — se neste avsnitt |
| 📊 | Vurderingskriterium. Feltet påvirker om søknaden godkjennes |
| 💤 | Feltet påvirker **ikke** vurderingen |
| ℹ️ | Forskningsrådets egen hjelpetekst, gjengitt |

## 🔁 Gjentakende blokker — les dette først

Noen deler av skjemaet er ikke ett felt du fyller ut én gang. De er **dialogbokser** som åpnes på nytt for hvert element du legger inn. Du trykker «Legg til …», fyller ut dialogen, trykker Bekreft, og gjentar.

I denne malen er slike deler markert med 🔁 og satt opp som **én nummerert blokk du kopierer** så mange ganger du trenger.

Det finnes fem gjentakende blokker i skjemaet:

| # | Blokk | Knapp i skjemaet | Antall |
|---|---|---|---|
| 1 | **Person** | «Legg til person» | Fritt. Fire ulike dialogtyper — se seksjon 3 |
| 2 | **Fagkode** | «Legg til flere fagkoder» | 1–5 |
| 3 | **Arbeidspakke** | «Legg til ny arbeidspakke» | 1–8 |
| 4 | **Aktivitet** *(inne i hver arbeidspakke)* | «Legg til ny aktivitet» | 2–8 **per arbeidspakke** |
| 5 | **Kostnad** *(inne i hver arbeidspakke)* | «Legg til kostnad» | Fritt **per arbeidspakke** |

**Merk at blokk 4 og 5 er nøstet inne i blokk 3.** Har du 8 arbeidspakker med 3 aktiviteter hver, fyller du aktivitetsdialogen 24 ganger.

## ⚠️ Det viktigste å vite på forhånd

**Budsjettet legges inn per arbeidspakke, ikke samlet.** Det finnes ingen side der du fyller inn et totalbudsjett. Du legger kostnader inn i hver enkelt arbeidspakke, fordelt på kostnadstype og på år. Totalbudsjettet regnes ut automatisk til slutt.

> ℹ️ *«Dersom du får godkjent SkatteFUNN-prosjektet, skal du senere rapportere tidsbruk og kostnader per arbeidspakke. Det er derfor lurt å tenke gjennom hvor mange arbeidspakker som er hensiktsmessig for prosjektet.»*

Arbeidspakkeinndelingen er altså også en **rapporteringsstruktur** du må leve med i flere år.

---

# 1. Prosjekttittel

⭐ 💤

> ℹ️ *Legg inn en beskrivende tittel på norsk og engelsk. Når søknaden er til behandling vil tittelen bli publisert på våre nettsider, så unngå sensitiv informasjon i tittelen.*

**Tittel på norsk** 📏 100 tegn

```
```

**Tittel på engelsk** 📏 100 tegn

```
```

---

# 2. Deltakende organisasjoner

⭐

> ℹ️ *Prosjektansvarlig er den organisasjonen som har ansvaret for at prosjektet blir gjennomført i henhold til kontrakten.*

| Felt | Verdi |
|---|---|
| Overordnet enhet | |
| Organisasjonsnummer | |
| Rolle | Prosjektansvarlig organisasjon |
| Utførende enhet | |

*Feltene hentes fra Enhetsregisteret når organisasjonsnummeret er lagt inn.*

---

# 3. Roller i prosjektet

⭐

> ℹ️ *Her skal du registrere personer som skal ha roller i gjennomføringen av prosjektet og andre som skal ha tilgang. E-postadresser og telefonnumre må være identisk med deres påloggingsinformasjon.*

⚠️ **E-post og mobilnummer må stemme nøyaktig med personens innlogging.** Er de ulike, kobles ikke personen til søknaden.

Seksjonen har tre grupper:

| Gruppe | Hva det er |
|---|---|
| **Obligatoriske roller** | Prosjektleder og organisasjonsrepresentant. Oppretter av søknaden fylles inn automatisk |
| **Andre prosjektdeltakere** | Personer med sentrale roller i gjennomføringen |
| **Andre som skal ha tilgang** | Prosjektadministrator, lesere. Ikke de som gjennomfører prosjektet |

> ℹ️ *«Kompetansen og erfaringen til prosjektgruppen må beskrives i søknaden og vil bli vurdert i søknadsbehandlingen.»*

**Det betyr:** listen over personer er bare registrering. Kompetansen deres må i tillegg beskrives i fritekst lenger ute i søknaden.

## 🔁 Blokk 1 — Person

Dialogen har **fire varianter** med ulike felt. Velg riktig variant etter hvilken rolle personen skal ha.

### 🔁 1a — Prosjektleder

Kopier blokken én gang per person.

| Felt | Verdi |
|---|---|
| Fornavn | |
| Mellomnavn | |
| Etternavn | |
| E-post | |
| Landskode | |
| Mobilnummer | |
| Organisasjon | *(søkefelt)* |

### 🔁 1b — Organisasjonsrepresentant

Samme som 1a, men **uten** organisasjonsfelt.

| Felt | Verdi |
|---|---|
| Fornavn | |
| Mellomnavn | |
| Etternavn | |
| E-post | |
| Landskode | |
| Mobilnummer | |

### 🔁 1c — Prosjektdeltaker

Den mest omfattende varianten. Krever **fødselsdato, nasjonalitet og kjønn** i tillegg.

| Felt | Verdi |
|---|---|
| Fornavn | |
| Mellomnavn | |
| Etternavn | |
| Fødselsdato (dd.mm.åååå) | |
| Nasjonalitet | *(standard: Norge)* |
| Kjønn | |
| E-post | |
| Landskode | |
| Mobilnummer | |
| Organisasjon | *(søkefelt)* |

### 🔁 1d — Andre som skal ha tilgang

| Felt | Verdi |
|---|---|
| Rolle | *(standard: Leser)* |
| Fornavn | |
| Mellomnavn | |
| Etternavn | |
| E-post | |
| Landskode | |
| Mobilnummer | |
| Organisasjon | *(søkefelt)* |

---

# 4. Tittel og tema

💤

> ℹ️ *«Her ber vi om generell informasjon om prosjektet. Informasjonen du legger inn på denne siden får ingen betydning for hvordan søknaden vurderes.»*

**Bruk lite tid her.** Unntaket er fagkode og kategori, som styrer hvilken saksbehandler du får.

## 4.1 Tittel

Samme tittel som i seksjon 1. Skjemaet spør to ganger.

**Prosjekttittel på norsk** 📏 100 tegn

```
```

**Prosjekttittel på engelsk** 📏 100 tegn

```
```

## 4.2 Kortnavn

*Valgfritt. Vises kun på Min side.*

**Kortnavn** 📏 60 tegn

```
```

## 4.3 Fagkoder

⭐ 🔁

> ℹ️ *Her skal du velge mellom én og fem fagkoder som passer til prosjektet. En fagkode er en måte vi klassifiserer forskning på i Norge. Vi bruker dette til statistiske formål og analyse.*

### 🔁 Blokk 2 — Fagkode

Kopier blokken 1–5 ganger. Hver fagkode velges i tre nivåer, ovenfra og ned.

| Nivå | Verdi |
|---|---|
| Fagområde | |
| Faggruppe | |
| Fagkode | |

## 4.4 Kategori for søknaden

⭐

> ℹ️ *Velg en kategori som er passende for innholdet i søknaden. Dette er informasjon vi bruker når vi fordeler søknaden til en saksbehandler.*

**Kategori:**

```
```

## 4.5 Videreføring av tidligere prosjekt

⭐

> ℹ️ *Fyll inn prosjektnummeret for det tidligere godkjente SkatteFUNN-prosjektet som dette prosjektet er en fortsettelse av.*

**Er prosjektet en videreføring?** ☐ Ja ☐ Nei

*Hvis ja — prosjektnummer:*

```
```

## 4.6 Flere bedrifter på samme prosjekt

⭐

> ℹ️ *Dersom to bedrifter skal søke SkatteFUNN for det samme prosjektet, må dere sende hver deres søknad for hver deres del av arbeidet.*

**Søkt om det samme prosjektet?** ☐ Ja ☐ Nei

## 4.7 Språk for prosjektdokumenter

⭐

**Språk:** ☐ Bokmål ☐ Nynorsk ☐ Engelsk

---

# 5. Bedriftens virksomhet og bakgrunnen for prosjektet

⭐

## 5.1 Beskriv bedriftens virksomhet

> ℹ️ *Skriv kort hva som er bedriftens virksomhet i dag, for eksempel hva dere produserer, hvilke markeder dere opererer i og om dere er en oppstartsbedrift eller en etablert aktør.*

📏 2 000 tegn

```
```

## 5.2 Beskriv bakgrunnen for prosjektet

> ℹ️ *Skriv kort hva som er bakgrunnen for prosjektet og hvorfor prosjektet er viktig for bedriften.*

📏 2 000 tegn

```
```

---

# 6. Forskning og utvikling (FoU) i prosjektet

⭐ 📊

> ℹ️ *Et SkatteFUNN-prosjekt må ta for seg en FoU-utfordring som ikke har noen kjent løsning i dag. En FoU-utfordring er en problemstilling eller noe som er usikkert og vanskelig som dere må bruke forskning og utvikling (FoU) for å finne ut av. I søknaden må dere beskrive hvordan dere skal gå systematisk frem for å få opp ny kunnskap eller nye ferdigheter som skal gi svar på det som er usikkert og vanskelig.*

## 6.1 Hva er FoU-innholdet i prosjektet?

> ℹ️ *Beskriv tydelig hvilken FoU-utfordring (problemstilling) dere tar for dere i prosjektet, hvorfor den krever forskning og innovasjon (FoU) for å løse, og hvilken metode (systematisk fremgangsmåte) dere skal bruke for å få opp ny kunnskap eller nye ferdigheter for å finne svar på det som er usikkert og vanskelig.*

📏 2 000 tegn

**Feltet krever tre ting i samme tekst:**

1. Hva er FoU-utfordringen?
2. Hvorfor krever den FoU — hvorfor holder ikke kjent kunnskap?
3. Hvilken systematisk metode skal brukes?

```
```

---

# 7. Hovedmål og nyhetsverdi

⭐ 📊

> ℹ️ *Vi bruker denne informasjonen til å vurdere om prosjektet møter dette kriteriet: Prosjektet skal ha som mål å utvikle en ny eller forbedre en eksisterende vare, tjeneste eller produksjonsprosess.*

## 7.1 Beskriv hovedmålet / hva prosjektet skal resultere i

> ℹ️ *Du må formulere et hovedmål som er konkret og som kan etterprøves. Beskriv hvilke nye eller forbedrede varer, tjenester eller produksjonsprosesser prosjektet skal resultere i.*

📏 **1 000 tegn** — merk at dette er et av de korteste feltene

```
```

## 7.2 Hvordan skiller det dere skal utvikle seg fra andre løsninger i markedet?

> ℹ️ *Det dere skal utvikle må ha nyhetsverdi i bransjen. Beskriv hva som er nytt og hvordan det skiller seg fra det som allerede finnes i markedet i dag og hvordan det skiller seg fra det konkurrentene deres har.*

📏 2 000 tegn

**Merk formuleringen:** skjemaet spør om *markedet og konkurrentene*, ikke om forskningsfronten. Svaret bør peke på begge deler.

```
```

---

# 8. Sammendrag

⭐

> ℹ️ *Sammendraget skal gi en kort oppsummering av prosjektet. Et sammendrag inneholder vanligvis en kort oppsummering av bakgrunnen for prosjektet, hva hovedmålet med prosjektet er, hvilke utfordringer dere må løse og hvilken fremgangsmåte dere skal benytte for å gjennomføre prosjektet.*

⚠️ **Sammendraget publiseres offentlig** på Forskningsrådets nettsider og i prosjektbanken hvis prosjektet godkjennes. Ikke skriv noe her du ikke vil at konkurrenter skal lese.

📏 **1 000 tegn**

```
```

---

# 9. Arbeidspakker

⭐ 📊

> ℹ️ *På denne siden skal du beskrive de ulike arbeidspakkene i prosjektet og hvilke aktiviteter dere skal gjøre i hver arbeidspakke. For hver arbeidspakke må dere beskrive FoU-utfordringen og metoden arbeidspakken handler om.*

## 9.1 Prosjektperiode

> ℹ️ *Prosjektperioden kan være 1 til 48 måneder.*
> ℹ️ *Prosjektets startdato må være innenfor perioden 01.01.2026 – 31.12.2026.*

⚠️ **Startdatoen kan settes tilbake i tid til 1. januar i inneværende år.** Det gjør det mulig å ta med kostnader fra arbeid som allerede er utført i år.

| Felt | Verdi |
|---|---|
| Startdato (dd.mm.åååå) | |
| Sluttdato (dd.mm.åååå) | |

## 9.2 Oversikt over arbeidspakker

> ℹ️ *Du må ha minimum 1 arbeidspakke, og kan ha 8 arbeidspakker totalt.*

| Nr. | Arbeidspakke | Startmåned | Sluttmåned |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| … | | | |

---

## 🔁 Blokk 3 — Arbeidspakke

**Kopier hele blokken under én gang per arbeidspakke. Maks 8.**

Hver arbeidspakke er en egen side i skjemaet, med egen FoU-beskrivelse, egne aktiviteter og eget budsjett.

### AP _N_ — navn

**Navn på arbeidspakke / delmål** 📏 100 tegn

```
```

### Varighet

Må ligge innenfor prosjektperioden fra 9.1.

| Felt | Verdi |
|---|---|
| Startmåned (mm/åååå) | |
| Sluttmåned (mm/åååå) | |

### Kategorisering av arbeidspakke

⭐ **Settes per arbeidspakke, ikke for prosjektet samlet.**

> ℹ️ *Velg hvilken kategori av FoU arbeidspakken faller inn under: industriell forskning eller eksperimentell utvikling. **Kategorien har betydning for hvor mye støtte bedriften kan få for prosjektet.***
>
> ℹ️ *For å falle inn under kategorien **industriell forskning**, må arbeidet bestå av planlagt forskning og kritisk undersøkelse med det formål å tilegne seg ny kunnskap og nye ferdigheter for å utvikle nye eller signifikant forbedrede produkter, prosesser eller tjenester.*
>
> ℹ️ ***Eksperimentell utvikling** er når arbeidet består av å tilegne seg og bruke eksisterende vitenskapelig, teknologisk, forretningsmessig og annen relevant kunnskap og ferdigheter for å utvikle nye eller forbedrede produkter, prosesser og tjenester.*
>
> ℹ️ *«De aller fleste SkatteFUNN-prosjekter er eksperimentell utvikling. Derfor har vi forhåndsmerket prosjektet ditt med dette. **Dersom du mener at prosjektet ditt er industriell forskning, må du være nøye med å beskrive hvorfor** når du beskriver FoU-innhold og metode.»*

⚠️ **Viktig.** Feltet er forhåndsutfylt med *eksperimentell utvikling*. Velger du *industriell forskning*, må begrunnelsen ligge i fritekstfeltene for FoU-innhold og metode — ikke bare i avkryssingen. Kategorien styrer taket for samlet offentlig støtte på kostnadene i arbeidspakken.

**Aktivitetskategori:** ☐ Eksperimentell utvikling ☐ Industriell forskning

### Beskriv FoU-utfordringen i arbeidspakken

> ℹ️ *Beskriv hvilke utfordringer som ikke har noen kjent løsning i dag og som dere skal løse i denne arbeidspakken.*

📏 **500 tegn** — svært kort. Én utfordring, presist formulert.

```
```

### Beskriv metoden (fremgangsmåten)

> ℹ️ *Beskriv hvordan dere skal gå systematisk fram for å løse FoU-utfordringen i arbeidspakken.*

📏 1 000 tegn

```
```

### 🔁 Blokk 4 — Aktivitet *(nøstet i blokk 3)*

> ℹ️ *Legg inn aktivitetene du planlegger å gjennomføre i arbeidspakken. Aktivitetene må være nødvendige for å løse utfordringen i arbeidspakken og må skille seg fra vanlig produktutvikling eller drift.*

**Kopier blokken 2–8 ganger per arbeidspakke.** Minimum 2 er obligatorisk.

⚠️ Aktiviteten må **skille seg fra vanlig produktutvikling eller drift**. Dette er stedet søknader oftest ryker.

#### Aktivitet _N_

**Navn på aktivitet** 📏 100 tegn

```
```

**Beskrivelse av aktivitet** 📏 500 tegn

```
```

### 🔁 Blokk 5 — Kostnad *(nøstet i blokk 3)*

> ℹ️ *Her legger du inn hvilke kostnader dere har i arbeidspakken og hvilken organisasjon som har kostnaden. Dersom det er kostnader til FoU-innkjøp i arbeidspakken, må dere legge inn hvem som er FoU-leverandør.*

**Kopier én rad per kostnadstype i denne arbeidspakken.** Beløp føres per år.

| Kostnadstype | Organisasjon | FoU-leverandør | 2026 (kr) | 2027 (kr) | 2028 (kr) |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |

*Feltet «FoU-leverandør» er kun påkrevd for kostnadstypen FoU-innkjøp.*

### Spesifikasjon av budsjettet for arbeidspakken

> ℹ️ *Bruk dette feltet hvis du trenger å utdype eller forklare noen av kostnadene i arbeidspakken.*

📏 500 tegn

**Nyttig her:** forklare timesatser, eller opplyse at en kostnad er et estimat med usikker gjennomføringsvei.

```
```

---
*(slutt på blokk 3 — kopier på nytt for neste arbeidspakke)*

---

# 10. Budsjett — samlet

🔒 **Leses kun. Fylles ikke ut.**

> ℹ️ *Nedenfor er budsjettet for prosjektet. Dersom du skal endre på noen av de budsjetterte kostnadene, må du gå tilbake til arbeidspakken der kostnaden er lagt inn og endre der. Dersom dere ikke har lagt inn budsjett på noen arbeidspakker enda, så vil totalbudsjettet være tomt.*

Totalen summeres automatisk fra kostnadene i hver arbeidspakke. **Vil du endre en sum, må du inn i arbeidspakken.**

| Kostnadskategori | Totalt (kr) |
|---|---|
| | |
| **Totalt** | |

---

# Vedlegg — alle tegngrenser

| Felt | Grense |
|---|---|
| Prosjekttittel, norsk | 100 |
| Prosjekttittel, engelsk | 100 |
| Kortnavn | 60 |
| Bedriftens virksomhet | 2 000 |
| Bakgrunnen for prosjektet | 2 000 |
| FoU-innholdet i prosjektet | 2 000 |
| **Hovedmål** | **1 000** |
| Nyhetsverdi mot markedet | 2 000 |
| **Sammendrag** *(publiseres)* | **1 000** |
| Navn på arbeidspakke | 100 |
| **FoU-utfordring per arbeidspakke** | **500** |
| Metode per arbeidspakke | 1 000 |
| Navn på aktivitet | 100 |
| Beskrivelse av aktivitet | 500 |
| Kostnadsspesifikasjon per arbeidspakke | 500 |

**Samlet fritekst i hele søknaden:** ca. 9 000 tegn i hovedfeltene, pluss 1 500 tegn per arbeidspakke og 600 tegn per aktivitet.

# Vedlegg — antallsgrenser

| Element | Min | Maks |
|---|---|---|
| Fagkoder | 1 | 5 |
| Arbeidspakker | 1 | **8** |
| Aktiviteter per arbeidspakke | **2** | 8 |
| Prosjektets varighet | 1 mnd | 48 mnd |
| Personer | — | Ingen oppgitt grense |
| Kostnadsrader per arbeidspakke | — | Ingen oppgitt grense |
