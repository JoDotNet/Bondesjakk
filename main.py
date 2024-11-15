class Spiller:
    def __init__(self, navn, symbol):
        """Konstrukterer en spiller med navn og symbol"""
        self.navn = navn
        self.symbol = symbol
        self.score = 0

class Brett:
    def __init__(self):
        """Konstrukterer et brett med 3x3 rutenett"""
        self.grid = [[' ' for _ in range(3)] for _ in range(3)]
    
    def vis_brett(self):
        """Viser brettet"""
        for i, row in enumerate(self.grid):
            print(' | '.join(row))
            if i < 2:
                print('---------')
    
    def oppdater(self, rad, kol, symbol):
        """Oppdaterer brettet med spillerens symbol"""
        if self.grid[rad][kol] == ' ':
            self.grid[rad][kol] = symbol
            return True
        return False
    
    def skjekk_vinner(self, symbol):
        """Sjekker om en spiller har vunnet"""
        for row in self.grid:
            if all(cell == symbol for cell in row):
                return True
                
        # Skjekker kolonner
        for col in range(3):
            if all(self.grid[row][col] == symbol for row in range(3)):
                return True
        
        # Skjekker diagonaler
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] == symbol:
            return True
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] == symbol:
            return True
        
        return False
    
    def er_fullt(self):
        """Sjekker om brettet er fullt"""
        return all(cell != ' ' for row in self.grid for cell in row)
    
    def tilbakestill(self):
        """Tilbakestiller brettet for ny runde"""
        self.grid = [[' ' for _ in range(3)] for _ in range(3)]

class Spill:
    def __init__(self):
        """Konstrukterer et nytt spill"""
        self.brett = Brett()
        self.spiller1 = Spiller("Spiller 1", "X")
        self.spiller2 = Spiller("Spiller 2", "O")
        self.aktiv_spiller = self.spiller1
    
    def bytt_spiller(self):
        """Bytter den aktive spilleren"""
        self.aktiv_spiller = self.spiller2 if self.aktiv_spiller == self.spiller1 else self.spiller1
    
    def vis_poengsum(self):
        """Viser nåværende poengsum for begge spillere"""
        print("\nPOENGSUM:")
        print(f"{self.spiller1.navn}: {self.spiller1.score}")
        print(f"{self.spiller2.navn}: {self.spiller2.score}")
    
    def spill_runde(self):
        """Spiller en runde av spillet"""
        while True:
            self.brett.vis_brett()
            print(f"\n{self.aktiv_spiller.navn} sin tur ({self.aktiv_spiller.symbol})")
            
            try:
                rad = int(input("Skriv inn rad (1-3): ")) - 1
                kol = int(input("Skriv inn kolonne (1-3): ")) - 1
                
                if rad not in range(3) or kol not in range(3):
                    print("Ugyldig inntasting! Skriv inn et tall mellom 1 og 3.")
                    continue
                
                if not self.brett.oppdater(rad, kol, self.aktiv_spiller.symbol):
                    print("Posisjonen er opptatt. Prøv igjen.")
                    continue
                
                if self.brett.skjekk_vinner(self.aktiv_spiller.symbol):
                    self.brett.vis_brett()
                    print(f"\nGratulerer! {self.aktiv_spiller.navn} har vunnet!")
                    self.aktiv_spiller.score += 1
                    return True
                
                if self.brett.er_fullt():
                    self.brett.vis_brett()
                    print("\nGame Over! Det ble uavgjort.")
                    return False
                
                self.bytt_spiller()
                
            except ValueError:
                print("Ugyldig inntasting! Skriv inn et tall.")
    
    def play(self):
        """Hovedspillløkke som håndterer flere runder"""
        print("Bondesjakk - Tre på rad")
        
        while True:
            self.brett.tilbakestill()
            self.spill_runde()
            self.vis_poengsum()
            
            while True:
                svar = input("\nVil dere spille en runde til? (Y/n): ").lower()
                if svar in ['y', 'n']:
                    break
                print("Vennligst svar 'y' for ja eller 'n' for nei.")
            
            if svar == 'n':
                print("\nTakk for spillet!")
                print("ENDELIG POENGSUM:")
                self.vis_poengsum()
                break

if __name__ == "__main__":
    spill = Spill()
    spill.play()