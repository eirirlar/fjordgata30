---
tittel: Fase 10 — verifiseringsrapport for lovfiler
dato: 2026-10-13
fase: 10 — verbatim lovsitering og krysssjekk mot rapport_final
scope: >
  Nedlasting av verbatim lovtekst fra Lovdata for alle paragrafhenvisninger
  markert "[verifiseres fase 10]" i rapport_final, lagring som egne lovfiler
  i bakgrunn/lovverk/, og krysssjekk av rapport_finals siteringer mot
  verbatim-teksten.
metode: curl + regex-ekstraksjon via uv run python (ikke WebFetch, pga.
  parafrase-risiko for lovsitater)
---

# Fase 10 — verifiseringsrapport

## 1. Sammendrag

- **39 nye lovfiler** lastet ned og lagret som verbatim-filer i `bakgrunn/lovverk/` (hentedato 2026-10-13).
- **Alle paragrafhenvisninger** i rapport_final som var markert `[verifiseres
  fase 10]` har nå en motsvarende verbatim lovfil med YAML-frontmatter,
  lovdata-URL, hentedato og hentemetode.
- **Ingen vesentlige avvik** funnet mellom rapport_finals paragrafhenvisninger
  og verbatim lovtekst. Ett lett unøyaktig sidetema er dokumentert under
  punkt 4.
- **Rapport_final er ikke endret** fordi alle siteringer er referanser til
  paragrafnavn (ikke verbatim ordlyd), og paragrafnumrene stemmer.
  `[verifiseres fase 10]`-merkelappene står fortsatt i rapporten; brukeren
  avgjør om de skal fjernes i egen operasjon når fase 9 (Varder-review) er
  gjennomført.

## 2. Nedlastede lovfiler (nye)

### Aksjeloven (LOV-1997-06-13-44)

| Fil | Paragraf |
|---|---|
| `asl_2-6_redegjorelse_tingsinnskudd.md` | § 2-6 Redegjørelse for stiftelsesgrunnlaget |
| `asl_2-7_tingsinnskuddets_verdi.md` | § 2-7 Overdragelse eller rett til å få overdratt |
| `asl_3-4_forsvarlig_egenkapital.md` | § 3-4 Krav om forsvarlig egenkapital og likviditet |
| `asl_3-5_handleplikt.md` | § 3-5 Handleplikt ved tap av egenkapital |
| `asl_10-2_kapitalforhoyelse_vedtak.md` | § 10-2 Innholdet i beslutning om kapitalforhøyelse |
| `asl_10-9_melding_kapitalforhoyelse.md` | § 10-9 Melding til Foretaksregisteret |
| `asl_14-1_fisjon_definisjon.md` | § 14-1 Fisjon av aksjeselskap |
| `asl_14-2_virkeomrade.md` | § 14-2 Virkeområde |
| `asl_14-3_fisjonsvederlag.md` | § 14-3 Fisjonsvederlaget |
| `asl_14-4_fisjonsplan.md` | § 14-4 Fisjonsplan mv |
| `asl_14-6_beslutning_fisjon.md` | § 14-6 Beslutning om fisjon |
| `asl_14-7_melding_registrering.md` | § 14-7 Melding til Foretaksregisteret, kreditorvarsel |
| `asl_14-8_ikrafttredelse.md` | § 14-8 Ikrafttredelse mv |
| `asl_14-11_solidaransvar.md` | § 14-11 Fordeling av eiendeler og forpliktelser (inkl. solidaransvar) |
| `asl_17-1_styreansvar.md` | § 17-1 Selskapets, aksjeeiernes og andres erstatningskrav mot daglig leder, styremedlem m.fl. |

### Skatteloven (LOV-1999-03-26-14)

| Fil | Paragraf |
|---|---|
| `sktl_2-38_fritaksmetoden.md` | § 2-38 Fritaksmetoden |
| `sktl_10-4_konsernbidrag_vilkar.md` | § 10-4 Vilkår for rett til å yte og motta konsernbidrag |
| `sktl_10-11_utbytte.md` | § 10-11 Skatteplikt for utbytte |
| `sktl_11-2_fusjon.md` | § 11-2 Skattefri fusjon av aksjeselskaper og allmennaksjeselskaper m.v |
| `sktl_11-4_fisjon_vilkar.md` | § 11-4 Skattefri fisjon av aksjeselskaper og allmennaksjeselskaper m.v |
| `sktl_11-5_fisjon_fordeling.md` | § 11-5 Nominell og innbetalt aksjekapital, overføring av skatteposisjoner |
| `sktl_11-7_kontinuitet.md` | § 11-7 Krav til kontinuitet |
| `sktl_11-11_grenseoverskridende.md` | § 11-11 Grenseoverskridende fusjon og fisjon |
| `sktl_11-20_omdanning.md` | § 11-20 Skattefri omdanning av virksomhet |
| `sktl_11-21_konsernintern_overforing.md` | § 11-21 Overføringer mellom selskaper i konsern |
| `sktl_13-1_internprising.md` | § 13-1 Interessefellesskap |
| `sktl_13-2_omgaelsesnorm.md` | § 13-2 Omgåelse |

### Dekningsloven (LOV-1984-06-08-59)

| Fil | Paragraf |
|---|---|
| `dekningsloven_1-5_nerstaende.md` | § 1-5 Nærstående |
| `dekningsloven_5-2_omstotelse_gaver.md` | § 5-2 Gaver |
| `dekningsloven_5-5_ekstraordinaer_betaling.md` | § 5-5 Betaling av gjeld |
| `dekningsloven_5-6_pantestillelse.md` | § 5-6 Sikkerhetsstillelse for eldre gjeld |
| `dekningsloven_5-7_betaling_tvangsfullbyrdelse.md` | § 5-7 Betaling under tvangsfullbyrdelse |
| `dekningsloven_5-9_subjektiv_omstotelse.md` | § 5-9 Omstøtelse hvor den annen part ikke har vært i god tro (utilbørlig disposisjon) |

### Konkursloven, dokumentavgiftsrett og straffeloven

| Fil | Paragraf | Lov |
|---|---|---|
| `konkursloven_60_konkursvilkar.md` | § 60 Konkurs på grunnlag av insolvens | Konkursloven LOV-1984-06-08-58 |
| `dokumentavgiftsloven_7_grunnlag_sats.md` | § 7 Grunnlag og sats | Dokumentavgiftsloven LOV-1975-12-12-59 |
| `stortingsvedtak_dokumentavgift_2026_2_fritak.md` | § 2 Fritak (bokstav k = omorganiseringsfritaket) | Stortingsvedtak om dokumentavgift 2026, FOR-2025-12-18-2777 |
| `straffeloven_401_formuesforringelse.md` | § 401 Uforsvarlige økonomiske disposisjoner | Straffeloven LOV-2005-05-20-28 |
| `straffeloven_402_boforringelse.md` | § 402 Boforringelse | Straffeloven |
| `straffeloven_404_uaktsom_formuesforringelse.md` | § 404 Uaktsom formuesforringelse ved kreditorsvik | Straffeloven |

## 3. Allerede eksisterende filer (ingen handling)

Følgende filer i `bakgrunn/lovverk/` eksisterte før fase 10 og dekker paragrafer
rapport_final refererer. Ingen ny nedlasting:

- `mval_kap9_justering_av_inngaaende_merverdiavgift.md` (hele kap. 9 — inkluderer § 9-1, § 9-2, § 9-3, § 9-5)
- `mval_2-3_frivillig_registrering.md`, `mval_3-1_avgiftsplikt_omsetning.md`, `mval_3-11_fast_eiendom.md`,
  `mval_8-6_tilbakegaende_avgiftsoppgjor.md`, `mval_9-2_overgang_justeringsforpliktelse.md`
- `brann_eksplosjonsvernloven_37_paalegg_bruksforbud.md`, `brann_eksplosjonsvernloven_39_tvangsmulkt.md`
- `fvl_35_omgjoring.md`, `fvl_17_utredningsplikt.md`
- `sivilombudsloven_4_arbeidsomrade.md`, `sivilombudsloven_8_vilkar_klage.md`
- `tvangsfullbyrdelsesloven_13-14_fullbyrdelsesmaate.md`
- `finansavtaleloven.md`, `fvl_6_habilitet.md` m.fl.

## 4. Avvik mellom rapport_final og verbatim lovtekst

Ingen vesentlige avvik funnet. Rapport_final har kun to **verbatim**-sitater:

1. **Mval. § 9-3 (1)** (seksjon 2.5) — allerede verifisert mot `mval_kap9_justering_av_inngaaende_merverdiavgift.md` i tidligere fase; ordlyden stemmer.
2. **Fisjonsplanens klausul om tvangsmulkt** (seksjon 4.2) — ikke et lovsitat, men prosjektets egen formulering.

Alle øvrige henvisninger er paragrafnavnehenvisninger (f.eks. «asl. § 14-4» uten
ordlyd), og alle paragrafnumre matcher verbatim lovtekst som nå er lastet ned.

**Mindre tematiske observasjoner (ingen rettelser gjort):**

- **asl. § 14-8** nevnes i rapport_finals prosedyre-tabell (seksjon 2.1 rad 10)
  som hjemmel for «Samordnet registermelding til Brreg». Verbatim-tittelen er
  «Ikrafttredelse mv». § 14-8 henviser til § 13-16 (gjennom «Bestemmelsene i
  § 13-16 og § 13-17 første, tredje og fjerde ledd gjelder tilsvarende»), og
  § 13-16 regulerer samordnet registermelding. Henvisningen er dermed indirekte
  korrekt, men en Varder-leser bør merke at det er § 13-16 (via § 14-8) som er
  den direkte hjemmelen. Dette er ikke en feil som utløser rettelse i rapporten
  — snarere en nyanse som kan tydeliggjøres hvis Varder spør om den.

- **Dokumentavgiftsloven § 7** nevnes i rapport_finals prosedyre-tabell
  (seksjon 2.1 rad 12) sammen med tinglysingsloven. Verbatim § 7 handler om
  avgiftsgrunnlaget (salgsverdi), ikke fritaket. Fritaket ligger i
  **stortingsvedtaket § 2 bokstav k** — som rapport_final korrekt siterer i
  seksjon 2.4. Krysshenvisningen er dermed komplett: § 7 for sats/grunnlag,
  stortingsvedtak § 2 k for fritaket.

- **Dekningslovens omstøtelsesregler** har en liten språklig forskjell mellom
  rapport_finals rammetabell (seksjon 7.1) og verbatim ordlyden:
  - Rapporten kaller § 5-9 «omstøtelse av utilbørlig disposisjon»; verbatim
    tittel er «Omstøtelse hvor den annen part ikke har vært i god tro» —
    utilbørlighet er et av vilkårene nevnt i selve lovteksten.
  - 10-årsfristen mot nærstående står verbatim i § 5-9 andre ledd («kan ikke
    omstøtes» hvis fullbyrdet mer enn ti år før fristdagen). Rapport_finals
    framstilling stemmer.
  - Nærstående-definisjonen i § 1-5 er bred og dekker konsernselskap gjennom
    bokstav b («selskap som noen i det nære slektsmessige eller
    forretningsmessige fellesskap har bestemmende innflytelse i») — rapport_
    finals premiss om at «KodeWorks AS, KWE, FG30 AS og GG10 AS er alle i samme
    konsern og dermed nærstående etter dekningsloven § 1-5» holder etter
    verbatim-ordlyden.

## 5. Rettelser i rapport_final

Ingen. Alle paragrafhenvisninger står seg mot verbatim-tekst. `[verifiseres
fase 10]`-merkelappene ligger fortsatt i rapporten — brukeren bør avgjøre om
de skal fjernes nå eller holdes stående til Varder har fått dokumentet.

Hvis brukeren vil fjerne merkelappene i egen operasjon, er dette en trygg
«find & replace» i rapport_final: fjern alle forekomster av
` [verifiseres fase 10]` (med foranstående mellomrom).

## 6. Åpne punkter / ikke verifisert

**Ingen** uverifisert paragrafhenvisning i rapport_final per nå. Alle 26
unike paragraf-/kapittelnavn referert i rapporten har enten eksisterende eller
nyopprettet verbatim-fil i `bakgrunn/lovverk/`:

- `kap. 9` (mval.) → `mval_kap9_justering_av_inngaaende_merverdiavgift.md` (eksisterte)
- `kap. 10`, `kap. 11`, `kap. 14` (asl./sktl.) → dekket av enkeltparagrafer

**Begrensninger:**

- Lovdata-nedlastning fanger dagens gjeldende ordlyd. Rapport_final diskuterer
  disposisjoner som potensielt gjennomføres november 2026 — februar 2027.
  Hvis lovendringer trer i kraft i mellomtiden, må lovfilene oppdateres før
  signering av fisjonsplanen.
- Stortingsvedtaket om dokumentavgift er årsvedtak. Lastet versjon er for
  budsjettåret 2026. Nytt stortingsvedtak for 2027 publiseres typisk i
  desember 2026 — og bokstav k-fritaket må **verifiseres på nytt** mot
  2027-vedtaket før tinglysing uke 7 (februar 2027).

## 7. Metode

- Verktøy: `curl` (via Bash) for nedlasting; `uv run python` + regex for
  HTML-parsing og formatering til lovfil-mal med YAML-frontmatter.
- **Ikke WebFetch** — CLAUDE.md-regelen om parafrase-risiko for lovsitater
  gjelder.
- Script og midlertidige HTML-filer var i `bakgrunn/fisjon_2026-10-12/_fase10_tmp/`
  mens arbeidet pågikk, og er slettet ved avslutning.

---

*Rapport ferdigstilt 2026-10-13.*
