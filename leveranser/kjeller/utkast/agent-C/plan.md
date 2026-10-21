---
tittel: "Kjellerplan Fjordgata 30 — Utkast C: RIB-gating, risiko og materialflyt"
versjon: utkast-C
dato: 2026-10-21
agent: agent-C
status: utkast
---

# Kjellerplan Fjordgata 30 — Utkast C
## RIB-gating, risiko og materialflyt

**Prosjekt:** Fjordgata 30 Minilager, KodeWorks Eiendom AS\
**RIB:** Ole Stenmo, Sivilingeniørene Harboe og Leganger AS\
**PGL antikvarisk istandsetting:** Ole Morten Lagmannssveen, HRP AS

---

## Innledning og forutsetninger

Dette dokumentet er et arbeidsinternt prosjekteringsunderlag — det utfyller NS 3420-beskrivelsen (HRP 19.10.2026) med det beskrivelsen ikke dekker: operasjonell rekkefølge, juridiske gates, risikoregister og logistikk. Det erstatter ikke NS 3420-dokumentet.

**Dimensjonerende vannstand:** kote +3,20 (satt av RIB, jf. notat 10.02.2026).\
**Eksponeringsklasse betong:** XS3 (tidevann/stormflo, saltvann, jf. Nidelven-tilknytning).\
**Bæreevnekrav:** 7,5 kN/m² (lagerareal plan –1 og 1; brannkrav R60 på hovedbæring).\
**Arkeologisk status (per 21.10.2026):** Dispensasjon etter kulturminneloven § 8 ikke innsendt. Riksantikvaren (Sissel Ramstad Skoglund) har bekreftet myndighet, tilbudt befaring og satt krav om målsatte tegninger av graveomfang. Ingen graving i faste masser er tillatt frem til dispensasjon foreligger.

---

## Del 1 — Sekvensdiagram og avhengighetskart

### 1.1 Faseinndeling

| Fase | Innhold | Seriell / parallell |
|---|---|---|
| **F0** | Forberedelser og klargjøring | Parallell internt; seriell mot F1 |
| **F1** | Opprydding og kartlegging | Delvis parallell; gate mot arkeolog og RIB |
| **F2** | Demontasje av bærende elementer (tømmer/tørrmur) | Seriell — avhenger av RIB-gate |
| **F3** | Prøvegraving og arkeologisk befaring | Gate mot graving i faste masser |
| **F4** | Dispensasjonssøknad og saksbehandling | Parallell med prosjektering |
| **F5** | Utsjakting og masseflytting | Seriell — avhenger av F4 |
| **F6** | Fundamenter (støp under vann) | Seriell — avhenger av F5 + RIB-gate |
| **F7** | Bunnplate (armering, støp) | Seriell — avhenger av F6 + RIB-gate |
| **F8** | Vegger (ensidig + tosidig forskaling, støp) | Seriell — avhenger av F7 |
| **F9** | Delevegger og søylegjennomføringer | Seriell — avhenger av F8 |
| **F10** | Overflatebehandling, isolasjon, katodisk vern | Avhenger av F9 |
| **F11** | Overgang til plan 1 (etasjeskille) | Avhenger av F10 + RIB-gate |

### 1.2 Detaljert avhengighetstabell

```
F0: Forberedelser
  ├─ F0a Vinterklargjøring (toalett/kjøkken til 1. etg, frostfritt vann)
  │       [PARALLELL med F0b–F0d]
  ├─ F0b Ny kjellernedgang fra 1. etg (der kjøkkenet sto)
  │       [BLOKKERER F5–F11 som rymningsvei og materialvei]
  ├─ F0c Søyleoppmåling innerst mot Fjordgata
  │       [Avventer: Ole Morten målinger 21.10.2026, ±10 cm toleranse]
  └─ F0d Kjellerplan ferdigstilt + sendt til RIB

F1: Opprydding og kartlegging
  ├─ F1a Fjerne løst materiale (sperretråder, løse bjelker, søppel)
  │       [BLOKKERER: RA-befaring — løst materiale må ryddes først]
  ├─ F1b Registrere søyler (posisjon, materiale: stål/tre)
  │       [Avventer: F0c]
  ├─ F1c Fotografisk dokumentasjon av nåværende tilstand
  │       [PARALLELL med F1a/F1b]
  └─ F1d Markere bjelker for gjenbruk (spray/lapp)

        *** GATE G1: Riksantikvar-befaring ***
        Trigger: F1a fullført (ryddig kjeller)
        Aktør: Riksantikvaren + Trøndelag fylkeskommune
        Blokkerer: F3, F5 (graving i faste masser)

F2: Demontasje av bærende elementer
  ├─ F2a Presentere kjellerplan for RIB (Ole Stenmo)
  │       *** GATE G2: RIB-signering for kutting av langsgående tømmer ***
  │       Aktør: Ole Stenmo, Harboe & Leganger AS
  │       Dokumentert: skriftlig, arkivert i prosjektmappe
  ├─ F2b Kutte langsgående tømmerstokker i 2–2,5 m lengder
  │       [AVHENGER av G2; ikke av arkeolog-gate]
  ├─ F2c Løfte/droppe kuttede bjelker gjennom gulvåpning (floa)
  │       [Tidsvindu: springflo, tidlig morgen]
  └─ F2d Tørrmur-stabilisering (løse stein flyttes internt — studenter)
          [AVHENGER: BYA har godkjent prøvegraving mot Fjordgata 28-hjørnet
           for ringmurskartlegging — denne aktiviteten pågår allerede]

        *** GATE G3: Arkeolog-dispensasjon (kml § 8) ***
        Trigger: Befaring holdt (G1), graveomfang tegnet opp (plan+snitt)
        Aktør: Riksantikvaren
        Saksbehandlingstid: minimum 4 uker etter fullstendig søknad
        Blokkerer: F5 (graving i faste masser, utover løs masse)

F3: Prøvegraving og arkeologisk befaring
  [AVHENGER av G1]
  └─ F3a Prøvegrave i 1–2 punkter for stratigrafisk vurdering
          (avklart med BYA; ikke faste masser — koordineres med NIKU)

F4: Dispensasjonssøknad
  ├─ F4a Utarbeide målsatte tegninger (plan + snitt) av graveomfang
  │       [Avhenger av F3a + RIB-detaljprosjektering]
  ├─ F4b Sende søknad til Riksantikvaren (kml § 8)
  └─ F4c Riksantikvaren behandler — NIKU-tilrådning, § 14-vurdering
          [4+ uker; kan gjøres parallelt med F0b, F1, F2]

F5: Utsjakting og masseflytting
  [AVHENGER av G3]
  ├─ F5a Utsjakting innvendig ca. 130 m³ (FD1.13319A)
  ├─ F5b Opplasting og containerlogistikk (Fjordgata-siden, FM1.2329A)
  └─ F5c Evt. graving under vann utenfor natursteinsmur (FD5.1131114A)
          *** GATE G4: Separat tillatelse for graving mot elv ***
          (kommunale myndigheter + evt. NVE, sjøgrunn)

F6: Fundamenter
  [AVHENGER av F5]
  ├─ F6a Klargjøre fundamentpunkter (grave ned, ±25 stk)
  ├─ F6b Armere fundamenter (B500NC, XS3, utfkl. 3)
  │       *** GATE G5: RIB armeringssjekk fundamenter ***
  └─ F6c Støpe fundamenter i vann (AUV-betong B45, MF40, LG5.1117613A)

F7: Bunnplate
  [AVHENGER av F6]
  ├─ F7a Legge drenslag 16/32 (inntil 200 mm, 30 m²)
  ├─ F7b Legge forsterkningslag 0/4 (inntil 100 mm)
  ├─ F7c XPS-isolasjon 50 mm under plate + under fundamenter
  ├─ F7d Radon-/fuktsperre (plastbasert belegg, skjøter tapes)
  ├─ F7e Armere bunnplate (B500NC, XS3, utfkl. 3)
  │       *** GATE G6: RIB armeringssjekk bunnplate ***
  ├─ F7f Legge svelleprofil + fugeblikk i vegg/gulv-overgang (65 lm)
  └─ F7g Støpe bunnplate vanntett betong B45, 450 mm (115 m³, LG2.1256120A)
          [Pumpbar betong — dagsvarsel + 24–48t bekreftelse]

F8: Yttervegger
  [AVHENGER av F7]
  ├─ F8a XPS kantisolasjon 50 mm mot natursteinsmur (innvendig, høykant)
  ├─ F8b Plast/tett duk mot natursteinsmur (hindrer sammenheving)
  ├─ F8c Ensidig forskaling mot natursteinsmur (110 m², LB1.4152A), h ca. 1,7m
  ├─ F8d Armere yttervegger (B500NC, Ø16 mm, XS3, stormflo)
  │       *** GATE G7: RIB armeringssjekk yttervegger ***
  ├─ F8e Støpe yttervegger etappe 1 (ensidig del, 52 m³, LG2.1556120A)
  ├─ F8f Tosidig forskaling over natursteinsmur (95 m², LB1.4192A)
  │       inkl. steng ved overgang naturstein/tosidig (65 lm, LB8.21312A)
  └─ F8g Støpe yttervegger etappe 2 (tosidig del, opp til bjelkelag)

F9: Delevegger og søylegjennomføringer
  [AVHENGER av F8]
  ├─ F9a Tosidig forskaling delevegger N og S (LB1.4112A / 05.9, 95 m²)
  ├─ F9b Armere delevegger (B500NC, Ø16 mm, XS3, LG4.155532A)
  ├─ F9c Svellebånd rundt søylegjennomføringer (25 stk, SF6.7121619A)
  └─ F9d Støpe delevegger (B45 m. tunge tilslag, 9–20 m³)

F10: Overflate, isolasjon, katodisk vern
  ├─ F10a Syrevaske innvendige betongvegger (295 m², LP2.1)
  ├─ F10b XPS 50 mm innvendig på natursteinsmur over gulvnivå
  ├─ F10c Rigging katodisk korrosjonsbeskyttelse (offeranode, GH8.71291)
  └─ F10d Overflatebearbeiding gulv/vegger (stålglatting/glattflate)

F11: Overgang til plan 1
  [AVHENGER av F10]
  *** GATE G8: RIB-signering av overgang til neste etasje ***
  └─ F11a Sjekk bæreevne + dokumentasjon av kjeller komplett
```

### 1.3 Parallelliseringsmuligheter

Disse aktivitetene kan kjøres parallelt uten å blokkere hverandre:

- **F0c** (søyleoppmåling) kan gjøres parallelt med **F0a/F0b** (vinterklargjøring).
- **F4** (dispensasjonsprosess) kan startes så snart **G1** (RA-befaring) er gjennomført — mens **F2b** (bjelkekutting, etter G2) pågår.
- **Prosjektering** av armerings- og forskalingstegninger hos RIB kan starte parallelt med **F1** (opprydding).
- **Betong-kontraktsavklaring** (valg av leverandør) er ikke avhengig av noen gate og kan gjøres nå.

---

## Del 2 — Risikoregister

| # | Beskrivelse | Sanns. (1–5) | Konsekvens kost (1–5) | Konsekvens tid (1–5) | Relasjonell konsekvens | Avbøtende tiltak | Ansvarlig | Trigger (fase) |
|---|---|---|---|---|---|---|---|---|
| R01 | **Setningsskader på naboeiendom** (Fjordgata 28 eller 32) under graving langs natursteinsmur | 2 | 4 | 3 | Høy — nabo kan stoppe arbeid, klage | Prøvegraving dokumenteres av arkeolog; fotodokumentasjon nabokjeller før start; setningsbolter ved mur; graving i etapper med støtting | PGL (Ole Morten) | F5 |
| R02 | **Grunnvann oversvømmer gravearbeid** — tidevann eller springflo stiger over laveste gravenivå | 4 | 3 | 4 | Lav | Dimensjoner kjellersump/lensepumpe; planlegg graveetapper etter tidevannstabell; AUV-betong for fundamentstøp | Entreprenør/utfører | F5, F6 |
| R03 | **Feil med vanntett sjikt** — støpeskjøt mellom bunnplate og vegg lekkasjer pga. monteringsfeil på svelleprofil/fugeblikk | 3 | 5 | 5 | Middels — BYA/tilskudd ikke direkte, men kostbar utbedring | SikaSwell-profil + fugeblikk Master VB2 monteres etter leverandørens anvisning; kontroll av RIB-representant ved avslutning av hvert sjikt; ikke støpe over til neste trinn uten godkjenning | RIB + utfører | F7, F8 |
| R04 | **Ustabil tørrmur raser under graving** — natursteinsmuren er ikke lim-bundet, kan få partielle ras når støttende masser fjernes | 3 | 3 | 3 | Middels — BYA (kulturhistorisk mur) | Stabilisere løse stein FØR graving; aldri grave mot murfot uten støtting; dokumenter murtilstand med foto før start; arbeids­punkt alltid fra midten utover | Ole Morten + utfører | F5 |
| R05 | **Bjelker kuttet uten RIB-signering** — noen kutter langsgående tømmerstokker før G2 (Ole Stenmo) er gitt | 2 | 4 | 3 | Høy — BYA og RA vil reagere på udokumentert inngrep; potensielt konstruktivt havari | Skriftlig arbeidsinstruks på stedet (laminert A4); sperrebånd rundt bjelkesonen; Kristian/Ain informert om at kutting = Gate G2 | Kristian (koordinator) | F2 |
| R06 | **Arkeologisk funn under graving** — menneskebein, skipsdeler, middelaldergjenstander som utløser stansplikt etter kml § 8 annet ledd | 3 | 3 | 5 | Høy — RA, BYA, fylkeskommune alle involvert; media-risiko positiv eller negativ | Avklar dispensasjon (F4) FØR graving; ha beredskapsplan (kontaktliste Sissel Ramstad Skoglund, NIKU); stopp umiddelbart ved funn | PGL (Ole Morten) | F5 |
| R07 | **Forsinket betong-levering** — pumpe­betong krever bestilling 24–48t i forveien; feil dimensjon eller konsistensklasse oppdages ved levering | 2 | 3 | 4 | Lav | Bekreft konsistensklasse S3, fasthetsklasse B45, bestandighetsklasse MF40 og kloridklasse Cl 0,10 skriftlig ved bestilling; ha kontakt hos leverandøren (Betong Øst/Unicon/Franzefoss); aldri bestill til mandag morgen | Utfører | F7, F8 |
| R08 | **Feil armering** — feil dimensjon, manglende overdekning for XS3 (saltvann), eller feil monteringsretning oppdages etter at pumpebilen er bestilt | 2 | 4 | 3 | Lav | RIB-armeringssjekk (G5, G6, G7) er bindende gate; armeringstegning fra RIB må foreligge på stedet; fotodokumentasjon av ferdig armering før bestilling | RIB + utfører | F6, F7, F8 |
| R09 | **Kald støp med sprekker** — støp under 5°C fører til ufullstendig herding, kapillarsprekker i vanntett konstruksjon | 3 | 4 | 3 | Lav | Støping kun når lufttemperatur > 5°C eller telt+varme etablert; bruk herdeplan (frosttelt, varmekabler, isolerende presenning); minimum herdetid 7 dager før nedtemperering | Utfører | F7, F8 (vinter) |
| R10 | **Ulykke i trange rom** — kjelleren har lav takhøyde (<2 m mange steder), dårlig ventilasjon, betongsag-støv, kvist- og trefall | 3 | 3 | 2 | Middels — HMS-brudd ved tilsyn | SHA-plan for kjellerarbeid; P3-støvmaske ved kapping; ventilasjon via ny kjellernedgang + kjellervindu; aldri arbeid alene i kjeller | Kristian (SHA) | F1–F11 |
| R11 | **Forsikringshull — egne folk utfører betongarbeid** — bunnplate og yttervegger utføres uten fagbrev (ansvarlig utførelse, SB); forsikring dekker ikke skade | 3 | 5 | 2 | Middels — forsikringsselskap og byggesak | Ansvarlig utførelse (SB) for betongarbeidene må meldes til kommunen; enten leies inn firma med fagbrev som ansvarlig utfører, eller begrenses egne folks rolle til ikke-strukturelle oppgaver (opplasting, transport) | Eirik (byggherre) | F6–F9 |
| R12 | **Riksantikvar-saksbehandling tar mer enn 4 uker** — NIKU-tilrådning, § 14-prosess og Trøndelag fylkeskommune kan forlenge saksbehandling til 8–12 uker | 3 | 2 | 5 | Middels — KMF-rapporteringsfrist 31.12.2026 under press | Start F4 så tidlig som mulig; søknad må være komplett (målsatte tegninger, tekstbeskrivelse) ved innsending; spor saken aktivt etter uke 4 | Eirik + PGL | F4 |
| R13 | **Tømmergjenbruk mislykkes** — kuttede bjelker er råteskadet innvendig (ikke synlig utenpå), egner seg ikke for remontasje mot kanalen | 3 | 2 | 2 | Middels — BYA forventer gjenbruk | Befar og kapp en prøvestokk; vurder tverrsnitt visuelt og med pren; ha plan for alternativt materiale (nytt rundtømmer, tilnærmet lik dimensjon) | Ole Morten | F2 |
| R14 | **Flom eller springflo under arbeid** — betongstøp som ennå ikke er herdet, oversvømmes av tidevann | 2 | 4 | 3 | Lav | Følg tidevannstabell (yr.no/se.no); ikke støpe i perioder med springflo varslet; ha lensepumpe + nødstopp-plan; tett sjikt av presenning etter støp | Utfører | F6, F7 |
| R15 | **BYA overraskes av faktisk inngrep** — Byantikvaren har per 04.09.2026 erkjent at de ikke hadde detaljkunnskap om tilstanden i kjelleren; ny overraskelse kan utløse krav om stans | 3 | 3 | 4 | Høy — BYA er tilskuddsgiver via KMF-kjeden og kan trekke anbefaling | Ferdigstill lettvekts BYA-versjon av kjellerplanen (Post 03 i møtereferat 20.10); gjennomfør BYA-orientering FØR intensivering av kjellerarbeid; inviter BYA til befaring før og etter opprydding | Eirik | F1 (umiddelbart) |
| R16 | **Katodisk korrosjonsbeskyttelse dimensjonert feil** — offeranode-systemet (GH8.71291) beregnet feil for aktuelle strømnivåer i Nidelven | 2 | 3 | 2 | Lav | Engasjer spesialist for dimensjonering og godkjenning av anodeplan; ikke inkluder i DIY-scope | Utfører (spesialist) | F10 |
| R17 | **Mangelfull dokumentasjon av eksisterende konstruksjon** — bolverk/kavlegulv ikke kartlagt fullstendig, trigger riksantikvar-krav om gransking etter § 10 | 3 | 3 | 4 | Høy — § 10-gransking er tiltakshavers kostnad, ukjent størrelse | Systematisk fotodokumentasjon og skissetegning av bolverket nå (FØR videre inngrep); Ole Mortens notat 15.08.2026 er godt grunnlag — supplement med koordinater og tegning | Ole Morten | F1 |

---

## Del 3 — RIB-signeringsmatrise

RIB i dette prosjektet er Ole Stenmo, Sivilingeniørene Harboe og Leganger AS. Alle signeringer skal være **skriftlige** (e-post med bekreftet mottak aksepteres som dokumentasjon), arkiveres i prosjektmappen og oversendes ansvarlig utfører på stedet (laminert utskrift i kjelleren).

| # | Operasjon | Hva RIB skal bekrefte | Gate-ID | Ansvarlig presentasjon | Timing |
|---|---|---|---|---|---|
| **RG-1** | Kutting av bærende langsgående tømmerstokker | Er det trygt å kutte uten midlertidig støtte? Hvis støtte kreves: spesifiser type, plassering og varighet. Kuttlengde 2–2,5 m bekreftes. | G2 | Ole Morten (kjellerplan + søyleskisse sendes RIB) | FØR Kristian/Ain starter kutting |
| **RG-2** | Demontering av tørrmur-elementer | Identifisere hvilke steinrader/partier som kan tas ned uten at murfoten destabiliseres. Spesifiser rekkefølge: ovenfra og ned, ikke undergraving | G2 (inngår i samme signering) | Ole Morten | FØR steinarbeid intensiveres |
| **RG-3** | Åpning av eksisterende vegger | Strukturell kontroll av hvilke vegger som er bærende (tverrgående betongvegger fra 1983). Oppriss av sikker åpningssekvens | Eget punkt i G2-signering | PGL | FØR hull tas i vegger |
| **RG-4** | Oppstart av graving til 3 m takhøyde (utsjakting innvendig) | Bekrefte at graveplan (etapper, skråningsprofil) ikke undergraver fundamenter eller natursteinsmur. Ref. RIB-notat: graveskråning graves rett ned til innvendig veggliv | G3 (etter dispensasjon) | Utfører (etter F4) | FØR graving under løsmasser |
| **RG-5** | Armering bunnplate — kontroll FØR støp | Overdekning (XS3, min. 50 mm), plassering og diameter (B500NC, 150 kg/m³), avstandsholdere sjekket | G6 | Utfører sender foto + skjema til RIB | Dagen før bestilling av betongpumpe |
| **RG-6** | Armering fundamenter — kontroll FØR støp | Eksponeringsklasse XS3 overdekning, sentrisk plassering av søylegjennomføring, svellebånd riktig plassert | G5 | Utfører sender foto til RIB | Dagen FØR støp |
| **RG-7** | Armering yttervegger og delevegger — kontroll FØR støp | Diametre og avstand (Ø16 mm, cc iht. konstruksjonstegning), overdekning (XS3 stormflo), svelleprofil/fugeblikk i vegge-/dekkeovergang | G7 | Utfører sender foto til RIB | FØR forskaling lukkes og betong bestilles |
| **RG-8** | Overgang til neste etasje (plan 1) | Helhetskontroll kjeller: vanntetthet, lastveier, etasjeskille dokumentert OK. Byggetillatelse fra kjeller til plan 1 | G8 | Ole Morten samler dokumentasjon | FØR arbeid rettes mot plan 1 |

### Operasjonalisering av RG-1 (langsgående tømmer — Post 05 i møtereferat)

**Bakgrunn:** Tverrgående tømmerstokker er i all vesentlighet borte. Det som gjenstår er langsgående stokker i ukjent antall — noen med potensielt bærende funksjon for plan 1-etasjeskillet.

**Fremgangsmåte:**
1. Ole Morten utarbeider en skisse over kjelleren med posisjon og dimensjon for hvert langsgående element som er igjen (dette er del av Post 04-oppmålingen).
2. Skissen sendes med kjellerplanen til Ole Stenmo, Harboe & Leganger.
3. Ole Stenmo bekrefter skriftlig for hvert element: (a) kan kuttes uten støtte, (b) krever midlertidig støtte — spesifiser, eller (c) skal ikke kuttes.
4. Kuttede stokker (etter G2) håndteres slik: kuttes til 2–2,5 m lengde, veier 200–300 kg per stokk. Droppes gjennom gulvåpning til springflo (tidsvindu ca. 4–6 timer) og flytes/transporteres langs kanal-siden. Remonteres på kanalveggen iht. BYAs anbefaling om at ytre del av stolpekonstruksjonen tilbakeføres.
5. Kristian er ansvarlig for praktisk gjennomføring. Ain kan ikke kutte bjelker alene — Kristian eller Ole Morten må være til stede.

---

## Del 4 — Materialflyt

### 4.1 Betong — innkjøp og leveranse

**Fasthetsklasse og konsistensklasse per konstruksjonsdel:**

| Konstruksjonsdel | Klasse | Bestillingsvolum |
|---|---|---|
| Fundamenter (innvendig, under grunnvann) | B45 MF40 Cl 0,10 AUV, utfkl. 3 | 40 m³ |
| Bunnplate (vanntett) | B45 MF40 Cl 0,10, utfkl. 2, pumpbar | 115 m³ |
| Yttervegger (vanntett) | B45 MF40 Cl 0,10, utfkl. 2, pumpbar | 52 m³ |
| Delevegger (innvendig, tørt miljø) | B45 M40 Cl 1,0 (tunge tilslag), utfkl. 2 | 9–20 m³ |
| Fundamenter mot elv (under vann) | B45 MF40 Cl 0,10 AUV, utfkl. 3, tidevann | volum avhenger av G4 |

**Leverandørkandidater (valg ikke tatt):**
- **Betong Øst AS** — dekker Trondheim-regionen, pumpe-tjeneste tilgjengelig
- **Unicon AS** — landets største, godt tilbud på AUV-betong
- **Franzefoss Minerals / Franzefoss Betong** — Franzefoss er allerede avfallsleverandør for prosjektet, mulig samarbeidsforhold

**Leveringstid:** Pumpebar betong bestilles med **dagsvarsel** (telefon kvelden før); men bestillingen bør bekreftes skriftlig **24–48 timer i forveien** for å sikre pumpe-ressurs. AUV-betong (under-vann-betong) kan ha lengre leveringstid — spesifiser ved forespørsel.

**Kritisk:** Betong må bestilles ETTER at RIB-armeringssjekk er fullført (G5/G6/G7). Konsekvens: plan alle tre kontroller for samme uke som støpen — ikke vent med RIB-kontroll til samme dag som pumpebilen er bestilt.

### 4.2 Stein og bjelker — interntransport og mellomlagring

**Steinhåndtering:**

Naturstein fra tørrmuren (og eventuelle løse stein i kjelleren) veier typisk 20–80 kg per stein. Håndtering krever ergonomisk tilnærming (ikke kast — legg).

**Mellomlager A — primær:** Utenfor Fjordgata-inngang, gangarealet ut mot gate. Containere settes ut og hentes ved behov (jf. NS 3420-post FM1.2329A). Fordel: kort transportvei opp via eksisterende kjellernedgang. Ulempe: blokkerer delvis gangvei, krever tillatelse fra kommunen for midlertidig lagring på fortau.

**Mellomlager B — sekundær, for gjenbruksstein:** Innenfor kjelleren, langs sørmur (kanalsiden), frem til BYA/RA har bestemt hvilke steiner som skal bevares og remonteres. Gjenbruksstein merkes med spray (rød = kast, grønn = gjenbruk). Studenter kan flytte stein fra aktiv graveflate til mellomlager B.

**Mellomlager C — for kuttede bjelker (floa):** Bjelker som kuttes i F2b, droppes gjennom gulvåpning i planke-sone mot kanalsiden, samles på floa (lekter/brygge) og remonteres der. Tidsvindu styres av springflo-tabell. Alternativt mellomlagres kuttede bjelker flatt på kanalbakken (utvendig) frem til remontasje.

**Bjelkemerking:**
- Alle gjenstående tømmerstokker befares av Ole Morten FØR kutting (Post 04-oppmåling).
- Merking: nummerert etikett (hvit spray på treverk + hengelapp) med posisjon (akse A1, A2 etc. fra et fast referansepunkt — nordøst-hjørne kjeller) og status: KUT (kan kuttes etter G2), BEV (bevares), UKL (uklart — avventer RIB).
- Fotodokumentasjon av merket bjelke FØR kutting.

**Bjelkekutting:**
- Kuttelengde: 2–2,5 m (spesifisert i referatets Post 05), tilpasset transport gjennom gulvåpning.
- Vekt per stokk: ca. 200–300 kg (jf. referat). To mann og talje kreves for kontrollert senking.
- Kappested: på stedet i kjelleren, rett ved gulvåpningen mot kanalsiden.
- Verktøy: kjedesag (støv- og støyskjerming), sperring av areal under.

### 4.3 Masseflytting — løsmasser

**Estimert volum:** ca. 130 m³ (post 03.1, regulerbar mengde).

**Karakter av masser:** Eldre elveavsetninger av sand, blandet med grus og mindre stein (jf. Ole Mortens notat 16.08.2026). Kan inneholde kulturhistoriske masser og gjenstander — arbeidsinstruksen krever at arkeolog er orientert.

**Viktig:** Masseflytting med graving i faste masser er blokkert av G3 (dispensasjon § 8). Studenter kan flytte løse masser (jord i hauger, sand som allerede er omrørt) uten å aktivere dispensasjonskravet, men dette avklares eksplisitt med Riksantikvaren under befaring.

**Containerlogistikk:** Containere settes i Fjordgata (kort containere, 10 m³). Tillatelse fra Trondheim kommune for midlertidig plassering må innhentes av byggherre. Containere hentes og bytter ved behov. Det antas at henting/bytte ikke kan gjøres på søndager — planlegg avslutning av gravedag til fredag for tømming.

**Avhending:** Massetypen er sannsynligvis «rene masser» (elvegrus), men kan inneholde kulturhistorisk organisk materiale. Leveringssted for masser er opp til entreprenør (NS 3420, post 03.5). Arkeolog kan kreve at masser sorteres/avleveres til NIKU for sålding ved funn av gjenstander.

### 4.4 Avhending — øvrige materialer

| Material | Mengde (anslag) | Håndtering | Leverandørkandidat |
|---|---|---|---|
| Gammel isolasjon (mineralull) | ~1–2 m³ | Gjenbrukes som nedforing 1. etg (Post 09, referat 20.10) | — |
| Elektriske installasjoner fra kjeller | Liten | Container elektrisk (Franzefoss) | Franzefoss Gjenvinning |
| Trevirke (ikke gjenbruksbjelker) | Variabel | Container tre (Franzefoss) | Franzefoss Gjenvinning |
| Kulturhistoriske gjenstander | Ukjent | Avleveres til arkeolog/NIKU | NIKU |

---

## Del 5 — Kartlegging av gjenværende tilstand

### 5.1 Hva gjenstår å registrere (per 21.10.2026)

**Gulvplanker:**
- Innerste del mot Fjordgata: gulvplank delvis fjernet (jf. Ole Mortens notat og Kristian 05.10).
- Kanalsiden/foran landkaret: kavlegulv delvis intakt (jf. Ole Mortens notat 15.08.2026).
- Mangler: eksakt kartlegging av hvilke felt som har gulvplank vs. åpent vs. løsmasse.

**Løse stein / ustabil tørrmur:**
- Hjørnet mot Fjordgata 28 og gata: markert for prøvegraving (avklart BYA, 05.10.2026).
- Tørrmur mot kanalen: tømmerfjerning igangsatt pr. 05.10.2026 — tilstand av mur etter fjerning er ikke dokumentert.
- Mangler: foto + skisse over murens tilstand etter tømmerfjerning (sprekker, løse partier, utbulinger).

**Løsmasser:**
- Jord og grus innenfor natursteinsmuren: omrørt i flere omganger siden 1800-tallet (jf. notat 15.08).
- Mangler: kartlegging av massetykkelse og -karakter i felt (prøvegraving F3a gir dette).

**Bjelker som allerede er kappet:**
- 1983-ombyggingen kappes en del av bolverket (jf. notat, Bilde 2).
- Mangler: systematisk oversikt over hvilke langsgående stokker som er kappet i 1983 vs. intakte.

**Søyler — oppmåling (pågår 21.10.2026):**
Ref. Post 04 i møtereferat: Ole Morten måler onsdag 21.10 med 10 cm toleranse.

| Søylerad | Material | Status |
|---|---|---|
| Innerst mot Fjordgata | Stål (HUP 150×150×5, jf. RIB-notat) | Oppmåling pågår 21.10 |
| Midtre søyler | Tre/betong — varierer | Mangler kartlegging |
| Ytre søyler (mot kanal) | Tre, råteskadede (jf. RIB-notat 10.02.2026) | Registrert i notat, men ikke koordinatfestet |
| Betongfundamenter (1983) | Betong, delvis uten forskaling | Mangler skadeomfang-vurdering |

### 5.2 Figurer / foto som må produseres FØR planen er komplett

Disse punktene er blokkerende for videre planarbeid og for dispensasjonssøknaden:

1. **Foto: tilstand tørrmur etter tømmerfjerning** — alle fire veggsider, oversiktsfoto og detaljer for sprekker/utbuling.
2. **Foto: bolverk og kavlegulv — fulldekkende** — systematisk rutenett (hvert 2. m²), med lys nede i undergulvet.
3. **Skjema: søyleoversikt** — etter Ole Mortens oppmåling 21.10. En rad per søyle: akse, posisjon (X/Y fra hjørne), materiale, synlig skade, fundament-type.
4. **Foto: fundamenter 1983** — hvert fundament som er synlig, med målestav.
5. **Foto: langsgående tømmerstokker som gjenstår** — ovenfra og fra siden, med målestav og nummeretikett.

---

## Del 6 — Vinterklargjøring og tilrettelegging

Basert på Post 07–09 i møtereferat 20.10.2026 og statusoppdatering 16.10.2026.

### Hva må på plass FØR kjellerarbeid intensiveres

**Prioritet 1 — umiddelbart (blokkerer kjellersikkerhet og HMS):**

| Tiltak | Beskrivelse | Ansvarlig | Status |
|---|---|---|---|
| Varm sone i 1. etg | Flytte toalett og minikjøkken fra 2. etg til 1. etg. 2 panelovner, OSB-plater, stendere, isolasjon. | Kristian + Ain | Ikke startet per 20.10 |
| Frostfritt vann | Rørlegger samler og sikrer vann til varm sone. Varmekabler på eksponerte rør. | Kristian + rørlegger | Planlagt |
| Vannsikringsnotat | Kortfattet notat som dokumenterer frosttiltak (forsikringsdokumentasjon). | Kristian | Ikke startet |
| Ny kjellernedgang | Fra 1. etg (der kjøkkenet sto) ned til kjeller mot kanalsiden. Gir rymningsvei nr. 2 og materialvei. | Kristian + Ain | Planlagt |

**Prioritet 2 — før betong-arbeider starter:**

| Tiltak | Beskrivelse | Ansvarlig | Status |
|---|---|---|---|
| Flytte kjellertrapp | Fra sikringsskap-sonen til ny posisjon (kjøkken-siden). Frigjør arbeidsflate og rydder sikkerhetssone. | Kristian + Ain | Planlagt |
| Belysning nede | Permanent lyslenke i kjelleren (allerede startet 05.10). Utbedre til 360° dekning for betongarbeider. | Kristian | Delvis utført |
| Ventilasjon | Under betongstøp: betongpumpe produserer avgasser. Sørg for åpning mot to sider (Fjordgata + kanal). | Utfører | Avventer plan |

**Prioritet 3 — sesongforsikring (vintersortiment):**

- Frosttelt / presenning over støpte flater under herding.
- Isolerende matter over fersk betong ved frost.
- Lensepumpe (min. 500 l/min) for tidevann-hendelser under og etter støp.

---

## Del 7 — Grov fremdriftsplan (Gantt-ukenivå)

Basert på situasjonen per uke 43 (21.10.2026). Kritisk sti er markert med **[KS]**.

```
Uke    43    44    45    46    47    48    49    50    51    52    1-4
       okt  nov  nov  nov  nov  nov  nov  des  des  des  jan-27

F0a-c  ████
(klargjøring, søyleoppmåling)

RIB-
presentasjon       ██
(G2-forberedelse)

G2 (RIB-signering  ██
tømmer/tørrmur)

F2b (kutting           ████
bjelker etter G2)

G1 (RA-befaring)        ██    [KS]
Avhenger: F1a ferdig

F4a (tegnings-              ████████
underlag for søknad)

F4b (søknad § 8)                    ██  [KS]

F4c (saks-                           ████████████  [KS]
behandling 4+ uker)

F0b (ny kjeller-   ████
nedgang, vinter)

F5 (utsjakting)                                          ████████ [KS]
(avhenger G3)

F6 (fundamenter                                              ████ [KS]
støp i vann)

F7 (bunnplate                                                    ████
armering + støp)

F8 (yttervegger)                                                     →2027
```

**Kritisk sti:** G1 (RA-befaring) → F4b (søknad) → F4c (4+ uker saksbehandling) → G3 → F5 (graving).

**Konsekvens:** Graving i faste masser tidligst uke 51–52 2026 **IF** befaring gjennomføres uke 44–45 og søknad sendes umiddelbart etter. Mer realistisk: graving starter januar 2027. Dette er under tidspress mot KMF-rapporteringsfrist 31.12.2026 — ferdigstillelse av kjeller vil gå utover 2026.

**Hva kan gjøres i 2026 under fristen:**
- F0: vinterklargjøring, søyleoppmåling (innen uke 44)
- F2: bjelkekutting etter G2 (uke 44–45)
- G1 + G2: parallelt
- F4: tegningsunderlag og søknadsinnsending (uke 46–48)
- Dokumentasjon for KMF: framdriftsrapport som viser at dispensasjonsprosessen er igangsatt, befaring gjennomført, søknad sendt.

---

## Del 8 — Figur-placeholders

Følgende figurer er nødvendige for å ferdigstille prosjektunderlaget. De beskrives presist nok for manuell tegning eller ChatGPT-generering. Formater som PNG/SVG egnet for innlimming i leveranser til BYA, RA og bank.

---

**Figur 1 — Plantegning kjeller (ovenfra), nåværende tilstand**

*Perspektiv:* Vertikalt ovenfra, nord opp.\
*Målestokk:* 1:50 (A3-format).\
*Innhold:*
- Yttervegger og natursteinsmur (med distinkt signatur for naturstein vs. betong vs. tre).
- Alle søyler med materiale-etikett (stål S, tre T, betong B) — posisjon fra Ole Mortens oppmåling 21.10.
- Eksisterende fundamenter fra 1983 (stiplet der de ikke er synlige).
- Tørrmur mot kanalsiden (naturstein, ukjent stabilitet).
- Åpne felt (der gulvplank er fjernet).
- Felt der kavlegulv/bolverk fortsatt er intakt.
- Mellomlager A (Fjordgata-siden) og mellomlager B (kanalsiden) inntegnet.
- Nord-pil, grafisk målestokk, dato for registrering.

---

**Figur 2 — Snitt langsgående (A-A), fra Fjordgata til kanalsiden**

*Perspektiv:* Vertikalt snitt i byggets lengderetning, sett mot syd.\
*Innhold:*
- Natursteinsmur (tverrgående mur ~2/3 fra gata) med eksisterende og prosjektert topp-nivå.
- Kavlegulv/bolverk innenfor muren (søndre del) og uten (nordre del mot kanal).
- Prosjektert bunnplate (kote-angivelse, 450 mm tykkelse).
- Eksisterende søyler med fundament-dybde (anslått).
- Tidevannsprofil (dimensjonerende kote +3,20, normal floa, normal fjøre).
- "Vektergang" mellom ny betongvegg og yttervegg.
- Ny kjellernedgang (F0b) plassert.
- Nord-pil, grafisk målestokk.

---

**Figur 3 — Snitt tverrgående (B-B), midt i kjelleren**

*Perspektiv:* Vertikalt tverrsnitt, sett mot vest.\
*Innhold:*
- Bredde kjeller (ca. 8–9 m fra innerliv til innerliv).
- Natursteinsmur begge langsider.
- Prosjektert bunnplate med armering prinsipp.
- Yttervegger etappe 1 (ensidig mot naturstein) og etappe 2 (tosidig over naturstein).
- Eksisterende etasjeskille kjeller/plan 1 (øverst i snitt).
- XPS-isolasjon posisjon (vertikalt langs mur).
- Radon-/fuktsperre under platen.
- Grafisk målestokk, nord-indikator.

---

**Figur 4 — Prinsippsnitt ny betongvegg mot naturstein (detaljert)**

*Perspektiv:* Vertikalt snitt 1:10, kun vegg/gulv-overgangen.\
*Innhold (lag-for-lag, nedenifra og opp):*
- Eksisterende masser / drenslag 16/32 / forsterkningslag 0/4.
- Radon-/fuktsperre (plastbelegg, oppkant langs mur).
- XPS 50 mm under plate (kantforankring).
- Bunnplate B45, 450 mm, med armering prinsipp.
- Svelleprofil (SikaSwell P Type H) + fugeblikk (Master VB2 160) i støpeskjøt vegg/gulv.
- XPS 50 mm vertikalt langs natursteinsmur (kantisol.).
- Plast-/tett duk som separasjonssjikt (hindrer samheftning).
- Ensidig betongvegg (innerliv mot rom), med innvendig forskalingsflate.
- Natursteinsmur (ytre forskalingsflate for nedre del av vegg).
- Tekst-forklaring per lag med produktreferanser.

---

**Figur 5 — Formsettingsplan i rekkefølge (etappe 1 → 2 → 3)**

*Perspektiv:* Tre separate plantegninger (1:100) med seksjonsfargelegging.\
*Innhold:*
- Etappe 1: ensidig forskaling langs alle fire yttervegger, fra drenslag til topp natursteinsmur. Rødt felt.
- Etappe 2: tosidig forskaling over natursteinsmur, fra topp naturstein til bjelkelag. Blått felt.
- Etappe 3: delevegger nord og syd (interne delelinjer). Grønt felt.
- Rekkefølge-pil mellom de tre tegningene.
- Støpeskjøt markert med dobbelstrek.

---

**Figur 6 — Mellomlagringsplan for stein og bjelker**

*Perspektiv:* Oversiktsfoto-basert skisse (planfragment Fjordgata 30 + uteareal), ikke i målestokk.\
*Innhold:*
- Mellomlager A (Fjordgata, container-plassering).
- Mellomlager B (innvendig, langs sørmur kjeller).
- Mellomlager C (floa/lekter, kanalsiden, kuttede bjelker).
- Piler som viser materialflyt fra graveflate til container.
- Bjelketransport-rute: gulvåpning → floa → kanal-lager.

---

**Figur 7 — Materialflytskisse (flytdiagram)**

*Perspektiv:* Lineært flytskjema, ikke geografisk.\
*Innhold (bokser og piler):*
- Input: løsmasser fra graving → silt / elvegrus → container → Franzefoss.
- Input: stein (tørrmur) → mellomlager B → gjenbruk kanal / container.
- Input: langsgående bjelker → kapping → mellomlager C → gjenbruk kanalvegg.
- Input: isolasjon → gjenbruk 1. etg.
- Input: elektrisk → container el → Franzefoss.
- Bifurkasjon ved kulturhistorisk gjenstand: avlevering NIKU.

---

## Del 9 — Åpne spørsmål som blokkerer videre fremdrift

Disse tre spørsmålene må lukkes FØR entreprenør kan prise eller egne folk kan starte graving/betongarbeider:

**1. Hvem er ansvarlig utfører (SB) for betongarbeider?**
Bunnplate, yttervegger og delevegger krever ansvarlig utfører med fagbrev for betongarbeider meldt til kommunen. Prosjektet mangler per nå slik deklarasjon. Alternativer: (a) leie inn firma med sentral godkjenning for betong (utf.kl. 2/3) som ansvarlig utfører, og bruke egne folk som hjelpere; (b) Kristians firma KMTE tar ansvarlig utfører-rollen hvis de er godkjent. Dette påvirker også forsikringsdekning (R11) og KMFs krav om dokumenterbar fagutførelse. **Ansvarlig for avklaring: Eirik.** Frist: FØR F6 starter.

**2. Hva er det eksakte graveomfanget, og er det besluttet å grave til 3 m takhøyde overalt?**
Dispensasjonssøknaden (F4) krever målsatte tegninger av nøyaktig graveomfang (krav fra Riksantikvaren, 24.09.2026). Det er ikke tatt en eksplisitt beslutning om graveomfang: skal hele kjelleren graves til 3 m takhøyde, eller kun nordre del (mot kanal, lavere naturstein-mur)? Svaret påvirker volumet (130 m³ er anslaget), kostnaden, og risikoen for arkeologisk gransking etter § 10. Uten beslutning kan hverken tegningsunderlag eller søknad ferdigstilles, og RA-befaringen (G1) gir ikke maksimal effekt. **Ansvarlig for avklaring: Eirik + Ole Morten + Ole Stenmo.** Frist: FØR G1-befaring.

**3. Hva er status på Riksantikvar-befaring — er tidspunkt foreslått?**
Dispensasjonsprosessen starter med at Riksantikvaren (Sissel Ramstad Skoglund) holder befaring på ryddet kjeller. Uten et bekreftet befaringstidspunkt er det ikke mulig å sette realistiske datoer på F4b (søknad) og G3. Per 21.10.2026 er det ikke bekreftet at kjelleren er tilstrekkelig ryddet for befaring, og dato er ikke foreslått. Hvert uke uten befaring skyver graving (F5) og betong (F6–F8) minst en uke. **Ansvarlig: Eirik.** Handling nå: kontakt Sissel Ramstad Skoglund og foreslå dato uke 44–45 (27.10–07.11.2026), forutsatt at Ain/Marcus fullfører opprydding i løpet av uke 43.
