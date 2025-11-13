from .proizvodi import Proizvod, skladiste


class Narudzba:
    def __init__(self, naruceni_proizvodi, ukupna_cijena):
        self.naruceni_proizvodi = naruceni_proizvodi
        self.ukupna_cijena = ukupna_cijena
    def ispis_narudzbe(self):
        proizvodi_str = ', '.join([f"{p.naziv} (Količina: {p.kolicina}, Cijena: {p.cijena} KM)" for p in self.naruceni_proizvodi])
        return f"Narudžba: {proizvodi_str} | Ukupna cijena: {self.ukupna_cijena} KM"

def napravi_narudzbu(proizvodi_za_narudzbu : list[Proizvod]) -> Narudzba:
    for proizvod in proizvodi_za_narudzbu:
        if proizvod.naziv not in [p.naziv for p in skladiste]:
            raise ValueError(f"Proizvod {proizvod.naziv} nije dostupan u skladištu.")
    if not isinstance(proizvodi_za_narudzbu, list):
        raise TypeError("Proizvodi za narudžbu moraju biti u listi.")
    if not all(isinstance(p, Proizvod) for p in proizvodi_za_narudzbu):
        raise TypeError("Proizvodi za narudžbu moraju biti instance klase Proizvod.")

    if not proizvodi_za_narudzbu:
        raise ValueError("Lista proizvoda ne smije biti prazna.")

    for proizvod in proizvodi_za_narudzbu:
        if not proizvod.naziv or not proizvod.naziv.strip():
            raise ValueError("Naziv proizvoda ne smije biti prazan.")
        if proizvod.cijena is None or proizvod.cijena <= 0:
            raise ValueError(f"Cijena proizvoda {proizvod.naziv} mora biti veća od 0.")
        if proizvod.dostupna_kolicina is None or proizvod.dostupna_kolicina <= 0:
            raise ValueError(f"Količina proizvoda {proizvod.naziv} mora biti veća od 0.")

    ukupna_cijena = sum(proizvod.cijena * proizvod.dostupna_kolicina for proizvod in proizvodi_za_narudzbu)
    narudzbe = Narudzba(proizvodi_za_narudzbu, ukupna_cijena)
    return narudzbe