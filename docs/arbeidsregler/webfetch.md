# WebFetch – når det er trygt, når det ikke er

Utdyping av kjerneregelen fra `CLAUDE.md`: WebFetch er tillatt for hverdagsoppslag, men forbudt for verbatim-tekst til leveranser og under brukerens override.

## Hvorfor det er en risiko

WebFetch returnerer AI-prosessert innhold: en liten modell oppsummerer, parafraserer eller kutter lange sider i stedet for å gi rå tekst. Dette er katastrofalt for juridisk arbeid, der parafraserte lovsitater kan ødelegge en sak.

Audit 06.10.2026 (`T157`) avdekket at verktøyet systematisk ga sammendrag for lange paragrafer selv når prompten eksplisitt bad om verbatim — og at parafrasene hadde glidd inn i leveranser sendt til forvaltningsorganer.

## Default-regel

For lovsitater, forskriftssitater, formelle uttalelser fra forvaltningsorganer, og all annen tekst der verbatim ordlyd skal inn i en leveranse — bruk `curl` via Bash-verktøyet, ikke WebFetch. Kombiner med egen HTML-parsing (regex eller BeautifulSoup via `uv run python`) for ekstraksjon.

For hverdagsoppslag der et sammendrag holder (selskapsinfo, generelle nettsider, bakgrunnslesing) er WebFetch greit og ofte raskere.

## Brukerens override

Når brukeren sier «bruk curl», «ikke bruk webfetch», «curl bare» eller lignende i en samtale eller prompt, er WebFetch forbudt for hele den samtalen — ingen unntak — inntil brukeren eksplisitt opphever det.

## Grunnregelen

Parafrase er aldri verdt risikoen når brukeren har bedt om rå tekst eller når leveransen skal til forvaltningsorganer.
