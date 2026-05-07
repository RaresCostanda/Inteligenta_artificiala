#ex2
nota = int(input("Introduceti nota la examen (0-10): "))

while nota < 0 or nota > 10:
    print("Nota invalida! Incearca din nou")
    nota = int(input("Introduceti o nota valida"))
if nota >= 9:
    print("Excelent")
elif nota >= 7:
    print("Bine")
elif nota >= 5:
    print("Suficient")
else:
    print("Reexaminare")




#ex3
nr_secret = 28
incercari = 1

print("Ghiceste numarul (1-50):")

ghicire = int(input("Introdu numarul: "))

while ghicire != nr_secret:
    if ghicire < nr_secret:
        print("Numarul este mai mare")
    else:
        print("Numarul este mai mic")

    ghicire = int(input("Ghiceste din nou: "))
    incercari += 1

print(f"Felicitari, Ai ghicit numarul in {incercari} incercari")




#ex4
orase = ["Bucuresti", "Cluj-Napoca", "Timisoara", "Iasi"]

for index, oras in enumerate(orase, start=1):
    print(f"{index}. {oras}")




#ex5
import random

print("Bine ai venit la Loteria Python")
print("Alege 6 numere intre 1 si 49")

numere_alese = []
nr_ct = 1

while nr_ct <= 6:
    n = int(input(f"Numarul {nr_ct}: "))
    if 1 <= n <= 49:
        numere_alese.append(n)
        nr_ct = nr_ct + 1
    else:
        print("alege un numar valid intre 1 si 49")

numere_extrase = random.sample(range(1, 50), 6)

numere_ghicite = []
for n in numere_alese:
    if n in numere_extrase:
        numere_ghicite.append(n)

print("-" * 20)
print(f"Numere extrase: {numere_extrase}")
print(f"Ai ghicit {len(numere_ghicite)} numere: {numere_ghicite}")

if len(numere_ghicite) >= 3:
    print("Felicitari... Ai castigat un premiu")
else:
    print("Mai incearca")



#ex6
inventar = []

print("Bine ai venit in Padurea Magica!")
print("Te afli la o rascruce.")

directie = input("In ce directie mergi? (stanga/dreapta): ")

if directie == "stanga":
    print("Ai ajuns la un lac de cristal. Vezi ceva stralucind in apa.")
    actiune = input("Vrei sa cercetezi sau sa pleci? (cercetez/plec): ")

    if actiune == "cercetez":
        print("Ai gasit o Cupa de Aur!")
        inventar.append("Cupa de Aur")
    else:
        print("Ai ales sa mergi mai departe si ai gasit o Potiune Magica pe drum.")
        inventar.append("Potiune Magica")

elif directie == "dreapta":
    print("Ai intrat intr-o pestera intunecata. Te intalnesti cu un spiridus.")
    actiune = input("Vrei sa vorbesti cu el sau sa fugi? (vorbesc/fug): ")

    if actiune == "vorbesc":
        print("Spiridusul este prietenos si iti daruieste o Cheie Veche.")
        inventar.append("Cheie Veche")
    else:
        print("In timp ce fugeai, ai scapat si ai gasit un Scut de Lemn.")
        inventar.append("Scut de Lemn")

else:
    print("Ai stat prea mult pe ganduri si ai fost gasit de un lup!")
    inventar.append("Blana de lup")

print("-" * 20)
print(f"Aventura s-a incheiat! Obiectele tale sunt: {inventar}")



#ex7
comentariu = input("Introdu un comentariu: ").lower()

pozitive = ["bine", "frumos", "super", "excelent", "minunat"]
negative = ["urat", "prost", "groaznic", "dezamagitor"]

este_pozitiv = False
este_negativ = False

for cuvint in pozitive:
    if cuvint in comentariu:
        este_pozitiv = True

for cuvint in negative:
    if cuvint in comentariu:
        este_negativ = True

if este_pozitiv:
    print("Comentariu pozitiv!")
elif este_negativ:
    print("Comentariu negativ!")
else:
    print("Comentariu neutru.")


