podatki = {}

for vrstica in open("zapisnik.txt"):
    predmet, ime, cena = vrstica.strip().split(",")
    cena = int(cena)

    if predmet not in podatki:
        podatki[predmet] = []

    podatki[predmet].append(cena)

#racunanje razlike
for predmet, cene in podatki.items():
    if len(cene) > 1:
        zadnje_cene = cene[-7:]
        razlika = zadnje_cene[-1] - zadnje_cene[0]
    else:
        razlika = 0

    print(f"{predmet} - {razlika}")
