#1
def joc_piatra_foarfeca():
    optiuni = ["piatra", "foarfeca", "hartia"]

    while True:
        jucator1 = input("Jucător 1: ").lower().strip()
        jucator2 = input("Jucător 2: ").lower().strip()

        if jucator1 not in optiuni or jucator2 not in optiuni:
            print("Opțiune invalidă!")
            continue

        if jucator1 == jucator2:
            print("Egalitate")
        elif (jucator1 == "piatra" and jucator2 == "foarfeca") or \
                (jucator1 == "foarfeca" and jucator2 == "hartia") or \
                (jucator1 == "hartia" and jucator2 == "piatra"):
            print(f"Felicitari Jucator 1! {jucator1} bate {jucator2}.")
        else:
            print(f"Felicitari Jucator 2! {jucator2} bate {jucator1}.")

        if input("Jucam din nou? (da/nu): ").lower().strip() != "da":
            break

joc_piatra_foarfeca()

#2
def genereaza_factura(nume_client, **produse):
    print(f"--- FACTURA PENTRU: {nume_client} ---")
    total = 0

    for produs, pret in produse.items():
        print(f"{produs.capitalize()}: {pret} RON")
        total += pret

    print("-" * 30)
    print(f"TOTAL DE PLATA: {total} RON")
    print("-" * 30)


genereaza_factura("Rares", laptop=4500, mouse=150, tastatura=300)

#3
import random


def normalize_data(lista):
    if not lista:
        return []

    minim = min(lista)
    maxim = max(lista)

    if maxim == minim:
        return [0.0] * len(lista)

    return [(x - minim) / (maxim - minim) for x in lista]


data_exemplu = [10, 20, 30, 40, 50]
print(f"Exemplu: {normalize_data(data_exemplu)}")

date_aleatorii = [random.randint(1, 100) for _ in range(5)]
print(f"Date aleatorii: {date_aleatorii}")
print(f"Normalizat: {normalize_data(date_aleatorii)}")

# Ex 4
my_list = [1, 2, 3]
lista_patrate = list(map(lambda x: x**2, my_list))
print(lista_patrate)

# Ex 5
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
sorted_a = sorted(a, key=lambda x: x[1])
print(sorted_a)

# Ex 6
orig_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = list(filter(lambda x: x % 2 == 0, orig_list))
odd_list = list(filter(lambda x: x % 2 != 0, orig_list))
print(even_list)
print(odd_list)

# Ex 7
preturi = [100, None, 50, 200, None, 30]
preturi_reduse = list(map(lambda x: x * 0.9, filter(lambda x: x is not None, preturi)))
print(preturi_reduse)

# Ex 8
import datetime
data_text = "2023-04-24 09:03:32.744178"
data_obiect = datetime.datetime.strptime(data_text, "%Y-%m-%d %H:%M:%S.%f")

extrage_an = lambda x: x.year
extrage_luna = lambda x: x.strftime("%m")
extrage_zi = lambda x: x.day
extrage_timp = lambda x: x.time()

print(extrage_an(data_obiect))
print(extrage_luna(data_obiect))
print(extrage_zi(data_obiect))
print(extrage_timp(data_obiect))
