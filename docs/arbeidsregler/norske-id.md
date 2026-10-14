# Norske personnummer og D-nummer

Utdyping av kjerneregelen fra `CLAUDE.md`: sjekk formatet før du flagger et 11-sifret nummer som ugyldig.

## Formatene

11-sifret norsk ID kan være enten fødselsnummer eller D-nummer.

- **Fødselsnummer** starter med DDMMYY (dag 01–31).
- **D-nummer** (tildeles utenlandske arbeidstakere) har samme struktur, men **dagsifrene er +40** (dag 41–71).

En person født 06.06.1973 har D-nummer som starter med `46 06 73 ...` (06+40=46).

## Praktisk regel

Sjekk begge norske formater før du antar at et 11-sifret nummer er utenlandsk (estisk isikukood eller lignende).

Særlig relevant i Fjordgata 30 fordi flere ansatte (Ain, Marko) er estiske men jobber i Norge og trenger norsk ID for A-melding.
