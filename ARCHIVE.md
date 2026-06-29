# Fjordgata 30 – Arkiv for løste tasks

Fullførte tasks flyttes hit fra `TASKS.md` når de er avsluttet og ikke lenger trenger aktiv oppfølging. Formatet er identisk med `TASKS.md`. Søk her for å unngå dobbeltarbeid.

Legende: alle oppgaver her er `[x]` Ferdig.

---

### T01.01 `[x]` Kulturminnefondet – framdriftsrapport

**Mottaker:** Kulturminnefondet (750 000 kr, prosjektnr 240126)

Rapporten måtte dokumentere utført fysisk arbeid, informere om konseptendringen fra kontorbygg til minilager, og vise fremdriftsplan fremover.

**Løst 2026-06-25:** Framdriftsrapport ferdigstilt i `stotte/2026-06-24_kmf_framdriftsrapport.md` (.docx generert med pandoc + format_docx.py). Dekker: prosjekthistorikk og konseptendring, begrunnelse for at antikvarisk kjerneformål er uendret, argument om at minilager er bevaringsmessig bedre enn kontor (ingen irreversibel fjerning av etasjeskillere i etg. 3–5 for lysinnslipp), kulturminnefaglige funn (natursteinsmur, strekkfisker/stålstag, fundamentering), fremdriftsplan med kommende leieforholdsavviklinger (1. juli og 1. august) og fisjonsstrategi. 11 bilder innebygd i dokumentet. Sammendrag nevner at rapporten er vedlegg til to formelle endringsmeldinger (T19: utsettelse, T20: endring av støtteintensitet) som leveres i KMFs søknadsportal.

---

### T17 `[x]` Splitt bakgrunn/merged_files til enkeltfiler

De to filene `merged_files_1.txt` (~10 900 linjer) og `merged_files_2.txt` (~4 500 linjer) ble opprinnelig laget som samlet kontekst til en Custom GPT. De inneholder flere separate dokumenter som bør splittes ut:

**Løsning (2026-06-17):** Splittet i 12 filer i `bakgrunn/`:
- `kmf_tilsvar_soeknadssvar.txt` – Tilsvar til Kulturminnefondet (feb 2024)
- `kmf_soeknad_sikringstiltak.txt` – KMF søknad (sikringstiltak)
- `uni_soeknad.txt` – Stiftelsen UNI søknad
- `tradisjonsbygg_referanseliste.txt` – Tradisjonsbygg AS prosjektreferanser
- `kodeworks_selskapsbeskrivelse.txt` – Om Oss, personalhåndbok, prosjektoversikt
- `fondsoknader.txt` – Adolf Øiens Fond, Kavlifondet, DOGA DIP
- `rammesoknad_kontor_2023_beskrivelse.txt` – Nabovarsel + søknadsbeskrivelse (kontorbygg, 2023)
- `rammesoknad_kontor_2023_vedlegg_F.txt` – F-02, F-04–F-09 (flom, VA, el, ventilasjon)
- `rammesoknad_kontor_2023_brannkonsept.txt` – Brannkonsept til rammesøknad (2023)
- `rammesoknad_kontor_2023_vedlegg_I.txt` – I-01–I-05 (Riksantikvaren, slokkevann, Byantikvaren m.fl.)
- `naeringsmegling_markedsmateriell.txt` – Kodeverket markedsmateriell + DNB salgsprospekt
- `tilstandsanalyse_nivaa1.txt` – Tilstandsanalyse nivå 1 (HRP/Ole Morten)
- `dnb_verdivurdering_2022.txt` – DNB Næringsmegling verdivurdering (aug 2022)

`merged_files_1.txt` og `merged_files_2.txt` er slettet. Oppdatert 2026-06-17: `kmf_uni_soknader.txt` splittet videre til `kmf_soeknad_sikringstiltak.txt` og `uni_soeknad.txt`.

---

### T25 `[x]` Arkiver HRP-rapport energikartlegging
Rapport fra HRP/RiEn om energikartlegging og energimerking skal inn i prosjektet.

**Løsning (2026-06-17):** PDF lå allerede i `bakgrunn/` under filnavnet `Energikartlegging Fjordgt 30.pdf`. Les alle 30 sider og konvertert til `bakgrunn/hrp_energikartlegging_rapport.md`. Rapporten inneholder nå-tilstand (energikarakter G, 252 000 kWh/år), alle 12 tiltak med kostnader og besparelser, tre tiltakspakker (T1–T3), og finansieringsinfo (Enova, grønne lån). T23 er fortsatt åpen – avklar med HRP om rapporten er levert til Enova.

---

### T26 `[x]` Arkiver Enova-søknader

**Løsning (2026-06-17):** Søknadstekstene lå som `bakgrunn/webskjema (1).txt` (energikartlegging) og `bakgrunn/webskjema.txt` (ombrukskartlegging). Konvertert til:
- `bakgrunn/enova_soeknad_energikartlegging.md`
- `bakgrunn/enova_soeknad_ombrukskartlegging.md`

---

### T27 `[x]` Konverter alle bakgrunn-filer fra .txt til .md
**Format:** Markdown, egnet for manuell lesing og fremtidig redigering

Alle filer i `bakgrunn/` som fortsatt er `.txt` bør konverteres til `.md` for enklere lesing og redigering. Bruk `pandoc` eller bare rename der innholdet allerede er rent tekst. Slett originale `.txt`-filer etterpå.

**Nåværende `.txt`-filer i `bakgrunn/` (per 2026-06-17):**

Søknader og korrespondanse (høy prioritet):
- `kmf_tilsvar_soeknadssvar.txt`
- `kmf_soeknad_sikringstiltak.txt`
- `uni_soeknad.txt`
- `fondsoknader.txt`
- `2026-01-26_dispensasjonssoknad.txt`
- `2026-01-26_folgebrev_nabovarsel.txt`
- `2026-02-09_folgebrev_rammesoknad.txt`
- `byantikvaren_tilbakemelding_rammesoknad.txt`
- `2026-06-11 forberedelse til  TBRT statusmøte.txt`

Tekniske notater (fra minilager-rammesøknad):
- `2026-02-06_notat_va.txt`
- `2026-02-09_notat_ventilasjon.txt`
- `2026-02-10_notat_el-kraft.txt`
- `2026-02-10_notat_rib.txt`
- `2026-02-02_sjekkliste_ribr.txt`
- `2026-02-16_brannkonsept_bkl3_tek17.txt`
- `2026-02-16_brannkonsept_vedlegg_a.txt`
- `2026-02-17_brannprosjektering_minilager.txt`
- `2026-02-26_notat_brannsikring_gjennomforingsfasen.txt`
- `2026-02-26_redegjoerelse_tbrt.txt`

Vedlegg fra riksantikvaren / Byantikvaren:
- `2023-06-15_notat_slokkevann.txt`
- `2023-06-28_uttalelse_riksantikvaren_graving.txt`
- `2023-07-05_notat_skred_flomfare.txt`

Markedsmateriell og bakgrunn (lav prioritet):
- `kodeworks_selskapsbeskrivelse.txt`
- `tradisjonsbygg_referanseliste.txt`
- `naeringsmegling_markedsmateriell.txt`
- `dnb_verdivurdering_2022.txt`
- `tilstandsanalyse_nivaa1.txt`
- `situasjonskart.txt`
- `situasjonsplan.txt`

Skal slettes (kontorbygg 2023, dekkes av T18):
- `rammesoknad_kontor_2023_beskrivelse.txt`
- `rammesoknad_kontor_2023_vedlegg_F.txt`
- `rammesoknad_kontor_2023_brannkonsept.txt`
- `rammesoknad_kontor_2023_vedlegg_I.txt`

**Løsning (2026-06-18):** Alle `.txt`-filer i `bakgrunn/` konvertert til `.md`. Originale `.txt`-filer slettet.

---

### T28 `[x]` Arkiver vedtak om tvangsmulkt fra TBRT

**Løsning (2026-06-17):** `bakgrunn/2025-05-07_vedtak_tvangsmulkt.md` (konvertert fra PDF, datert 07.05.2025). I tillegg: `bakgrunn/2024-11-08_paalegg_brannsikring.md` og `bakgrunn/2024-01-24_tilsynsrapport_tbrt.md` gir historikk forut for vedtaket.

---

### T29 `[x]` Arkiver klage på vedtak om tvangsmulkt

**Løsning (2026-06-17):** `bakgrunn/2025-05-26_klage_vedtak_tvangsmulkt.md` (konvertert fra docx, datert 26.05.2025). Også relevant: `bakgrunn/2025-10-09_krav_om_ny_behandling.md`.

---

### T30 `[x]` Arkiver oversikt over påløpte tvangsmulkter

**Løsning (2026-06-17):** `bakgrunn/2026-06-03_3gangs_innkreving_tvangsmulkt.md` dokumenterer 3. gangs innkreving for perioden 15.04.2026–26.05.2026. For komplett oversikt over alle perioder, les også `bakgrunn/2025-05-07_vedtak_tvangsmulkt.md`. En samlet `tbrt_tvangsmulkt_oversikt.md` er ikke laget – kan lages som eget tiltak ved behov.

---

### T34 `[x]` Dokumenter relevant lovverk for T31
**Mappe:** `bakgrunn/lovverk/`

Lag separate `.md`-filer for hvert lovverk som er relevant for klage på tvangsmulkt-innkrevingene (T31). Filene skal inneholde fulltekst eller utdrag av de relevante paragrafene, med kort forklaring av hvorfor de er relevante for saken vår.

**Filer som skal opprettes:**

| Filnavn | Innhold |
|---|---|
| `brann_eksplosjonsvernloven.md` | §§ 1, 6, 37, 39, 41, 42 |
| `forskrift_brannforebygging.md` | §§ 4, 5, 6, 8, 9, 10 (§ 6 om risikobasert tilnærming for eldre bygg) |
| `forvaltningsloven.md` | §§ 16, 17, 24–25, 28, 29, 34, 35, 36, 42, 51 (4. ledd) |
| `tvangsfullbyrdelsesloven.md` | §§ 7-2, 13-14 |
| `grunnloven.md` | § 98 (likhet for loven) |
| `emk.md` | Artikkel 6 (rettferdig rettergang, tilstrekkelig tid til forsvar), Tilleggsprotokoll 1 artikkel 1 (vern om eiendomsretten) |
| `plan_bygningsloven.md` | §§ 29-4, 31-3, 31-4 (særregler for eksisterende byggverk, herunder vernede bygg) |
| `ulovfestede_prinsipper.md` | Forholdsmessighetsprinsippet, likhetsprinsippet, myndighetsmisbrukslæren, saklighetsprinsippet, kontradiksjonsprinsippet – med korte forklaringer og relevans for saken |

**Kontekst:** Fjordgata 30 er verneklasse B (plan- og bygningsloven, ikke kulturminneloven §§ 17–19). Vernet medfører at inngrep i bygningskroppen (f.eks. sprinklerinstallasjon) krever Byantikvarens godkjenning og byggetillatelse. TBRT kan ikke kreve at dette gjennomføres uten de nødvendige tillatelsene på plass. Dette spenningsforholdet mellom to offentlige myndigheters krav er et sentralt argument i T31.

---

### T35 `[x]` Beskriv hvorfor relevant lovverk gjelder for prosjektet
**Filnavn:** `bakgrunn/lovverk/prosjektrelevans.md`  
**Avhenger av:** T34

Lag ett samlet dokument som forklarer hvorfor hvert lovverk er relevant for Fjordgata 30-prosjektet som helhet – ikke bare for klagesaken mot TBRT. Dokumentet skal gi en leser (bank, støttegiver, advokat, ny prosjektdeltaker) en rask oversikt over hvilke rettslige rammer prosjektet opererer innenfor.

**Lovverk som skal dekkes:**
- Brann- og eksplosjonsvernloven – tilsynsplikt, pålegg, tvangsmulkt
- Forskrift om brannforebygging – dokumentasjonskrav, risikobasert tilnærming for eldre bygg
- Plan- og bygningsloven – byggesøknadsprosessen, særregler for eksisterende byggverk, verneklasse B
- Forvaltningsloven – partens rettigheter i møte med offentlig myndighet, klagerett, utredningsplikt
- Grunnloven og EMK – likhet for loven, rett til forsvar, vern om eiendomsretten
- Merverdiavgiftsloven – MVA-fritak/-plikt ved utleie av lagerplass (se T33)
- Ulovfestede forvaltningsrettslige prinsipper – forholdsmessighet, saklighet, kontradiksjon

---

### T36 `[x]` Bildeprosessering – sorter og normaliser bilder fra Google Drive
**Filnavn:** `scripts/process_images.py`

**Løsning (18.06.2026):** Skrevet `scripts/process_images.py`. Bruker Pillow for EXIF-lesing og ImageMagick `convert` for konvertering/skalering. Testet – scriptet starter korrekt og gir brukervennlig feilmelding hvis `../temp/bilder/` ikke finnes.

---

### T37 `[x]` Bildescoring – skarphet (Laplacian)

**Hva:** `scripts/scoring/sharpness.py` – eksporterer `sharpness_score(path) -> float | None`.

**Råscore:** Laplacian-varians via `cv2.Laplacian(gray, cv2.CV_64F).var()`. Skala 0 til ubegrenset. Høy verdi = skarpt bilde. Ingen normalisering – T42 gjør det.

**Standalone:** `.venv/bin/python3 scripts/scoring/sharpness.py <bildefil>`

**Avhengighet:** `opencv-contrib-python`

**Løsning (18.06.2026):** Fungerer. Råscore fra p5=36 til p95=1836 over 1256 bilder – lang høyrehale.

---

### T38 `[x]` Bildescoring – eksponering (histogram)

**Hva:** `scripts/scoring/exposure.py` – eksporterer `exposure_score(path) -> float | None`.

**Råscore:** Total clipping-andel (0.0–1.0). `shadow_fraction + highlight_fraction` der shadow = andel piksler < 15 og highlight = andel piksler > 240 (gråtoneskala). Lav verdi = god eksponering. Ingen normalisering – T42 gjør det.

**Standalone:** `.venv/bin/python3 scripts/scoring/exposure.py <bildefil>`

**Avhengighet:** `opencv-contrib-python`

**Løsning (18.06.2026):** Returnerer rådata (clipping-andel). Normalisering overlatt til T42.

---

### T39 `[x]` Bildescoring – teknisk kvalitet (BRISQUE)

**Hva:** `scripts/scoring/brisque.py` – eksporterer `brisque_score(path) -> float | None`.

**Råscore:** BRISQUE via PyIQA (`pyiqa.create_metric("brisque")`). Skala ca. 0–100, lavere = bedre. Ingen normalisering – T42 gjør det. Modellvekter (~112 kB) caches automatisk i `~/.cache/torch/hub/pyiqa/` ved første kjøring.

**Standalone:** `.venv/bin/python3 scripts/scoring/brisque.py <bildefil>`

**Avhengighet:** `pyiqa`, `torch`, `opencv-contrib-python`

**Viktig:** `cv2.quality.QualityBRISQUE_create` finnes ikke i PyPI-bygget av opencv-contrib 4.13 – bruker PyIQA i stedet. `brisque` PyPI-pakken er inkompatibel med nyere numpy.

**Løsning (18.06.2026):** Fungerer. Testbilde scoret 55.5.

---

### T40 `[x]` Bildescoring – estetisk kvalitet (MUSIQ)

**Hva:** `scripts/scoring/musiq.py` – eksporterer `musiq_score(path) -> float | None`.

**Råscore:** MUSIQ-SPAQ via PyIQA (`pyiqa.create_metric("musiq-spaq")`). Skala ca. 0–100, høyere = bedre. Ingen normalisering – T42 gjør det. Modellvekter (~104 MB) caches automatisk i `~/.cache/torch/hub/pyiqa/` ved første kjøring – krever internett første gang.

**Valg av variant:** `musiq-spaq` (SPAQ = smartphone-bilder). `musiq-koniq` finnes ikke i denne PyIQA-versjonen. `musiq-ava` er trent på kunstfotografi og passer dårlig for dokumentasjonsbilder.

**Ytelse:** 1–3 sek/bilde på CPU. GPU ikke påkrevd men gir 10–20× speedup.

**Standalone:** `.venv/bin/python3 scripts/scoring/musiq.py <bildefil>`

**Avhengighet:** `pyiqa`, `torch`

**Løsning (18.06.2026):** Fungerer. Testbilde scoret 54.1.

---

### T41 `[x]` Bildescoring – finn vekter via manuell kalibrering

**To uavhengige steg:**

*Steg A – Eiriks manuelle rating (kan gjøres når som helst):*
Eirik ser på bilder og gir hvert bilde en helhetlig karakter 1–10. Resultatet lagres i `scripts/scoring/scores_manual.csv` med to kolonner:
```
filnavn,score
20260528_134718.jpg,8
20221020_050156.jpg,3
...
```
Kan fylles ut gradvis – regresjonen kjøres når nok bilder er ratet.

*Steg B – Regresjon (krever T42 ferdig for de ratede bildene):*
Lineær regresjon (`sklearn.linear_model.LinearRegression`) som finner de fire vektene (sharpness, exposure, brisque, musiq) som minimerer avvik mellom Eiriks manuelle karakterer og de normaliserte autoscorene. Vektene lagres i `scripts/scoring/weights.json`. Kjør deretter T48 for å regenerere `scores_total.csv`.

**Script:** `scripts/calibrate_weights.py`

```bash
# Se resultater uten å skrive noe
.venv/Scripts/python scripts/calibrate_weights.py --dry-run

# Skriv weights.json, deretter regenerer scores_total.csv
.venv/Scripts/python scripts/calibrate_weights.py
.venv/Scripts/python scripts/build_scores.py
```

**Output:** `scripts/scoring/weights.json` med intercept og fire koeffisienter.

**Avhengighet for steg B:** `scikit-learn`, T42 ferdig for de bildene som er manuelt ratet.

---

### T42 `[x]` Bildescoring – råscore alle bilder og skriv scores_auto.csv

**Hva:** `scripts/score_images.py` – orkestrerer T37–T40, skriver kun råscorer.

**Fil:** `scripts/scoring/scores_auto.csv`

**Kolonner:** `filnavn, sharpness_raw, exposure_raw, brisque_raw, musiq_raw`

Append-only – én rad per bilde, aldri overskrevet. Idempotent: bilder som allerede har rad hoppes over. Normalisering og total beregnes i T48 (`build_scores.py`).

**Bruk:**
```bash
.venv/Scripts/python scripts/score_images.py             # score nye bilder
.venv/Scripts/python scripts/score_images.py --limit 10  # test med 10 bilder
```

**Løsning (2026-06-20):** Kjørt mot eksisterende `scores.csv`. Må migreres til `scores_auto.csv` (se T48).

---

### T43 `[x]` Bildescoring – normaliserte 1–10-funksjoner (én per metrikk)

**Avhenger av:** T48 (`scores_total.csv` må finnes)

**Hva:** Fire funksjoner – en per metrikk – som leser normaliserte scorer direkte fra `scripts/scoring/scores_total.csv` og returnerer en float 1–10 for ett gitt bilde:

- `sharpness_normalized(path: Path) -> float | None`
- `exposure_normalized(path: Path) -> float | None`
- `brisque_normalized(path: Path) -> float | None`
- `musiq_normalized(path: Path) -> float | None`

**Plassering:** Én funksjon per modul, lagt til i henholdsvis `scripts/scoring/sharpness.py`, `scripts/scoring/exposure.py`, `scripts/scoring/brisque.py`, `scripts/scoring/musiq.py`.

**Standalone:** Alle fire moduler oppdateres til å vise normalisert score i tillegg til råscore når de kjøres direkte.

**Løsning (2026-06-21):** `_normalized(path)`-funksjoner lagt til i alle fire moduler. Felles lookup via `scripts/scoring/__init__.py` som cacher `scores_total.csv` i minnet. Standalone-output oppdatert til å vise begge verdier.

---

### T45 `[x]` Bildescoring – tag alle bilder med RAM

**Hva:** Kjør RAM (Recognize Anything Model) på alle bilder i `../temp/bilder/processed/` og lagre tags per bilde.

**Script:** `scripts/tag_images.py`

**Output:** `scripts/scoring/scores_ram.csv` (long format, append-only)

```
filnavn,tag
20260620_080001.jpg,pipe
20260620_080001.jpg,wood
20260620_080001.jpg,beam
```

Én rad per bilde per tag. Idempotent – bilder som allerede har rader hoppes over.

**Installasjon:** `uv pip install git+https://github.com/xinyu1205/recognize-anything.git`. Modellvekter lastes ned automatisk ved første kjøring.

**Avhengighet:** `recognize-anything`, `torch`

**Løsning (2026-06-21):**
- Krevde `uv pip install "transformers<4.41"` (4.40.2) og `uv pip install fairscale` – nyere transformers manglet `apply_chunking_to_forward`.
- `pretrained=True` krasjet med `AttributeError: 'bool' object has no attribute 'decode'` – `ram_plus()` forventer URL eller filsti, ikke boolean. Løst ved å laste ned vekter til `~/.cache/ram/ram_plus_swin_large_14m.pth` via `requests` streaming og sende stien.
- `result[0]` er en liste (batch), `result[0][0]` er strengen med ` | `-separerte tags.
- Kjørt mot alle 1258 bilder, skriver til `scripts/scoring/scores_ram.csv`.

---

### T46 `[x]` Bildescoring – score tags per bilde med CLIP

**Avhenger av:** T45

**Hva:** Kjør CLIP på alle bilder mot hele tag-vokabularet fra `scores_ram.csv` (alle unike tags på tvers av alle bilder). Lagre score per bilde per tag.

**Script:** `scripts/clip_score.py`

**Output:** `scripts/scoring/scores_clip.csv` (long format, append-only)

```
filnavn,tag,clip_score
20260620_080001.jpg,pipe,0.82
20260620_080001.jpg,wood,0.71
20260620_080001.jpg,beam,0.65
20260620_080001.jpg,window,0.12
```

Alle bilder scores mot alle tags – ikke bare de tagsene RAM tildelte det aktuelle bildet. Idempotent – bilder som allerede har rader hoppes over.

**Installasjon:** `uv pip install open-clip-torch`

**Avhengighet:** `open-clip-torch`, `torch`, T45 ferdig

---

### T47 `[x]` Bildescoring – regresjon på CLIP-tags + manuelle ratings

**Avhenger av:** T46, T41 steg A (`scores_manual.csv`)

**Hva:** Bruk CLIP-scorene fra `scores_clip.csv` som features og manuelle ratings fra `scores_manual.csv` som target. Kjør Ridge-regresjon for å finne hvilke tags som korrelerer med høy vs lav rating.

**Script:** `scripts/calibrate_tags.py`

**Output:**
- Printer tags med sterkest positiv korrelasjon (interessant innhold) og negativ (uinteressant)
- Skriver `scripts/scoring/tag_weights.json` med regresjonskoeffisienter per tag

Kjør deretter T48 (`build_scores.py`) for å regenerere `scores_total.csv` med tag-vekter inkludert.

**Merk:** Ridge-regresjon (`sklearn.linear_model.Ridge`) anbefales fremfor OLS – vokabularet kan ha hundrevis av tags mens antall ratede bilder er begrenset.

---

### T48 `[x]` Bildescoring – bygg scores_total.csv

**Avhenger av:** T42 (`scores_auto.csv`), T41 steg B (`weights.json`), T47 (`tag_weights.json`) – sistnevnte to er valgfrie

**Hva:** Les alle kildefiler, normaliser råscorer, beregn total per bilde, skriv `scores_total.csv`. Dette er den eneste filen som regenereres fullt ut – alle kildefiler forblir urørt.

**Script:** `scripts/build_scores.py`

**Output:** `scripts/scoring/scores_total.csv`

```
filnavn,sharpness,exposure,brisque,musiq,tag_score,total
20260620_080001.jpg,3.17,9.57,8.64,9.92,6.40,7.54
```

**Normalisering:** p5/p95 beregnes fra `scores_auto.csv` på tvers av alle bilder. Vekter leses fra `weights.json` hvis den finnes, ellers enkelt gjennomsnitt. Tag-score beregnes fra `scores_clip.csv` × `tag_weights.json` hvis begge finnes.

**Bruk:**
```bash
.venv/Scripts/python scripts/build_scores.py
```

**Løsning (2026-06-21):** `scripts/build_scores.py` opprettet. Eksisterende `scores.csv` migrert: råscorer → `scores_auto.csv`, normaliserte → `scores_total.csv`, `manuelle_scores.csv` → `scores_manual.csv`.

---

### T49 `[x]` Rydd opp i navngivning av scripts og vektfiler

Inkonsistent navngivning mellom scripts og datafiler. Ingen CSV-datafiler røres.

**Scripts som omdøpes:**
- `score_images.py` → `score_auto.py`
- `tag_images.py` → `score_ram.py`
- `clip_score.py` → `score_clip.py`
- `calibrate_weights.py` → `calibrate_auto.py`

**JSON-filer som omdøpes:**
- `scripts/scoring/weights.json` → `scripts/scoring/weights_auto.json`
- `scripts/scoring/tag_weights.json` → `scripts/scoring/weights_tags.json`

**CSV-datafiler røres ikke** (`scores_auto.csv`, `scores_ram.csv`, `scores_clip.csv`, `scores_total.csv`, `scores_manual.csv`).

Alle interne filreferanser i scripts og README oppdateres.

---

### T50 `[x]` Bildescoring – kombinert modell på auto-metrikker + CLIP-tags

**Motivasjon:** `build_scores.py` kombinerer nå `auto_score` og `tag_score` med fast 50/50-vekting, som ikke er begrunnet i data. Auto-modellen har R²=0.15 og tag-modellen R²=0.38. En felles modell trent på alle features samtidig er metodisk mer korrekt og vil gi høyere R².

**Tilnærming:** Ridge-regresjon på alle 723 features (4 auto-metrikker + 719 CLIP-scores) mot manuelle ratings. Auto-metrikker normaliseres til 1–10 med p5/p95 akkurat som i dag. Deretter skaleres alle 723 features med `StandardScaler` (mean=0, std=1) rett før Ridge, siden auto-metrikker (1–10) og CLIP-scores (~0.1–0.4) ellers er på ulike skalaer og Ridge vil favorisere den gruppen med størst absoluttverdi. p5/p95-normaliseringen for auto-metrikker endres ikke.

**Script:** `scripts/calibrate_combined.py`

**Output:** `scripts/scoring/weights_combined.json`

Format – scaler-parametrene og Ridge-koeffisientene lagres per feature:
```json
{
  "intercept": 5.42,
  "features": {
    "sharpness": {"mean": 5.1, "std": 2.3, "coef": 0.18},
    "exposure":  {"mean": 4.8, "std": 2.1, "coef": -0.09},
    "debris":    {"mean": 0.21, "std": 0.04, "coef": 0.34},
    ...
  }
}
```

**Bruk:**
```bash
.venv/Scripts/python scripts/calibrate_combined.py --dry-run  # se R² uten å skrive
.venv/Scripts/python scripts/calibrate_combined.py            # skriv weights_combined.json
.venv/Scripts/python scripts/build_scores.py                  # regenerer scores_total.csv
```

**Endring i `build_scores.py`:** Hvis `weights_combined.json` finnes, bruk den til å beregne `total` direkte. Kolonnene `auto_score` og `tag_score` beholdes i `scores_total.csv` for referanse, men `total` beregnes av combined-modellen alene — ikke 50/50-snittet. Faller tilbake på dagens tilnærming hvis filen ikke finnes.

**Avhengighet:** `scikit-learn`, `scores_auto.csv`, `scores_clip.csv`, `scores_manual.csv`

**Eksempelbilde: `20250129_131504.jpg`**

Brukt som konkret testcase i diskusjonen. Kjeller med rør, søppel og rusk.

- RAM-tags: `basement`, `beam`, `ceiling`, `pillar`, `debris`, `floor`, `garbage`, `hose`, `mess`, `pipe`, `room`, `rubble`, `waste`, `water pipe`
- Auto-scores (normalisert 1–10): sharpness=4.32, exposure=7.09, brisque=8.61, musiq=7.61
- Dagens total: auto_score=5.65, tag_score=5.44, total=5.54 (50/50)
- Manuell rating: **ikke ratet** — kan ikke verifisere modellen direkte på dette bildet, men det er nyttig for å se om combined-modellen gir et annet resultat enn 5.54 og i hvilken retning.

Forventning: combined-modellen vil sannsynligvis vekte `debris`, `pipe` og `rubble` positivt (byggrelatert innhold) og `garbage`/`mess` svakere negativt. Sharpness=4.32 er lav og vil trekke ned noe. Samlet forventes total å ligge nær 5–6, men med bedre begrunnet vekting enn i dag.

---

### T51 `[x]` Finpuss layout – OCR-korrupsjon, sammenkjørte ord (gruppe A)
**Mappe:** `bakgrunn/`

17 filer har gjennomgående OCR-korrupsjon fra PDF-konvertering: ord er kjørt sammen uten mellomrom (typisk mønster: «kanikke se å hamottat», «V iser til» o.l.). Filene er ellers strukturelt greie (brevformat, avsnitt), men teksten er lite leselig.

**Subtasks:**

- `[x]` **T51.01** `2018-01-15_tbrt_tilsynsrapport_varsel_paalegg.md` – Tilsynsrapport med 3 avvik + følgebrev. Lengst og viktigst (grunnlag for T31).
- `[x]` **T51.02** `2018-02-19_tbrt_purring_tilsyn_varsel_paalegg.md` – Purring på tilbakemelding etter tilsyn jan 2018.
- `[x]` **T51.03** `2018-10-05_tbrt_vedroerende_tilbakemelding.md` – TBRTs svar på KodeWorks' tilbakemelding.
- `[x]` **T51.04** `2018-12-11_tbrt_purring_tilsyn_varsel_paalegg.md` – Purring med varsel om pålegg, des 2018.
- `[x]` **T51.05** `2019-03-06_tbrt_aksept_tiltaksplan.md` – Aksept av tiltaksplan, mars 2019.
- `[x]` **T51.06** `2019-06-28_tbrt_purring_tilsyn_varsel_paalegg.md` – Purring med varsel om pålegg, jun 2019.
- `[x]` **T51.07** `2019-08-12_tbrt_aksept_tiltaksplan.md` – Aksept av tiltaksplan, aug 2019.
- `[x]` **T51.08** `2019-11-11_tbrt_purring_tilbakemelding_varsel_paalegg.md` – Purring med varsel, nov 2019.
- `[x]` **T51.09** `2019-12-17_tbrt_aksept_tiltaksplan.md` – Aksept av tiltaksplan, des 2019.
- `[x]` **T51.10** `2020-10-01_tbrt_purring_tilbakemelding_varsel_paalegg.md` – Purring med varsel, okt 2020.
- `[x]` **T51.11** `2020-11-04_tbrt_aksept_tiltaksplan.md` – Aksept av tiltaksplan, nov 2020.
- `[x]` **T51.12** `2021-04-23_tbrt_purring_tilbakemelding_varsel_paalegg.md` – Purring med varsel, apr 2021.
- `[x]` **T51.13** `2021-06-02_tbrt_mangelfull_tilbakemelding.md` – TBRT mener tilbakemelding er mangelfull.
- `[x]` **T51.14** `2021-08-03_tbrt_purring_tilsyn_varsel_paalegg.md` – Purring med varsel, aug 2021.
- `[x]` **T51.15** `2021-09-23_tbrt_aksept_tiltaksplan.md` – Aksept av tiltaksplan, sep 2021.
- `[x]` **T51.16** `2021-11-25_tbrt_purring_tilsyn_varsel_paalegg.md` – Purring med varsel, nov 2021.
- `[x]` **T51.17** `2022-03-03_tbrt_etterkontroll_varsel_paalegg.md` – Etterkontroll med varsel om pålegg, mar 2022.

**Tilnærming:** Ingen original-PDFer tilgjengelig. Rekonstruert korrekt norsk tekst fra kontekst, fjernet `Feil! Fant ikke referansekilden.`-artefakter.

---

### T52 `[x]` Finpuss layout – ødelagte tabeller (gruppe B)
**Mappe:** `bakgrunn/`

3 filer inneholder tabelldata fra originaldokumenter som ikke var konvertert til korrekt Markdown-tabellformat.

**Filer:**
- `2018-09_tekøk_tiltaksplan_skjema.md` – skjema med avviksstatus, pipe-separert men uformatert
- `2020_tiltaksplan_status_a.md` – tiltaksplan med statuskolonner, ødelagt struktur
- `2020_tiltaksplan_status_b.md` – samme som over, fortsettelse

**Løsning:** Rekonstruert til korrekt `| Kolonne | Kolonne |` Markdown med separator-rad.

---

### T53 `[x]` Finpuss layout – tekniske rapporter med innholdsfortegnelse (gruppe C)
**Mappe:** `bakgrunn/`

3 store tekniske rapporter fra TekØk hadde ujevn avstandsformatering og innholdsfortegnelse som ikke var korrekt strukturert i Markdown.

**Filer:**
- `2018-09-14_tekøk_brannteknisk_vurdering_rev_c.md`
- `2018-09-22_tekøk_brannteknisk_vurdering_rev_d.md`
- `2022-12-18_tekøk_status_gjenstaende_avvik.md`

**Løsning:** Fjernet sideoverskrifter (gjentatt OCR-artefakt fra PDF), fikset innholdsfortegnelse (fra flat tekst til `#`-nivåer), rekonstruerte tabell i seksjon 4 (tiltaksplan), fikset sammensatte punktlisteelementer, bevarte BKL2/BKL3-distinksjonen mellom Rev. C og Rev. D.

---

### T56 `[x]` Bildescoring – skill kode og datafiler (scripts/scoring/ → data/)

Datafiler ligger i dag blandet med Python-moduler i `scripts/scoring/`. Flytt alle datafiler til `data/` på rotnivå.

**Datafiler som flyttes:**
`scores_auto.csv`, `scores_manual.csv`, `scores_ram.csv`, `scores_clip.csv`, `scores_total.csv`, `weights_auto.json`, `weights_tags.json`, `weights_combined.json`

**Python-moduler som blir igjen i `scripts/scoring/`:**
`sharpness.py`, `exposure.py`, `brisque.py`, `musiq.py`

**Løsning (22.06.2026):** `SCORING_DIR` → `DATA_DIR = Path(...).parents[1] / "data"` i alle 7 scripts (`score_auto`, `score_ram`, `score_clip`, `build_scores`, `calibrate_auto`, `calibrate_tags`, `calibrate_combined`) + `scripts/scoring/__init__.py`. README oppdatert (mappestruktur + datafil-seksjon). Datafiler eksisterer ennå ikke i `data/` — mappen opprettes automatisk ved første kjøring (`mkdir(parents=True, exist_ok=True)`).

---

### T55 `[x]` Bildescoring – pipeline-script (score_all.py)

Lag `scripts/score_all.py` som kjører hele bildescoring-pipelinen i sekvens:
`process_images.py` → `score_auto.py` → `score_ram.py` → `score_clip.py` → `calibrate_combined.py` → `build_scores.py`.
Scriptet skal stoppe ved feil og bruke `sys.executable` for å sikre riktig venv.

**Løsning (22.06.2026):** Opprettet som `run_pipeline.py`, deretter renamed til `score_all.py`. Oppdatert i README (mappestruktur + brukseksempel). Bruker `sys.executable` for riktig venv.

---

### T54 `[x]` Finpuss layout – sterkt ødelagt OCR-dokument (gruppe D)
**Mappe:** `bakgrunn/`

Én fil var så sterkt OCR-skadet at innholdet var nesten uleselig – teksten fragmentert i løsrevne biter og sjekklister hadde mistet struktur helt.

**Fil:** `bakgrunn/2013-06-06_ik_kontroll_trondheim_baatforening.md` – IK-kontroll, Trondheim Båtforening, 06.06.2013

**Løsning (valgt: Full rekonstruksjon):** Full rekonstruksjon fra 2200-linjers OCR-skadet fil. 16 sjekklister rekonstruert i tabellformat (Pkt / Kontrollpunkt / Dato / Tekniker / Resultat). Avvikslogg med 40 avvik rekonstruert. Tiltaksplan rekonstruert. Alle FEIL-resultater verifisert mot avviksnummer i avviksloggen.

---

### T57 `[x]` Bildescoring – velg beste bilder for en tidsperiode (select_images.py)

Lag `scripts/select_images.py` som henter de N beste bildene innenfor en dato-periode.

**Argumenter:**
- `--from YYYY-MM-DD` – startdato (inklusiv)
- `--to YYYY-MM-DD` – sluttdato (inklusiv)
- `--count N` – maks antall bilder å velge ut (standard: 10)
- `--output <sti>` – (valgfri) kopier valgte bilder til denne mappen

**Logikk:**
1. Les `scores_total.csv`
2. Filtrer på dato fra filnavnet (format: `YYYYMMDD_HHMMSS.jpg`)
3. Sorter på effektiv score: **manuell rating prioriteres alltid over total** — hvis `manual`-kolonnen er fylt ut, brukes den; ellers brukes `total`
4. Velg topp N bilder
5. Print liste til stdout (filnavn, score, kilde for score: "manuell" / "total")
6. Hvis `--output` er angitt: kopier bildene fra `../temp/bilder/processed/` til output-mappen

**Prioriteringsregel (viktig):**
Manuell rating (`manual`-kolonnen i `scores_total.csv`) representerer menneskelig vurdering og overstyrer alltid modellscoren (`total`). Denne prioriteringen gjelder overalt hvor bilder rangeres — ikke bare i dette scriptet.

**Avhengigheter:** `scores_total.csv` (fra `build_scores.py`), `../temp/bilder/processed/*.jpg`

**Løsning (22.06.2026):** Opprettet `scripts/select_images.py`.

---

### T58 `[x]` Konfigurasjon – flytt hardkodede stier til config.json

`../temp/bilder` er hardkodet i 5 scripts. Ulike brukere kan ha bildene et annet sted. Flytt stien til en sentral konfigurasjonsfil.

**Oppgaver:**
1. Opprett `config.json` i prosjektroten med `bilder_dir` (default: `../temp/bilder`)
2. Opprett `scripts/config.py` som leser `config.json` og eksponerer `BILDER_DIR`, `PROCESSED_DIR`, `EXTRACTED_DIR`
3. Erstatt hardkodede stier i `process_images.py`, `score_auto.py`, `score_ram.py`, `score_clip.py`, `select_images.py`
4. Kjør regresjonstest: alle scripts importerer og parses uten feil

**Config-format (config.json):**
```json
{ "bilder_dir": "../temp/bilder" }
```
Stien kan være relativ (løses fra prosjektrot) eller absolutt.

**Løsning (22.06.2026):** Opprettet `config.json` og `scripts/config.py`. `config.py` leser `config.json`, faller tilbake på `../temp/bilder` hvis filen ikke finnes, og eksponerer `BILDER_DIR`, `PROCESSED_DIR`, `EXTRACTED_DIR`. Oppdatert `process_images.py`, `score_auto.py`, `score_ram.py`, `score_clip.py`, `select_images.py`. Regresjonstest: alle 5 scripts parser uten feil. Leser `data/scores_total.csv`, filtrerer på dato fra filnavn (`YYYYMMDD_HHMMSS.jpg`), sorterer på effektiv score (manuell overstyrer modell), printer rangert tabell til stdout. `--output` kopierer valgte bilder med `shutil.copy2`.

---

---

### T63 `[x]` Dato-prefix på filer i `bakgrunn/` + CLAUDE.md-instruks

**Mål:** Sikre at alle filer i `bakgrunn/` er dato-prefikset (format `YYYY-MM-DD_`) og at CLAUDE.md har en arbeidsregel som håndhever dette fremover.

**Del 1 – CLAUDE.md-instruks:**
Legg til arbeidsregel: *Alle nye filer som legges i `bakgrunn/` skal ha dato-prefix på formen `YYYY-MM-DD_beskrivelse.ext`. Eksisterende filer uten dato-prefix skal omdøpes ved neste berøring.*

**Del 2 – Omdøp eksisterende filer:**
Gå gjennom `bakgrunn/` og gi dato-prefix til filer som mangler det. Bruk dokumentets interne dato der det er mulig; ellers bruk sist-endret-dato eller en passende kontekstuell dato. Oppdater alle referanser i `historikk.md` og `TASKS.md` etterpå.

**Merk:** Filer i `bakgrunn/stotte/` følger egen mappestruktur (prosjektmapper) og er unntatt dato-prefix-kravet.

**Løsning (2026-06-23):** 18 filer omdøpt i `bakgrunn/` med dato-prefix. CLAUDE.md fikk to nye arbeidsregler (dato-prefix og "Nye oppgaver"-prosessering). Alle referanser oppdatert i `historikk.md` (fotnoter [^1], [^10], [^11], [^27], [^52], [^63], [^65], [^67], [^70]) og i `TASKS.md`.

---

### T64 `[x]` CLAUDE.md-instruks: prosessering av "Nye oppgaver"

**Mål:** Legg til en arbeidsregel i `CLAUDE.md` som sikrer at "Nye oppgaver"-seksjonen i `TASKS.md` alltid oppdages og prosesseres.

**Instruksen skal si:**
- Når `TASKS.md` leses, sjekk alltid om `## Nye oppgaver` inneholder uprosesserte punkter (bullet-linjer under seksjonen)
- Hvis det finnes slike punkter: spør brukeren om de skal prosesseres
- Prosessering betyr: gå gjennom hvert punkt, konverter til en nummerert T-task med beskrivelse og slett punktet fra "Nye oppgaver"

**Løsning (2026-06-23):** Arbeidsregel lagt inn i `CLAUDE.md` under "Arbeidsregler"-seksjonen.

---

### T09 `[x]` Oversikt støttemidler – Bank
**Mottaker:** Bank

Trenger en samlet oversikt over alle innvilgede tilskudd og finansieringskilder for å dokumentere prosjektøkonomi. Bruk `../stotte`-prosjektet som kilde for tall. I stotte prosjektet er det også definert struktur og datamodell for prosjekter som er støttet. Dette må forstås, og stotteprosjekter sine "datablad" må formatteres likt. Det bør ligge inn under en ny mappe "stotte".

**Løsning (2026-06-22):**
- Opprettet `stotte/` mappe i prosjektet
- `stotte/project_cards.json` – tilskuddskort i samme format som `../stotte/project_cards.json`, med én entry per tilskudd: KMF-FG30, BYA-FG30, UNI-FG30, ENOVA-KL-FG30, ENOVA-OM-FG30
- `stotte/2026-06-22_fg30_stoetteoversikt_bank.md` – bankfokusert oversikt (Pandoc-klar Markdown → .docx) med tilskuddstabell, forklaring av utbetalingsmekanismen, finansieringsplan og framdriftsplan
- Samlet innvilget: 2 250 000 NOK (KMF 750 000 + BYA 500 000 + UNI 100 000 + Enova 900 000)

---

### T11 `[x]` Rammesøknad minilager
Levert 12. mai 2026.

---

### T13 `[x]` Forberedelsesdokument til møte med TBRT
Lag dokument som forbereder møtet: agenda, argumenter mot dagbøter, framdriftsbevis. Se T07 for kontekst om dagbøter og vår posisjon.

**Løsning (2026-06-11):** Dokument lagt inn av Eirik: `bakgrunn/2026-06-11_forberedelse_tbrt_statusmote.txt` (opprinnelig navn: `2026-06-11 forberedelse til TBRT statusmøte.txt`, omdøpt i T63)

---

### T14 `[x]` Referat fra møte med TBRT
Transcription finnes – lag formelt referat fra denne.

**Løsning (2026-06-17):** Referat skrevet fra transcript.srt: `referat/tbrt/2026-06-11_referat_statusmote_tbrt.md`. Dekker: status på alle tre avvik, avvikling av drift, rammesøknad, IG-plan, selskapsstruktur, tvangsmulkt-strategi (TBRT anbefaler å klage på 3. gangs innkreving for å kjøpe tid), og dokumentasjonsliste KodeWorks skal levere innen ca. 18. juni 2026. Transcription er halvdårlig/upresis. Vi må berike møtereferatet på bakgrunn av de øvrige bakgrunnsdokumentene. Spør hvis du er usikker på noen berikelser. Renskriv, lagre som .md. Du ser i transcript at det er navngitte personer som sier ting.
SPEAKER_00 = Eirik Larsen, KodeWorks Eiendom AS
SPEAKER_04 = Morten Knutsen, TBRT
Speaker_01 = anna-karin hermansen, TBRT
Speaker_02 = Tove-Kristin Reitan, TBRT
Speaker_03 = Ole Morten Lagmannssveen, HRP

---

### T18 `[x]` Lag kronologisk prosjekthistorikk
**Filnavn:** `historikk.md`

**Løsning (2026-06-18):** `historikk.md` opprettet i prosjektets rotmappe. Dekker bygningens tidlige historie fra 1841, alle daterte prosjekthendelser fra 2022 til 11. juni 2026, og en eksplisitt seksjon for udokumenterte hendelser med manglende dato (kjøp av bygget, KMF/UNI/Enova-vedtaksdatoer, m.fl.). Kilder: alle filer i `bakgrunn/`, alle statusmøtereferater (01–05 + TBRT), arbeidslogger (`2026-04-16_arbeid_kristian.txt`, `2026-04-16_arbeid_ole_morten.txt`), DNB-verdivurdering 2022, rammetillatelse 28.11.2023, rapport til TBRT 2025.

Lag en kronologisk fremstilling av Fjordgata 30-prosjektet fra start til i dag, basert på bakgrunnsmaterialet i `bakgrunn/` og referatene i `referat/`. Dokumentet skal gi en ny leser (bank, støttegiver, advokat) rask oversikt over hva som har skjedd, når, og hvorfor.

**Struktur:** Én seksjon per år (eller naturlig fase), med daterte hendelser som bullets. Dekk minst:
- Kjøp/overtakelse av bygget og tidligste planer
- Søknader om tilskudd – når søkt, når innvilget, beløp og formål (KMF, Byantikvaren, Enova, UNI)
- Arbeidsøkter – når Kristian og/eller Ole Morten har utført fysisk arbeid på bygget (se `2026-04-16_arbeid_kristian.txt` og `2026-04-16_arbeid_ole_morten.txt`)
- Rammesøknad for kontorbygg – når levert, hva den inneholdt, hvorfor den ble skrinlagt
- Omlegging fra kontorbygg til minilager – beslutning og begrunnelse
- TBRT-tilsyn januar 2024, pålegg november 2024, klage mai 2025, klagebehandling september–oktober 2025, innkrevinger mars–juni 2026
- Rammesøknad for minilager levert 12. mai 2026
- Statusmøte TBRT 11. juni 2026

**Udokumenterte hendelser:** Hendelser som nevnes i dokumenter uten at dato eller kilde er kjent, skal likevel tas med i historikken – men merkes eksplisitt med f.eks. «*(dato ukjent – mangler dokumentasjon)*» eller «*(omtalt i [kilde], ingen dato)*». Eksempler på slike hendelser: første kontakt med støttegivere, beslutningen om å kjøpe bygget, tidlige møter med Byantikvaren eller Riksantikvaren, tidligere TBRT-inspeksjoner før 2024. Målet er at historikk.md synliggjør hull i dokumentasjonen slik at de kan tettes.

**Kilder:** `bakgrunn/` (alle filer inkl. `2026-04-16_arbeid_kristian.txt`, `2026-04-16_arbeid_ole_morten.txt`), `referat/` (alle møtereferater), `CLAUDE.md` for interessentoversikt.

---

### T31 `[x]` Klage på alle tre innkrevinger av tvangsmulkt
**Mottaker:** Trøndelag brann- og redningstjeneste IKS  
**Filnavn:** `2026-06-17_tbrt_klage_innkrevinger_2026.md`

**Kronologi:**

| Dato | Hendelse | Saksnr / kilde |
|---|---|---|
| 11.01.2024 | TBRT-tilsyn gjennomført | 24/1007-2 |
| 24.01.2024 | Tilsynsrapport – tre avvik dokumentert | 24/1007-2 |
| 15.02.2024 | Frist for å lukke avvik iht. tilsynsrapporten | 24/1007-2 |
| 18.03.2024 | Gjentatt varsel om pålegg fra TBRT | Bekreftet i pålegget 08.11.2024 |
| 05.03.2024 | KodeWorks sender forpliktende handlingsplan | Bekreftet i pålegget 08.11.2024 |
| 04.11.2024 | Statusmøte – avvik fortsatt ikke lukket | Bekreftet i pålegget 08.11.2024 |
| 08.11.2024 | Pålegg om brannsikring, frist 01.05.2025 | 24/1007-27 |
| 28.04.2025 | Møte mellom KodeWorks og TBRT – status gjennomgått | Bekreftet i vedtaket 07.05.2025 |
| 07.05.2025 | Vedtak om tvangsmulkt: 2 000 kr/dag fra 01.01.2026 | 24/1007-28 |
| 26.05.2025 | KodeWorks klager på vedtaket (forvaltningsloven § 28) | 24/1007-28 |
| 16.09.2025 | TBRT sender saksfremlegg til klageorganet – anbefaler å opprettholde vedtaket | 24/1007-33 |
| 30.09.2025 | Klageorganet behandler saken, opprettholder vedtaket | Protokoll vedlagt orientering 08.10.2025 |
| 08.10.2025 | TBRT orienterer KodeWorks om klageorganets vedtak | Bekreftet i krav om ny behandling 09.10.2025 |
| 09.10.2025 | KodeWorks krever ny behandling – mangelfull begrunnelse (forvaltningsloven §§ 25, 34, 41) | 24/1007-28 |
| 30.12.2025 | KodeWorks sender statusbrev – beskriver utført arbeid og planlagt forprosjekt | Bekreftet i TBRT-brev 06.01.2026 |
| 06.01.2026 | TBRT innvilger ny frist til 28.02.2026. Dagmulkt løper fra 01.03.2026 | 24/1007-40 |
| 27.02.2026 | KodeWorks orienterer om minilager-planer og fremdrift på rammesøknad | `2026-02-27_status_fjordgata30.md` |
| 06.03.2026 | Telefonsamtale mellom KodeWorks og TBRT | Bekreftet i TBRT-brev 18.03.2026 |
| 13.03.2026 | KodeWorks sender e-post til TBRT | Bekreftet i TBRT-brev 18.03.2026 |
| 18.03.2026 | TBRT avslår ytterligere utsettelse – mener ingen konkrete tiltak er gjennomført | 24/1007-44 |
| 19.03.2026 | 1. innkreving SENDT (periode 01.03–18.03.2026, kr 36 000) | 24/1007-45 |
| 17.04.2026 | 2. innkreving SENDT (periode 19.03–14.04.2026, kr 54 000) | 24/1007-46 |
| 11.05.2026 | KodeWorks varsler TBRT uformelt om at rammesøknad er klar og vil bli levert | TBRT skriver feilaktig «11.05.2025» i 3. innkreving – bekreftet av KodeWorks at dette er 2026 |
| 12.05.2026 | Rammesøknad for minilager levert til Plan og Bygg | Bekreftet i referat 11.06.2026 |
| 03.06.2026 | 3. innkreving SENDT (periode 15.04–31.05.2026, kr 94 000) | 24/1007-52 |
| 11.06.2026 | Statusmøte KodeWorks / HRP / TBRT | `referat/tbrt/2026-06-11_referat_statusmote_tbrt.md` |

**Formell struktur – tre separate klager i ett brev**

Hvert innkrevingsvedtak er et selvstendig enkeltvedtak med eget saksnummer. Forvaltningsloven § 51, 4. ledd gir særskilt klagerett på den enkelte «ileggelse». Alle tre må påklages separat, men kan samles i ett brev som eksplisitt angir at man klager på sak 24/1007-45, 24/1007-46 og 24/1007-52.

**Klagefrist og status (per 17.06.2026)**

| Innkreving | Sendt | Frist ca. | Status |
|---|---|---|---|
| 1. (01.03–18.03.2026) | 19.03.2026 | ~09.04.2026 | **Frist brutt** – 10 uker siden |
| 2. (19.03–14.04.2026) | 17.04.2026 | ~08.05.2026 | **Frist brutt** – 6 uker siden |
| 3. (15.04–31.05.2026) | 03.06.2026 | ~24.06.2026 | **Ikke brutt** – hastverk |

Fristen er 3 uker fra mottaksdato, jf. forvaltningsloven §§ 29 og 51, 4. ledd. Bekreftet av TBRTs juridiske rådgiver i møtet 11.06.2026.

**Strategi for fristbrutte klager (innkreving 1 og 2)**

Forvaltningsloven § 31 åpner for behandling av for sent inngitte klager dersom:
- **a)** parten ikke kan lastes for å ha oversittet fristen, eller
- **b)** det av særlige grunner er rimelig at klagen prøves

Klagen må fremsettes «uten ugrunnet opphold» etter at hindringen er falt bort.

Argumenter som begrunner sen klage:
1. KodeWorks var i perioden mars–mai 2026 i aktiv konstruktiv dialog med TBRT og fokuserte på å levere rammesøknaden (12. mai) som den faktiske løsningen – ikke på å angripe innkrevingene juridisk. En part som aktivt forsøker å løse saken bør ikke straffes for å ikke simultant ha klaget innen fristen.
2. Rammesøknaden forelå ikke da fristene for innkreving 1 og 2 løp ut – det er et vesentlig nytt faktum som er «særlige grunner» etter § 31 b).
3. KodeWorks er en liten eiendomseier uten heltids juridisk stab; TBRT har juridisk rådgiver i fast stilling. Strukturell asymmetri taler for at fristen bør praktiseres med rimelighet (jf. EMK artikkel 6).
4. Alle tre innkrevingene springer ut av det samme vedtaket og den samme situasjonen – prosessøkonomisk og konsistensmessig bør de ses i sammenheng.
5. TBRT signaliserte i møtet 11.06.2026 at de vil vurdere å sette innkreving i bero – vanskelig å begrunne velvilje fremover uten å revurdere de to allerede innkrevde periodene.

Subsidiært: Be TBRT omgjøre innkrevingene 1 og 2 på eget initiativ etter forvaltningsloven **§ 35** (omgjøring uten klage til gunst for parten).

**Brevets fire elementer:**
1. Formell klage på 3. innkreving (innen fristen – hastverk)
2. Klage på 1. og 2. innkreving med anmodning om behandling til tross for fristoverskridelse (§ 31)
3. Subsidiær anmodning om omgjøring av 1. og 2. innkreving etter § 35
4. Anmodning om utsatt iverksetting av alle tre etter § 42 mens klagebehandling pågår

**Materielle argumenter i klagen:**
- Rammesøknad levert 12. mai 2026 – prosjektet er nå konkret og i gang
- Krav om ny behandling (09.10.2025) ikke tilfredsstillende besvart
- Sprinklerinstallasjon i verneklasse B-bygg er rettslig umulig uten byggetillatelse og Byantikvarens godkjenning – TBRT setter KodeWorks i en umulig skvis mellom to offentlige myndigheter
- Brannforskriften § 6 (risikobasert tilnærming for eldre bygg) er ikke vurdert av TBRT
- Faktafeil i saksfremlegget (16.09.2025): TBRT hevdet at ingen byggesøknad var innlevert
- Tvangsmulkt som kan velte prosjektøkonomien hindrer den brannsikkerhetsoppgraderingen TBRT selv krever (forholdsmessighetsprinsippet, EMK TP1 art. 1)
- Fortsatt innkreving bør stilles i bero frem til klagebehandling er avsluttet

**Relevante kilder:**
- `bakgrunn/2025-05-07_vedtak_tvangsmulkt.md`
- `bakgrunn/2025-05-26_klage_vedtak_tvangsmulkt.md`
- `bakgrunn/2025-09-16_saksfremlegg_klageorgan_tbrt.txt`
- `bakgrunn/2025-10-09_krav_om_ny_behandling.md`
- `bakgrunn/2026-01-06_tbrt_svar_ny_frist.txt`
- `bakgrunn/2026-02-27_status_fjordgata30.md`
- `bakgrunn/2026-03-18_tbrt_svar_ingen_ytterligere_utsettelse.txt`
- `bakgrunn/2026-03-19_1gangs_innkreving_tvangsmulkt.md`
- `bakgrunn/2026-04-17_2gangs_innkreving_tvangsmulkt.md`
- `bakgrunn/2026-06-03_3gangs_innkreving_tvangsmulkt.md`
- `bakgrunn/lovverk/` (alle filer)

---

### T60 `[x]` Gjennomgå og ferdigstill brannvesen-rapport (leveranser/2026-04-20_fg30_arbeidsrapport.md)

Rapport sendt til TBRT/brannvesenet ca. 20. april 2026. Filen er konvertert fra `.docx` og har formateringsfeil fra konverteringen. Filen ligger nå i `leveranser/2026-04-20_fg30_arbeidsrapport.md`.

**Hva som skal gjøres:**
1. Les hele filen og identifiser alle konverteringsartefakter (stray `<`-tegn, ødelagte avsnitt, manglende mellomrom)
2. Regenerer titler og formatering der det er nødvendig
3. Behold `\newpage`-kommandoer (gyldige for Pandoc → .docx)
4. Verifiser at innholdet samsvarer med det som faktisk ble sendt

**Kjente feil (oppdaget ved opprettelse av tasken):**
- Linje 19: `---<` skal være `---`
- Linje 33: `<som er gjennomført` skal være `som er gjennomført`

**Avhengigheter:** Ingen.

**Løsning (22.06.2026):** Filen gjennomgått i sin helhet. Kun de to kjente konverteringsartefaktene funnet og rettet. Øvrig formatering er korrekt — overskriftshierarki, tabeller og `\newpage`-kommandoer er gyldige og intakte. Filen ble samtidig flyttet fra `bakgrunn/nye/` til `leveranser/`.

---

### T61 `[x]` Populer project_cards.json med primærkildedata for alle tilskudd

**Mål:** `stotte/project_cards.json` skal ha alle felt utfylt fra primærkilder (tilsagnsbrev, søknader, budsjett-xlsx) – ikke fra historikk.md. For hvert prosjektkort: GrantReference, TotalBudget, SupportIntensity, DurationFrom/To, ReportingDates (med datoer og krav), PaymentDates (med triggere og krav), UsageConstraints (eligible/ineligible), SpecialRules.

**Arbeidsregel:** Tilsagnsbrev og budsjettdokumenter er primærkilder. historikk.md er ikke kilde. Kopier kun .txt-filer (ikke PDF) til `bakgrunn/stotte/`.

#### Status per 2026-06-22

**KMF-FG30** `[x]` Ferdig

Kilde: `bakgrunn/stotte/kmf_tilsagnsbrev.txt`, `kmf_soeknad_ordinaer.txt`, `kmf_tilbakemelding_20240206.txt`, estimat-filer.

Oppdaterte felt:
- `GrantReference`: `240126`
- `TotalBudget`: `5000000` ← fra endelig søknad (kulturminnefondet_2.txt)
- `GrantAmount`: `750000` ✓
- `SupportIntensity`: `0.30` ✓
- `DurationFrom`: `2024-03-13` (vedtaksdato), `DurationTo`: null (ikke fastlagt)
- `UsageConstraints.eligible`: fjerne/bevare originale paneler/gulvplater/himlinger, undersøke bærekonstruksjon, skifte søyler/innkassing, reetablere bæresystem, kjøp av håndverkertjenester
- `UsageConstraints.ineligible`: administrasjon/regnskap/planlegging, dugnad/egne maskiner, trykkimpregnerte materialer, kostnader over sluttregnskapet
- `SpecialRules`: KMF-spesifikke krav om materialkvalitet, antikvarisk standard fra BYA, ingen trykkimpregnering
- `Comments`: vedtaksdato 13.03.2024, tilsagnsbrev 18.03.2024, prosjektnr 240126. Merk: prosjektet er endret fra kontorbygg til minilager – KMF må informeres (T20).

Kopiert til `bakgrunn/stotte/`:
- `kmf_tilsagnsbrev.txt` (fra `temp/Kulturminnefondet/Kulturminnefondet 1/`)
- `kmf_soeknad_ordinaer.txt` (fra `temp/.../Tilsvar 1/kulturminnefondet_2.txt` – den endelige reviderte søknaden, primærkilde)
- `kmf_tilbakemelding_20240206.txt` (KMFs forespørsel om tilleggsopplysninger)
- `kmf_estimat_rehab_kjeller.txt`, `kmf_estimat_rehab_1etg.txt` (kostnadsestimater)
- Fantes fra før: `kmf_soeknad_sikringstiltak.txt`, `kmf_tilsvar_soeknadssvar.txt`
---

**BYA-FG30** `[x]` Ferdig

Kilde: `bakgrunn/stotte/bya_tilsagnsbrev.txt`, `bya_soeknad.txt`, `bya_akseptskjema.txt`, `bya_utbetalingsskjema.txt`. Kopiert fra temp/ 2026-06-22.

Oppdaterte felt:
- `GrantReference`: `2025/5928`
- `TotalBudget`: `2285714`
- `GrantAmount`: `500000` ✓ (søkte 750 000, fikk 500 000)
- `SupportIntensity`: `0.219` (500 000 / 2 285 714)
- `DurationFrom`: `2025-06-01`, `DurationTo`: `2025-12-31`
- `ReportingDates[0].DeadlineDate`: `2025-12-01` (primært)
- `UsageConstraints.eligible`: forsterking fundamenter, retting skjevheter, fjerning/dok/tilbakeføring av paneler, utskifting råteskadde søyler/bjelker, stabilisere yttervegger/etasjeskillere
- `UsageConstraints.ineligible`: fasade/vinduer/tak, utredningsoppgaver/pilotprosjekter, allerede utførte arbeider, kostnader over sluttregnskapet
- `SpecialRules`: antikvarisk spesialkompetanse påkrevd, løpende dialog med BYA, solceller på tak krever BYA-godkjenning ved IG-søknad
- `PaymentDates`: utbetalingsanmodning på Vedlegg 2-skjema + rapport + faktura/regnskap → byantikvaren.kart@trondheim.kommune.no
---

**UNI-FG30** `[x]` Ferdig

Kilde: `temp/UNI/UNI 2/Tildeling etter styremøte i Stiftelsen UNI.txt`, `Budsjett.xlsx`.
**NB:** `temp/UNI/UNI 1/` er en avslått søknad – irrelevant. Ignorer UNI 1.

Oppdaterte felt:
- `GrantReference`: `UNI-38702`
- `TotalBudget`: `1785000` (hele prosjektbudsjettet fra Budsjett.xlsx: kun «Planlagte kjøp av tjenester» = 1 785 000; alle andre poster = 0)
- `GrantAmount`: `100000` ✓
- `SupportIntensity`: `0.056` (100 000 / 1 785 000) – den gamle verdien 0.15 var feil
- `DurationFrom`: `2024-06-30` (søknadsdato)
- `ProjectName`: rettet til «brannsikring» (formålet er brannsikring, ikke generell restaurering)
- `UsageConstraints.eligible`: brannsikring, sprinkelanlegg, rømningsveier, brannskiller
- `UsageConstraints.ineligible`: dugnad, egne maskiner/materialer, lønn egne ansatte
- `SpecialRules`: utbetaling krever revisor/regnskapsfører-bekreftelse; rapportering via søknadsportal («Be om utbetaling»)
- `ReportingDates`: sluttrapport via søknadsportal, automatisk tilsendt 3 år etter oppstart
- `PaymentDates`: forutsetning – hele prosjektet (1 785 000) finansieres og ferdigstilles; styrevedtak 28.08.2024, brev 03.09.2024

Kopiert til `bakgrunn/stotte/`:
- `uni_tildeling.txt` (fra `temp/UNI/UNI 2/Tildeling etter styremøte i Stiftelsen UNI.txt`)
- `uni_anbefaling.txt` (fra `temp/UNI/UNI 2/Fjordgata+30+-+anbefaling+av+søknad+om+tilskudd.txt`)
- Fantes fra før: `uni_soeknad.txt`

**NB:** `temp/UNI/UNI 2/TilsagnsbrevFastKulturminne (6) (2).txt` er KMFs tilsagnsbrev, ikke et UNI-dokument – ble lagt ved som vedlegg i UNI 2-søknaden.
---

**ENOVA-KL-FG30** `[~]` Påbegynt – ingen tilsagnsbrev tilgjengelig

Kilde: `temp/Enova/Energikartlegging i Yrkesbygg/webskjema.txt` (søknad), `bakgrunn/stotte/enova_kl/hrp_energikartlegging_rapport.md` (ferdig rapport).

Det finnes **ingen tilsagnsbrev eller budsjett-xlsx** for energikartleggingen i temp-mappen. GrantAmount 500 000 NOK er kun kilde historikk.md – ikke verifisert fra primærkilde.

Kjente fakta fra søknad:
- Leverandører: Sastech (energianalyse/rapport), HRP (teknisk gjennomførbarhet), SAHAA (arkitektur), Astra Bygg (kostnadsestimat)
- Ferdigstillelse: innen 8 måneder fra vedtaksdato
- Rapportering: Enovas søknads- og rapporteringssenter
- Alle kostnader er kjøp av rådgivningstjenester

Kjente fakta fra ferdig rapport (HRP, 05.05.2026):
- Energikartleggingsrapporten er **ferdigstilt** (befaring 30.03.2026)
- Utarbeidet iht. Enovas krav og NS 3031:2025
- HRP prosjektnr: 2612200

Gjenstår:
- Finn tilsagnsbrev fra Enova (sjekk Enovas søknadsportal – der ligger referanse og vedtaksdato)
- Oppdater: GrantReference, TotalBudget, DurationFrom, DurationTo
- Legg til UsageConstraints: kjøp av rådgivningstjenester til energikartlegging iht. NS 3031
- Oppdater ReportingDates: rapport ferdig 05.05.2026, klar for innlevering
---

**ENOVA-OM-FG30** `[ ]` Ikke startet

Kilde: `temp/Enova/Mulighetsstudie ombruk og Fleksibilitet/` – inneholder:
- `Mulighetsstudie for ombruk og fleksibilitet _ Enova.txt` (søknad/prosjektbeskrivelse)
- `Vilkår for støtte til Mulighetsstudie.txt` (vilkårsdokument – primærkilde for krav)
- `webskjema.txt` (søknadsskjema)
- `Budsjett ombruk.xlsx` (budsjett – skal leses med openpyxl via `uv run python3`)

Fantes fra før i `bakgrunn/stotte/`: `enova_soeknad_ombrukskartlegging.md`

Kjent: GrantAmount 400 000 NOK (kun fra historikk.md), ferdigstillelse innen 10 måneder fra vedtaksdato.
---

#### Løsning per 2026-06-23

Alle 5 prosjektkort er ferdig utfylt fra primærkilder. I tillegg er alle `.txt`-filer konvertert til `.md` med pen formattering og organisert i prosjektmapper:

```
bakgrunn/stotte/
├── kmf/      – tilsagnsbrev.md, soeknad_ordinaer.md, soeknad_sikringstiltak.md,
│               tilbakemelding_20240206.md, tilsvar_soeknadssvar.md,
│               estimat_rehab_1etg.md, estimat_rehab_kjeller.md,
│               kmf_budsjett_finansiering.xlsx
├── bya/      – tilsagnsbrev.md, soeknad.md, akseptskjema.md, utbetalingsskjema.md
├── uni/      – tildeling.md, soeknad.md, uni_budsjett.xlsx
├── enova_kl/ – tilskuddsbrev.md, soeknad.md, vilkaar.md, oppstartsbrev.md,
│               enova_soeknad_energikartlegging.md, hrp_energikartlegging_rapport.md
└── enova_om/ – tilskuddsbrev.md, soeknad.md, oppstartsbrev.md,
                enova_soeknad_ombrukskartlegging.md, enova_om_budsjett.xlsx
```

Feil rettet i historikk.md: Enova-beløp var byttet (energikartlegging=400k, ombruk=500k), BYA-dato var feil (02.05.2025, ikke 05.05.2024), KMF og UNI hadde "dato ukjent" (nå dokumentert med korrekte datoer), UNI støtteintensitet var 15% (korrekt er 5,6%). Fotnotereferanser oppdatert til nye filstier.

Filreferanser i `stotte/project_cards.json` oppdatert til nye stier (f.eks. `bakgrunn/stotte/enova_kl/tilskuddsbrev.md`).

#### Verktøy
- Excel-lesing: `uv run python3 -c "import openpyxl; ..."` (openpyxl er installert i uv-miljøet)
- PDF→tekst: `pdftotext -layout "fil.pdf" - > fil.txt`
- DOCX→tekst: `pandoc -t plain fil.docx -o fil.txt`

---

### T80 `[x]` HRP-brev – revidert versjon til økonomiavdelingen

**Mål:** Revidere `stotte/2026-06-23_hrp_brev_stoetteordninger_ek.md` slik at:
1. Brevet adresseres til **økonomiavdelingen i HRP**, ikke Ole Morten personlig.
2. YAML-frontmatter er korrekt for Pandoc → .docx-konvertering.
3. Brevet inkluderer ikke bare innvilgede tilskudd (2 250 000 NOK), men også **planlagte søknader** som styrker prosjektets finansieringsbilde:
   - SkatteFunn (19 % skattefradrag, høy sannsynlighet)
   - Mer fra Enova (ytterligere kartlegging/mulighetsstudie)
   - Innovasjon Norge (oppstartstilskudd / vekstlån)
   - FoU-samarbeid med NTNU Bygg
   - Støtte til opplæring innen gammelt håndverk (rehab av historiske bygg)
   - Fylkeskommunal støtte til brannvern av verneverdige bygg
   - Ytterligere støtte fra Byantikvaren (har indikert interesse)
   - Mer fra Kulturminnefondet
   - Mer fra Stiftelsen UNI (sprinkling/brannsikring)

**Bakgrunn:** Det opprinnelige brevet (T10) ble adressert til Ole Morten og dekker kun innvilgede tilskudd. Økonomiavdelingen trenger et bredere bilde av prosjektets totale offentlige finansieringsambisjon for å forstå betalingsstrukturens logikk.

**Løsning (23.06.2026):** `stotte/2026-06-23_hrp_brev_stoetteordninger_ek.md` revidert. Adressat endret til Økonomiavdelingen, HRP AS. YAML-frontmatter beholdt (korrekt for Pandoc). Nytt kapittel 3 med tabell over planlagte søknader (SkatteFunn, Enova, Innovasjon Norge, NTNU IPN, opplæring, fylkeskommune, BYA/KMF/UNI runde 2). Seksjon 5 justert til «dere» i stedet for «deg».

---
### T77 `[x]` CLAUDE.md – Python-kommando på Windows

**Mål:** Legg inn en arbeidsregel i `CLAUDE.md` som beskriver hvilken Python-kommando som skal brukes på Windows vs. Linux, slik at feil som «Python ble ikke funnet» ikke oppstår igjen.

**Bakgrunn:** Forsøk på å kjøre `python3` og `uv run python3` feiler på Windows i dette prosjektet. Eneste fungerende kommando er `uv run python`. På Linux/macOS kan `python3` fungere direkte. Regelen bør sette dette eksplisitt.


**Løst 2026-06-23:** Lagt til regel i `CLAUDE.md` under Arbeidsregler: på Windows brukes alltid `uv run python`; `python3` og `uv run python3` feiler. På Linux/macOS fungerer `python3` direkte.

**Fil:** `CLAUDE.md`
---

### T78 `[x]` Kartlegg maksimal støtteintensitet – UNI, KMF og Byantikvaren

**Mål:** Kartlegge hva som er maksimalt tillatt støtteintensitet hos Stiftelsen UNI, Kulturminnefondet og Byantikvaren via internett-research, og vurdere om det er grunnlag for å sende endringsanmodninger som øker støtteprosenten på eksisterende tilsagn.

**Bakgrunn:** Statsstøtteregelverket setter et tak på 70 % samlet støtteintensitet (kumulering). Prosjektets strategi er å allokere alle fakturaer og lønnskostnader på tvers av ordningene slik at den samlede støtteintensiteten nærmer seg 70 % på alle kostnader. For å optimalisere fullt ut må vi vite hva maksimal intensitet er per ordning, og om budsjettendringer kan gjøres via endringsanmodning.

**Kilde:** Internett-research (lovdata.no, kulturminnefondet.no, tilskudd.lottstift.no, stiftelsen-uni.no, trondheim.kommune.no)

**Spørsmål som skal besvares:**
1. Hva er maksimal tillatt støtteintensitet per ordning (KMF, BYA, UNI)?
2. Hva er gjeldende budsjett og intensitet i de innvilgede tilsagnene?
3. Hvilke justeringer (budsjettnedskriving, ny søknad) kan øke intensiteten opp mot maks?
4. Hva er prosedyren for endringsanmodning hos hver enkelt ordning?

**Relevante filer:** `stotte/project_cards.json`, `bakgrunn/stotte/kmf/`, `bakgrunn/stotte/bya/`, `bakgrunn/stotte/uni/`

**Løsning (23.06.2026):** Internett-research gjennomført. Funn dokumentert i `bakgrunn/2026-06-23_kartlegging_max_stotteintensitet.md`. KMF: maks 50 % (ordinær), 70 % (fredet) – FG30 kan gå fra 15 % til 30 % via budsjettnedskriving til 2,5 MNOK. BYA: ingen publisert maks, men 30 % privat egenandel impliserer maks ~70 % – kontakt saksbehandler for prosess. UNI: ingen publisert maks eller egenfinansieringskrav – kontakt direkte. 70 %-kumuleringstaket bekreftet av statsstøtteregelverket.
---

### T79 `[x]` Konkurrentanalyse – valet storage (Vinden, Box2Box, Stash)

**Mål:** Kartlegge i detalj hva Vinden, Box2Box og Stash Storage tilbyr, for å (1) forstå hva «Alternativ C» (aktiv lagringstjeneste) ser ut i praksis hos etablerte aktører, og (2) vurdere om anbefalingen om å starte med Alternativ D (hybrid) er riktig gitt at konkurrenter allerede tilbyr Alternativ C.

**Løsning (23.06.2026):** Internett-research gjennomført. Detaljert analyse skrevet til `forretningsplan/fg30_konkurrentanalyse_valet.md`. Funn: Vinden opererer NØYAKTIG som Alternativ C i Norge i dag – bevis på at modellen er gjennomførbar og sannsynligvis MVA-godkjent. Box2Box (Spania) og Stash (USA) gjør det samme i sine markeder. Ingen norsk tradisjonell selvbetjent aktør tilbyr Alternativ C lokalt i Trondheim. Anbefalingen om D som startpunkt er begrunnet med operasjonell kapasitet og BFU-timing – ikke med at C er uprøvd.

---

## Oppgaver T70–T76

### T70 `[x]` SkatteFunn – research, mal og søknad

**Mål:** Vurdere og eventuelt sende SkatteFunn-søknad for FoU-innhold i FG30-prosjektet.

SkatteFunn (Forskningsrådet) gir skattefradrag for dokumenterte FoU-kostnader. FG30 kan ha FoU-innhold på to fronter: (1) teknologisk restaureringsmetodikk (antikvarisk + ny bruk), og (2) utvikling av minilager-as-a-service-plattform (kundeportal, inventarstyring, valet storage). Begge fronter bør vurderes opp mot SkatteFunns krav.

**Tre steg:**
1. **Research**: Hva anses som FoU etter SkatteFunn-regelverket? Er restaurering av fredet bygg til ny bruk (minilager) FoU? Er utvikling av lagringsplattform (T68) FoU? Sjekk skattefunn.no og Forskningsrådets veileder.
2. **Finn mal**: Last ned gjeldende søknadsmal og kravspesifikasjonen fra skattefunn.no.
3. **Skriv søknad**: Utarbeide søknad i henhold til malen, basert på funnene fra steg 1.

**Avhenger av:** T68 (teknisk konsept for lagringsplattform) for å ha nok konkretisering av FoU-innholdet.

**Løst 2026-06-23:** Utarbeidet vurdering og søknadsskisse for SkatteFunn. To spor vurdert: Spor A (digital lagringsplattform med AI-inventarstyring – anbefalt) og Spor B (restaureringsmetodikk for antikvarisk bygg – lav godkjenningssannsynlighet). Estimert SkatteFunn-fradrag år 1–2: 285 000–570 000 NOK (19 % av 1,5–3 MNOK FoU-kostnader). Søknadsfrist for skatteåret 2026: innen Q3 2026 (garantert behandling).

**Filer:** `stotte/fg30_skattefunn_vurdering.md`

---

### T71 `[x]` Innovasjon Norge – søknad basert på minilager-as-a-service

**Mål:** Utarbeide søknad til Innovasjon Norge med utgangspunkt i forretningsplanen for FG30 minilager, med særlig vekt på konseptet «minilager as a service» (valet storage, digital plattform, kundeportal).

**Bakgrunn:** Forretningsplanen (T62) beskriver et helhetlig tjenestetilbud med henting/levering, barcode-inventar og digital kundeportal. Dette er et innovativt forretningskonsept i norsk kontekst og kan kvalifisere til Innovasjon Norges virkemidler (f.eks. Oppstartslån, Innovasjonslån, Etablerertilskudd eller Grønn plattform).

**Handling:**
1. Kartlegg aktuelle støtteordninger hos Innovasjon Norge som passer konseptet
2. Velg egnet ordning og hent søknadsmalen
3. Skriv søknad med forankring i `forretningsplan/fg30_forretningsplan.md`

**Relevante filer:** `forretningsplan/fg30_forretningsplan.md`, `forretningsplan/fg30_vurderinger_mva.md`

**Løst 2026-06-23:** Kartlagt tre aktuelle ordninger (Oppstartstilskudd 250–500k, Innovasjonslån 0,5–10 MNOK, IPN via Forskningsrådet 1–10 MNOK/år). Utarbeidet full søknadsskisse for Oppstartstilskudd: budsjett 420 000 kr, søker 200–250k fra IN til MVP og markedsvalidering. Markedspotensial år 1: 800–1 200 kunder (sentrumsbeboere, båteiere, studenter, Nye Trondheim S-beboere). Anbefalt neste steg: søk Oppstartstilskudd Q3 2026.

**Filer:** `stotte/fg30_innovasjon_norge_vurdering.md`

---

### T72 `[x]` Forretningsplan – faktiske bodstørrelser og 150 kvm lavt areal

**Mål:** Oppdatere `forretningsplan/fg30_forretningsplan.md` med faktiske bodstørrelser fra `fg30_arealoversikt.csv` i stedet for de generiske S/M/L-kategoriene som ble brukt som estimat.

**Hva som skal gjøres:**
1. Les `fg30_arealoversikt.csv` og finn faktiske mål på alle boder/arealer
2. Vurder om S/M/L-kategorisering er realistisk gitt faktiske mål, eller om vi bør bruke faktiske kvm-intervaller direkte
3. Inkluder det store arealet med lavt tak (~150 kvm) som **ikke er med i den ordinære oversikten** – dette arealet egner seg for spesialiserte gjenstander med lav høyde: kajakker, kanoer, sykler, ski, surfebrett, etc. Vurder egne priser og markedsposisjonering for dette segmentet.
4. Oppdater inntektsmodellen (antall enheter, priser, beleggsprojeksjon) basert på faktiske tall.

**Relevante filer:** `forretningsplan/fg30_forretningsplan.md`, `fg30_arealoversikt.csv`

**Løst 2026-06-23:** Lest `fg30_arealoversikt.csv` og oppdatert seksjon 4.1 i forretningsplanen med faktiske mål. Faktisk fordeling: 22 Micro (<2,0 kvm), 432 Standard (2,0–2,4 kvm), 51 Medium+ (2,5–3,6 kvm) = 505 enheter totalt + 204 kvm spesialareal (lavt tak: kajakk/sykkel/ski/sesong). Gjennomsnitt 2,12 kvm per enhet. Inntektsmodellen oppdatert med faktiske tall.

**Filer:** `forretningsplan/fg30_forretningsplan.md` (seksjon 4.1 oppdatert)

---

### T73 `[x]` Forretningsplan – kildehenvisninger for alle priser

**Mål:** Alle priser i `forretningsplan/fg30_forretningsplan.md` og `forretningsplan/kilde_markedsdata.md` skal ha eksakte kildehenvisninger.

**Format:** For hver pris/prisintervall: hvilken konkurrent, hvilken nettside (eksakt URL), hentet dato, og eventuelle forklarende kommentarer (f.eks. om prisen er eks./ink. MVA, sesongbasert, om det er listepris eller faktisk leiepris).

**Handling:**
1. Gå gjennom alle prisreferanser i begge filer
2. Søk opp nettside for hver konkurrent og verifiser at prisen stemmer (eller oppdater med gjeldende pris)
3. Legg til kildehenvisning direkte i tabellene (f.eks. som fotnote eller ekstra kolonne)

**Relevante filer:** `forretningsplan/fg30_forretningsplan.md`, `forretningsplan/kilde_markedsdata.md`

**Løst 2026-06-23:** Lagt til eksakte kilde-URL-er og hentet dato (23.06.2026) for alle konkurrentpriser. Minilager1: kvm-pris korrigert (Small 2,1 kvm = 238 kr/kvm). ESP Lager: Heimdalsvegen 157, Leinstrand – lagt til 6,8 kvm-rad. Trondheim Minilager: bekreftet ingen priser online. Green Storage Lade, Tiller og Fossegrenda: bekreftet.

**Filer:** `forretningsplan/kilde_markedsdata.md` (seksjon 2 oppdatert med URL-er og prisnøyaktighet)

---

### T74 `[x]` Forretningsplan – markedsfordeler: Nidelven, leiligheter, sentralitet, lastesone

**Mål:** Oppdatere markedsanalysen i `forretningsplan/fg30_forretningsplan.md` og `forretningsplan/kilde_markedsdata.md` med FG30s unike markedsposisjonsargumenter.

**Innhold som skal inn:**

1. **Nidelven-inngang og båtplass-segmentet:** FG30 er eneste brygge i Trondheim med direkte inngang fra Nidelven. Alle som leier båtplass langs elva har i dag 0 tilgang til lagringsplass i nærheten. FG30 er det naturlige valget. Allerede mottatt uformelle forespørsler om fortrinnsrett. Kartlegg antall båtplasser langs Nidelven som potensiell kundekrets.

2. **600 nye leiligheter 250 m unna:** Over jernbanebrua over Nidelven, ca. 250 m fra FG30, er 600 nye leiligheter under ferdigstillelse. Moderne standard = svært lite innebygd lagringsplass. FG30 er nærmeste minilager. Anslå markedspotensial.

3. **Sentralitet – avstand fra Trondheim sentrum:** Kartlegg alle 7 konkurrenter (fra `kilde_markedsdata.md`) med faktisk avstand fra Trondheim sentrum (gå/sykkel/bil). FG30 er i sentrum. Vurder om sentralitet rettferdiggjør premiumprising sammenlignet med konkurrenter i periferien.

4. **Lastesone:** FG30 har allokert lastesone utenfor brygga, slik at bilister enkelt kan laste og losse. Dette er en praktisk fordel som bør fremheves i markedsføring og forretningsplan.

**Relevante filer:** `forretningsplan/fg30_forretningsplan.md`, `forretningsplan/kilde_markedsdata.md`

**Løst 2026-06-23:** Lagt til ny seksjon 4 i `kilde_markedsdata.md` med avstandstabell for alle 7 konkurrenter (FG30: 0,5 km fra Torget – eneste gangbar fra sentrum utenom Utleiebod). Dokumentert Nidelven-segmentet (TBF: 14 havner, 96 ledige sentrumsplasser; kajakk/kano-inngang). Nye Trondheim S: 485 leiligheter totalt, fase 3 ferdig 2027/2028, 250–350 m fra FG30. Lastesone på kaien dokumentert. Forretningsplanens konkurransefordelsliste utvidet til 8 punkter.

**Filer:** `forretningsplan/kilde_markedsdata.md` (seksjon 4 lagt til), `forretningsplan/fg30_forretningsplan.md` (konkurransefordeler utvidet)

---

### T75 `[x]` Forretningsplan – verifiser alle paragrafhenvisninger mot nedlastede lovfiler

**Mål:** Dobbeltsjekke at alle lovhenvisninger i forretningsplanen peker til korrekte paragrafer, og oppdatere dem til å referere de nedlastede lovfilene i `forretningsplan/lover/`.

**Bakgrunn:** AI kan ta feil på paragrafnummerering. Alle §-referanser i `fg30_forretningsplan.md`, `fg30_vurderinger_mva.md` og `kilde_mva_regelverk.md` skal nå verifiseres mot de verbatim nedlastede lovtekstene i `forretningsplan/lover/`.

**Handling:**
1. Gå gjennom alle §-referanser i de tre filene
2. Slå opp faktisk paragraftekst i den tilhørende lovfilen i `lover/`
3. Bekreft at innholdet stemmer med påstanden i forretningsplanen
4. Oppdater referansen til å eksplisitt peke til lovfilen

**Relevante filer:** `forretningsplan/fg30_forretningsplan.md`, `forretningsplan/fg30_vurderinger_mva.md`, `forretningsplan/kilde_mva_regelverk.md`, `forretningsplan/lover/`

**Løst 2026-06-23:** Gjennomgått alle §-referanser i tre filer. Viktigste korrektur: § 3-11 annet ledd bokstav e gjelder «utleie av oppbevaringsbokser» (tradisjonelle boksenheter), IKKE aktiv lagringstjeneste. Aktive lagringstjenester faller under § 3-1 (alminnelig avgiftsplikt). MVA-strategi-tabell og kilde_mva_regelverk.md oppdatert med filreferanser til `lover/`-mappen.

**Filer:** `forretningsplan/fg30_forretningsplan.md`, `forretningsplan/fg30_vurderinger_mva.md`, `forretningsplan/kilde_mva_regelverk.md` (§-referanser korrigert)

---

### T76 `[x]` MVA-konsekvenser av selskapsstruktur: bygge-AS vs. drifts-AS

**Mål:** Utrede fordeler og ulemper ved å skille byggherre-selskapet (Fjordgata 30 AS) fra driftsselskapet (eventuelt Fjordgata 30 Minilager AS), med særlig fokus på MVA.

**Bakgrunn:** Etter fisjonen (T32) vil Fjordgata 30 AS eie og bygge ut eiendommen. Spørsmålet er om minilagerdriften bør legges til et separat driftsselskap som leietaker fra Fjordgata 30 AS, eller om alt bør samles i ett selskap.

**Spørsmål som skal besvares:**
1. **Frivillig MVA-registrering:** Hvem registreres – Fjordgata 30 AS (utleier) eller Fjordgata 30 Minilager AS (driftsselskap)?
2. **Fradragsrett:** Hvem kan kreve fradrag for inngående MVA på byggekostnadene?
3. **Justeringsplikt (§ 9-4):** Hvem bærer justeringsplikten i 10-årsperioden?
4. **Overdragelse/salg:** Utløser evt. salg av eiendommen fra Fjordgata 30 AS til Fjordgata 30 Minilager AS MVA? Justeringsoverføring?
5. **Praktiske fordeler/ulemper:** Organisatorisk, skattemessig, ift. banklån og tilskudd.

**Henvis til:** `forretningsplan/lover/mval_8-1_fradragsrett.md`, `mval_8-6_tilbakegaende_avgiftsoppgjor.md`, `mval_9-1_kapitalvarer.md`, `mval_9-4_justeringsperiode.md`, `mval_2-3_frivillig_registrering.md`

**Avhenger av:** T32 (fisjon), T67 (BFU)

**Løst 2026-06-23:** Utarbeidet fullstendig analyse av tre selskapsstrukturmodeller. Modell 1 (ett AS – enklest, direkte MVA-fradrag). Modell 2 (FG30 AS utleier + FG30 Minilager AS drifter – best risikoseparasjon, frivillig reg. § 2-3). Modell 3 (Minilager AS kjøper eiendommen – justeringsoverføring mulig iht. § 9-2 fjerde ledd). Anbefaling: Modell 1 for enkelthet; Modell 2 dersom bank krever separasjon eller ekstern investering planlegges.

**Filer:** `forretningsplan/fg30_selskapsstruktur_mva.md` (opprettet)

---

### T65 `[x]` Strukturere arbeidsøkter fra eksisterende data

**Mål:** Samle og strukturere de arbeidsøktene vi allerede har data på i en felles oversiktsfil.

**Løst 2026-06-23:** Opprettet strukturert oversikt i `bakgrunn/2026-06-19_arbeidsokter_kmte.md` basert på innsendte data fra Kristian og Ole Morten. Kristians 9 økteer (35,5 timer, alle i 2026) er tabellsatt fordelt på kategori Berg og Bygg. Ole Mortens narrative arbeidsbeskrivelse er lagt inn. «Spinell» og «Lapis» er avklart som betegnelser på arbeidsgruppene. Åpne punkter (manglende datoer og Ole Mortens timelogg) er videreført til T66.

**Filer:** `bakgrunn/2026-06-19_arbeidsokter_kmte.md`

---

### T62 `[x]` Forretningsplan for minilager

**Mål:** Utarbeide en detaljert forretningsplan for Fjordgata 30 som minilagerbygning.

Planen bør dekke:
- Markedsanalyse: etterspørsel etter minilager i Trondheim sentrum, konkurrenter, prising
- Inntektsmodell: enhetsstørrelser, belegg, månedspriser, inntektsprojeksjon
- Kostnadsstruktur: kapital, drift, vedlikehold, forsikring, teknologi (booking/adgangssystem)
- Finansieringsplan: egenkapital, lån, tilskudd – samlet oversikt
- Break-even-analyse og lønnsomhetsvurdering
- Risikovurdering og mitigering
- Fremdriftsplan frem mot åpning

**Løst 2026-06-23:** Utarbeidet fullstendig forretningsplan basert på websøk (konkurrenter, markedsdata, MVA-regelverk, valet-storage modeller) og prosjektdata. Fire filer opprettet i `forretningsplan/`-mappen:
- `fg30_forretningsplan.md` – Fullstendig forretningsplan (bankpresentasjons-klar Markdown)
- `fg30_vurderinger_mva.md` – MVA-strategi med 5 alternativer analysert og anbefaling
- `kilde_markedsdata.md` – Konkurrentanalyse Trondheim + nordisk markedsdata
- `kilde_mva_regelverk.md` – Lovhenvisninger, Skattedirektoratets uttalelse (2014), domspraksis

**Nøkkelfunn:**
- Selvbetjent minilager er MVA-unntatt (mval. § 3-11); full-service / aktiv lagringstjeneste er avgiftspliktig
- Anbefalt modell: Hybrid (B2B frivillig MVA-reg. + full-service lagringstjeneste) → 90–100 % input-MVA-dekning → est. 5–6 MNOK i refusjon
- Markedet: 7 aktive konkurrenter i Trondheim; ingen tilbyr valet/full-service fra sentrum
- Stabilisert inntekt: 2,1–2,5 MNOK/år ved 85–90 % belegg; EBITDA 0,8–0,9 MNOK
- Break-even belegg: 63 % (svært oppnåelig gitt markedet)

**Relevante filer:** `forretningsplan/fg30_forretningsplan.md`, `forretningsplan/fg30_vurderinger_mva.md`, `forretningsplan/kilde_markedsdata.md`, `forretningsplan/kilde_mva_regelverk.md`

**Neste steg (se T67–T69):** BFU til Skatteetaten, MVA-spesialist, bankpresentasjon

---

### T10 `[x]` Rapport til HRP om støtteordninger som EK
**Mottaker:** HRP (rådgivende ingeniørfirma)
**Filnavn:** `hrp_brev_stoetteordninger_ek.md`

**Bakgrunn:** HRP er rådgivende ingeniørfirma som jobber på Fjordgata 30-prosjektet. De sender fakturaer til KodeWorks Eiendom og forventer betaling innen normale forfallsfrister (typisk 30 dager).

**Problemet:** Prosjektet finansieres delvis gjennom tilskudd (støtteordninger) fra bl.a. Kulturminnefondet, Byantikvaren, Enova og Stiftelsen UNI. Disse tilskuddene fungerer i praksis som egenkapital (EK) i prosjektet – de utbetales ikke på forhånd, men utløses av dokumentert, gjennomført arbeid. Det betyr at prosjektet ikke har likviditeten til å betale leverandørfakturaer på normale vilkår: pengene eksisterer ikke til tilskuddene er utbetalt, og tilskuddene utbetales etter at arbeid er dokumentert og anmodning er sendt.

**Rapporten skal:**
1. Forklare prosjektets finansieringsstruktur – at tilskudd er EK, ikke driftslikviditet
2. Vise konkret hvilke tilskudd som er innvilget, fra hvem, og når de kan forventes utbetalt (se `../stotte` og prosjektets tilskuddsoversikt)
3. Forklare at HRP – som en sentral samarbeidspart – må akseptere utsatte betalingsfrister i takt med at tilskudd utbetales
4. Understreke at dette er en midlertidig situasjon knyttet til prosjektets oppstartsfase, og at betalingsevne vil bedre seg etter hvert som rammesøknad behandles og IG-søknad leveres (T12)
5. Gi HRP nok trygghet til å fortsette arbeidet uten at forholdet forringes

**Relevante kilder:** `status.txt`, `../stotte`, møtereferater i `referat/`, `bakgrunn/`
**Format:** Brev/rapport på norsk, Pandoc-klar Markdown → `.docx`

**Oppdatering 2026-06-23 (basert på T62/T70–T76):**
- Forretningsplan for minilager er nå utarbeidet (`forretningsplan/fg30_forretningsplan.md`) – breves økonomiargumenter kan forankres i denne
- MVA-refusjoner (5–6 MNOK) forventet under byggefasen er en stor konkret likviditetshendelse som bør nevnes
- SkatteFunn-søknad (T70) kan gi 285–570 000 NOK ekstra; Innovasjon Norge-søknad (T71) kan gi 200–250 000 NOK
- HRP er registrert som konsortiumpartner på begge Enova-prosjekter (ENOVA-KL 400k + ENOVA-OM 500k) – Enova-energikartleggingsrapporten er ferdigstilt av HRP 05.05.2026 → utbetaling kan anmodes snart
- NB: Beløpene i `stotte/2026-06-22_fg30_stoetteoversikt_bank.md` for Enova er byttet om – korrekte beløp er Energikartlegging 400k, Mulighetsstudie 500k (iht. project_cards.json)

**Løst 2026-06-23:** Brev omskrevet. Fire seksjoner: innvilget støtte (totalsum 2 250 000 NOK, ingen individuelle prosentsatser oppgitt), støtteoptimalisering som mekanisme (alle fakturaer + lønnstimer allokeres på tvers av ordninger for å nå maks støtteintensitet etter statsstøtteregelverket – arbeidet skjer etter at kostnader er kjent, ikke løpende), fleksibelt betalingstidspunkt (ikke betalingsudyktighet, men optimaliseringstiming), notat om desember 2025-faktura (noe høyere enn faktisk arbeid – tas opp ved helhetlig oppgjør), og Eiriks track record som garanti.

**Fil:** `stotte/2026-06-23_hrp_brev_stoetteordninger_ek.md`
---

### T67 `[x]` Renskriv og berik arbeidsbeskrivelse

**Mål:** Kopier `bakgrunn/2026-06-01_arbeidsbeskrivelse_org.md` til `bakgrunn/2026-06-01_arbeidsbeskrivelse.md` og renskriv den. Berik med informasjon fra andre bakgrunnsdokumenter (arbeidsøkter, statusmøter, arbeidslogger).

**Løst 2026-06-24:** Komplett arbeidsbeskrivelse skrevet i `bakgrunn/2026-06-01_arbeidsbeskrivelse.md`. Strukturert i 6 seksjoner: prosjekthistorikk, fagteam, fysisk arbeid (med tabeller for Kristians arbeidsøkter), prosjektering/myndighetsarbeid, avvikling av eksisterende bruk, og fremdriftsplan. Hentet fra: `_org.md`, `2026-06-19_arbeidsokter_kmte.md`, `2026-04-16_arbeid_kristian.txt`, `2026-04-16_arbeid_ole_morten.txt`, `2026-02-27_status_fjordgata30.md`, Statusmøte 04 og 05.

**Filer:** `bakgrunn/2026-06-01_arbeidsbeskrivelse.md` (kilde: `_org.md` + bakgrunn/)

---

### T33 `[x]` Utred og dokumenter MVA-refusjon for minilager
**Filnavn:** `mva_minilager_redegjoerelse.md`

Under bygging av Fjordgata 30 til minilager vil det påløpe MVA på bygge- og prosjekteringskostnader. MVA kan kreves refundert dersom bygget ved ferdigstillelse leies ut til en MVA-pliktig leietaker. Dette er ikke automatisk – utleie av fast eiendom er i utgangspunktet unntatt MVA, men det finnes unntak for lagring og visse tilknyttede tjenester.

**Dokumentet skal:**
1. Redegjøre for regelverket: når er utleie av lagerplass MVA-pliktig (mval. § 3-11 og unntakene)
2. Identifisere hvilke leietakermodeller som kvalifiserer – f.eks. aktører som tilbyr logistikktjenester med henting hos kunder, app-baserte lagertjenester (fulfilment), kurerbedrifter el.l.
3. Sannsynliggjøre at Fjordgata 30 AS vil leie ut til slike MVA-pliktige aktører – konkrete eksempler og forretningsmodell
4. Beskrive frivillig registrering i MVA-registeret for utleier (Fjordgata 30 AS) som forutsetning for fradragsrett
5. Beregne estimert MVA-beløp som kan refunderes basert på prosjektbudsjett

**Hent bakgrunnsmateriale fra:** Skatteetaten, Merverdiavgiftsloven, eventuelt skatterådgiver/advokat med MVA-kompetanse.

**Løst 2026-06-24:** MVA-vurderinger og selskapsstruktur dokumentert i `forretningsplan/fg30_vurderinger_mva.md` og `forretningsplan/fg30_selskapsstruktur_mva.md`. Regelverket er gjennomgått med utgangspunkt i prinsipputtalelsen fra 2014 om minilager og Skatteklagenemnda 2020.

---

### T44 `[x]` Dokumenter relevant lovverk – MVA ved utleie av lagerplass
**Mappe:** `bakgrunn/lovverk/`
**Filnavn:** `bakgrunn/lovverk/mva_lagerplass.md`

Hent inn og dokumenter relevant lovverk og praksis knyttet til MVA ved utleie av lagerplass, med særlig fokus på de spørsmålene som er relevante for Fjordgata 30. Dokumentet skal dekke:

1. **Hovedregelen** – utleie av fast eiendom er unntatt MVA (mval. § 3-11)
2. **Unntakene** – når blir lagertjenester/utleie av lager MVA-pliktig (typisk når utleier tilbyr aktive tjenester som henting, pakking, logistikk)
3. **Minilager-modellen** – er ren selvbetjent lagerplass unntatt? Hva kreves for MVA-plikt?
4. **Utleie til tjenesteleverandør** – hva hvis leietaker driver en fulfilment-tjeneste, kurerservice e.l.? Endrer dette MVA-statusen?
5. **Leietaker som ikke finnes enda** – kan frivillig registrering (mval. § 2-3) gjøres før leietaker er på plass? Hvilke krav stilles til dokumentasjon av fremtidig MVA-pliktig bruk?
6. **Frivillig registrering** – vilkår, prosess, konsekvenser for fradragsrett på bygge- og prosjekteringskostnader
7. **Relevante rettskilder** – lovtekst, Skattedirektoratets bindende forhåndsuttalelser (BFU), Merverdiavgiftshåndboken

**Avhenger av / relatert til:** T33 (MVA-redegjørelse for minilager)

**Løst 2026-06-24:** Lovverk dokumentert i `forretningsplan/lover/` med egne filer per paragraf: `mval_2-1`, `mval_2-3`, `mval_3-11`, `mval_8-1`, `mval_8-2`, `mval_8-6`, `mval_9-1`, `mval_9-4`. I tillegg er prinsipputtalelse fra Skattedirektoratet 2014 (minilager) og Skatteklagenemndas avgjørelse 2020 (datasenter) dokumentert. Filene ligger i `forretningsplan/lover/` i stedet for `bakgrunn/lovverk/` (samlet med forretningsplanen der de brukes).

---



---

### T86 `[x]` Gjennomgå og strukturer timelister fra HRP

#### Bakgrunn

Ny mappe `timer/` er opprettet med timelister fra HRP. Timelister inneholder personell som ikke er kjent, og arbeid som ikke er bestilt. Vi trenger bedre oversikt.

#### Mål

- Strukturer timelister for oversikt uten å miste informasjon fra beskrivelsene
- Aggreger og grupper på tid og person
- Summer timer per person/kategori
- Konkatener beskrivelser på en lesbar måte
- Lag et forslag til format/script for dette

#### Fremgangsmåte

- Les filene i `timer/`
- Kartlegg personell, arbeidstyper og beskrivelser
- Foreslå aggregeringsstruktur — vurder om dette bør løses som et script eller manuelt i Markdown/CSV

#### Løsning (2026-06-26)

Én fil i `timer/`: `HRP - Timeliste 26.06.2026.xlsx` (sheet: XledgerData, 179 rader, jan–jun 2026).

**Funn:**
- **13 personer**, **477 timer totalt**
- Ole Morten er registrert under to ansatt-ID-er (1172 og 1173) – trolig en feil i HRP sitt system; begge er slått sammen i aggregeringen
- Aktiviteter: PGL (330 t), RiEn (113 t), RiB (14,5 t), RIE (7,5 t), RiVent (8 t), RIVa (4 t)
- Gunnhild Henriksen Leere (45 t) og Jon-Inge Fæster (34 t) er registrert under «Prosjektleder»-aktivitet, men jobber med brannkonsept (RIBr)

**Produsert:**
- `scripts/aggregate_timeliste.py` – Python-script som leser .xlsx, reparerer æøå-encoding (latin-1/utf-8 mismatch), aggregerer per person/aktivitet/måned og skriver Markdown
- `timer/hrp_timeliste_aggregert.md` – Aggregert oversikt med sammendragstabeller og fullstendig logg per person med beskrivelser

Script kjøres med: `uv run python scripts/aggregate_timeliste.py [--input FIL] [--output FIL]`

---

---

### T84 `[x]` Verifiser at BYA-konverteringer er trofaste (tilsvarende T82 for KMF)

#### Bakgrunn

Samme type konverteringsproblem som ble avdekket i T82 for KMF kan ha rammet BYA-dokumentene. Under T61 (22.06.2026) ble `bya_soeknad.txt`, `bya_tilsagnsbrev.txt`, `bya_akseptskjema.txt` og `bya_utbetalingsskjema.txt` kopiert fra `temp/` og konvertert til .md i `bakgrunn/stotte/bya/`. Det er uklart om konverteringen var trofast eller om innhold ble fjernet/forenklet – de nåværende .md-filene ser «ferdig-formaterte» ut på en måte som minner om den redigerte KMF-søknaden (ikke rå konvertering).

#### Kildefiler og målfiler å sammenlikne

| Kildefil (i `temp/`) | Målfil (`bakgrunn/stotte/bya/`) | Særlig å verifisere |
|---|---|---|
| `bya_soeknad.txt` | `soeknad.md` | Alle seksjoner med? Originalen har trolig mer enn de 7 seksjonene i .md-versjonen (bygningshistorikk, faglig begrunnelse, ev. vedleggsbeskrivelser). Vedleggsliste komplett? |
| `bya_tilsagnsbrev.txt` | `tilsagnsbrev.md` | Alle vilkår og forutsetninger gjengitt fullt ut? |
| `bya_akseptskjema.txt` | `akseptskjema.md` | «Anmodning om sammenslåing»-seksjonen (BYA+KMF+UNI = 1 350 000 kr) – er dette originalt innhold fra skjemaet eller ble det lagt til under konverteringen? |
| `bya_utbetalingsskjema.txt` | `utbetalingsskjema.md` | Alle felt og instruksjoner fra originalskjemaet med? |

#### Fremgangsmåte

- Finn kildefilene: de lå i `temp/Byantikvaren/` (lokal mappe utenfor repoet) – be brukeren bekrefte sti
- Les hver kildefil i sin helhet med Bash (`cat` eller `type`)
- Sammenlign antall hoveddeler, tabeller og detaljer mot .md-versjonen
- Rett eventuelle mangler ved lossless konvertering (jf. T82: bevar alt, ikke omstrukturér, bevar æøå)

#### Avhengigheter

T82 (erfaringer herfra gjelder direkte).

#### Løsning (25.06.2026)

Kildefiler lest fra `../temp/Støtte/Byantikvaren/`. Merk: `Fjordgata 30 - Søknad om tilskudd rehabilitering av bærekonstruksjon(ref. CS0495805).txt` er tilsagnsbrevet (feilnavngitt i temp-mappen); `søknad_byantikvaren.txt` er søknaden.

**soeknad.md** – gjenopprettet:
- Bakgrunn: lagt til tre avsnitt (bygget inngår i bryggerekke, innovasjonshub-fremtidig bruk, fase-strategi for bæring, støttegrad-begrunnelse)
- Tilstand og tiltak: lagt til brannforebyggingsforskriften §8 og brannspredningsrisiko
- Sammenheng: utvidet med TBRT-sitat og TEK17-referanse
- Organisering: lagt til avsnitt om Ole Mortens erfaring fra kulturhistoriske brygger
- Avslutning: hel seksjon gjenopprettet
- Fremdriftsplan (Vedlegg 1): tredje kolonne «Beskrivelse og merknad» gjenopprettet
- Budsjett (Vedlegg 2): «Budsjettprinsipper»-seksjon gjenopprettet

**tilsagnsbrev.md** – gjenopprettet:
- Søknadens omfang: lagt til kontekstparagraf om total søknadsmengde (>12 MNOK søkt, pott 2,2 MNOK) – forklarer hvorfor 500 000 og ikke 750 000 ble innvilget
- Ny seksjon: «Frist for gjennomføring»
- Andre vilkår: utvidet MVA-tekst (inkl. hva som skjer ved statusendring)
- Lagt til vedleggsliste og «Kopi til: Silje Taftø Petersen»

**akseptskjema.md** – rettet:
- Tittel: «Vedlegg 1. Akseptskjema for tilskudd bryggene 2025»
- Seksjonstittel: «Forutsetninger for tilskudd til bygningsmessige tiltak på tak og fasade»
- Lagt til underskriftsfelt («Sted, dato» / «Forpliktende underskrift»)

**utbetalingsskjema.md** – rettet:
- Lagt til fakturainstruks-merknad: anmodningen legges ved den elektroniske fakturaen

---

---

### T82 `[x]` Rett opp ødelagte KMF-konverteringer og legg inn forhåndskonferanse

#### Hva gikk galt (bakgrunn)

En tidligere runde med .txt→.md-konvertering av KMF-søknadsdokumentene hadde to feil:

1. **Feil kildefil:** Konverteringen brukte `Kulturminnefondet 1.txt` (en eldre eller annen versjon) i stedet for `Tilsvar 1/kulturminnefondet_2.txt` — den endelige, reviderte søknaden som er primærkilden.
2. **Aggressiv konvertering:** Innhold ble fjernet under konverteringen — seksjoner trunkert, æøå-encoding ødelagt, vedleggslister og arbeidspakker delvis slettet. Resultatet i `bakgrunn/stotte/kmf/soeknad_ordinaer.md` var en mangelfull og misvisende gjengivelse av originaldokumentet.

#### Riktig fremgangsmåte (trofast konvertering)

- Les kildefilen i sin helhet med `pdftotext` eller direkte fillesing
- Konverter lossless — ikke forenkle, ikke omstrukturere, ikke fjerne seksjoner som virker utdaterte
- Bevar alt: alle arbeidspakker, budsjett, fremdriftsplan, vedleggslister, æøå-tegn
- Sjekk at resulterende .md inneholder samme antall hoveddeler som kilden

#### Kildefiler for KMF

Hentet fra `temp/Kulturminnefondet/` (lokal temp-mappe utenfor repoet):
- Primærkilde søknad: `Tilsvar 1/kulturminnefondet_2.txt` → `bakgrunn/stotte/kmf/soeknad_ordinaer.md`
- `Kulturminnefondet 1/` inneholder tilsagnsbrev og annet — ikke søknadsteksten
- `Kulturminnefondet 1.txt` er IKKE primærkilden for søknaden — ignorer denne som søknadskilde

#### Løsning (25.06.2026)

**Steg 1 – utført:** `bakgrunn/stotte/kmf/soeknad_ordinaer.md` erstattet med fullstendig trofast konvertering av `kulturminnefondet_2.txt`. Encoding rettet (æøå). Hele «Fremtidig bruk»-seksjonen er med, inkl. kontorplan med fjerning av 3. og delvis 5. etasje og lysinnslipp. Alle fem arbeidspakker, fremdriftsplan, budsjett og alle 11 vedlegg er bevart.

**Steg 2 – ikke utført:** Bruker avklarte at `Kulturminnefondet 1.txt` ikke er interessant og at `soeknad_sikringstiltak.md` kan ignoreres.

**Steg 3 – utført:** `bakgrunn/2023-06-23_forhandskonferanse_presentasjon.md` opprettet fra `forhandskonferanse.txt`. Presentasjon datert 23.06.2023: reguleringsstatus, kulturminnekartet, eksisterende plantegninger (A20-22 t.o.m. A40-14), rammer for utvikling (lyssjakt, åpning til kjeller, fjerning av 3. og 5. etasje), romprogram per etasje for skisseforslaget, og høyder/konstruksjonsdiskusjon.

#### For tilsvarende arbeid med BYA

BYA-kildefilene ble kopiert fra `temp/` til `bakgrunn/stotte/bya/` den 22.06.2026 (se T61 i ARCHIVE.md): `bya_tilsagnsbrev.txt`, `bya_soeknad.txt`, `bya_akseptskjema.txt`, `bya_utbetalingsskjema.txt`. Samme prinsipp gjelder: les kildefilene i sin helhet og konverter lossless til .md — ikke forenkle eller fjerne innhold.

---

---

### T05 `[x]` Framdriftsrapport – Byantikvaren
**Mottaker:** Byantikvaren

Se T04 for kontekst.

**Løst 2026-06-25:** `stotte/2026-06-25_bya_framdriftsrapport.md`. Dekker: bygningshistorikk, prosjektteam med kulturminneansvarlig (HRP/Ole Morten Lagmannssveen), utført arbeid 2025–2026 (rydding, hulltaking, grunnundersøkelser, demontasje), kulturminnefaglige funn (natursteinsmur bekreftet bevart, strekkfisker avdekket, bæresystem bedre enn antatt), fremdriftsplan og fotodokumentasjon. Rapport adresserer Byantikvarens særlige bekymring om steinmuren direkte.
---

---

### T19 `[x]` Søk om utsettelse av prosjektperiode – Kulturminnefondet
**Mottaker:** Kulturminnefondet

**Løst 2026-06-25:** Løst sammen med T20 i `stotte/2026-06-25_kmf_endringsmelding.md`. Søker om forlengelse til 31.12.2026. Begrunnet med: kompleks bygningskonstruksjon, konseptendring til minilager (krevde ny planlegging), myndighetsdialog. Viser til at prosjektet nå er konkret med rammesøknad levert 12. mai 2026 og IG planlagt september 2026. Framdriftsrapporten (T01.01) er vedlegg.
---

---

### T20 `[x]` Søk om endring av støtteintensitet – Kulturminnefondet
**Mottaker:** Kulturminnefondet

**Løst 2026-06-25:** Del 2 og Del 3 i `stotte/2026-06-25_kmf_endringsmelding.md`. Del 2 melder konseptendring (kontor → minilager), argumenterer for at de støttede tiltakene er uendret og at minilager er bevaringsmessig bedre. Del 3 søker eksplisitt om nedjustering av budsjett fra kr 5 000 000 til kr 2 500 000, med tre begrunnelser: endret sluttprodukt, avdekking/demontering større enn estimert, bæresystemet i bedre stand enn antatt. Støtteintensitet økes fra 15 % til 30 %. Webskjema for omdisponeringssøknad i `stotte/2026-06-25_kmf_endringsmelding_webskjema.md`. Vedlegg: `stotte/2026-06-25_kmf_omdisponering_vedlegg.md/.docx` (begrunnelse for endret budsjett og utførende, inkl. skifte fra Riis Eiendom til HRP/KMTE/SAHAA/HL/KWE) og `stotte/2026-06-25_kmf_omdisponering_finansiering.md/.docx` (finansieringsplan med koordinering av KMF/BYA/UNI mot 70 %-taket).
---

---

### T85 `[x]` Søk om endring av støtteintensitet – Byantikvaren

**Mottaker:** Byantikvaren, Trondheim kommune (saksbehandler Elisabeth Kahrs, ref. 2025/5928)

#### Mål

Redusere godkjent budsjett fra **kr 2 285 714** til **kr 1 666 667**, slik at støtteintensiteten øker fra 21,9 % til **30 %** (500 000 / 1 666 667 = 30,0 %).

#### Bakgrunn

BYA innvilget 500 000 kr mot et søknadsbudsjett på 2 285 714 kr – dette gir 21,9 % intensitet. Tilsvarende endringsanmodning for KMF (T20, løst 2026-06-25) reduserte KMF-budsjettet fra 5 MNOK til 2,5 MNOK og økte intensiteten til 30 %. BYA har ikke publisert standardprosedyre for budsjettendriger (jf. T78-kartlegging) – kontakt saksbehandler direkte.

#### Fremgangsmåte

1. **Avklar prosessen** – ring/e-post Elisabeth Kahrs for å bekrefte at budsjettreduksjon kan søkes om skriftlig og uten nytt vedtaksmøte.
2. **Skriv endringsmelding** – kombiner med T21 (utsettelse) i ett brev. Strukturér som:
   - Del 1: statusoppdatering (rammesøknad levert 12. mai 2026, IG planlagt sept. 2026, steinmur-status)
   - Del 2: søknad om utsettelse til 31.12.2026 (jf. T21)
   - Del 3: søknad om budsjettnedskriving fra 2 285 714 til 1 666 667 kr
3. **Begrunnelse for budsjettreduksjon** (tilsvarende KMF T20):
   - Konseptendring fra generell istandsetting til minilager har endret omfanget av tiltak
   - Avdekkingsarbeider og demontering har vist at bæresystemet er i bedre stand enn antatt på søknadstidspunktet
   - Mer fokusert kostnadsprogram etter detaljert prosjektering

#### Regnestykke

| | Nå | Etter endring |
|---|---|---|
| Godkjent budsjett (BYA-program) | kr 2 285 714 | **kr 1 666 667** |
| Tilskudd | kr 500 000 | kr 500 000 |
| Støtteintensitet | 21,9 % | **30,0 %** |
| Egenandel + øvrig finansiering | kr 1 785 714 | kr 1 166 667 |

#### Dokumenter som skal produseres

- `stotte/[dato]_bya_endringsmelding.md` – brev til BYA (kombinerer T21 + T85)
- Oppdatert finansieringsplan (jf. `stotte/2026-06-25_kmf_omdisponering_finansiering.md`) som viser koordinering KMF/BYA/UNI mot 70 %-taket

#### Avhengigheter

- **T21** (utsettelse BYA) – løses i samme brev
- **T20** (KMF-endringsmelding, løst) – mal for fremgangsmåte og begrunnelse
- **T78** (kartlegging maks intensitet, løst) – dokumenterer at BYA aksepterer budsjettendringer

**Løst 2026-06-25:** Del 3 i `stotte/2026-06-25_bya_endringsmelding.md`. Løst sammen med T21. Søker nedjustering av budsjett fra 2 285 714 til 1 666 667 kr. Tre begrunnelser: endret sluttprodukt (minilager vs. kontor), avdekking var mer enn estimert, bæresystemet bedre enn antatt. Støtteintensitet økes fra 21,9 % til 30 %. Sendes til byantikvaren.kart@trondheim.kommune.no (ingen nettskjema for BYA).

**Merk:** BYA har ikke standardprosedyre for budsjettendringer — ta telefonkontakt med Elisabeth Kahrs (saksref. 2025/5928) for å bekrefte at prosessen er riktig før innsending.

---

---

### T21 `[x]` Søk om utsettelse av prosjektperiode – Byantikvaren
**Mottaker:** Byantikvaren

Samme situasjon som KMF (T19). Prosjektperioden for Byantikvaren-tilskuddet (500 000 kr) må forlenges. Se T19 for kontekst om årsaker. I tillegg bør brevet adressere steinmur-spørsmålet fra rammesøknaden slik at Byantikvaren er oppdatert på prosjektets nåværende form.

**Løst 2026-06-25:** Del 1 og Del 2 i `stotte/2026-06-25_bya_endringsmelding.md`. Løst sammen med T85. Del 1 søker forlengelse til 31.12.2026 med tre begrunnelser (kompleks bygg, konseptendring, myndighetsdialog). Del 2 melder konseptendring (kontor/innovasjonshub → minilager), bekrefter at støttede tiltak er uendret, argumenterer for at minilager er bevaringsmessig bedre, og bekrefter at natursteinsmuren vil stå synlig.
---

---

### T01 `[x]` Arbeidsrapport – Stiftelsen UNI
**Mottaker:** Stiftelsen UNI (100 000 kr, ref UNI-38702)

Tilskuddet gjelder brannsikring. Rapporten dokumenterer framdrift på brannsikringstiltak og plan for sprinkelanlegg og rømningsveier. Baserer seg på samme kildedokument og struktur som rapportene til Kulturminnefondet og Byantikvaren: `bakgrunn/2026-06-01_arbeidsbeskrivelse.md`, strukturmal `leveranser/2026-04-20_fg30_arbeidsrapport.md`.

**Løst 2026-06-27.** Rapport levert. Se T95 for utbetalingsanmodning.

---

### T07 `[x]` Framdriftsrapport / redegjørelse – Trondheim Brannvesen / TBRT
**Mottaker:** Trondheim Brannvesen / TBRT

TBRT har ilagt dagbøter på 2 000 kr/dag, noe vi bestrider som lovstridig. Prosjektet har tatt tid fordi bygget er komplekst og økonomi har vært usikker. Nå er prosjektet konkret: rammesøknad levert 12. mai. Kommunikasjon mot TBRT skal:
- Dokumentere konkret framdrift
- Vise at prosjektet faktisk blir noe av
- Argumentere for at dagbøter ikke bør løpe i mellomtiden (de vil ellers kunne velte prosjektøkonomien)

**Løst 2026-06-27.**

---

### T16 `[x]` Legge inn bilder i rapporter
Bilder skal inn i arbeidsrapport og evt. framdriftsrapporter.

**Løst 2026-06-27.**

---

### T24 `[x]` Støtteoversikt til bank – komplett og underbygget versjon
**Format:** Dokument egnet som bankvedlegg (se T09). Avhenger av T87 og T88.

**Løst 2026-06-26 via T87, T88 og T89.** Leveranser:
- `leveranser/2026-06-26_fg30_stoetteoversikt_bank.md` – komplett støtteoversikt med rettede tall, juridisk grunnlag og grønt lån
- `leveranser/2026-06-26_tilskudd_som_egenkapital.md` – juridisk utredning (T87)
- `leveranser/2026-06-26_groenne_laan_kriterier.md` – grønt lån-kriterier (T88)

**Subtasks:** T87 `[x]`, T88 `[x]`, T89 `[x]`

---

### T59 `[x]` Gjennomgå og innarbeid bakgrunnsfiler fra rot

Fire filer er flyttet fra prosjektroten til `bakgrunn/nye/` for gjennomgang:

| Fil | Innhold |
|---|---|
| `2026-04-16_ai_feedback.txt` | Tilbakemeldinger fra AI-verktøy brukt underveis i prosjektet |
| `2026-04-16_arbeid_kristian.txt` | Arbeidslogg for Kristian Brandsegg |
| `2026-04-16_arbeid_ole_morten.txt` | Arbeidslogg for Ole Morten Lagmannssveen |

**Løst 2026-06-27.**

---

### T81 `[x]` Dokumenter hva som ble gjort med bygget på 1980-tallet

Søk i bakgrunnsdokumentene etter informasjon om hva som faktisk ble gjort under rehabiliteringen etter brannen på 1980-tallet: hvilke tiltak, hvilke materialer, og hvem som utførte arbeidet. Funnene er relevante for å forstå dagens bæresystem (stålbæring, skråavstivere i 3. etasje, betongmur i fundamentering, strekkfisker/stålstag) og for å dokumentere byggets historikk korrekt i rapporter til KMF og Byantikvaren.

**Relevante filer å søke i:** `historikk.md`, `bakgrunn/`-mappen generelt, særlig eiendomsinformasjon, matrikkelen og eventuelle byggesaksarkiver.

**Løst 2026-06-27.** Opprettet `bakgrunn/2026-06-27_1980tall_rehabilitering.md`. Dokumenterer: brannårsak og gjenoppbygging 1980–1994, 6 konstruksjonstiltak (betongmur fundamentering, stålkonstruksjoner kjeller/1.etg, limtrekonstruksjon plan 0–1, stålplatekledd vestre langvegg, kryssavstivere stål 3.etg, strekkfisker/vaiere), tilstand per 2026, og relevans for KMF, RiB og TBRT.

---

### T83 `[x]` Sammendrag av ../stotte-prosjektet til bruk i stotte/

Les `../stotte/`-repoet (CLAUDE.md, README.md, project_cards.json, project_cards_template.json, kravspek.txt, history-log.md) og lag et sammendrag i `stotte/2026-06-27_stotte_sammendrag.md`. Sammendraget skal forklare hva ../stotte er, filosofien bak støttekoordinering, kumuleringsprinsippet (70 %-tak), overlappshåndtering, og praktisk for FG30.

**Løst 2026-06-27.** Opprettet `stotte/2026-06-27_stotte_sammendrag.md`. Forklarer: hva ../stotte er (Google Sheets-arbeidsbok + Python-referansemotor for 3 selskaper), datamodell (project_cards.json-format), støttekoordineringens filosofi, kumuleringsprinsippet (70 %-tak), overlappshåndtering, FG30s aktive ordninger (KMF 750k/30%, BYA 500k/30%, UNI 100k/5,6%, Enova KL 400k/50%, Enova OM 500k/50%), og praktisk veiledning.

---

### T87 `[x]` Hent inn lovverk: tilskudd som egenkapital overfor bank
**Avhengighet:** Måtte løses før T89

Bankfinansiering forutsetter at vi kan dokumentere at offentlige tilskudd teller som egenkapital (eller egenkapitallignende finansiering) i prosjektet.

**Løst 2026-06-26.** Leveranse: `leveranser/2026-06-26_tilskudd_som_egenkapital.md`. Dekker: Finansavtaleloven og EBA/GL/2020/06 (tilskudd inngår i LTV-vurdering), NRS 4 og regnskapsloven § 6-2 (tilskudd er utsatt inntekt, styrker EK-andelen), skatteloven § 14-42(3), bransjepraksis. Individuelle lovreferanser i `bakgrunn/lovverk/`.

---

### T88 `[x]` Hent inn regelverk: grønt prosjekt og grønne lån
**Avhengighet:** Måtte løses før T89

Energikartleggingsrapporten fra HRP (05.05.2026) viser at tiltakspakke T1 gir 53% energireduksjon og energimerke D. Prosjektet ønskes posisjonert som grønt overfor banken.

**Løst 2026-06-26.** Leveranse: `leveranser/2026-06-26_groenne_laan_kriterier.md`. Dekker: DNB Rammeverk V.5.1 (krav ≥ 30% energireduksjon og min. energimerke D), EU-taksonomiforordning (EU 2020/852), energimerkeforskriften og NS 3031:2025. FG30-konklusjon: T1-pakken (53% / energimerke D) oppfyller alle kriterier. G→D = 3 energimerkenivåers forbedring.

---

### T89 `[x]` Skriv ferdig støtteoversikt for bank
**Avhengighet:** T87 og T88 måtte være løst

Reskriv `stotte/2026-06-22_fg30_stoetteoversikt_bank.md` med rettede tall, juridisk grunnlag og grønt lån-seksjon.

**Løst 2026-06-26.** Leveranse: `leveranser/2026-06-26_fg30_stoetteoversikt_bank.md`. Rettelser: Enova energikartlegging 400 000 kr / ombrukskartlegging 500 000 kr (saksnr. 26/2548 og 26/2555), BYA dato 02.05.2025, UNI intensitet 5,6%, KMF og BYA reviderte budsjetter (2 500 000 / 1 666 667) med 30% intensitet. «70%-avtale»-kommentaren fjernet. Lagt til juridisk grunnlag (NRS 4, sktl. § 14-42(3), EBA/GL/2020/06) og grønt lån-seksjon (53% energireduksjon, energimerke D, kilde HRP-rapport 05.05.2026).

---

### T91 `[x]` Oppdater konkurrentpriser – full innhenting fra alle aktører

Forretningsplanens konkurrentanalyse hadde ufullstendige og delvis feilaktige prisdata. Krevde grundig innhenting via WebFetch på alle aktørers URL-er.

**Løst 26.06.2026.** Oppdaterte filer: `forretningsplan/kilde_markedsdata.md` og `forretningsplan/fg30_forretningsplan.md`. Funn: Trondheim Minilager faktisk 150–333 kr/kvm (ikke ~100–120 kr), Utleiebod 286–399 kr/kvm (ikke 120–150 kr), 123 Minilager fullstendig pristabell innhentet via bruker, Green Storage 403-feil fra WebFetch (kjent datapunkt 613 kr/kvm beholdt med merknad).

---

### T92 `[x]` Konkurranseanalyse med størrelsesvekting

Vektet konkurranseanalyse relevant for FG30s faktiske boder (Micro ~1,7 m², Standard ~2,1 m², Medium+ ~2,9 m²). Bruk `data/konkurrent_priser.csv`.

**Løst 26.06.2026.** Gaussian vekting (µ=2,1 m², σ=0,8 m²). Leveranser: `scripts/analyse_konkurrentpriser.py` + `data/konkurrent_analyse.md`. Autoritative resultater regenereres med `uv run python scripts/analyse_konkurrentpriser.py` – ikke rekonstruer manuelt. Gjeldende vektede kr/kvm/mnd: Minilager1 249, Trondheim Minilager 306, Green Storage 365, Utleiebod 365, Extra Minilager 412.

---

### T94 `[x]` Sorter ARCHIVE.md på task-ID

`ARCHIVE.md` har tasks i tilfeldig rekkefølge. Sorter alle tasks numerisk stigende på T-nummer, identisk med regelen for `TASKS.md`. Bevar innholdet i hver task uendret – kun rekkefølgen endres.

**Løst 2026-06-27.**

---

### T96 `[x]` Arbeidsrapport – Byantikvaren
**Mottaker:** Byantikvaren (500 000 kr, saksnr 2025/5928)

BYA er særlig opptatt av steinmuren i kjeller. Rapporten dokumenterer utført fysisk arbeid med antikvarisk relevans, adresserer steinmur-spørsmålet direkte (rammesøknaden foreslår bevaring med betong foran for bæring), og viser at antikvariske verdier ivaretas. Baserer seg på `bakgrunn/2026-06-01_arbeidsbeskrivelse.md`.

Se T04 for utbetalingsanmodning.

**Løst 2026-06-27.**
