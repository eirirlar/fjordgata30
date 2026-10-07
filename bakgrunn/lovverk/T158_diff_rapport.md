# T158 diff-rapport — 2026-10-06

## Metode

For hver eksisterende paragraf-fil i `bakgrunn/lovverk/`:

1. `curl -sL -A "Mozilla/5.0" <lovdata-URL> -o <lov>.html`
2. `pup --charset utf-8 'div#PARAGRAF_<nr>' -f <lov>.html` isolerer paragrafblokken
3. `uv tool run html2text` konverterer blokk-HTML til markdown
4. Normaliserer begge sider (eksisterende fil og html2text-output) med tekst-slicing (strip markdown-header, trailing "Del paragraf", endringshistorikk-rader, markdown-emphasis, pipe-separatorer fra html2text sin DL→tabell-rendering, zero-width spaces fra `<sup>`-splitting, nedsiffer-superscripts `²`→`2`, non-breaking spaces, space-før-punktum fra link-stripping, numbered-list escapes `1\.`→`1.`). Paragraf-interne linjeskift kollapses til space; blank linje = paragrafbrudd.
5. `diff -u <eksisterende_norm> <lovdata_norm>` — tom diff = MATCH, ikke-tom diff = reelt avvik i verbatim lovtekst.

HTML-ekstraksjon utføres kun av `pup` + `html2text`. Python-koden gjør kun shell-orchestrering (`subprocess` for curl/pup/html2text), filhåndtering og tekst-normalisering på allerede-konvertert markdown — ingen HTML-parsing.

**Verktøyversjoner:** `pup 0.4.0` · `html2text 2025.4.15` · `curl 8.18.0`.

**EMK art. 6** krevde egen pup-selektor (`div[id="emkn/ARTIKKEL_6"]`) fordi menneskerettsloven-vedlegg bruker `<lov>/<vedleggsnavn>/ARTIKKEL_<nr>`-ankere, ikke `PARAGRAF_<nr>`. Lovdata-URL i T158-spec (`.../VEDLEGG_2`) traff feilaktig menneskerettsloven selv og ikke EMK-vedlegget — korrekt URL er `https://lovdata.no/dokument/NL/lov/1999-05-21-30/emkn/ARTIKKEL_6`. Eksisterende fil hadde allerede korrekt URL i metadata-header.

**Negativ test av normaliseringen:** manuell tampering av én fil (endret "kommunen" → "SKATTEETATEN" i brann-eksplosjonsvernloven § 39) ble korrekt detektert som DIFF av scriptet. Normaliseringen masker altså kun format-forskjeller, ikke verbatim-innhold.

## Oversikt

- **Totalt verifisert:** 51 paragraf-filer
- **MATCH (ingen avvik i verbatim lovtekst):** 51
- **DIFF (avvik funnet):** 0
- **REGENERERT:** 0
- **IKKE FUNNET på Lovdata:** 0
- **ERROR:** 0

Ingen regenerering av paragraf-filer er nødvendig. Alle filer i `bakgrunn/lovverk/` som ble produsert via det tidligere custom-regex-forsøket (T158 forsøk 2, 06.10.2026 kveld) matcher Lovdata verbatim når format-forskjeller (table-rendering av `<dl>`, linjebryting, zero-width spaces rundt `<sup>`, markdown-emphasis-wrapping) normaliseres bort.

**Konsekvens for leveranser (T147):** Siden ingen paragraf-fil hadde reelt avvik i verbatim lovtekst, trenger ingen av de affiserte leveransene korreksjon basert på T158-funn. De tidligere identifiserte avvikene i leveranser (feil § 6/§ 8 i forskrift-brannforebygging-sitater, § 29-4/§ 29-5-forveksling i pbl) var feil **før** paragraf-filene ble regenerert og tilhører derfor T157/T147-sporet, ikke T158. Paragraf-filene er nå autoritative og kan brukes som kildegrunnlag.

## Per-fil-resultat

### brann_eksplosjonsvernloven_1_formaal.md
- Status: MATCH
- Kilde: <https://lovdata.no/lov/2002-06-14-20/%C2%A71>

### brann_eksplosjonsvernloven_6_sikringstiltak.md
- Status: MATCH
- Kilde: <https://lovdata.no/lov/2002-06-14-20/%C2%A76>

### brann_eksplosjonsvernloven_37_paalegg_bruksforbud.md
- Status: MATCH
- Kilde: <https://lovdata.no/lov/2002-06-14-20/%C2%A737>

### brann_eksplosjonsvernloven_39_tvangsmulkt.md
- Status: MATCH
- Kilde: <https://lovdata.no/lov/2002-06-14-20/%C2%A739>

### brann_eksplosjonsvernloven_40_tvangsgjennomforing.md
- Status: MATCH
- Kilde: <https://lovdata.no/lov/2002-06-14-20/%C2%A740>

### brann_eksplosjonsvernloven_41_klage.md
- Status: MATCH
- Kilde: <https://lovdata.no/lov/2002-06-14-20/%C2%A741>

### brann_eksplosjonsvernloven_42_straff.md
- Status: MATCH
- Kilde: <https://lovdata.no/lov/2002-06-14-20/%C2%A742>

### emk_art_6_rettferdig_rettergang.md
- Status: MATCH
- Kilde: <https://lovdata.no/dokument/NL/lov/1999-05-21-30/emkn/ARTIKKEL_6>
- Merk: fetched med egen pup-selektor (`div[id="emkn/ARTIKKEL_6"]`) pga. vedlegg-anker-skjema.

### finansavtaleloven_1-5.md
- Status: MATCH
- Kilde: <https://lovdata.no/lov/2020-12-18-146/%C2%A71-5>

### finansavtaleloven_3-1.md
- Status: MATCH
- Kilde: <https://lovdata.no/lov/2020-12-18-146/%C2%A73-1>

### finansforetaksloven_13-5_forsvarlig_virksomhet.md
- Status: MATCH
- Kilde: <https://lovdata.no/lov/2015-04-10-17/%C2%A713-5>

### forskrift_brannforebygging_4_kunnskap_brannsikkerhet.md
- Status: MATCH
- Kilde: <https://lovdata.no/forskrift/2015-12-17-1710/%C2%A74>

### forskrift_brannforebygging_5_kontroll_bygningsdeler.md
- Status: MATCH
- Kilde: <https://lovdata.no/forskrift/2015-12-17-1710/%C2%A75>

### forskrift_brannforebygging_6_fyringsanlegg.md
- Status: MATCH
- Kilde: <https://lovdata.no/forskrift/2015-12-17-1710/%C2%A76>

### forskrift_brannforebygging_8_oppgradering.md
- Status: MATCH
- Kilde: <https://lovdata.no/forskrift/2015-12-17-1710/%C2%A78>

### forskrift_brannforebygging_9_systematisk_sikkerhetsarbeid.md
- Status: MATCH
- Kilde: <https://lovdata.no/forskrift/2015-12-17-1710/%C2%A79>

### fvl_11_veiledningsplikt.md
- Status: MATCH
- Kilde: <https://lovdata.no/lov/1967-02-10/%C2%A711>

### fvl_17_utredningsplikt.md
- Status: MATCH
- Kilde: <https://lovdata.no/lov/1967-02-10/%C2%A717>

### fvl_24_naar_begrunnes.md
- Status: MATCH
- Kilde: <https://lovdata.no/lov/1967-02-10/%C2%A724>

### fvl_25_begrunnelsens_innhold.md
- Status: MATCH
- Kilde: <https://lovdata.no/lov/1967-02-10/%C2%A725>

### fvl_29_klagefrist.md
- Status: MATCH
- Kilde: <https://lovdata.no/lov/1967-02-10/%C2%A729>

### fvl_41_virkning_feil.md
- Status: MATCH
- Kilde: <https://lovdata.no/lov/1967-02-10/%C2%A741>

### fvl_42_utsatt_iverksetting.md
- Status: MATCH
- Kilde: <https://lovdata.no/lov/1967-02-10/%C2%A742>

### fvl_51_tvangsmulkt.md
- Status: MATCH
- Kilde: <https://lovdata.no/lov/1967-02-10/%C2%A751>

### grunnloven_97.md
- Status: MATCH
- Kilde: <https://lovdata.no/lov/1814-05-17/%C2%A797>

### grunnloven_98.md
- Status: MATCH
- Kilde: <https://lovdata.no/lov/1814-05-17/%C2%A798>

### kulturminneloven_3_forbud_inngrep.md
- Status: MATCH
- Kilde: <https://lovdata.no/lov/1978-06-09-50/%C2%A73>

### kulturminneloven_4_automatisk_fredete.md
- Status: MATCH
- Kilde: <https://lovdata.no/lov/1978-06-09-50/%C2%A74>

### kulturminneloven_8_tillatelse_inngrep.md
- Status: MATCH
- Kilde: <https://lovdata.no/lov/1978-06-09-50/%C2%A78>

### kulturminneloven_15_fredning_nyere_tid.md
- Status: MATCH
- Kilde: <https://lovdata.no/lov/1978-06-09-50/%C2%A715>

### kulturminneloven_19_fredning_omrade.md
- Status: MATCH
- Kilde: <https://lovdata.no/lov/1978-06-09-50/%C2%A719>

### kulturminneloven_20_fredning_kulturmiljo.md
- Status: MATCH
- Kilde: <https://lovdata.no/lov/1978-06-09-50/%C2%A720>

### mval_2-3_frivillig_registrering.md
- Status: MATCH
- Kilde: <https://lovdata.no/lov/2009-06-19-58/%C2%A72-3>

### mval_3-1_avgiftsplikt_omsetning.md
- Status: MATCH
- Kilde: <https://lovdata.no/lov/2009-06-19-58/%C2%A73-1>

### mval_3-11_fast_eiendom.md
- Status: MATCH
- Kilde: <https://lovdata.no/lov/2009-06-19-58/%C2%A73-11>

### mval_8-6_tilbakegaende_avgiftsoppgjor.md
- Status: MATCH
- Kilde: <https://lovdata.no/lov/2009-06-19-58/%C2%A78-6>

### mval_9-2_overgang_justeringsforpliktelse.md
- Status: MATCH
- Kilde: <https://lovdata.no/lov/2009-06-19-58/%C2%A79-2>

### pbl_29-4_byggverkets_plassering.md
- Status: MATCH
- Kilde: <https://lovdata.no/lov/2008-06-27-71/%C2%A729-4>

### pbl_31-2_tiltak_eksisterende_byggverk.md
- Status: MATCH
- Kilde: <https://lovdata.no/lov/2008-06-27-71/%C2%A731-2>

### pbl_31-3_tiltak_strid_med_plan.md
- Status: MATCH
- Kilde: <https://lovdata.no/lov/2008-06-27-71/%C2%A731-3>

### pbl_31-4_unntak_tekniske_krav.md
- Status: MATCH
- Kilde: <https://lovdata.no/lov/2008-06-27-71/%C2%A731-4>

### regnskapsloven_6-2_balanse.md
- Status: MATCH
- Kilde: <https://lovdata.no/lov/1998-07-17-56/%C2%A76-2>

### sivilombudsloven_4_arbeidsomrade.md
- Status: MATCH
- Kilde: <https://lovdata.no/lov/2021-06-18-121/%C2%A74>

### sivilombudsloven_8_vilkar_klage.md
- Status: MATCH
- Kilde: <https://lovdata.no/lov/2021-06-18-121/%C2%A78>

### sivilombudsloven_9_klagefrist.md
- Status: MATCH
- Kilde: <https://lovdata.no/lov/2021-06-18-121/%C2%A79>

### skatteloven_5-30_virksomhetsinntekt.md
- Status: MATCH
- Kilde: <https://lovdata.no/lov/1999-03-26-14/%C2%A75-30>

### skatteloven_14-42_grunnlag_avskrivning.md
- Status: MATCH
- Kilde: <https://lovdata.no/lov/1999-03-26-14/%C2%A714-42>

### skatteloven_14-43_avskrivningssatser.md
- Status: MATCH
- Kilde: <https://lovdata.no/lov/1999-03-26-14/%C2%A714-43>

### tek17_12-7_rom_oppholdsareal.md
- Status: MATCH
- Kilde: <https://lovdata.no/forskrift/2017-06-19-840/%C2%A712-7>

### tvangsfullbyrdelsesloven_7-2_tvangsgrunnlag_utlegg.md
- Status: MATCH
- Kilde: <https://lovdata.no/lov/1992-06-26-86/%C2%A77-2>

### tvangsfullbyrdelsesloven_13-14_fullbyrdelsesmaate.md
- Status: MATCH
- Kilde: <https://lovdata.no/lov/1992-06-26-86/%C2%A713-14>

## Script

Verifiseringen er automatisert i `scripts/t158_verify_lovverk.py`. Kjøres på nytt med `uv run python scripts/t158_verify_lovverk.py` (krever `pup` på PATH + `html2text` som uv-tool). Scriptet er idempotent og kan brukes framover til å re-verifisere paragraf-filer før de siteres i nye leveranser.
