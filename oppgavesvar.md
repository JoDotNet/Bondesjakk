# Svar på oppgaver - Tre på rad

## Del 1: Forståelse av "Tre på rad"

### Oppgave 1:
- **Målet med spillet:** Å få tre like symboler (X eller O) på rad - horisontalt, vertikalt eller diagonalt
- **Hvordan spilles det:** To spillere bytter på å plassere symbolene sine (X og O) på et 3x3 brett
- **Nødvendige komponenter:**
  - Brett-klasse for å håndtere spillbrettet og dets tilstand
  - Spiller-klasse for å håndtere spillerinformasjon og symboler
  - Spill-klasse for å kontrollere spillflyten
  - System for å registrere og validere trekk
  - System for poengberegning

## Del 2: Grunnleggende OOP-konsepter

### Oppgave 2:
I min implementasjon bruker jeg:
- **Klasser:** Brett, Spiller, og Spill som maler
- **Objekter:** Konkrete instanser som spiller1, spiller2, og brettet

### Oppgave 3:
- **Formål med konstruktør:** Å initialisere nye objekter med startverdier
- **Definisjon i Python:** Ved bruk av `__init__`-metoden som kjøres automatisk når et nytt objekt opprettes

### Oppgave 4:
Attributter er egenskaper eller data som tilhører objektet (som navn eller symbol), mens metoder er funksjoner som definerer hva objektet kan gjøre (som å gjøre et trekk eller sjekke for vinner).

## Del 5: Forståelse av 2D-lister

### Oppgave 7:
- Man får tilgang til en bestemt celle ved å bruke indekser: `brett[rad][kolonne]`
- `brett[1][2]` representerer cellen i andre rad (indeks 1) og tredje kolonne (indeks 2)

## Del 11: Diskusjon om Lagring av Objekter

### Oppgave 18:
Vi valgte 2D-liste fordi:
- Det gir en naturlig representasjon av brettet
- Lett å visualisere og forstå
- Enkel tilgang til celler med rad/kolonne-indeksering

Alternative lagringsmåter:
- **Ordbok:**
  - Fordeler: Fleksibel, kan ha vilkårlige posisjoner
  - Ulemper: Mer komplisert å implementere
- **1D-liste:**
  - Fordeler: Enkel datastruktur
  - Ulemper: Mindre intuitiv, krever konvertering mellom 1D og 2D posisjoner

## Del 12: Refleksjon over OOP-konsepter

### Oppgave 19:
OOP har hjulpet med:
- Organisering av kode i logiske enheter
- Gjenbruk av kode
- Lettere vedlikehold
- Mer oversiktlig struktur

Eksempler på bruk:
- Konstruktører: Initialisering av spillere og brett
- Attributter: Spillernavn, symboler, bretttilstand
- Metoder: Trekk-håndtering, vinnersjekk

## Del 14: Oppsummering

### Oppgave 21:
Læringsutbytte:
- Strukturering av kode i klasser og objekter
- Praktisk anvendelse av OOP-prinsipper
- Viktigheten av god planlegging
- Håndtering av spillogikk

### Oppgave 22:
For å legge til poengtellingsfunksjonalitet:
- Lagt til `score` attributt i Spiller-klassen
- Implementert metode for å oppdatere poeng
- Vis poengoversikt etter hver runde
- Lag mulighet for å spille flere runder