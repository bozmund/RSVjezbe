class Proizvod:
    def __init__(self, naziv, cijena, dostupna_kolicina):
        self.naziv = naziv
        self.cijena = cijena
        self.dostupna_kolicina = dostupna_kolicina

    def ispis(self):
        return f"{self.naziv} - Cijena: {self.cijena} KN, Količina: {self.dostupna_kolicina}"
def dodaj_proizvod(proizvod):
    skladiste.append(proizvod)
skladiste = [Proizvod("Laptop", 1500, 10),
             Proizvod("Telefon", 800, 25)]
