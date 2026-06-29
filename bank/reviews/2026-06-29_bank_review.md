---
title: "Multi-agent rolle-review av bankpakken – Fjordgata 30"
author: "Generert 2026-06-29"
subtitle: "Intern kvalitetssikring før utsending"
---

# Rolle-review av bankpakken

Dette dokumentet samler vurderinger av bankpakken fra syv simulerte bank-roller, gjennomført som parallell agent-kjøring 29.06.2026. Formålet er å avdekke svakheter før pakken sendes til reelle banker (Nidaros Sparebank, DNB, Trønderbanken).

**Caveat:** Agentene er LLM-er som imiterer rollene basert på allmenn kunnskap om norsk bankpraksis – ikke faktiske bankspesialister med 20 års erfaring. Bruk vurderingene som idégrunnlag, ikke som autoritativ kritikk.

---

## 1. Sammendrag og rangering

**Gjennomsnittlig helhetsrating: 5,7 / 10**

| Rolle | Helhetsrating | Tone |
|---|---:|---|
| Kunderådgiver / Bedriftsrådgiver | 7/10 | Pakken kan sendes, men kjerne-asken må strammes opp |
| Kredittanalytiker | 5/10 | Driftsøkonomien for tynt fundert; base-case er hele caset |
| Kredittsjef / Kredittkomité | 6/10 | Mye å lese for et smalt prinsippspørsmål; inkonsistens vil dominere møtet |
| Risk officer | 5/10 | Énvariabel stresstest; sektor/motpartsrisiko mangler |
| ESG- / Grønt lån-rådgiver | 6/10 | Tallene sitter, men DNSH og energiattest-prosessen mangler |
| Jurist / Legal counsel | 6/10 | Juridisk overselgende på EBA-referanser; fisjonsstruktur underbelyst |
| Næringseiendomsspesialist (CRE) | 5/10 | Verdsettelse og EBITDA-margin for offensive for ny aktør |

### Per-dokument rating (gjennomsnitt på tvers av roller)

| Rang | Dokument | Snitt | Spredning |
|---:|---|---:|---|
| 1 | 08 Energirapport (HRP) | **8,3** | 8–9 |
| 2 | 07 Grønt lån – kriteriedokument | **7,4** | 7–8 |
| 3 | 05 Støtteoversikt | **7,0** | 6–8 |
| 4 | 03 MVA-strategi | **6,7** | 3–8 (ESG ga 3, ikke deres felt) |
| 5 | 02 Finansieringsplan | **6,3** | 5–7 |
| 6 | 00 Bankhenvendelse | **6,1** | 6–7 |
| 7 | 06 Tilskudd som EK | **5,9** | 2–8 (ESG ga 2, ikke deres felt) |
| 8 | 04 Konkurrent og marked | **5,6** | 3–8 |
| 9 | 01 Forretningsplan | **5,4** | 4–7 |

**Mønster:** Tredjepartsdokumentasjon scorer høyt (energirapport, grønt lån-kriterier). Egne strategiske dokumenter (forretningsplan, konkurrentanalyse) scorer lavest. Det er fordi flere agenter mener at driftsantakelser, prisantakelser og verdsettelse er for offensive og for tynt benchmarket.

---

## 2. Gjennomgående styrker (på tvers av roller)

1. **Tredjepartsdokumentasjon er sterk.** Energirapport fra HRP (NS 3031:2025, Simien Pro, navngitt rådgiver) gir robust grunnlag. Grønt lån-mapping mot DNB V.5.1 og EU-taksonomi 7.2 er metodisk solid.
2. **Sensitivitetsanalyser er bankvennlig presentert.** Tre scenarier for tilskudd, BFU-utfall som egen tabell, kombinert worst case (LTV 87,5 %) – flere roller fremhever at dette signaliserer modenhet.
3. **Kvartalsvis kontantstrøm gjennom byggefasen.** Risk og kredittanalytiker setter pris på at toppkapitalbehov Q2–Q3 2027 er eksplisitt synlig – det er drawdown-egnet for byggelånsdimensjonering.
4. **Korrekte lovreferanser i MVA-strategi.** §§ 2-3, 3-1, 3-11, prinsipputtalelse 18.11.2014 og SKNS1-2020-134 er presist sitert.
5. **Tilsagnsbrev-referanser er konkrete og verifiserbare.** Saksnummer, datoer, kontaktpersoner per ordning – jurist og kredittsjef sier banken kan ringe Byantikvaren direkte for verifikasjon.
6. **Klar oppfyllelses-tabell mot DNBs rammeverk** med margin (53 % vs. 30 %-krav, G→D vs. minimum D).

---

## 3. Gjennomgående svakheter (på tvers av roller)

Sortert etter hvor mange roller som flagget den:

| # | Svakhet | Roller som flagget |
|---|---|---|
| 1 | **«Realistisk base» inkluderer ikke-innvilgede tilskudd som om de var nær-sikre.** Bare 2,25 MNOK er bevilget; resten er søknader. LTV-bildet blir kunstig pent | Kred, Sjef, Risk, Jur, CRE |
| 2 | **EBA/GL/2020/06 overselger.** Retningslinjene anerkjenner ikke eksplisitt tilskudd som «EK-ekvivalent» – det er tolkning. Modér til «kan inngå som reduksjon i bankens nettoeksponering» | Kund, Jur, CRE |
| 3 | **Inkonsistente tall på tvers av pakka** – LTV (55/56/58/60 %), tilskuddsbase (8,0 vs. 7,7–8,2), egenkapital (1,5 vs. 2–3 MNOK), verneklasse (B vs. C), total prosjektkostnad (6–15 vs. 30 MNOK) | Sjef, ESG, Jur, CRE |
| 4 | **KMF/BYA endringsmelding (kontor → minilager) er «svar avventes».** Materiell tilbakekallsrisiko som ikke flagges som risiko – tilskuddene ble gitt til en annen bruk | Sjef, Risk, Jur, CRE |
| 5 | **TBRT-dagbøter ikke åpent kommunisert i pakka.** Inkonsistens at TBRT også gir «anbefalingsbrev» blir lagt merke til ved due diligence | Sjef, Risk, Jur, CRE |
| 6 | **EBITDA-margin 64 % er urealistisk høy** for full-service med varebil/sjåfør/plattform. Bransjenorm 35–50 % (Vinden, Shurgard, Clutter) | Kred, CRE |
| 7 | **Eiendomsverdi 50 MNOK ved cap rate 6,0 % er offensivt** for ny aktør / single-asset SPV. Realistisk 7,5–8,5 % gir 35–40 MNOK – realistisk LTV blir 70–75 %, ikke 58 % | Sjef, CRE |
| 8 | **Worst case 87,5 % LTV uten kvantifisert mitigering** – ingen aksjonærgaranti, cost-overrun-fasilitet eller pant utenfor objektet | Kred, Sjef, Risk |
| 9 | **DSCR/rente i byggefasen ikke modellert.** Kapitalisert rente ~2 MNOK i 12–15 mnd; DSCR år 1 sårbar | Kred, Risk |
| 10 | **Uforutsett 10 % er stramt** for 1857-bygg med råte og fundamenteringsusikkerhet. Bransjenorm 15–25 % | Kred |
| 11 | **Fisjonsstruktur underdokumentert** – ikke datert fisjonsplan, kreditorvarsel etter asl. kap. 14, eller hvordan eksisterende 15,5 MNOK panthaver håndteres ved debitorskifte | Sjef, Jur, CRE |
| 12 | **Pant i tilskuddsrettigheter forutsetter transportabilitet** – KMF, Enova, UNI har vilkår som kan begrense pantsettelse uten samtykke | Jur |
| 13 | **53 %-beregningsbasen i HRP-rapporten** er mot referansebygg (427 000 kWh), ikke byggets opprinnelige ytelse (252 000 kWh). DNB V.5.1 og taksonomi 7.2 krever sistnevnte | ESG |
| 14 | **DNSH-vurdering mangler.** Vann (Nidelva-nærhet), klimatilpasning (flom), sirkulær økonomi (Enova ombruk – ubrukt!), biologisk mangfold | ESG |
| 15 | **Energiattest fra registrert energirådgiver mangler.** Energikartlegging ≠ energiattest. DNB V.5.1 krever sistnevnte | ESG |
| 16 | **Belegg-banen er aggressiv** – 60/50 % allerede år 1 uten lease-up-periode. Bransjenorm 18–30 mnd til 60–70 % | Kred, CRE |
| 17 | **Markedsabsorpsjon ikke dokumentert** – ingen LOI/pre-booking; «hundrevis av leiligheter innen 250–350 m» er spekulativt | CRE |

---

## 4. Prioritert handlingsliste

Konsolidert på tvers av rolle-anbefalingene. Sortert etter konsensusgrad og bank-impact:

### Høyeste prioritet – må rettes før utsending

1. **Skill bevilget tilskudd (2,25 MNOK) fra under-søknad i base-LTV-beregningen.** Vis basis med kun bevilget støtte, og legg høy-sannsynlighets-tilskudd som oppside. Realistisk base-LTV vil da være ~65–70 %, ikke 58 %.
2. **Modér EBA/GL/2020/06-formuleringene** fra «anerkjennes som EK-ekvivalent» til «kan tas i betraktning som reduksjon i nettoeksponering». Gjør samme endring i 00, 02 og 06.
3. **Rens opp tallinkonsistens på tvers av pakka.** Spesielt: verneklasse (B vs. C), egenkapital (1,5 vs. 2–3 MNOK), total prosjektkostnad (6–15 vs. 30 MNOK i støtteoversikt-tabellen), LTV-prosenter.
4. **Adresser KMF/BYA endringsmelding eksplisitt.** Be om skriftlig bekreftelse før utsending, eller flagg som risiko med kvantifisert tilbakekallseksponering.
5. **Legg til DSCR-bane år 1–5 med rentekostnad i byggefasen.** ~28–30 MNOK × 6,5 % × 1,25 år ≈ 2,3 MNOK kapitalisert rente. Vis når DSCR ≥ 1,3 oppnås.

### Middels prioritet – styrker pakken vesentlig

6. **Avklar fisjonsstruktur og personlig/morselskaps-garanti.** Datert fisjonsplan, kreditorvarsel-prosess, og om Eirik Larsen / KodeWorks Eiendom AS stiller garanti.
7. **Re-baselin EBITDA-margin med realistisk driftskost.** Legg til 0,8–1,2 MNOK for full-service-bemanning/varebil/IT. EBITDA-margin 45–55 % er forsvarbart; 64 % er ikke det.
8. **Innhent indikativ uavhengig takst** (Newsec, Akershus Eiendom el.) eller juster cap rate til 7,5 % i base-case for å reflektere ny aktør.
9. **Konkretiser uforutsett til 15–20 %** (4,5–6 MNOK) – ikke 10 %.
10. **TBRT-saken adresseres åpent i bankhenvendelsen.** To setninger om dagbøter (bestridt) + status i tilsynssaken. Bedre at dere eier narrativet enn at banken oppdager det selv.

### Lavere prioritet – kvalitetshevninger

11. **Få utstedt energiattest** for nå-tilstand og prosjektert post-rehab fra registrert energirådgiver.
12. **Be HRP om tilleggsnote** som dokumenterer 53 %-reduksjonen mot byggets opprinnelige ytelse (kWh/m²/år), ikke kun mot referansebygg.
13. **Legg til DNSH-vedlegg** for taksonomi 7.2 – alle seks miljømål. Enova ombrukskartlegging er ubrukt potensial her.
14. **Bygg en bottom-up markedsabsorpsjon-modell** for Trondheim sentrum – ikke ekstrapoler fra Skandinavia-data. Helst med 5–10 LOI fra forhåndskunder.
15. **Komprimér juridiske vedlegg (03, 06)** til 2–3 sider med fullversjon på forespørsel. Signaliserer prioriteringsevne.

---

## 5. Rolle-vurderinger i sin helhet

Under følger hver agent sitt fulle svar (uredigert).

---

## Kunderådgiver / Bedriftsrådgiver

**Helhetsvurdering av pakken:** 7/10
**Kort begrunnelse:** Pakken er uvanlig grundig og profesjonelt skrevet for å være en kundepresentert sak – jeg kan trygt sende den til kredittkomiteen. Men kjernen er begravet under for mye juss og finlirsanalyse, "anmodningen" er for innelukket og forsiktig, og noen sentrale tall (drifts-EBITDA mot 28–30 MNOK gjeld, byggekostnad-spennvidde, EK-utløsning fra fisjonen, sponsor-CV) gir komiteen materielle oppfølgingsspørsmål jeg ikke kan svare på alene.

### Per dokument

| Dokument | Rating | Styrker | Svakheter |
|---|---|---|---|
| 00 Bankhenvendelse | 6/10 | • God struktur og høflig tone – fungerer som en reell oppvarmer<br>• Tydelig signal om at det er gjort hjemmelekser (forretningsplan, MVA, BFU, konkurrentanalyse, energi)<br>• Henviser konsekvent til vedlegg uten å gjenta alt | • "Konkret anmodning" gjelder bare en prinsippvurdering av tilskudd som EK – dette er en mikrosak å selge inn en 30 MNOK-ramme på, og forvirrer komiteen om hva de egentlig blir bedt om<br>• Mangler én-siders "ask": ramme, formål, sikkerhet, LTV, DSCR, repaymentprofil, sponsor og tidshorisont<br>• Beløpet 30 MNOK står ikke i følgebrevet – komiteen må grave i finansieringsplanen for å forstå størrelsen |
| 01 Forretningsplan | 7/10 | • Solid og internt konsistent: konsept, marked, prising, MVA, drift og risiko er gjennomarbeidet<br>• Konkurranseargumentene (sentralitet, Nidelv, full-service, krypkjeller) er differensierte og troverdige<br>• Klar break-even (36 %) og EBITDA-trapp som er enkel å peke på i komitéen | • Driftskostnader (1,6 MNOK) virker lavt sammenlignet med en valet-modell med varebil, sjåfør, fotografering, app, forsikring og henting/levering – komiteen vil spørre hvorfor personell kun er 0,5 MNOK<br>• EBITDA stab. 3,0 MNOK mot gjeld 28–30 MNOK gir DSCR-ratioer som ikke vises – ved 5 % rente og 25 års nedbetaling er gjeldstjenesten alene ~2,0 MNOK, så marginen er tynnere enn fortellingen antyder<br>• Byggekostnad 30 MNOK er spennvidder-styrt (8–12, 3–5 osv.) uten anbud/kontraktstrategi – komiteen vil etterspørre RIB-rapport og totalentreprenør |
| 02 Finansieringsplan | 7/10 | • Tre-scenario-tabell med LTV-utregninger er akkurat slik komiteen liker det presentert<br>• Worst case er eksplisitt kalkulert (LTV 87,5 %) – det viser modenhet og at byggherre ikke skjuler nedsiden<br>• Kontantstrømtabell pr. kvartal gjør at jeg kan dimensjonere trekkrammen mot toppbelastning, ikke slutt-LTV | • Eiendomsverdi 50 MNOK er prosjektets egen cap-rate-kalkyle (6 % på 3,0 MNOK EBITDA) – en uavhengig takst mangler, og LTV-historien står og faller på den<br>• "Realistisk base" inkluderer 5,4–5,9 MNOK i ikke-innvilgede tilskudd – det gir for optimistisk LTV-bilde i basisscenario; komiteen vil insistere på at kun bekreftede 2,25 MNOK regnes inn<br>• Sikkerhetsstrukturen er kun skisseaktig ("1. prioritets pant + pant i tilskuddsrettigheter") – det mangler kausjon fra sponsor, morselskapsgaranti, completion guarantee og cost overrun-garanti, alle ting komiteen vil kreve |
| 03 MVA-strategi | 8/10 | • Solid juridisk analyse med korrekte lovreferanser (§ 2-3, § 3-1, § 3-11), Skattedirektoratets 2014-uttalelse og Vinden som markedsbenchmark<br>• Hybridmodellen (Alt D) er klokt valgt – og fallback til ren passiv utleie er beskrevet eksplisitt<br>• Kvantifisering av 7,5 MNOK MVA-effekt er konkret og treffer komiteens interesse | • Komiteen vil ikke forstå dybden av analysen – burde vært komprimert til en 1-siders BFU-status med sannsynlighet og likviditetseffekt<br>• Forholdet 95 % MVA-dekning i hybridmodellen (30 % B2B + 70 % full-service) forutsetter at det leies ut nøyaktig slik fra dag én – sensitivitet på utleiemiks mangler<br>• Justeringsplikten over 10 år (§ 9-4) nevnes i risikotabellen, men ikke kvantifisert mot lånets løpetid – komiteen vil spørre om dette ved senere bruksendring |
| 04 Konkurrent og marked | 8/10 | • Eksepsjonelt grundig prisinnhenting med datoer og kilder per konkurrent – dette er sjelden kost fra en SMB-låner<br>• Sentralitetsargumentet og premium-prismål er kvantitativt underbygget (Stortrack 2025) og virker forsvarlig<br>• Avstandstabellen mot Torget og analyse av Nye Trondheim S/Nyhavna gir konkret etterspørselsdrivere | • Markedsstørrelse for Trondheim spesifikt mangler – nasjonale tall (Statista, CBRE) er ikke nedbrutt til adresserbart marked i Trondheim sentrum<br>• Belegg-forutsetninger (85–90 % stabilisert) er ikke benchmark mot konkurrentenes faktiske belegg – komiteen vil spørre om Trondheim Minilager med 500 boder er full eller halvfull<br>• Ingen sensitivitet mot prisfall: hva skjer hvis 123 Minilager eller en ny aktør dumper pris til 200 kr/kvm/mnd? |
| 05 Støtteoversikt | 8/10 | • Tilsagnsbrevreferansene (saksnumre, datoer, kontaktpersoner) er konkrete og verifiserbare – komiteen kan ringe Byantikvaren direkte<br>• Utbetalingsmekanikk forklart eksplisitt – komiteen forstår at midlene er etterskuddsvise og ikke kan brukes til topp-likviditet<br>• Sammenligningen mot Husbankens praksis er et godt argumentasjonsgrep | • Endringsanmodning til KMF/BYA om bruksendring fra kontor til minilager er fortsatt ubesvart (25.06.2026) – dette er en reell tilbakeholdingsrisiko som ikke er flagget tydelig nok<br>• "Estimert total prosjektkostnad ~6–15 MNOK" i tabell 6 er inkonsistent med 30 MNOK i forretningsplanen<br>• Stiftelsen UNI krever revisorbekreftelse på at hele prosjektet er finansiert før utbetaling – det betyr at 100 000 kr ikke kommer før bankavtalen er på plass, en sirkelreferanse |
| 06 Tilskudd som EK | 7/10 | • Korrekte lovreferanser (NRS 4, regnskapsloven § 6-2, skatteloven § 14-42, EBA/GL/2020/06)<br>• Klassifiseringen "bevilget/utbetalt" i bankvekting er realistisk og samsvarer med faktisk praksis<br>• Tilbakebetalingsklausulene som betinget gjeld er nevnt | • Skriftet hevder noen ganger sterkere enn det rettskildene rekker – EBA/GL/2020/06 sier ikke eksplisitt at tilskudd "behandles som ekvivalent til egenkapital"<br>• Mangler praktisk eksempel: hva ville en faktisk LTV-beregning se ut hvis banken aksepterte 2,25 MNOK 100 %, 5,4 MNOK 50 %, og 4 MNOK 0 %?<br>• Husbank-referansen er en analogi som ikke er direkte overførbar til næringseiendom – risikerer å virke som "argument by stretch" |
| 07 Grønt lån | 7/10 | • Klar tabell mot DNBs rammeverk V.5.1 og EU-taksonomi art. 7.2 – komiteen kan kvittere ut umiddelbart<br>• Tre-nivåers løft (G→D) er et sterkt markedsføringspunkt overfor banken<br>• Henviser direkte til HRP-rapporten med sidereferanser | • Forutsetter at investeringen i T1 (9,3 MNOK) faktisk gjennomføres som beskrevet – hvis byggherre senere kutter for å spare penger, faller grønt-lån-grunnlaget bort<br>• Forskjellen mellom "levert energi" og PED er nevnt, men ikke avklart – komiteen kan sende videre til ESG-avdelingen<br>• Selve rentepremien for grønt lån er ikke kvantifisert (typisk 10–25 bps) |
| 08 Energirapport | 9/10 | • Profesjonelt utført av tredjepart (HRP AS) med korrekt beregningsstandard (NS 3031:2025, Simien Pro)<br>• Detaljerte beregninger per tiltak gir komiteen trygghet for at tallene tåler en stikkprøve<br>• Tiltakspakke T1 er klart definert med energimerke D og 53 % besparelse | • Investeringskostnaden for T1 (9,3 MNOK) skal være "inkludert" i den samlede byggekostnaden 30 MNOK – men det er ikke vist hvor i kostnadsoppstillingen<br>• Rapportens egen advarsel om Simien-oppdatering ("om dette er reelt eller en feilkilde i programmet er vanskelig å si") svekker tilliten til besparelsestallene noe<br>• Inneholder ingen ESG/DNSH-vurdering som taksonomien strengt tatt krever |

### Hovedanbefalinger til justering før utsending

1. **Skriv om følgebrevet til en ekte forespørsel.** Faktaboks: ramme (~30 MNOK), formål (15,5 refi + 12–14 ny konstruksjon), sikkerhet, LTV (~58 %), DSCR, løpetid, grønt-lån-status, BFU-status, tidshorisont. Plassér prinsippspørsmålet som ett av flere agendapunkter.
2. **Levér uavhengig takst og DSCR-tabell.** Eiendomsverdi 50 MNOK hviler på prosjektets egen cap-rate-anslag. Legg ved DSCR-tabell år 1–5.
3. **Skill skarpere mellom bekreftet og forventet.** Tre kolonner: (a) Committed, (b) Sannsynlig (50 % vekt), (c) Oppside.
4. **Fyll ut sponsor- og selskapssaken.** Fisjonsplan, åpningsbalanse FG30 AS, sponsor-CV.
5. **Adresser TBRT-dagbøtene og endringsmeldingen til KMF/BYA eksplisitt.**
6. **Kutt 30–40 % av tekstvolumet i juridiske vedlegg** eller flytt til bilags-appendix.

---

## Kredittanalytiker

**Helhetsvurdering av pakken:** 5/10
**Kort begrunnelse:** Pakken er godt strukturert juridisk og dokumentasjonsmessig, men driftsøkonomien er for tynt fundert (urealistisk høy EBITDA-margin, fragmenterte konkurrentpriser strukket til premium-prismål, ingen tomgangsperiode, manglende rentekostnad i sensitiviteten) og kombinert worst case viser 87,5 % LTV uten reell mitigering – det betyr at base-casen er hele caset.

### Per dokument

| Dokument | Rating | Styrker | Svakheter |
|---|---|---|---|
| 00 Bankhenvendelse | 7/10 | • Tydelig formulert prinsippspørsmål (tilskudd som EK) gir banken noe konkret å svare på<br>• Ryddig vedleggsliste og klar avsender<br>• Adresserer både MVA, grønt lån og tilskudd i én pakke | • Selger maksimumsnivåer ("opp til 12,5 MNOK", "53 % reduksjon") tidlig uten å forankre i base case først<br>• Refererer til "dagbøter 2 000 kr/dag" via bakgrunn men nevner ikke TBRT-saken eksplisitt<br>• "Fysisk forberedende arbeid pågår – dokumentasjon på forespørsel" virker tilbakeholdent |
| 01 Forretningsplan | 4/10 | • God strukturell oppbygging og konsept tydelig forklart<br>• Eksplisitt benchmark mot Stortrack og CBRE Nordic gir et minimum av eksternt belegg<br>• Differensieringsargument (Nidelv, sentralitet, full-service) er konkret | • EBITDA-margin 64 % er svært høy for et bemannet full-service-konsept (Vinden/Shurgard ligger 35–50 %); 0,5 årsverk drift + 0,5 sjåfør for 478 enheter er underdimensjonert<br>• Belegg 60/50 % allerede i år 1 er optimistisk – ingen tomgangsperiode/lease-up; bransjenorm er 18–30 mnd til 60–70 %<br>• "Realistisk base" inkluderer fire ikke-innvilgede tilskudd – per definisjon ikke "realistisk" før vedtak<br>• Byggekostnad 30 MNOK med 10 % uforutsett er stramt for et 1857-bygg med råte; bransjenorm 15–25 % |
| 02 Finansieringsplan | 5/10 | • Eksplisitte tre scenarier med LTV-utregning<br>• Kvartalsvis kontantstrømskisse – uvanlig god praksis<br>• Erkjenner BFU-risiko og fallback til passiv utleie | • LTV beregnes mot taksert verdi 50 MNOK som er en intern cap-rate-øvelse, ikke en uavhengig takst<br>• Worst case viser 87,5 % LTV, men mitigering er ikke kvantifisert<br>• Rentekostnader i byggefasen (kapitalisert rente på 28–30 MNOK i 12–15 mnd) er ikke modellert – fort 1,5–2,5 MNOK ekstra<br>• "Realistisk" base baserer LTV-tall på tilskudd som ikke er innvilget |
| 03 MVA-strategi | 7/10 | • Solid juridisk gjennomgang med konkrete §§ og prinsipputtalelse 18.11.2014<br>• Vinden-presedensen er et reelt og verdifullt holdepunkt<br>• BFU planlagt før byggestart er riktig sekvensering | • "90–95 % MVA-dekning" i hybrid forutsetter 70 % full-service som er en forretningsmodell-antagelse<br>• Justeringsrisikoen over 10 år er bare nevnt – ikke kvantifisert (potensielt 0,75 MNOK/år ved omklassifisering år 1)<br>• B2B-delens "frivillig reg." krever at leietakerne er MVA-registrerte – ikke alle SMB-arkivkunder er det |
| 04 Konkurrent og marked | 6/10 | • Verifiserte priser med hentedato fra flere konkurrenter er reelt grunnlag<br>• Ærlig om datahull<br>• Geografisk avstandstabell er konkret | • FG30s prismål 300/360 kr/kvm/mnd plasseres rett under Utleiebod (286–399), men Utleiebod har 3 m takhøyde – nyttevolum-justert er FG30 dyrere per m³<br>• "20–35 % sentralitetspremie" hentes fra Stortrack Europe og overføres direkte til Trondheim uten lokal kalibrering<br>• Stab-pris 350–420 kr fra år 3 forutsetter at marked aksepterer 15–25 % prisøkning innen 2 år – ingen historisk evidens |
| 05 Støtteoversikt | 7/10 | • Tilsagnsbrev, prosjektnummer, dato per ordning – verifiserbart<br>• Ærlig på etterskuddsutbetaling og utbetalingsmilepæler<br>• KMF/BYA-endringsmelding 25.06.2026 nevnes – viktig honesty | • KMF og BYA er informert om endret bruk og svar avventes – materiell åpen risiko som ikke flagges som risiko<br>• "Estimert total prosjektkostnad 6–15 MNOK" motsier 30 MNOK i forretningsplan<br>• Stiftelsen UNI krever revisorbekreftelse og at "hele prosjektet er finansiert og ferdigstilt" – materiell betingelse |
| 06 Tilskudd som EK | 6/10 | • Korrekt skille mellom regnskaps-EK og bankens LTV-vurdering<br>• Riktige rettskilder (NRS 4, EBA/GL/2020/06, § 14-42 (3))<br>• Anerkjenner tilbakebetalingsrisiko | • EBA/GL/2020/06 sier ikke eksplisitt at tilskudd "behandles ekvivalent til egenkapital" – det er forfatterens tolkning, ikke ordlyd<br>• Påstand om at "norske banker anerkjenner konsistent" – uten kildehenvisning til faktisk bankpraksis<br>• Husbank-analogien gjelder forbrukerlån og overføres for raskt til CRE |
| 07 Grønt lån | 7/10 | • Klar tabell mot DNB-rammeverk og EU-taksonomi<br>• Korrekt referanse til artikkel 7.2 og Delegert forordning 2021/2139<br>• Erkjenner PED vs. levert energi-distinksjonen | • Grønt lån-rente er ikke kvantifisert – typisk 5–25 bps fordel<br>• DNSH-kravet nevnes men dokumenteres ikke<br>• Energiattest etter rehab er en utstedelses-betingelse som lett kan glippe – ikke i fremdriftsplan |
| 08 Energirapport | 8/10 | • Tredjeparts (HRP), NS 3031:2025/Simien Pro – solid teknisk grunnlag<br>• Eksplisitt om Simien-oppdateringen og usikkerhet<br>• Strakstiltak og effekt-tabell konkret og brukbar | • Investeringskostnad T1 9,29 MNOK ligger inne i "30 MNOK total" – energi-tiltakene kannibaliserer altså strukturell rehabilitering<br>• Inntjeningstider >100 år viser at investeringen drives av regelverk/finansiering, ikke driftsøkonomi<br>• Verneklasse oppgis C her, men "verneklasse B" i tilskuddsdokumentet |

### Hovedanbefalinger til justering før utsending

1. **Reklassifiser "realistisk base" – kall det "ambisjonsbase".** Vis en LTV-tabell der kun innvilget tilskudd er base.
2. **Modellér rentekostnad i byggefasen og DSCR-bane år 1–4.** 28–30 MNOK i 15 mnd à ~6,5 % = ~2,3 MNOK kapitalisert rente.
3. **Bygg en konservativ driftscase parallelt:** belegg 30/25 % år 1, 50/45 % år 2, 70/65 % år 3; EBITDA-margin 45–50 %; lease-up 6 mnd.
4. **Konkretiser uforutsett til 15–20 % (4,5–6 MNOK), ikke 10 %.**
5. **Adresser TBRT-saken, endringsmelding til KMF/BYA og fisjon eksplisitt** under risikoer.
6. **Erstatt cap-rate-takst med uavhengig verditakst** eller forventningsavklaring (bransjen 6,5–7,5 % stabilisert; nytt og uprøvd: 7,5–8,5 % = 35–40 MNOK verdi, ikke 50).
7. **Differensier prismål: bekreft launch-pris med betinget LOI** fra 5–10 forhåndskunder.
8. **Konsolider EK-tall:** 1,5 vs. 2–3 MNOK må synkroniseres.

---

## Kredittsjef / Kredittkomité

**Helhetsvurdering av pakken:** 6/10
**Kort begrunnelse:** Pakken er overraskende grundig og gir kredittkomiteen veldig mye å lese, men forespørselen er smalt og prinsipielt formulert mens dokumentmengden inviterer til full kredittvurdering — det skaper friksjon. Det er også flere inkonsistente nøkkeltall mellom dokumentene (særlig verneklasse, areal, refinansieringsbeløp og enkelte konkurrentpriser) og enkelte juridiske påstander som er overstrukket relativt til hva norsk bankpraksis faktisk gjør i dag.

### Per dokument

| Dokument | Rating | Styrker | Svakheter |
|---|---|---|---|
| 00 Bankhenvendelse | 6/10 | • Tydelig signatur, kontaktinfo og ryddig vedleggsoversikt<br>• Eksplisitt at "vi forventer ikke konkret kredittvurdering nå" — riktig forventningsstyring<br>• God åpning som refererer til tidligere dialog | • Forespørselen er prinsipiell men leverer 8 tunge vedlegg — pakken misforholder seg til ambisjonsnivået på spørsmålet<br>• Mangler "ask box": hvilket beløp, hvilken løpetid, hvilken bank-rolle, hvilken tidshorisont for svar<br>• Refinansieringsdimensjonen (15,5 MNOK) er begravet — burde stått i en tabell øverst |
| 01 Forretningsplan | 6/10 | • Solid struktur: konsept, marked, MVA, finansiering, risiko, fremdrift<br>• Sensitivitetstabell og break-even på 36 % belegg gir komiteen noe konkret å teste mot<br>• Konkurranseargumentasjon er konkret | • Sentrale tall vandrer: 8 MNOK realistisk vs. 7,7–8,2 (finansplan); LTV "~55 %" vs. 58 % vs. 56–60 % — komiteen merker dette umiddelbart<br>• EBITDA-margin 64 % på minilager er høyt — driftskostnader virker undervurdert<br>• "Trondheim Minilager 306 kr/kvm/mnd" vs. 275–333 kr ulike steder — internt avvik |
| 02 Finansieringsplan | 7/10 | • Sensitivitetsmatrise bankvennlig og viser at kombinert worst case 87,5 % LTV er adressert<br>• Klassifisering av tilskudd i sannsynlighetslag er ærlig<br>• Eksplisitt kontantstrømstabell viser at toppkapitalbehov ligger Q2–Q3 2027 | • Worst case 87,5 % LTV uten klart svar på hvordan den dekkes — kredittkomité vil se konkret EK-buffer eller pant utenfor objektet<br>• "Privat EK 2–3 MNOK" på 30 MNOK byggebudsjett er svært tynt — typisk 10–15 % kontant-EK kreves<br>• Eiendomsverdi 50 MNOK ved cap rate 6,0 % er sirkulær (egne forutsetninger) og bør utfordres med uavhengig verdivurdering |
| 03 MVA-strategi | 8/10 | • Klare lovreferanser og prinsipputtalelse 18.11.2014<br>• Sammenligner alternativene kvantitativt og lander på hybrid med 90–95 % MVA-dekning<br>• Adresserer fallback ved negativ BFU | • For et bank-publikum er dette grunnleggende et MVA-notat; konsekvenser for låneservice (likviditet i byggefasen) ikke fremhevet<br>• 10-årig justeringsrisiko vises som "lav sannsynlighet" — kredittkomiteen vil ønske formell BFU-status som covenant<br>• Vinden-referansen er anekdotisk — Skatteetatens praksis bekreftes ikke gjennom konkurrent-suksess |
| 04 Konkurrent og marked | 7/10 | • Solid datainnsamling med datostempel og kilder<br>• Sentralitetsargumentet er konkret og kvantifiserbart<br>• Stortrack-referansen gir ekstern validering | • Belegg-forutsetninger (85–90 % stabilisert) er ikke validert mot Trondheim-spesifikk data<br>• Green Storage 613 kr/kvm/mnd er "ikke verifisert" men brukes likevel<br>• Driver av betalingsvillighet (kundeintervjuer, ventelister, LOI) ikke dokumentert |
| 05 Støtteoversikt | 7/10 | • Hver ordning har tilsagnsdato, saksnummer og kontaktperson<br>• Korrekt skille mellom innvilget og potensial<br>• Refererer til separat juridisk utredning | • Tabellen i kap. 6 har "TBD" og "~6–15 MNOK estimert total prosjektkostnad" — totalt uforenlig med 30 MNOK i øvrige dokumenter<br>• KMF-endringsmelding "svar avventes" på endret bruk — materiell risiko som nedtones<br>• UNI-kausalitet er bakvendt: tilskudd kan ikke brukes som EK hvis utbetaling forutsetter ferdig finansiering |
| 06 Tilskudd som EK | 6/10 | • God systematikk: regnskap, skatt, bank — riktig rammeverk<br>• Riktig nyansering av "ikke EK regnskapsmessig, men reduserer nettoeksponering"<br>• Skiller bevilget/utbetalt — anerkjenner at vekting varierer | • Påstander om bankenes anerkjennelse er strekkere enn rettskildene gir grunnlag for<br>• Husbank-referansen er ikke overførbar til næringseiendom<br>• Mangler det viktigste: konkrete eksempler fra norske banker i sammenlignbare prosjekter |
| 07 Grønt lån | 8/10 | • Klar tabell mot DNB-rammeverk, EU-taksonomi, SpareBank 1 m.fl.<br>• Korrekt nyansering av PED vs. levert energi<br>• BREEAM-diskusjonen er nyansert | • "Verneklasse B" vs. "verneklasse C" i HRP — internt avvik<br>• Enova-støtten på 2,3 MNOK er en kalkyle, ikke en søknad — bør beskrives som potensial<br>• Mangler bankens egne dokumentasjonskrav for grønt lån (energiattest, årsrapportering) |
| 08 Energirapport | 8/10 | • Profesjonell tredjepartsrapport — sterkest dokumentbevis i pakken<br>• Tre tiltakspakker med tydelig økonomi<br>• HRP er åpen om beregningsusikkerhet — øker troverdighet | • Inntjeningstid >100 år på T1 betyr at energitiltakene ikke er bedriftsøkonomisk lønnsomme isolert<br>• Verneklasse C vs. B i grønne lån-dokumentet<br>• Solcelletiltaket "ikke lønner seg" men inkludert i T2/T3 — internt motstridende |

### Hovedanbefalinger til justering før utsending

1. **Skarp opp forespørselen og forventningsstyringen.** Følgebrev i ett avsnitt: (a) totalt kapitalbehov, (b) refinansiering (15,5) vs. ny (12–15), (c) bank-rolle, (d) svartidshorisont, (e) at full kredittsak vil følge Q3/Q4 2026.
2. **Eliminer tallinkonsistenser.** Verneklasse, areal, Trondheim Minilager-pris, "estimert total prosjektkostnad 6–15 MNOK" vs. 30, LTV, tilskuddsbase. En kredittkomité bruker første time på å lete etter inkonsistenser.
3. **Tilstram juridisk argumentasjon i dok. 06.** Erstatt "EBA anerkjenner tilskudd som EK-ekvivalent" med presis ordlyd. Fjern Husbank-referansen. Legg til 1–2 konkrete sammenlignbare case.
4. **Styrk kontant-EK eller forklar fraværet.** 2–3 MNOK på 30 MNOK er under det de fleste banker forventer.
5. **Adresser KMF-endringsmeldingen eksplisitt.** Få skriftlig bekreftelse fra KMF før utsending, eller flagg risikoen tydelig.
6. **Legg ved indikativ eiendomsverdivurdering** fra uavhengig takstmann.

---

## Risk officer / Risikoavdeling

**Helhetsvurdering av pakken:** 5/10
**Kort begrunnelse:** Pakken er imponerende ryddig på lov, MVA og grønt lån, men risikoanalysen er overfladisk og énvariabel: ingen makro-scenarier (rente, resesjon, energipris), ingen sektorbenchmark for minilager-syklisitet, og «realistisk base» behandler søknader-under-utforming som om de var nær-sikre. Verstefall-tabellen mangler de stresscenariene en risikoavdeling faktisk vil teste.

### Per dokument

| Dokument | Rating | Styrker | Svakheter |
|---|---|---|---|
| 00 Bankhenvendelse | 6/10 | • Konkret og avgrenset spørsmål gjør det enkelt å gi raskt prinsippsvar<br>• Henviser tydelig til vedlegg slik at risk kan dybdesjekke<br>• Nevner TBRT-dialog – men kun via vedlegg | • Skjuler at TBRT har ilagt dagbøter (bestridt) og at rehab er offentlig pålagt – materielt for både regulatorisk og omdømmerisiko<br>• Henvendelsen omtaler ~30 MNOK uten å fortelle drawdown-profil<br>• Mangler helt motpartsrisiko-vinkling (leietakerstruktur, churn, sektorfølsomhet) |
| 01 Forretningsplan | 5/10 | • Komplett bilde av konsept, areal, MVA og tilskuddsstruktur<br>• Eksplisitt break-even-belegg (36 %)<br>• Energi/grønt-kvalifikasjon er konkret og dokumentert | • Risikotabell (kap. 9) er generisk: kun «lav/middels/høy» uten sannsynlighet × konsekvens i kr, ingen tail-scenarier<br>• Konkurranserisiko vurdert «lav» når Green Storage og 123 Minilager alle ekspanderer – sektor-tilbudssjokk ikke vurdert<br>• Sentrale antakelser (BFU, 30/70-miks) presenteres som forutsetninger, ikke risikofaktorer |
| 02 Finansieringsplan | 6/10 | • Eksplisitt LTV-stige (46/58/70 %) og kombinert worst case (87,5 % LTV)<br>• Kvartalsvis kontantstrøm gjennom byggefasen<br>• BFU-sensitivitet er vist isolert med tre utfall | • «Worst case» kombinerer kun 3 variabler – ingen rentestress, leieprisstress eller belegg-stress<br>• Kategorisering av tilskudd som «høy sannsynlighet» med 95–100 % vekting i base-LTV er optimistisk<br>• Ingen sensitivitet på EBITDA/rente-dekning (ICR/DSCR); med 3 MNOK EBITDA og 28–30 MNOK gjeld er DSCR sårbar ved renter over 6–7 % |
| 03 MVA-strategi | 7/10 | • Stringent juridisk gjennomgang med Skattedir-uttalelse 2014 og fallback til passiv utleie<br>• Kvantifiserer MVA-utfall per alternativ tydelig<br>• Adresserer 10-årig justeringsrisiko ved bruksendring | • Justeringsrisiko vises bare som «lav/høy» – ingen tallsetting av kostnad ved bruksendring 5–7 år ut<br>• Bruker Vinden som «bevis» – ikke en BFU og kan ikke vektes som juridisk sikkerhet<br>• Driftsrisikoen i full-service er underspilt – 70 % av inntektene avhenger av logistikkoperasjon byggherre aldri har drevet |
| 04 Konkurrent og marked | 5/10 | • Konkrete verifiserte priser per konkurrent<br>• Tydelig avstand-tabell viser sentralitetspremiet<br>• Innrømmer datahull | • Sektor-syklisitet og makrofølsomhet ikke berørt: minilager er etterspørselsdrevet av flytting/livshendelser, som faller i resesjon<br>• Tilbudssjokk vurderes ikke: Green Storage og Trondheim Minilager kan utvide raskt<br>• Bruker n=1 fra Green Storage (613 kr) som referansepunkt – metodisk svakt |
| 05 Støtteoversikt | 7/10 | • Hver tilskuddsordning har dato, saksnr, intensitet og utbetalingsmekanisme<br>• Skiller eksplisitt bevilget (2,25 MNOK) fra under-søknad<br>• Tilbakebetalingsklausuler nevnt | • Konsentrasjonsrisiko ikke vurdert: nesten alt under-søknad-volum hviler på Enova Energioppgradering – ett avslag flytter LTV fra 58 % til 65 %+<br>• Endringsmelding til KMF/BYA «svar avventes» – materiell tilbakekallsrisiko ikke kvantifisert<br>• Sluttutbetalings-betingelser ikke konsekvensvurdert for trekkrammen |
| 06 Tilskudd som EK | 8/10 | • Solid juridisk vertikal<br>• Skiller eksplisitt bevilget vs. utbetalt og vekter ulikt<br>• Erkjenner at tilskudd er utsatt inntekt, ikke EK regnskapsmessig | • Påstanden «bevilget tilskudd anerkjennes som ekvivalent egenkapital» er for absolutt – mange banker vekter bevilget-men-ikke-utbetalt nærmere 50–70 %, ikke 100 %<br>• Tilbakebetalingsrisiko ved bruksendring (KMF/BYA pågår) burde vært konkretisert med beløpseffekt på LTV<br>• «Husbanken som referanse» er svakt analogi-grunnlag |
| 07 Grønt lån | 7/10 | • Klar oppfyllelses-tabell mot DNB V.5.1 og taksonomi 7.2 med tall over kravet<br>• Erkjenner PED vs. levert-energi-nuansen<br>• Dokumentasjonspakken er konkret listet | • Grønt lån-margin (5–25 bp) ikke kvantifisert<br>• DNSH-kravet er kort nevnt men ikke dokumentert<br>• Forutsetter at T1-pakken faktisk bygges; ved kostnadskutt kan tiltak strykes og kvalifikasjonen ryke |
| 08 Energirapport | 8/10 | • Tredjeparts (HRP, NS 3031:2025, Simien Pro)<br>• Ærlig om systemtap-usikkerhet<br>• Effekttall (220→40 kW) gir konkret operasjonell innsikt | • Tiltaksinntjeningstid >100 år – understreker at investeringen er drevet av tilskudd, ikke energiøkonomi<br>• Som-bygget-energiattest kan avvike fra Simien-modellen – ikke clawback-vurdert<br>• Energipris-sensitivitet ikke vist |

### Hovedanbefalinger til justering før utsending

1. **Legg ved en stresstest med simultane sjokk:** rente +300 bp + belegg −20 pp + leiepris −15 % + byggekostnad +15 %, og vis DSCR og LTV i hvert scenario.
2. **Skill tydeligere mellom bevilget (bindende) og under-søknad** i LTV-tabellen. Hovedscenariet skal være kun bevilget støtte + MVA. Da forsvinner inntrykket av at base-LTV er 58 % når det realistisk er 65–70 %.
3. **Adresser sektor- og motpartsrisiko eksplisitt:** minilagers syklisitet, churn, hvor «klissete» 478 enkeltkunder er.
4. **Kvantifiser den regulatoriske halen:** TBRT-dagbøter status, KMF/BYA-endringsmelding tilbakekallsrisiko, rammesøknad delvis avslag.
5. **Erstatt det «kreative» MVA-argumentet med BFU-tidslinje** – bank vil ikke kommittere konstruksjonsramme før BFU er på plass eller fallback er priset inn.
6. **Vis rentedekning (ICR/DSCR), ikke bare LTV.** Med ~3 MNOK stabil EBITDA og 28–30 MNOK gjeld er DSCR ved 6 % rente ca. 1,4–1,5x – på grensen av mange bankers covenant-krav.

---

## ESG- / Grønt lån-rådgiver

**Helhetsvurdering av pakken:** 6/10
**Kort begrunnelse:** Energitallene er solide og dokumenterte (53 % reduksjon, G→D, NS 3031:2025, Simien Pro) og kvalifiserer formelt til grønt lån etter DNBs V.5.1. Men pakken har en alvorlig svakhet på DNSH-siden (vann/sirkulær økonomi/biologisk mangfold er knapt nevnt), mangler post-rehab energiattest fra registrert energirådgiver, og blander sammen PED (primærenergi) og levert energi uten å adressere konsekvensen for taksonomi-art. 7.2.

### Per dokument

| Dokument | Rating | Styrker | Svakheter |
|---|---|---|---|
| 00 Bankhenvendelse | 6/10 | • Nevner grønt lån eksplisitt med 53 %/G→D og henviser til HRP-rapport, EU-taksonomi art. 7.2 og DNB-rammeverk<br>• Kobler kvalifikasjon til konkret Enova-spor (~2,3 MNOK) | • Ingen omtale av DNSH eller monitoreringsrammeverk for grønt lån<br>• Snakker om "grønt lån" som etablert sannhet uten å nevne at endelig taksonomivurdering må kvalitetssikres av ESG-rådgiver<br>• Energiattest (krav fra 1.1.2021) er ikke nevnt som leveranse |
| 01 Forretningsplan | 6/10 | • Kapittel 2.4 setter krav vs. faktisk verdi i tabell<br>• Erkjenner at T1 koster 9,3 MNOK og inkluderer dette i totalbudsjettet | • Energiprofilen er en bolt-on – ikke integrert i risikomatrisen kap. 9 (ingen «grønn risiko» som regulatorisk endring av taksonomi)<br>• Ingen klimatilpasningsbetraktning for et bryggebygg på Nidelvas bredd – flomrisiko/havnivå burde adresseres<br>• Ingen ombruksargumentasjon koblet til T1, selv om Enova ombrukskartlegging er innvilget – manglende sirkulær-økonomi-narrativ |
| 02 Finansieringsplan | 7/10 | • Tydelig kobling mellom T1, Enova Energioppgradering og grønt lån-prising<br>• Erkjenner at PED vs. levert energi har nyanser | • Behandler grønt lån som ren rente-rabatt-mekanisme; ingen omtale av rapporteringsforpliktelser (årlig energiforbruk, allokeringsrapport)<br>• «Pant i tilskuddsrettigheter» som sikkerhet på Enova Energioppgradering er anførselsverdig<br>• Ingen scenario der grønt lån-rabatten kvantifiseres |
| 03 MVA-strategi | 3/10 | • Velskrevet og grundig på sitt eget felt | • Ingen relevans for ESG/grønt lån-vurdering |
| 04 Konkurrent og marked | 3/10 | • Solid prisbenchmarking – relevant for kredittvurdering, ikke ESG | • Ingen ESG-/grønt-vinkling overhodet; ikke ett ord om at konkurrenter er klimastyrt/sertifisert eller bærekraft som differensiator |
| 05 Støtteoversikt | 6/10 | • Kapittel 5 er kompakt og setter T1 i tabell mot DNB-krav<br>• Henviser eksplisitt til HRP-rapport | • "34 % reduksjon mot energimerkekravet" er upresis – DNB-kravet er 30 % mot byggets opprinnelige ytelse, ikke "mot energimerkekravet"<br>• Enova ombrukskartlegging er innvilget, men koblingen til DNSH "sirkulær økonomi" ikke trukket<br>• Mangler sluttdokumentasjon (energiattest post-rehab) |
| 06 Tilskudd som EK | 2/10 | • Ryddig juridisk utredning på sitt felt | • Ingen ESG/grønt lån-relevans; bortkastet plass i en pakke som markedsfører grønt lån-kvalifikasjon |
| 07 Grønt lån | 8/10 | • Mest kompetente dokumentet: refererer DNB V.5.1, EU 2021/2139 art. 7.2, NS 3031:2025<br>• Erkjenner eksplisitt skillet mellom PED og "levert energi"<br>• Adresserer BREEAM-spørsmålet kirurgisk | • DNSH-kravet er nevnt, men ikke operasjonalisert: ingen konkret vurdering for vann, biologisk mangfold, sirkulær økonomi, klimatilpasning<br>• "34 % reduksjon mot energimerkekravet" gjentas – uklart om dette refererer til samme tall som 53 %<br>• Klimatilpasningsmål (sea-level rise, flom) – et bryggebygg på elvebredden er åpenbart eksponert |
| 08 Energirapport | 8/10 | • Riktig metodikk: NS 3031:2025, Simien Pro, navngitt sertifisert rådgiver<br>• Konsistente og rapporterte tall<br>• Erkjenner egne usikkerheter: Simien-oppdatering kan ha overdrevet systemtap | • Rapporten beregner besparelsen mot **referansebygget etter ombygging** (427 000 kWh), ikke mot **byggets opprinnelige energiytelse** (256 kWh/m² nå). DNB V.5.1 og art. 7.2 krever "sammenliknet med byggets opprinnelige energiytelse"<br>• Mangler dokumentert PED-beregning (kun "levert energi") – kritisk for EU-taksonomi-samsvar<br>• Ingen energiattest er utstedt (kun energikartlegging); DNB V.5.1 krever sertifisert energiattest både før og etter |

### Hovedanbefalinger til justering før utsending

1. **Få utstedt energiattest fra registrert energirådgiver for nå-tilstand (G) og prosjektert post-rehab (D).** Energikartlegging er ikke det samme som energiattest.
2. **Klargjør beregningsbasen for 53 %-tallet i HRP-rapporten.** Få HRP til å levere en kort tilleggsnote som dokumenterer reduksjonen også mot opprinnelig ytelse i kWh/m²/år.
3. **Tilføy et DNSH-vedlegg som operasjonaliserer alle seks miljømål** for taksonomi 7.2. Vann, sirkulær økonomi (Enova ombruk = ubrukt potensial), biologisk mangfold, forurensning, klimatilpasning.
4. **Rens opp "34 % reduksjon mot energimerkekravet"-formuleringen.**
5. **Definer rammeverk for monitorering og rapportering** for grønt lån (årlig energiforbruk, allokeringsrapport).
6. **Knytt sirkulær økonomi til Enova ombrukskartlegging eksplisitt.** Originalt laftet treverk gjenbrukes – kvantifiser klimanytte.
7. **Adressér klimatilpasning** (havnivåstigning/flomrisiko) for bryggebygg på Nidelvas bredd.

---

## Jurist / Legal counsel

**Helhetsvurdering av pakken:** 6/10
**Kort begrunnelse:** Pakken er gjennomarbeidet og siterer korrekte rettskilder, men flere sentrale juridiske påstander framstilles som mer kategoriske enn rettskildene tillater – særlig EBA-referansene og full-service-MVA-klassifiseringen. Selskapsrettslige forhold rundt fisjonen er underbelyst og bør strammes opp før utsending.

### Per dokument

| Dokument | Rating | Styrker | Svakheter |
|---|---|---|---|
| 00 Bankhenvendelse | 6/10 | • Klar struktur og avgrenset, konkret anmodning (prinsippvurdering)<br>• Signaturen identifiserer korrekt at selskapet er "under etablering" | • Henviser til EBA/GL/2020/06 som om disse eksplisitt anerkjenner tilskudd som EK-ekvivalent – det går lengre enn ordlyden<br>• Mangler henvisning til hvem som har juridisk eierskap til søknadsspor og innvilgede tilskudd ved overgangen fra KodeWorks Eiendom AS til Fjordgata 30 AS<br>• "TBRT har gitt prosjektet skriftlig anbefaling" – tilsynsmyndighet som "anbefaler" et tilsynsobjekt er en uvanlig formulering |
| 01 Forretningsplan | 6/10 | • Selskapsstrukturen identifiseres tydelig<br>• Risikomatrisen er ærlig om både MVA- og brannvesen-tvister<br>• Erklærer eksplisitt at TBRT-dagbøter er "bestridt" | • Fisjonsprosessen er ikke datert eller dokumentert (vedtak, kreditorvarsel, frister etter asl. kap. 14)<br>• "Eksisterende gjeld 15,5 MNOK refinansieres inn" – ingen omtale av hvordan eksisterende panthavers stilling håndteres i fisjonen<br>• Risikoen "TBRT-dagbøter" er ikke kvantifisert (akkumulert beløp) |
| 02 Finansieringsplan | 6/10 | • Sensitivitetsanalysen er juridisk ryddig – ikke skjult risiko<br>• Sikkerhetsstrukturen nevner eksplisitt "pant i tilskuddsrettigheter"<br>• Tilbakebetalingsvilkår nevnes | • Pant i tilskuddsrettigheter: ingen drøftelse av om tilskuddsbrevene faktisk er transportable. KMF, Enova og UNI har vilkår som kan utelukke pantsettelse uten samtykke<br>• "Anerkjent med moderasjon" / "fullt anerkjent" tabellen framstilles som etablert bankpraksis – er forfatterens egen kategorisering<br>• Ingen vurdering av om eksisterende långiver vil samtykke til refinansiering |
| 03 MVA-strategi | 7/10 | • Lovhenvisninger er presise og korrekt sitert<br>• Skattedirektoratets prinsipputtalelse og SKNS1-2020-134 relevant og korrekt anvendt<br>• Justeringsreglene identifisert som risiko | • "Vinden opererer modellen" brukes som bevis – Vinden kan ha annen faktisk modell, og argumentet er ikke rettskilde<br>• Skillet mellom "aktiv lagringstjeneste" og "passiv utleie" presenteres som klart; Skatteetaten har vurdert grensetilfeller strengt<br>• Hybrid Alternativ D forutsetter at forholdsmessig fradrag etter mval. § 8-2 holder – arealfordeling 30/70 må dokumenteres reelt |
| 04 Konkurrent og marked | 5/10 | • God metodisk transparens om hvor data er hentet<br>• Sentralitetsargument og Nidelv-tilknytning er konkrete differensiatorer | • Begrenset juridisk relevans for kredittvurdering<br>• Premiumargumentet er sitert til Stortrack uten å belyse at konkurrenter også kan tilpasse pris<br>• Inneholder ingen vurdering av konkurrenters MVA-praksis – relevant for å validere FG30s eget MVA-grep |
| 05 Støtteoversikt | 7/10 | • Hvert tilskudd har dokumentreferanse – etterprøvbart<br>• Tilbakebetalingsklausuler nevnes eksplisitt<br>• Utbetalingsmekanismen korrekt beskrevet | • Tilbakebetalingsrisikoen presenteres som "lav" uten gjennomgang av faktiske vilkår (vesentlig formålsendring fra kontor til minilager er allerede meldt)<br>• Skriver "KodeWorks Eiendom AS" som tilskuddsmottaker – manglende drøftelse av om tilskudd kan overføres til Fjordgata 30 AS ved fisjon uten utløsende tilbakebetalingsklausul<br>• Bruksendring fra kontor til minilager er materielt – risiko for revurdering ikke vurdert |
| 06 Tilskudd som EK | 6/10 | • God strukturert gjennomgang av NRS 4, regnskapsloven § 6-2, skatteloven § 14-42 (3)<br>• Korrekt skille mellom regnskapsmessig klassifisering og bankenes vurdering<br>• Husbanken og Innovasjon Norge som referanser er relevante analogier | • EBA/GL/2020/06 påstås å "åpne eksplisitt" – ordlyden er mer åpen og rammeverkspreget<br>• Tabellen "anerkjennes fullt/anerkjennes med forsiktighet" presenteres som etablert praksis, men er forfatterens egen typologi<br>• Mangler diskusjon av subordineringspraksis (banken vil kreve at EK-ekvivalent tilskudd er låst og ikke kan tilbakebetales før banken er innfridd) |
| 07 Grønt lån | 7/10 | • EU-taksonomiforordningen og Delegert forordning korrekt sitert<br>• Skillet mellom PED og "levert energi" er flagget – ærlig<br>• DNSH-kravet er nevnt – ofte oversett | • DNBs rammeverk V.5.1 – ingen direkte kildelenke<br>• "Norsk bankpraksis er harmonisert på 30 %" er en konsensuspåstand uten underbygging<br>• Verneklassen oppgis ulikt – "verneklasse B" omtales i pkt. 4.3, mens energirapporten oppgir "verneklasse C" |
| 08 Energirapport | 8/10 | • Faglig forankret rapport fra HRP AS med navngitt rådgiver og kontrollør<br>• Bruker NS 3031:2025 og Simien Pro<br>• Ærlige forbehold om Simiens nye versjon | • Rapporten brukes som juridisk bevis for grønt-lån-kvalifisering – forutsetter at energiattest faktisk utstedes<br>• Verneklasse oppgis som "C" – avviker fra grønt-lån-dokumentets "B"<br>• Inneholder ingen "akkreditert uavhengig ekspert"-erklæring – EU-taksonomien stiller dette kravet eksplisitt |

### Hovedanbefalinger til justering før utsending

1. **Selskapsrettslig dokumentasjon for fisjonen må strammes opp.** Banken kan ikke ta sikkerhet i et selskap "under etablering" uten datert fisjonsplan, kreditorvarsel, frister etter asl. kap. 14, og særlig en avklaring av hvordan eksisterende panthaver (15,5 MNOK) håndteres.
2. **Tilskuddsoverdragelse og bruksendring må adresseres eksplisitt.** Endringsmelding om minilager er allerede sendt KMF/BYA og "svar avventes". Banken vil spørre: (a) krever tilskuddsgiver samtykke til overdragelse til Fjordgata 30 AS? (b) er bruksendring innenfor tilsagnsbrevets formål? (c) hva er tilbakebetalingsrisikoen ved negativt svar?
3. **Modér EBA/GL/2020/06-formuleringene.** Skriv "kan tas i betraktning som faktor som reduserer bankens nettoeksponering" i stedet for "anerkjennes som ekvivalent til egenkapital".
4. **Pant i tilskuddsrettigheter må kvalifiseres juridisk.** KMF, Enova og UNI-tilsagn har vilkår som kan begrense pantsettelse/overdragelse uten samtykke. Sjekk transportabilitet med hver tilskuddsgiver.
5. **MVA-strategien: be om at BFU formelt blir vilkår, ikke milepæl.** Bankjurist vil typisk akseptere full-service-modellen kun under forutsetning av positiv BFU før utbetaling av byggelån.
6. **Rydd inkonsistens om verneklasse (B vs. C) og om TBRT-saken.** TBRT som tilsynsmyndighet "anbefaler" et tilsynsobjekt under aktiv sak – krever forklaring. Foreslå å fjerne "anbefalingsbrev fra TBRT" som kredittargument og i stedet legge ved en kort statusoppdatering med oppgitt akkumulert dagbøtebeløp.

---

## Næringseiendomsspesialist / CRE-team

**Helhetsvurdering av pakken:** 5/10
**Kort begrunnelse:** Solid juridisk og energiteknisk dokumentasjon, men forretningsmodellen hviler på en uprøvd «valet storage»-differensiering med svært høy operasjonell kompleksitet, og verdsettelsen (50 MNOK ved 6 % yield) er for offensiv for et ny-utviklet minilager i Trondheim drevet av en førstegangsaktør.

### Per dokument

| Dokument | Rating | Styrker | Svakheter |
|---|---|---|---|
| 00 Bankhenvendelse | 6/10 | • Tydelig, fokusert anmodning – ikke kredittsøknad<br>• Refinansiering av eksisterende 15,5 MNOK åpent kommunisert<br>• Henviser konkret til EBA/GL/2020/06 og rammeverk | • Skjuler at «Fjordgata 30 AS» ikke er etablert ennå – CRE vil vurdere mot KodeWorks' track record, ikke en tom SPV<br>• Anbefalingsbrev fra TBRT framstilles som styrke, men at tilsynsmyndigheten gir prosjektet skriftlig anbefaling parallelt med pågående tilsyn med dagbøter er underkommunisert<br>• «~50 MNOK eiendomsverdi» presenteres som faktum, ikke som avhengig variabel av belegg og cap rate |
| 01 Forretningsplan | 4/10 | • God strukturell oppstilling av areal, MVA-modell og pris-tier<br>• Krypkjeller- og Nidelv-vinkelen er en reell og uutnyttet differensiator<br>• Sensitivitet på belegg er nevnt og break-even på 36 % gir margin | • EBITDA-margin 64 % er urealistisk høy for en full-service-modell (Vinden/Stuff U Need-typer ligger 30–45 %); driftskost 1,6 MNOK er sterkt undervurdert<br>• Belegg på 85–90 % stabilisert som «typisk» – CBRE/Stortrack-data for nye norske anlegg ligger 70–82 % stabilisert<br>• Cap rate 6,0 % på et 478-enheters single-asset SPV er for skarp – realistisk 7,5–8,5 % gir verdi 35–40 MNOK, ikke 50 MNOK |
| 02 Finansieringsplan | 6/10 | • Eksplisitt sensitivitet på BFU-utfall og worst case er ærlig<br>• Kvartalsvis trekk-/utbetalingskurve<br>• Klassifiseringen av tilskudd etter sannsynlighet er disiplinert | • LTV beregnet mot 50 MNOK som «basisscenario» smitter inn med samme verdsettelsesproblem – ved realistisk 38 MNOK blir realistisk LTV ~76 %, ikke 58 %<br>• Eier-EK på 2–3 MNOK kontant mot ~30 MNOK byggekost er svært tynt; tilskudd som «EK» løser ikke at reell cash-skin-in-the-game er ~7 % av prosjektkost<br>• «Pant i tilskuddsrettigheter» – etterskuddsvise og avhengige av at byggherre fullfører tiltakene; ikke en likvid sikkerhet i en stress-situasjon |
| 03 MVA-strategi | 7/10 | • Solid juridisk analyse<br>• BFU planlagt før byggestart – riktig sekvensering<br>• Vinden referert som operasjonelt presedens er nyttig | • MVA-fradraget settes pari med EK, men det er en likviditetspost med justeringsplikt 10 år (§ 9-4)<br>• «Alternativ D gir 90–95 % dekning» avhenger av at 70 % faktisk drives full-service<br>• Lite om risiko for at full-service-volumet ikke materialiserer seg og 70/30-fordelingen må omgjøres |
| 04 Konkurrent og marked | 5/10 | • Verifiserte priser fra fem konkurrenter med kildehenvisning<br>• Riktig identifisert at Utleiebod er nærmeste reelle benchmark<br>• Sentralitet-premium 20–35 % er konsistent med Stortrack-referanser | • Cherry-picking: 300–360 kr/kvm/mnd plasseres «under nærmeste sentrale konkurrent» (Utleiebod 286–399), men FG30 har 478 enheter mot Utleiebods ~20–30<br>• Markedsstørrelse: ingen estimat på TAM/SAM for Trondheim sentrum<br>• «Hundrevis av leiligheter innen 250–350 m» som etterspørselsdriver er ren spekulasjon – ingen survey eller pre-bookinger |
| 05 Støtteoversikt | 7/10 | • Saksnummer, datoer og kontaktperson per ordning<br>• Skiller eksplisitt bevilget/utbetalt/under søknad<br>• Etterskuddsvis utbetaling adressert | • Tabellen «Estimert total prosjektkostnad ~6–15 MNOK» motsier forretningsplanens 30 MNOK<br>• KMF/BYA «svar avventes» – materiell usikkerhet om tilskuddene faktisk vil bli stående<br>• Egenkapital KodeWorks oppgitt til ~1,5 MNOK – mismatch mot finansieringsplanens 2–3 MNOK |
| 06 Tilskudd som EK | 6/10 | • Riktig henvisning til NRS 4, skatteloven § 14-42 (3), EBA/GL/2020/06<br>• Disiplinert om utbetalingsstatus<br>• Tilbakebetalingsklausul korrekt identifisert | • Overselger konklusjon – EBA 5.2.7 og 6.1 sier *ikke* at tilskudd skal behandles som EK<br>• Husbankens startlån er ikke analog til CRE-prosjektfinansiering<br>• Mangler benchmark fra norske CRE-bankers faktiske skjønnsutøvelse |
| 07 Grønt lån | 8/10 | • Solid mapping mot DNB Rammeverk V.5.1, EU-taksonomi 2021/2139 seksjon 7.2 og NS 3031:2025<br>• Korrekt nyansering om PED vs. levert energi<br>• BREEAM riktig avgrenset bort | • For CRE er det realiteten ikke kvalifikasjonen som gir lavere rente – grønt rente-rabatt typisk 0,05–0,20 prosentpoeng; dokumentet selger inn at «grønt lån gir lavere lånerente» uten kvantifisering<br>• Enova-støtten på 2,3 MNOK er allerede telt med i «høy sannsynlighet»-tilskuddsbasen – ikke isolert oppside<br>• Mangler vurdering av hvordan eierselskap som SPV under etablering kan utstede grønt lån i seg selv |
| 08 Energirapport | 9/10 | • Uavhengig tredjepart (HRP) med NS 3031:2025 og Simien Pro – CRE-grade dokumentasjon<br>• Tydelig tiltakspakke T1 med tall, kostnader og energimerke (G→D)<br>• Ærlig om usikkerheter | • Inntjeningstid >100 år på flere bygningskropp-tiltak – CRE vil notere at 9,3 MNOK i energiinvestering er kommersielt ulønnsomt isolert sett<br>• Rapporten er bygd opp som energirådgivning, ikke som bank-leveranse – mangler eksplisitt erklæring/signatur ift bankens dokumentasjonskrav<br>• Verneklasse C vs. forretningsplanens «fredet/verneverdig» – verneklasse-status bør harmoniseres |

### Hovedanbefalinger til justering før utsending

1. **Reduser eiendomsverdsettelsen til realistisk nivå.** Cap rate 6,0 % og 50 MNOK terminal value er for offensivt. Bruk 7,5–8,5 % på base-case (gir 35–40 MNOK) og presenter 6 % som oppside. Realistisk LTV blir 70–75 %.
2. **Re-baselin EBITDA-margin og driftskostnader for full-service-modellen.** 64 % EBITDA på 70 % valet-mix er ikke konsistent med Vinden/MakeSpace/Clutter. Legg til minimum 0,8–1,2 MNOK i bemanning, varebil, IT, kundetjeneste. EBITDA-margin 45–55 % er forsvarbart.
3. **Bygg ut markedsabsorpsjon konkret for Trondheim.** Erstatt «Skandinavia 920 anlegg» med en bottom-up absorpsjon-modell. Helst LOI eller pre-booking-kampanje med depositum.
4. **Innhent og fremlegg KMF/BYA bekreftelse på endret bruk før utsending.** Vent på svar eller fremlegg muntlig bekreftelse skriftlig – ellers kan tilskuddene ikke regnes inn.
5. **Demp framstillingen av tilskudd som EK-ekvivalent.** Reformuler til «tilskudd som reduksjon i netto finansieringsbehov».
6. **Avklar SPV-strukturen og personlig garantistilling.** Når er fisjonen planlagt? Hvilken EK starter SPV med? Stiller Eirik Larsen personlig kausjon?
7. **Harmoniser tall på tvers av dokumentene.** Egenkapital, total prosjektkostnad, verneklasse, Enova-støtte-double-counting.

---

*Generert av multi-agent rolle-review, 29.06.2026.*
