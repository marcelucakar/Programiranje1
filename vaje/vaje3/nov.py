#preberi celotno datoteko z zapisnikom dražbe (zapisnik.txt iz zadnje domače naloge) v seznam seznamov.
zapisnik = []
for vrstica in open("zapisnik.txt"):
    predmet, ime, cena = vrstica.split(",")
    majhen_seznam = predmet, ime, int(cena)
    zapisnik.append((predmet, ime, int(cena)))
    #zapisnik.append(majhen_seznam)

#TOREJ
# append metoda bere samo po eno spremenljivko naenkrat
# Da lahko v list zapisnik shranimo vse tri podatke naenkrat, jih zapakiramo v manjsi pomozni seznam
# Ta seznam damo v append ALI PA vse te spremenljivke damo še v DODATEN OKLEPAJ
#       S tem dobimo TUPLE, kot je pri nalogi v kino.py

#for i, (predmet, ime, cena) in enumerate(zapisnik): #to bos delal kasneje

#Izpiši vse stvari, za katere se je zanimala Ana.
print("1. naloga\nAna se je zanimala za:")
ana_se_zanimala = []

for predmet, ime, cena in zapisnik:
    if ime == "Ana":
        ana_se_zanimala.append(predmet)

last_predmet = ""
for trenutni_predmet in ana_se_zanimala:
    if trenutni_predmet != last_predmet:
        print(trenutni_predmet)
        last_predmet = trenutni_predmet


print("\n2. naloga")
# Bi znal(a) sestaviti slovar, katerega ključi so imena oseb,
# vrednosti pa seznam vseh predmetov, za katere se je zanimala ta oseba?

nakupi = {}
for predmet, ime, cena in zapisnik:

    nakupi.setdefault(ime, [])

    if predmet not in nakupi[ime]:
        nakupi[ime].append(predmet)

    #nakupi.setdefault(ime, []).append(predmet)


print(nakupi)

#for ime, predmet in nakupi.items():
    #print(f"{ime}, {predmet}")
