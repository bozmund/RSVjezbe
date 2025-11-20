# Zadatak 1
import asyncio


async def fetch_data():
    await asyncio.sleep(3)
    data = [i for i in range(1, 11)]
    print("Podaci dohvaćeni.")
    return data


async def zad1():
    data = await fetch_data()
    print("Dohvaćeni podaci:", data)


asyncio.run(zad1())

# Zadatak 2
import asyncio


async def fetch_data_2zad(object_to_return, delay):
    await asyncio.sleep(delay)
    print(f"Podaci dohvaćeni nakon {delay} sekundi.")
    return object_to_return


async def zad2():
    lista_usera, lista_proizvoda = await asyncio.gather(
        fetch_data_2zad([{"marko": "3 godine"}, {"ana": "5 godina"}], 3),
        fetch_data_2zad([{"mlijeko": "1l"}, {"kruh": "500g"}], 5)
    )
    user_data, product_data = lista_usera, lista_proizvoda
    print("Dohvaćeni podaci o korisnicima:", user_data)
    print("Dohvaćeni podaci o proizvodima:", product_data)


asyncio.run(zad2())

# Zadatak 3
import asyncio

baza_korisnika = [
    {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
    {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
    {'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
    {'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]

baza_lozinka = [
    {'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
    {'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
    {'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
    {'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
]


async def provjeri_korisnika(korisnicko_ime, email):
    await asyncio.sleep(3)
    for korisnik in baza_korisnika:
        if korisnik['korisnicko_ime'] == korisnicko_ime and korisnik['email'] == email:
            return korisnik
    return f"Korisnik {korisnicko_ime} nije pronađen."


async def autorizacija(korisnik, lozinka):
    await asyncio.sleep(2)
    for entry in baza_lozinka:
        if entry['korisnicko_ime'] == korisnik['korisnicko_ime']:
            if entry['lozinka'] == lozinka:
                return f"Korisnik {korisnik['korisnicko_ime']}: Autorizacija uspješna."
            else:
                return f"Korisnik {korisnik['korisnicko_ime']}: Autorizacija neuspješna."
    return f"Korisnik {korisnik['korisnicko_ime']}: Lozinka nije pronađena u bazi."


async def autentikacija(opis_korisnika):
    rezultat = await provjeri_korisnika(opis_korisnika['korisnicko_ime'], opis_korisnika['email'])
    if isinstance(rezultat, str):
        return rezultat
    # rezultat is korisnik dict from baze
    return await autorizacija(rezultat, opis_korisnika['lozinka'])


asyncio.run(autentikacija({'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com', 'lozinka': 'super_teska_lozinka'}))

# Zadatak 4
import asyncio
import random


async def provjeri_parnost(broj):
    await asyncio.sleep(2)
    if broj % 2 == 0:
        return f"Broj {broj} je paran."
    else:
        return f"Broj {broj} je neparan."


async def main():
    lista_brojeva = [random.randint(1, 100) for _ in range(10)]
    lista_taskova = [asyncio.create_task(provjeri_parnost(broj)) for broj in lista_brojeva]
    resultat = await asyncio.gather(*lista_taskova)
    for res in resultat:
        print(res)


asyncio.run(main())

# Zadatak 5
import asyncio

lista_rjecnika_osjetljivih_podataka = [
    {"prezime": "Horvat", "broj_kartice": "1234-5678-9012-3456", "CVV": "123"},
    {"prezime": "Kovač", "broj_kartice": "9876-5432-1098-7654", "CVV": "456"},
    {"prezime": "Babić", "broj_kartice": "1111-2222-3333-4444", "CVV": "789"}
]
async def secure_data(rjecnik_osjetljivih_podataka):
    await asyncio.sleep(3)
    var = lambda korisnik: {
        "prezime": korisnik["prezime"],
        "broj_kartice": hash(korisnik["broj_kartice"]),
        "CVV": hash(korisnik["CVV"])
    }
    return var(rjecnik_osjetljivih_podataka)

async def zad5():
    lista_taskova = [asyncio.create_task(secure_data(rjecnik)) for rjecnik in lista_rjecnika_osjetljivih_podataka]
    rezultat = await asyncio.gather(*lista_taskova)
    for res in rezultat:
        print(res)

asyncio.run(zad5())

# Zadatak 6
import asyncio, time
async def fetch_data(param):
    print(f"Nešto radim s {param}...")
    await asyncio.sleep(param)
    print(f'Dovršio sam s {param}.')
    return f"Rezultat za {param}"
async def main():
    task1 = asyncio.create_task(fetch_data(1)) # schedule
    task2 = asyncio.create_task(fetch_data(2)) #schedule
    result1 = await task1
    print("Fetch 1 uspješno završen.")
    await asyncio.sleep(3)  # čekanje da se task2 dovrši
    return [result1]

t1 = time.perf_counter()
results = asyncio.run(main()) # pokretanje event loop-a
t2 = time.perf_counter()
print(results)
print(f"Vrijeme izvođenja {t2 - t1:.2f} sekunde")

# Zadatak 7
import asyncio
async def timer(name, delay):
    for i in range(delay, 0, -1):
        print(f'{name}: {i} sekundi preostalo...')
        await asyncio.sleep(1)
    print(f'{name}: Vrijeme je isteklo!')
async def main():
    timers = [
        asyncio.create_task(timer('Timer 1', 3)),
        asyncio.create_task(timer('Timer 2', 5)),
        asyncio.create_task(timer('Timer 3', 7))
    ]
    await asyncio.gather(*timers)
asyncio.run(main())

# Objašnjenje:
# 1. Kada se pozove asyncio.run(main()), stvara se novi event loop i pokreće se korutina main().
# 2. Unutar main(), tri korutine timer() se raspoređuju kao zadaci (tasks) pomoću asyncio.create_task().
# 3. Svaki timer() započinje izvršavanje i ulazi u stanje "running". Prvi timer ispisuje "Timer 1: 3 sekundi preostalo..." i zatim poziva await asyncio.sleep(1).
# 4. Poziv await asyncio.sleep(1) stavlja korutinu u stanje "waiting", dopuštajući event loop-u da izvršava druge zadatke dok čeka.
# 5. Event loop nastavlja izvršavati ostale timere. Timer 2 i Timer 3 također ispisuju svoje poruke i ulaze u stanje "waiting" nakon poziva sleep.
# 6. Nakon što prođe 1 sekunda, event loop budi sve korutine koje su bile u stanju "waiting". Timer 1 nastavlja izvršavanje, ispisuje "Timer 1: 2 sekundi preostalo..."
#    i ponovno poziva await asyncio.sleep(1), vraćajući se u stanje "waiting".
# 7. Ovaj proces se ponavlja za sve timere dok ne istekne njihovo vrijeme. Svaki timer ispisuje preostalo vrijeme i ulazi u stanje "waiting" nakon svakog poziva sleep.
# 8. Kada timer dosegne 0, ispisuje "Vrijeme je isteklo!" i završava izvršavanje, prelazeći u stanje "done".
# 9. Event loop nastavlja raditi dok svi timeri ne završe. Kada su svi zadaci dovršeni, asyncio.gather() vraća kontrolu natrag u main(), koja zatim završava.
# 10. Event loop se zatvara nakon što main() završi, završavajući cijeli program