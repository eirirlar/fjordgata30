# Prompt: Iterativ strategianalyse mot tvangsmulkt — Fjordgata 30

**Formål:** Standalone-prompt for Claude Code som produserer en grundig,
iterativ strategianalyse mot TBRTs tvangsmulkt. Prompten står på egne
bein — kan limes inn i en ny chat uten ytterligere kontekst.

**Bakgrunn for prompten:** Et første forsøk 11.10.2026 produserte en
tynn, feilaktig rapport (feil beløp, 271 linjer, 1-setnings «analyser»
på komplekse temaer). Prompten under er resultatet av iterativ
feilsøking: hvorfor sviktet forrige kjøring, og hvilke konkrete
instruksjoner forhindrer samme svikt neste gang.

**Modellvalg:** Research-agenter: Sonnet (fem parallelle). Orkestrator/
syntese/review: Opus (den chat prompten limes inn i). Alternativ:
alle på Opus for høyere konsistens, høyere kostnad.

**Tidsbudsjett:** 180 minutter default. Minimum 90 for noe nyttig.
Over 240 gir diminishing returns.

**Fil-output:** `bakgrunn/brann/strategi_tvangsmulkt_<ISO-dato>/` med
én fil per iterasjon pluss review-filer og logg.

**Advarsel ved bruk:** Prompten starter kjøring umiddelbart når den
limes inn. Hvis du vil justere faktaarket før agentene starter, legg
til «vis faktaark og vent 2 minutter før første iterasjon» i prompten.

---

## Selve prompten (kopiér fra kodeblokken under)

```
# OPPDRAG: Iterativ strategianalyse mot tvangsmulkt — Fjordgata 30

Du er orkestrator for et iterativt dypdykk i strategiske muligheter for å
unngå, redusere eller forsinke en norsk tvangsmulkt mot KodeWorks Eiendom
AS. Du kjører et antall iterasjoner til du er tom for tid. Siste iterasjon
er leveransen.

## TIDSBUDSJETT
Du har 180 minutter totalt fra oppdragsstart. Noter starttidspunkt.
Oppdraget kan overstyres av bruker — hvis bruker sier «budsjett N minutter»
ved start, bruk det tallet i stedet, men ikke under 90.

Stop-vilkår: Avbryt iterasjonsløkken når
    (gjenstående_minutter) < (snitt_minutter_per_iterasjon_hittil × 1.2)
Da anses siste fullførte iterasjon som rapporten.

## HARDE KRAV — IKKE OMFORMULERBARE

### K1. Iterativ natur
Dette er ikke én kjøring. Det er flere iterasjoner. Første iterasjon
kjører alle 5 research-agenter fra bunnen. Etterfølgende iterasjoner
kjører bare de agentene reviewen har flagget som svake, pluss ny syntese
som bygger på forrige iterasjon og reviewens funn. Bruker ser ikke
mellomresultat — bruker venter til stop-vilkår inntreffer og leser den
siste filen.

### K2. Filstruktur
Opprett ved start en mappe:
    bakgrunn/brann/strategi_tvangsmulkt_<ISO-dato>/
Legg i den:
    faktaark.md
    iterasjon_01_<HHMM>.md
    review_01.md
    iterasjon_02_<HHMM>.md
    review_02.md
    ...
    logg.md             (en linje per iterasjon: tidsbruk, antall linjer,
                         hvilke agenter som ble kjørt, review-funn)
    rapport_final.md    (kopieres fra siste iterasjon når stop-vilkår treffer)
Ingen fil overskrives. Hver iterasjon får ny fil.

### K3. Omfang
Final-rapport minimum 2 000 linjer, forventet 2 500–4 000. Hver av de
fem analyseaksene skal ha minst 12 reelt drøftede underpunkter, hvert
minst 400 ord. Review-skritt skal eksplisitt flagge seksjoner under
denne terskelen.

### K4. Format
Komplekse argumenter skrives som PROSA. Punktlister bare for lister uten
vurdering (navn, datoer, kontaktinfo, lovreferanser). Setninger som «EMK
P1-1 er egnet som proporsjonalitetsargument» er forbudt — vis hvorfor,
mot hvilken rettspraksis, med hvilken forventet motstand fra TBRT, med
hvilken konkret anførselstekst som trolig vinner frem.

Negativt eksempel:
    **Fisjon av KWE**
    Fisjon isolerer historisk mulkt i gammelt KWE, men asl § 14-11 gir
    solidaransvar begrenset til nettoverdi.

Positivt eksempel:
    ### Fisjon av KWE med isolering av tvangsmulkten i overdragende
    selskap

    Grunntanken er å splitte KodeWorks Eiendom AS i (minst) to selskaper
    gjennom fisjon etter aksjeloven kapittel 14, slik at Fjordgata
    30-eiendommen overdras til et nytt selskap («Fjordgata 30 AS») mens
    forpliktelsen rundt tvangsmulkt forblir i det overdragende KWE. For
    at manøvren skal ha praktisk effekt mot TBRTs krav, må vi forstå
    nøyaktig hvordan solidaransvaret i asl § 14-11 virker, hvilken
    verdsettelsesnorm som brukes for «nettoverdi», og hvilke mottrekk
    TBRT har tilgjengelig gjennom kreditorinnsigelse etter asl § 14-7.

    [Deretter: 400+ ord konkret drøfting av hvert punkt, konkrete
    tall-eksempler på nettoverdiberegning, hvordan den kan reduseres
    gjennom pantsettelse før fisjon, kreditorvarslingsprosedyre med
    frister, hva som skjer hvis TBRT reiser innsigelse, hva som skjer
    hvis de ikke gjør det, verdsettelsesspørsmål ved tvangsdekning,
    interaksjon med dekningsloven § 5-9 omstøtelsesregler, risiko for
    gjennomskjæring etter skatteloven § 13-1, konkrete norske rettssaker
    som har prøvet tilsvarende manøvre.]

### K5. Faktaforankring
Alle beløp, datoer, saksreferanser og hendelser skal spores til
faktaarket. Faktaarket skal spores til primærkilder i prosjektet eller
eksterne kilder med URL + hentedato. Alle lovsitater skal hentes verbatim
fra lovdata.no via curl og siteres med URL + hentedato. Ingen tall skal
fremkomme uten kilde. Hvis en agent rapporterer tall som avviker fra
faktaarket, stopp, verifiser, korrigér faktaarket eller korrigér agentens
output — og dokumentér i review-filen.

### K6. Målgruppe
Operasjonell for en jurist eller strategirådgiver som skal handle direkte
på rapporten — ikke sammendrag til styremøte. Bruk konkrete utkast til
formulering der det er mulig («slik bør avsnittet i søknaden til DSB lyde:
...», «slik bør brevet til Representantskapet åpne: ...»).

### K7. Verktøyvalg
Dette oppdraget krever verbatim kilder (lovtekst, forvaltningsuttalelser,
saksdokumenter som skal siteres). WebFetch er DISKVALIFISERT for dette
oppdraget — verktøyet returnerer AI-parafrasert innhold som er farlig i
juridisk arbeid. Bruk WebSearch for breddesøk og curl via Bash for all
verbatim henting. Parse HTML med regex eller BeautifulSoup via
`uv run python` ved behov. Dette overstyrer prosjektets default-regel
(som tillater WebFetch for hverdagsoppslag) — i denne oppgaven er curl
eneste tillatte henting av tekst.

### K8. Agentkonfigurasjon
Research-agenter: `subagent_type: general-purpose`, `model: sonnet`,
UTEN `isolation: worktree`. Syntese- og review-arbeid gjør du selv
(orkestrator). Etter hver iterasjon kjør `ls .claude/worktrees/` og
rapportér avvik i logg.md.

### K9. Lovforankring
Når en strategi støtter seg på en konkret lovparagraf, last ned
paragrafens ordlyd verbatim fra lovdata.no via curl og sitér med URL +
hentedato. Ikke parafrasér lovtekst.

### K10. Chat-adferd
Minimér chat-utspill. Hver iterasjon: én linje som rapporterer
tidsstempel, hvilke agenter som ble kjørt, linjetall i produsert
iterasjon, antall svakheter identifisert av review. Ingen innhold fra
rapporten dumpes i chat. Final-leveranse: en kort oppsummering som peker
på rapport_final.md.

## PROSESS

### Steg 0: Oppstart
    - Noter starttidspunkt. Beregn deadline.
    - Les CLAUDE.md, historikk.md, TASKS.md, ARCHIVE.md (søk tvangsmulkt-
      relaterte oppføringer), alle filer i `bakgrunn/brann/` som gjelder
      tvangsmulkt (prioritér nyeste + de som nevner Intrum, konkursvarsel,
      DSB, Sivilombudet, bero-beslutning), alle filer i `leveranser/brann/`
      fra siste 60 dager, relevante filer i `bakgrunn/lovverk/`.
    - Opprett iterasjonsmappen.

### Steg 1: Faktaark
Produsér faktaark.md som dekker minimum:
    - Nøyaktige datoer og saksnumre for alle TBRT-vedtak
    - Nøyaktig påløpt mulkt per vedtak (dagsats, startdato, perioder med
      bero/stans), skilt mellom «teoretisk påløpt» og «faktisk krevd inn
      gjennom Intrum»
    - Nøyaktig beløp oversendt Intrum med saksnummer
    - Status for alle pågående klager (DSB, Sivilombudet) med datoer og
      saksnumre
    - Status for rammesøknad med saksnummer og dato
    - Alle navngitte saksbehandlere hos TBRT, DSB, Byantikvaren, kommunen
    - Alle støttebeløp (Kulturminnefondet, Byantikvaren, Enova, UNI) med
      tildelingsdatoer
    - Fisjonsstatus — planlagt, besluttet, gjennomført?
    - Rettslig status for Fjordgata 30 (verneklasse, pbl-krav)
    - Konkursvarselstatus med forkynnelsesdato og frister
Ukjente punkter: skriv «UKJENT — må bekreftes av bruker». Ikke dikt opp.
Legg faktaarket i mappen. Vis det IKKE i chat (unntatt en kort linje som
sier at det er skrevet og hvilke punkter som er UKJENT). Fortsett.

### Steg 2: Første iterasjon (full)
Start 5 research-agenter i parallell med spesifikasjonene under. Hver
agent får:
    - Hele faktaarket som bindende grunnlag
    - Sitt perspektiv og mindset
    - Alle harde krav K3–K9
    - Ingen tidsinstruksjon (de skal arbeide til de er grundig ferdige,
      ikke til en bestemt klokkeslett)
    - Instruks om minimum 12 underpunkter à minst 400 ord

Når alle 5 har returnert: skriv iterasjon_01_<HHMM>.md ved å integrere
materialet etter rapportstrukturen (se nedenfor). Ikke destiller —
bevar agentenes dybde.

Oppdatér logg.md: iterasjonsnummer, start- og sluttidspunkt, antall
linjer i iterasjonsfilen, hvilke agenter som ble kjørt, kort kommentar.

### Steg 3: Review
Les iterasjon_NN_<HHMM>.md. Produsér review_NN.md som eksplisitt
identifiserer:
    - Seksjoner under 400 ord
    - Punktlister der prosa kreves
    - Tall uten kilde
    - Lovsitater som ikke er verbatim fra lovdata
    - Manglende konkrete handlingsutkast
    - Faktaavvik mellom agenter som ikke er løst
    - Manglende mottrekk-analyse («hva gjør TBRT, hva gjør vi deretter»)
    - Manglende drøfting av strategikonflikter og rekkefølge
    - Hvilke underpunkter som bør utvides
    - Hvilke nye underpunkter som bør legges til
For hvert funn: hvilken agent-domene det tilhører.

### Steg 4: Stop-sjekk
Beregn snitt_minutter_per_iterasjon basert på logg.md. Beregn
gjenstående_minutter. Hvis
    gjenstående_minutter < snitt_minutter_per_iterasjon × 1.2
→ gå til Steg 6.
Ellers → Steg 5.

### Steg 5: Målrettet iterasjon
Start kun de agentene hvis domene har review-funn. Hver agent får:
    - Faktaarket
    - Forrige iterasjons innhold for sitt domene
    - review_NN.md sine funn for sitt domene
    - Spesifikk instruks: «utvid, fordyp, legg til, korrigér»
Når agentene har returnert, skriv iterasjon_(NN+1)_<HHMM>.md ved å:
    - Starte fra forrige iterasjon
    - Erstatte oppdaterte seksjoner med nytt innhold
    - Legge til nye seksjoner identifisert av reviewen
    - Beholde alt som ikke er flagget
Oppdatér logg.md. Gå til Steg 3.

### Steg 6: Final-leveranse
    - Kopiér siste iterasjon til rapport_final.md
    - Egen-review: les gjennom hele rapporten. Hvis fortsatt noe under
      400 ord, bulletlister der prosa kreves, eller tall uten kilde:
      flagg i egen seksjon «Kjente svakheter ved stopp» i slutten av
      rapporten.
    - Kjør `ls .claude/worktrees/` og rapportér.
    - Kort chat-oppsummering: antall iterasjoner, totalt tidsforbruk,
      linjetall, filsti til rapport_final.md.

## AGENTSPESIFIKASJONER

Hver agent-prompt starter med dette grunnavsnittet (fyll inn
faktaarkets tekst og agentspesifikke seksjoner):

    FAKTAGRUNNLAG (bindende — alle tall og datoer i din leveranse skal
    spores hit):
    [Faktaarkets fulle tekst]

    HARDE KRAV:
    - WebFetch er diskvalifisert for dette oppdraget (parafraserer
      juridisk tekst). Bruk WebSearch og curl via Bash — ingen unntak.
    - Lovsitater: last ned verbatim fra lovdata.no via curl, inkludér
      URL og hentedato.
    - Komplekse argumenter: prosa, ikke punktliste.
    - Hvert underpunkt minst 400 ord.
    - Minimum 12 underpunkter.
    - Alle tall skal ha kilde.
    - For hver strategi: hjemmel, konkret handling, forventet motstand,
      mottrekk, interaksjon med andre strategier, konkret utkast til
      formulering der mulig.

### Agent 1 — Maksimalistjurist
Mindset: Norsk forvaltningsrettsadvokat med 25 års erfaring som nekter å
overse noen kanal. Du leter etter hjemler, ikke konklusjoner. Hver kanal
utredes selv om den sannsynligvis ikke vinner frem — parallellitet er
strategien.

Minimum underpunkter (12+, utvid gjerne): DSB-frafall bel. § 39,
Statsforvalterklage (IKS-kompetanse), omgjøring fvl. § 35, utsatt
iverksetting fvl. § 42, søksmål om ugyldighet fvl. § 50, midlertidig
forføyning tvl. kap. 34, innsigelser etter tvfl., klage i
konkursbegjæringssaken, EMK P1-1 proporsjonalitet, EMK art. 6,
Grunnloven § 102, sakskostnader fvl. § 36, ettergivelse/nedsettelse fvl.
§ 51, konstateringskrav fvl. § 51 annet ledd (umulighet),
erstatningssøksmål mot TBRT, DSB-overprøving.

### Agent 2 — Prosessguerilla
Mindset: Aggressiv prosessør som ser hver forvaltningsmessig unnlatelse
som en åpning. Fokus: utredningsplikt, kontradiksjon, begrunnelsesplikt,
innsyn, foreldelse, saksbehandlingstid, habilitet. Ikke «unngå straff» —
«hvordan er saken sabotert av TBRT på en måte som gjør vedtakene
ugyldige».

Minimum underpunkter (12+): utredningspliktsfeil fvl. § 17, faktafeil
som bestemmende fvl. § 41, kontradiksjonsbrudd, begrunnelsesmangler
fvl. §§ 24-25, foreldelse fl. §§ 2/3/17 (konkret regning per periode),
Sivilombudets 2023-prinsipp om utsatt iverksetting-forsinkelse,
inhabilitet fvl. § 6, upresis angivelse av påleggsinnhold (Sivilombudet
2009/848), innsynsoffensiv fvl. § 18 c og offentleglova, treghet i
klagebehandling fvl. § 11a, krav om fornyet behandling ved endret
faktum, uforholdsmessig inndrivingstiltak.

### Agent 3 — Selskapsrettslig arkitekt
Mindset: M&A-advokat under tidspress. Ingen manøver skal utgjøre
kreditorsvik eller omgåelse. Legal defense in depth gjennom
selskapsstruktur, pant, rekonstruksjon.

Minimum underpunkter (12+): fisjon asl kap. 14 og solidaransvar asl §
14-11, kreditorvarsling asl § 14-7, bankpant tinglyst før
utleggsforretning, holdingstruktur, overføring til markedspris,
rekonstruksjon, IKS-krav mot eierkommunene (IKS-loven § 3, § 38),
dekningsloven § 5-9 omstøtelse, skatteloven § 13-1 gjennomskjæring,
konkursfølger for TBRT som uprioritert fordring, massefordring vs
alminnelig fordring, styreansvar asl § 17-1, straffansvar strl § 406,
forhandling om nedbetaling/nedsettelse, gjeldsforhandling, SI vs Intrum.

### Agent 4 — Politisk strateg
Mindset: PR- og politisk kommunikasjonsstrateg, 20 års erfaring med
forvaltningssaker. Sivilombudet reagerer negativt på åpenbart koordinert
press — men offentlig narrativ forskyver maktbalansen når det bygges
rett. Finn navngitte personer, konkrete publikasjoner, konkrete
politiske kanaler.

Minimum underpunkter (12+): «stat mot stat»-narrativ (oppbygning +
motnarrativ-håndtering), lokale medier med navngitte journalister,
nasjonale medier, kronikk-strategi med utkast til vinkling,
Fortidsminneforeningen og Rødlista, Riksantikvaren, Norges
Kulturvernforbund, Byantikvaren som intern alliert, Trondheim bystyre og
interpellasjon, TBRTs representantskap som omgjøringsorgan, Stortinget
med skriftlig spørsmål, Trondheim kontrollutvalg og kommunerevisjon,
Statsforvalteren, kommunevalget 2027 som timing.

### Agent 5 — Djevelens advokat
Mindset: Du ser etter manøvre de fire andre overser. Game theory-
forhandler. Absolutt regel: ingen anbefaling bryter norsk lov, ingen
trusler, ingen falske tips, ingen trakassering. Men pragmatisk-aggressiv
innenfor loven: asymmetrier, jurisdiksjonshull, institusjonelle
svakheter hos TBRT, timing-trekk.

Minimum underpunkter (12+): rettslig umulighet som nytt frafallsgrunnlag
(DSB uprøvd), tolkningsveiledning fvl. § 11, objektendring (tomt bygg,
redusert risikoklasse), fradik etter TEK17 § 11-12, formell
Byantikvar-uttalelse om søknadsplikt, deloppfyllelse brannforskriften
§ 8, kompartmentering i brannseksjoner, negativ fastsettelsesdom,
Representantskapet som omgjøringskanal, motregning mot TBRT for
forsinkelse, kostnadsavtale, tredjepartsmegling via bank/Byantikvar,
riksrevisjonsinnslag, forliksrådet, kreative strategikombinasjoner.

## RAPPORTSTRUKTUR (gjelder hver iterasjonsfil og final)

    # [tittel]

    ## Metadata
    Dato, iterasjonsnummer, hvilke agenter som bidro, hvor lenge
    iterasjonen varte, hvilke avvik mellom agentene som ble flagget og
    hvordan de ble løst.

    ## Verifisert sakssituasjon (fra faktaarket)
    Full tekst av faktaarket.

    ## Umiddelbare prioriteringer (neste 7 dager)
    Prosa med rangering og begrunnelse. Minimum 500 ord.

    ## Del 1 — Formelle rettsmidler (Agent 1-materiale)
    Minimum 15 % av dokumentet. Minimum 12 underpunkter à 400+ ord.

    ## Del 2 — Prosessuelle forsinkelser (Agent 2)
    Minimum 15 %. Samme krav.

    ## Del 3 — Selskapsrettslige grep (Agent 3)
    Minimum 15 %.

    ## Del 4 — Mediestrategi og politisk mobilisering (Agent 4)
    Minimum 15 %.

    ## Del 5 — Kreative/ukonvensjonelle manøvre (Agent 5)
    Minimum 15 %.

    ## Kombinasjonsstrategier
    Minimum 800 ord. Hvordan strategier forsterker eller konflikter med
    hverandre, hvilken rekkefølge, hvilke fallgruver.

    ## Hva som er over streken — eksplisitt
    Manøvre forkastet som ulovlige, med begrunnelse.

    ## Forventet motstand fra TBRT og mottrekk
    For hver av våre hovedstrategier: hva TBRT sannsynligvis gjør, og
    vårt neste trekk.

    ## Risiko- og sannsynlighetsmatrise
    Prosa som drøfter, deretter tabell som oppsummerer.

    ## Konkrete utkast
    Utkast til brev, formuleringer, anførsler som kan brukes direkte.

    ## Kildeliste
    Alle lover med lovdata-URL og hentedato, alle presedenser, alle
    nettsider.

    ## Kjente svakheter ved stopp (kun i final)
    Hva som ikke rakk å bli grundig nok. Hva som bør addresseres i en
    etterfølgende kjøring.

## STARTINSTRUKS

1. Noter starttidspunkt. Beregn deadline.
2. Les prosjektfiler (Steg 0).
3. Opprett iterasjonsmappen.
4. Produsér faktaark (Steg 1). Rapportér i chat med én linje: «faktaark
   skrevet; N UKJENT-punkter».
5. Kjør full første iterasjon (Steg 2). Én linje i chat.
6. Review (Steg 3). Én linje i chat med antall funn.
7. Stop-sjekk (Steg 4). Hvis stopp: gå til Steg 6. Ellers: Steg 5.
8. Målrettet iterasjon (Steg 5). Én linje i chat. Tilbake til Steg 3.
9. Final-leveranse (Steg 6). Kort oppsummering i chat.

Begynn med Steg 0.
```
