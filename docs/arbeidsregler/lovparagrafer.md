# Lovparagrafer – verifisering før sitering

Utdyping av kjerneregelen fra `CLAUDE.md`: lovparagrafer skal verifiseres mot nedlastet verbatim kilde før de siteres, både i leveranser og i chat/utkast.

## Grunnregel for leveranser

Når en leveranse (klage, søknad, notat, rapport) refererer til en konkret lovparagraf, skal paragrafens ordlyd lastes ned verbatim fra lovdata.no og lagres som egen .md-fil i `bakgrunn/lovverk/` (eller `forretningsplan/lover/` for MVA-paragrafer). Lagre bare refererte paragrafer, ikke hele loven.

Filnavn: `<lov_kortnavn>_<paragraf>_<beskrivelse>.md` (eks. `fvl_17_utredningsplikt.md`, `sivilombudsloven_8_vilkar_klage.md`, `mval_3-11_fast_eiendom.md`).

Hver fil skal ha metadata-header med lovens fulle tittel, dato/lovnr., lovdata-URL og hentedato — deretter paragraftekst verbatim.

- Finnes paragrafen allerede som fil: re-verifisér at leveransens sitater og paragrafhenvisning stemmer mot filen før utsending.
- Finnes den ikke: last ned først.

**Grunn:** Feil paragrafreferanse eller unøyaktig sitat kan gjøre et dokument juridisk ugyldig — særlig kritisk for klager til Sivilombudet, DSB, Skatteetaten, byggesakskontor og lignende forvaltningsorganer der hjemmelsgrunnlaget er beviset.

## Hele-loven-filer

Hele-loven-filer som allerede ligger i `bakgrunn/lovverk/` (eks. `forvaltningsloven.md`) kan brukes som kilde, men da må den konkrete paragrafens tekst likevel ekstraheres til egen fil ved første referanse — hele-loven-filer er fortsatt gyldige som referansegrunnlag, men gir ikke samme kildesikkerhet som en paragraf-fil med lovdata-URL og hentedato.

## Også for utkast, forslag og chat

Dette gjelder også for utkast, forslag og tekst i chat — ikke bare for ferdige leveranser.

Før du navngir en konkret paragraf, ledd eller punktum (eks. «fvl § 29», «offentleglova § 32 andre ledd», «brann- og eksplosjonsvernloven § 39 tredje punktum») i *noe* du produserer — chat-svar, utkast, forslag, plan, oppsummering — må du først bekrefte at paragrafen finnes som verifisert .md-fil i `bakgrunn/lovverk/` eller `forretningsplan/lover/` med metadata-header og verbatim tekst.

Finnes den ikke, enten:

- (a) last ned først, eller
- (b) omformulér til generelt språk uten paragrafnavn («etter forvaltningsloven», ikke «etter fvl § 29»; «etter offentleglovas klageregler», ikke «etter offl § 32 andre ledd»).

Særlig kritisk for ledd-, bokstav- og punktum-henvisninger — disse er påstander om tekstens strukturering som brukeren ikke rimelig kan dobbeltsjekke uten å gå til Lovdata selv.

**Grunn:** Brukere limer regelmessig chat-utkast rett inn i e-post eller inn i en kommende leveranse, så en feil paragrafhenvisning i chat går like gjerne ut til mottaker som en feil i en ferdig fil. Verbatim-reglen for leveranser blir da for sent utløst — feilen er allerede inkorporert i det brukeren jobber med. Paragraf-, ledd- og punktum-henvisninger fra hukommelsen går jevnlig galt (feil paragraf, feil ledd, hallusinert regel), så minimumsterskelen må være en faktisk filverifisering i samme samtale.

**Symptom å se etter i egne svar før du sender:** naken «§ X», «jf. § Y andre ledd», «hjemmel i § Z» uten at Glob/Grep/Read av lovverk-mappen er gjennomført tidligere i samme samtale.

Ved tvil: omformulér uten paragrafnavn eller stopp og last ned.
