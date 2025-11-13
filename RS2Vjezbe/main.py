# 1. zadatak lambda izrazi
# 1. zadatak
from RS2Vjezbe.shop.narudzbe import napravi_narudzbu

lambda x: x ** 2
# 2. zadatak
lambda x,b: (x + b) ** 2
# 3. zadatak
lambda niz: len(niz) ** 2
# 4. zadatak
lambda x,y: (y*5) ** x
# 5. zadatak
lambda x: x%2 == 0

# 2. zadatak funkcije višeg reda
# 1. zadatak
nizovi = ["jabuka", "kruška", "banana", "naranča"]

kvadrirane_duljine = list(map(lambda niz: len(niz) ** 2, nizovi))

print(kvadrirane_duljine)
# 2. zadatak
brojevi = [1, 21, 33, 45, 2, 2, 1, -32, 9, 10]

veci_od_5 = list(filter(lambda x: x > 5, brojevi))

print(veci_od_5)
# 3. zadatak
brojevi = [10, 5, 12, 15, 20]
transform = dict(map(lambda x: (x, x ** 2), brojevi))
print(transform) # {10: 100, 5: 25, 12: 144, 15: 225, 20: 400}

# 4. zadatak
studenti = [
{"ime": "Ivan", "prezime": "Ivić", "godine": 19},
{"ime": "Marko", "prezime": "Marković", "godine": 22},
{"ime": "Ana", "prezime": "Anić", "godine": 21},
{"ime": "Petra", "prezime": "Petrić", "godine": 13},
{"ime": "Iva", "prezime": "Ivić", "godine": 17},
{"ime": "Mate", "prezime": "Matić", "godine": 18}
]
svi_punoljetni = all(map(lambda student: student["godine"] >= 18, studenti))
print(svi_punoljetni) # False

# 5. zadatak
rijeci = ["jabuka", "pas", "knjiga", "zvijezda", "prijatelj", "zvuk", "čokolada", "ples",
"pjesma", "otorinolaringolog"]
min_duljina = input("Unesite minimalnu duljinu riječi: ")
# min_duljina = 7
duge_rijeci = list(filter(lambda rijec: len(rijec) >= int(min_duljina), rijeci))
print(duge_rijeci)

# 3. zadatak Comprehension sintaksa

# 1. Koristeći list comprehension, izgradite listu parnih kvadrata brojeva od 20 do 50:
parni_kvadrati = [x ** 2 for x in range(20, 51) if x % 2 == 0]
print(parni_kvadrati)

# 2. Koristeći list comprehension, izgradite listu duljina svih nizova u listi rijeci , ali samo za nizove koji sadrže slovo a :
rijeci = ["jabuka", "pas", "knjiga", "zvijezda", "prijatelj", "zvuk", "čokolada", "ples",
"pjesma", "otorinolaringolog"]
duljine_sa_slovom_a = [len(x) for x in rijeci if 'a' in x]
print(duljine_sa_slovom_a) # [6, 3, 6, 8, 9, 8, 6, 17]

# 3. Koristeći list comprehension, izgradite listu rječnika gdje su ključevi brojevi od 1 do 10, a vrijednosti su kubovi tih brojeva, ali samo za neparne brojeve, za parne brojeve neka vrijednost bude sam broj:
kubovi = [{x: x ** 3} if x % 2 != 0 else {x:x} for x in range(1, 11)]
print(kubovi) # [{1: 1}, {2: 2}, {3: 27}, {4: 4}, {5: 125}, {6: 6}, {7: 343}, {8: 8}, {9: 729}, {10: 10}]

import math
# 4. Koristeći dictionary comprehension, izgradite rječnik iteriranjem kroz listu brojeva od 50 do 500 s korakom 50, gdje su ključevi brojevi, a vrijednosti su korijeni tih brojeva zaokruženi na 2 decimale:
korijeni = {x : round(math.sqrt(x), 2) for x in range(50, 501, 50)}
print(korijeni) # {50: 7.07, 100: 10.0, 150: 12.25, 200: 14.14, 250: 15.81, 300: 17.32, 350: 18.71, 400: 20.0, 450: 21.21, 500: 22.36}

#5. Koristeći list comprehension, izgradite listu rječnika gdje su ključevi prezimena studenata, a vrijednosti su zbrojeni bodovi, iz liste studenti :
studenti = [
{"ime": "Ivan", "prezime": "Ivić", "bodovi": [12, 23, 53, 64]},
{"ime": "Marko", "prezime": "Marković", "bodovi": [33, 15, 34, 45]},
{"ime": "Ana", "prezime": "Anić", "bodovi": [8, 9, 4, 23, 11]},
{"ime": "Petra", "prezime": "Petrić", "bodovi": [87, 56, 77, 44, 98]},
{"ime": "Iva", "prezime": "Ivić", "bodovi": [23, 45, 67, 89, 12]},
{"ime": "Mate", "prezime": "Matić", "bodovi": [75, 34, 56, 78, 23]}
]

zbrojeni_bodovi = [{x["prezime"]: sum(x["bodovi"]) } for x in studenti]
print(zbrojeni_bodovi)

# 6. Koristeći dictionary comprehension, izgradite rječnik gdje su ključevi brojevi od 1 do 10, a vrijednosti su liste faktorijela tih brojeva.
import math
faktorijeli = {x:[math.factorial(y) for y in range(1,x+1)] for x in range(1,11)}
print(faktorijeli)

#Zadatak 4: Klase i objekti
# Definirajte klasu Automobil s atributima marka , model , godina_proizvodnje i kilometraža .
# Dodajte metodu ispis koja će ispisivati sve atribute automobila.
from datetime import datetime
class Automobil:
    def __init__(self, marka, model, godina_proizvodnje, kilometraža):
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina_proizvodnje
        self.kilometraža = kilometraža
    def ispis(self):
        print(f"{self.marka} {self.model}, {self.godina_proizvodnje}, {self.kilometraža} km")
    def starost(self):
        return datetime.now().year - self.godina_proizvodnje

auto1 = Automobil("Toyota", "Corolla", 2015, 75000)
auto1.ispis()
print(f"Starost automobila: {auto1.starost()} godina")

#2. Definirajte klasu Kalkulator s atributima a i b . Dodajte metode zbroj , oduzimanje , mnozenje , dijeljenje , potenciranje i korijen koje će izvršavati odgovarajuće operacije nad atributima a i b.
import math
class Kalkulator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def zbroj(self):
        return self.a + self.b
    def oduzimanje(self):
        return self.a - self.b
    def mnozenje(self):
        return self.a * self.b
    def dijeljenje(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Dijeljenje s nulom nije dozvoljeno"
    def potenciranje(self):
        return self.a ** self.b
    def korijen(self):
        return math.sqrt(self.a), math.sqrt(self.b)

# 3. Definirajte klasu Student s atributima ime , prezime , godine i ocjene . Iterirajte kroz sljedeću listu studenata i za svakog studenta stvorite objekt klase Student i dodajte ga u
# novu listu studenti_objekti :
studenti = [
{"ime": "Ivan", "prezime": "Ivić", "godine": 19, "ocjene": [5, 4, 3, 5, 2]},
{"ime": "Marko", "prezime": "Marković", "godine": 22, "ocjene": [3, 4, 5, 2, 3]},
{"ime": "Ana", "prezime": "Anić", "godine": 21, "ocjene": [5, 5, 5, 5, 5]},
{"ime": "Petra", "prezime": "Petrić", "godine": 13, "ocjene": [2, 3, 2, 4, 3]},
{"ime": "Iva", "prezime": "Ivić", "godine": 17, "ocjene": [4, 4, 4, 3, 5]},
{"ime": "Mate", "prezime": "Matić", "godine": 18, "ocjene": [5, 5, 5, 5, 5]}
]
class Student:
    def __init__(self, ime, prezime, godine, ocjene):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
        self.ocjene = ocjene
    def prosjek(self):
        return sum(self.ocjene) / len(self.ocjene)

studenti_objekti = []
for s in studenti:
    student_objekt = Student(s["ime"], s["prezime"], s["godine"], s["ocjene"])
    studenti_objekti.append(student_objekt)
najbolji_student = max(studenti_objekti, key=lambda student: student.prosjek())

# Definirajte klasu Krug s atributom r . Dodajte metode opseg i povrsina koje će računati opseg i
# površinu kruga.
import math
class Krug:
    def __init__(self, r):
        self.r = r
    def opseg(self):
        return 2 * math.pi * self.r
    def povrsina(self):
        return math.pi * self.r ** 2
krug1 = Krug(5)
print(f"Opseg kruga: {krug1.opseg()}")
print(f"Površina kruga: {krug1.povrsina()}")

# Definirajte klasu Radnik s atributima ime , pozicija , placa . Dodajte metodu work koja će
# ispisivati "Radim na poziciji {pozicija}".

class Radnik:
    def __init__(self, ime, pozicija, placa):
        self.ime = ime
        self.pozicija = pozicija
        self.placa = placa
    def work(self):
        print(f"Radim na poziciji {self.pozicija}")

class Menadzer(Radnik):
    def __init__(self, ime, pozicija, placa, department):
        super().__init__(ime, pozicija, placa)
        self.department = department
    def work(self):
        print(f"Radim na poziciji {self.pozicija} u odjelu {self.department}")
    def give_raise(self, radnik, povecanje):
        radnik.placa += povecanje

radnik1 = Radnik("Ivana", "Programer", 6000)
radnik1.work()
menadzer1 = Menadzer("Marko", "Menadžer", 9000, "IT")
menadzer1.work()
menadzer1.give_raise(radnik1, 500)

#Zadatak 5: Moduli i paketi
from RS2Vjezbe.shop.proizvodi import Proizvod, dodaj_proizvod, skladiste
from RS2Vjezbe.shop.narudzbe import napravi_narudzbu

proizvodi_za_dodavanje = [
{"naziv": "Laptop", "cijena": 5000, "dostupna_kolicina": 10},
{"naziv": "Monitor", "cijena": 1000, "dostupna_kolicina": 20},
{"naziv": "Tipkovnica", "cijena": 200, "dostupna_kolicina": 50},
{"naziv": "Miš", "cijena": 100, "dostupna_kolicina": 100}
]
for p in proizvodi_za_dodavanje: dodaj_proizvod(Proizvod(p["naziv"], p["cijena"], p["dostupna_kolicina"]))
for proizvod in skladiste:
    print(proizvod.ispis())

# U main.py datoteci učitajte modul narudzbe.py iz paketa shop i pozovite funkciju napravi_narudzbu s
# listom proizvoda iz prethodnog zadatka.

lista_proizvoda = [Proizvod(proizvod["naziv"], proizvod["cijena"], proizvod["dostupna_kolicina"]) for proizvod in proizvodi_za_dodavanje]
napravi_narudzbu(lista_proizvoda)
