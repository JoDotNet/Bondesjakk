# Arbeidsark: Innføring i Objektorientert Programmering med "Tre på rad"

---

## **Introduksjon**

Dette arbeidsarket vil veilede deg gjennom utviklingen av spillet **"Tre på rad"** ved hjelp av **objektorientert programmering (OOP)** i Python. Målet er å forstå og anvende de grunnleggende konseptene i OOP, inkludert **klasse**, **objekt**, **konstruktør**, **attributter** og **metoder**. Du vil også lære om hvordan man best kan lagre objekter, bruke **UML-diagrammer** for å planlegge programmet ditt, og diskutere hvilke datastrukturer som passer best for lagring av spilltilstanden.

---

## **Del 1: Forståelse av "Tre på rad"**

Før vi begynner å programmere, er det viktig å forstå spillets regler og mekanikk.

### **Oppgave 1:**

- **Beskriv spillet "Tre på rad":**
  - Hva er målet med spillet?
  - Hvordan spilles det?
  - Hvilke komponenter trenger vi for å lage spillet?

**Diskuter med sidemannen og noter svarene dine.**

---

## **Del 2: Grunnleggende OOP-konsepter**

### **1. Klasse og Objekt**

- **Klasse**: En mal eller blåkopi som definerer egenskapene og oppførselen til objekter.
- **Objekt**: En instans av en klasse med konkrete verdier.

### **Oppgave 2:**

- **Forklar forskjellen mellom en klasse og et objekt med egne ord.**

---

### **2. Konstruktør**

- **Konstruktør**: En spesialmetode i en klasse som brukes til å initialisere nye objekter.

### **Oppgave 3:**

- **Hva er formålet med en konstruktør i en klasse?**
- **Hvordan definerer du en konstruktør i Python?**

---

### **3. Attributter og Metoder**

- **Attributter**: Variabler som lagrer objektets tilstand eller egenskaper.
- **Metoder**: Funksjoner som definerer objektets oppførsel.

### **Oppgave 4:**

- **Hva er forskjellen mellom attributter og metoder?**

---

## **Del 3: Introduksjon til UML-diagrammer**

**UML (Unified Modeling Language)** er et visuelt verktøy som brukes til å planlegge og dokumentere systemer i objektorientert programmering. Et UML-klassediagram viser klassene i systemet, deres attributter, metoder og relasjoner til hverandre.

### **Eksempel på et UML-klassediagram:**

```
+----------------+
|    KlasseNavn  |
+----------------+
| - attributt1   |
| - attributt2   |
+----------------+
| + metode1()    |
| + metode2()    |
+----------------+
```

**Symbolforklaring:**

- **Klassenavn**: Navnet på klassen.
- **Attributter**: Variabler i klassen (minustegn indikerer private, men i Python brukes ofte public attributter).
- **Metoder**: Funksjoner i klassen (plustegn indikerer public metoder).

### **Oppgave 5:**

- **Hvorfor er UML-diagrammer nyttige når vi planlegger et program?**
- **Hvordan kan de hjelpe oss med å forstå strukturen i programmet?**

---

## **Del 4: Planlegging av "Tre på rad" med UML-diagram**

Før du begynner å kode, er det nyttig å planlegge strukturen ved hjelp av et UML-diagram.

### **Oppgave 6:**

- **Tegn et UML-diagram for "Tre på rad" med følgende klasser:**
  - **Spill**
  - **Brett**
  - **Spiller**

- **For hver klasse, inkluder:**
  - **Attributter (med datatype)**
  - **Metoder (med parameterliste)**

### **Forklaring av klassene:**

- **Spill-klasse**:
  - **Formål**: Kontrollerer spillflyten. Den håndterer veksling mellom spillere, sjekker for seier eller uavgjort, og starter spillet.
  - **Hvorfor trenger vi denne klassen?**: Selv om det kan virke overflødig, hjelper denne klassen oss med å organisere koden og holde spilllogikken atskilt fra andre deler. Det gjør koden mer modulær og enklere å vedlikeholde.

- **Brett-klasse**:
  - **Formål**: Representerer spillbrettet. Den lagrer tilstanden til brettet og inneholder metoder for å oppdatere og vise brettet, samt sjekke for vinnende kombinasjoner.
  - **Hvorfor trenger vi denne klassen?**: Brettet er en sentral del av spillet, og å ha en egen klasse gjør det enkelt å håndtere brettets tilstand og operasjoner på det.

- **Spiller-klasse**:
  - **Formål**: Representerer en spiller i spillet. Den lagrer spillerens navn og symbol (f.eks. 'X' eller 'O').
  - **Hvorfor trenger vi denne klassen?**: Hver spiller har egne egenskaper, og å representere dem som objekter gjør det enklere å administrere spillernes tilstander og handlinger.

**Diskuter i grupper og del dine UML-diagrammer med klassen.**

---

## **Del 5: Forståelse av 2D-lister (matriser)**

Et **2D-liste**e er en liste av lister i Python, som kan brukes til å representere et rutenett som i "Tre på rad".

### **Visualisering av brettet:**

```
+---+---+---+
|   |   |   |   Rad 0
+---+---+---+
|   |   |   |   Rad 1
+---+---+---+
|   |   |   |   Rad 2
+---+---+---+
  Kol 0 Kol 1 Kol 2
```

I koden representeres dette som:

```python
brett = [
    [' ', ' ', ' '],  # Rad 0
    [' ', ' ', ' '],  # Rad 1
    [' ', ' ', ' ']   # Rad 2
]
```

### **Oppgave 7:**

- **Hvordan får du tilgang til en bestemt celle i brettet?**
- **Hva representerer `brett[1][2]`?**

**Svar:**

- `brett[rad][kolonne]`, så `brett[1][2]` refererer til raden med indeks 1 og kolonnen med indeks 2 (midterste rad, høyre kolonne).

---

## **Del 6: Implementering av Klassene**

Nå skal du begynne å implementere klassene i Python.

#### **Klassen `Spiller`**

### **Oppgave 8:**

- **Definer klassen `Spiller` med følgende:**
  - **Attributter:**
    - `navn` (str)
    - `symbol` (str) - enten 'X' eller 'O'
  - **Konstruktør som initialiserer attributtene**

**Formål med `Spiller`-klassen:**

- **Lagres spillerinformasjon**: Navn og symbol.
- **Enkelt å utvide**: Kan legge til flere egenskaper senere, som poengsum.

**Eksempel:**

```python
class Spiller:
    def __init__(self, navn, symbol):
        self.navn = navn
        self.symbol = symbol
```

#### **Klassen `Brett`**

### **Oppgave 9:**

- **Definer klassen `Brett` med følgende:**
  - **Attributter:**
    - `rutenett` - en 3x3 2D-liste som representerer brettet
  - **Konstruktør som initialiserer `rutenett` til en 3x3 liste fylt med tomme strenger**

**Formål med `Brett`-klassen:**

- **Lagres tilstanden til brettet**.
- **Inneholder metoder for å oppdatere og vise brettet**.

**Eksempel:**

```python
class Brett:
    def __init__(self):
        self.rutenett = [
            [' ', ' ', ' '],  # Rad 0
            [' ', ' ', ' '],  # Rad 1
            [' ', ' ', ' ']   # Rad 2
        ]
```

```python
class Brett:
    def __init__(self):
        self.rutenett = [[' ' for _ in range(3)] for _ in range(3)]
```



**Forklaring:**

- **Listeforståelse**: Vi bruker listeforståelse for å lage en 3x3 matrise.
- **Tomme strenger**: Representerer tomme celler på brettet.

### **Oppgave 10:**

- **Implementer metoden `vis_brett()` som viser brettet på en lesbar måte**

**Eksempel:**

```python
    def vis_brett(self):
        for i, rad in enumerate(self.rutenett):
            print(' | '.join(rad))
            if i < 2:
                print('---------')
```

**Visualisering:**

```
  |   |  
---------
  |   |  
---------
  |   |  
```

### **Oppgave 11:**

- **Implementer metoden `oppdater_brett(rad, kolonne, symbol)` som plasserer et symbol på brettet hvis plassen er ledig**

**Eksempel:**

```python
    def oppdater_brett(self, rad, kolonne, symbol):
        if self.rutenett[rad][kolonne] == ' ':
            self.rutenett[rad][kolonne] = symbol
            return True
        else:
            print("Plassen er allerede opptatt. Prøv igjen.")
            return False
```

---

## **Del 7: Spilllogikk i `Brett`-klassen**

#### **Metoden `sjekk_vinner(symbol)`**

### **Oppgave 12:**

- **Implementer metoden `sjekk_vinner(symbol)` som sjekker om en spiller har tre på rad**

**Formål:**

- **Sjekke for vinnende kombinasjoner**: Rader, kolonner og diagonaler.

**Eksempel:**

```python
    def sjekk_vinner(self, symbol):
        # Sjekk rader
        for rad in self.rutenett:
            if all([celle == symbol for celle in rad]):
                return True
        # Sjekk kolonner
        for kolonne in range(3):
            if all([self.rutenett[rad][kolonne] == symbol for rad in range(3)]):
                return True
        # Sjekk diagonaler
        if self.rutenett[0][0] == self.rutenett[1][1] == self.rutenett[2][2] == symbol:
            return True
        if self.rutenett[0][2] == self.rutenett[1][1] == self.rutenett[2][0] == symbol:
            return True
        return False
```

#### **Metoden `er_fullt()`**

### **Oppgave 13:**

- **Implementer metoden `er_fullt()` som sjekker om brettet er fullt**

**Eksempel:**

```python
    def er_fullt(self):
        return all([celle != ' ' for rad in self.rutenett for celle in rad])
```

---

## **Del 8: Klassen `Spill`**

**Formål med `Spill`-klassen:**

- **Kontrollerer spillflyten**: Håndterer turer, sjekker for seier eller uavgjort.
- **Organiserer koden**: Holder spilllogikken atskilt fra andre deler.

### **Oppgave 14:**

- **Definer klassen `Spill` med følgende:**
  - **Attributter:**
    - `brett` (Brett)
    - `spiller1` (Spiller)
    - `spiller2` (Spiller)
    - `aktiv_spiller` (Spiller)
  - **Konstruktør som initialiserer attributtene**

**Eksempel:**

```python
class Spill:
    def __init__(self):
        self.brett = Brett()
        self.spiller1 = Spiller('Spiller 1', 'X')
        self.spiller2 = Spiller('Spiller 2', 'O')
        self.aktiv_spiller = self.spiller1
```

### **Oppgave 15:**

- **Implementer metoden `bytt_spiller()` som bytter mellom `spiller1` og `spiller2`**

**Eksempel:**

```python
    def bytt_spiller(self):
        self.aktiv_spiller = self.spiller1 if self.aktiv_spiller == self.spiller2 else self.spiller2
```

---

## **Del 9: Hovedløkken i Spillet**

### **Oppgave 16:**

- **Implementer metoden `spill_spill()` som kontrollerer spillets gang**

- **Funksjonalitet:**
  - Vis brettet
  - Be den aktive spilleren om å gjøre et trekk
  - Oppdater brettet hvis trekket er gyldig
  - Sjekk om det er en vinner eller uavgjort
  - Bytt spiller hvis spillet fortsetter

**Eksempel:**

```python
    def spill_spill(self):
        while True:
            self.brett.vis_brett()
            print(f"{self.aktiv_spiller.navn}'s tur ({self.aktiv_spiller.symbol})")
            try:
                rad = int(input("Velg rad (0-2): "))
                kolonne = int(input("Velg kolonne (0-2): "))
                if rad not in range(3) or kolonne not in range(3):
                    print("Ugyldig valg. Prøv igjen.")
                    continue
            except ValueError:
                print("Ugyldig input. Prøv igjen.")
                continue
            if self.brett.oppdater_brett(rad, kolonne, self.aktiv_spiller.symbol):
                if self.brett.sjekk_vinner(self.aktiv_spiller.symbol):
                    self.brett.vis_brett()
                    print(f"{self.aktiv_spiller.navn} vinner!")
                    break
                elif self.brett.er_fullt():
                    self.brett.vis_brett()
                    print("Uavgjort!")
                    break
                else:
                    self.bytt_spiller()
```

---

## **Del 10: Testing av Programmet**

### **Oppgave 17:**

- **Kjør spillet ditt og spill mot en klassekamerat**
- **Noter eventuelle feil eller problemer som oppstår**
- **Rett opp i feilene og test på nytt**

---

## **Del 11: Diskusjon om Lagring av Objekter**

### **Oppgave 18:**

- **Hvorfor valgte vi å bruke en 2D-liste for å representere brettet?**

**Svar:**

- **Naturlig representasjon**: Et 2D-brett passer godt med en 2D-liste, der rader og kolonner kan representeres enkelt.
- **Enkel tilgang**: Vi kan få tilgang til en celle med `brett[rad][kolonne]`.
- **Oversiktlighet**: Det gir en visuell og intuitiv forståelse av brettet.

- **Diskuter alternative måter å lagre brettet på**

  - **Ordbok (dict)**: Kunne bruke posisjoner som nøkler.
  - **Enkel liste**: Flate ut 2D-listen til en 1D-liste.

- **Hvilke fordeler og ulemper har de forskjellige metodene?**

  - **Ordbok**:
    - **Fordeler**: Fleksibel med posisjoner, spesielt hvis brettet ikke er en fast størrelse.
    - **Ulemper**: Mer komplisert å håndtere for enkle spill.

  - **Enkel liste**:
    - **Fordeler**: Enkel struktur.
    - **Ulemper**: Mindre intuitiv når det gjelder rad og kolonne, krever beregning for å finne posisjoner.

---

## **Del 12: Refleksjon over OOP-konsepter**

### **Oppgave 19:**

- **Hvordan har bruken av klasser og objekter hjulpet deg med å strukturere programmet?**

**Svar:**

- **Modularitet**: Klasser lar oss dele opp programmet i logiske enheter.
- **Gjenbrukbarhet**: Metoder kan brukes flere steder uten å skrive samme kode på nytt.
- **Lesbarhet**: Koden blir mer organisert og lettere å forstå.

- **Gi eksempler på hvordan konstruktører, attributter og metoder har blitt brukt i programmet ditt**

**Svar:**

- **Konstruktører** initialiserer objektene med nødvendige attributter, f.eks. `__init__` i `Spiller`-klassen.
- **Attributter** lagrer objektets tilstand, som `navn` og `symbol` i `Spiller`.
- **Metoder** definerer objektets oppførsel, som `oppdater_brett` i `Brett`.

---

## **Del 13: Ekstra Elementer for Økt Forståelse**

#### **Visualisering av Spillets Flyt**

### **Oppgave 20:**

- **Tegn et flytdiagram som viser spillets gang fra start til slutt**
- **Inkluder beslutningspunkter som sjekk for vinner og uavgjort**

#### **Eksempel på Flytdiagram:**

```
[Start] --> [Vis brett] --> [Spillerens tur] --> [Oppdater brett]
      --> [Sjekk vinner?] --Yes--> [Vis brett] --> [Vinner melding] --> [Slutt]
      |                              ^
      No                             |
      |--> [Sjekk uavgjort?] --Yes-->[Vis brett] --> [Uavgjort melding] --> [Slutt]
      |                              ^
      No                             |
      |--> [Bytt spiller] --> [Gå tilbake til Spillerens tur]
```

---

## **Del 14: Oppsummering og Videre Arbeid**

### **Oppgave 21:**

- **Hva har du lært om objektorientert programmering gjennom denne oppgaven?**
- **Hvordan kan du bruke disse konseptene i fremtidige programmeringsprosjekter?**

### **Oppgave 22:**

- **Utfordring:** Legg til funksjonalitet for å telle poeng over flere runder.
- **Tips:** Legg til en attributt `poeng` i `Spiller`-klassen og oppdater den når noen vinner.

---

**Ekstra Tips:**

- **Kommenter koden din** for å gjøre den lettere å forstå for deg selv og andre.
- **Test ofte** for å fange opp feil tidlig.
- **Bruk print()-funksjoner for debugging**: Hvis noe ikke fungerer, skriv ut variablene for å se hva som skjer.

---

**Vi håper du har hatt glede av å lære om objektorientert programmering gjennom denne praktiske tilnærmingen. Fortsett å utforske og utvikle dine programmeringsferdigheter!**

---

**Oppsummering**

Gjennom dette arbeidsarket har du:

- Utforsket de grunnleggende konseptene i objektorientert programmering.
- Lært om UML-diagrammer og hvordan de brukes til å planlegge programmer.
- Implementert "Tre på rad" ved å bruke klasser, objekter, konstruktører, attributter og metoder.
- Forstått hvorfor vi bruker en 2D-liste for å representere brettet og hvordan det fungerer.
- Reflektert over hvordan OOP hjelper med å organisere og strukturere kode.
- Diskutert og sammenlignet forskjellige måter å lagre objekter på.

---

