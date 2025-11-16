najvisja_cena = 0

#berem vrstice iz datotek(e)
for vrstica in open("zapisnik.txt"):
    #razdelimo in shranimo podatke
    kaj, kdo, koliko = vrstica.split(",")
    if int(koliko) > najvisja_cena:
        najvisja_cena = int(koliko)
        max_kdo = kdo
        max_kaj = kaj

#za vsak predmet bom shranil ceno
cene = {}
for vrstica in open("zapisnik.txt"):
    kaj, kdo, koliko = vrstica.split(",")
    cene[kaj] = int(koliko) #zadnja cena predmeta

#koliko je bilo visanj?
visanj = {}
for vrstica in open("zapisnik.txt"):
    kaj, _, _ = vrstica.split(",")
    if kaj not in visanj:
        visanj[kaj] = 0
    visanj[kaj] += 1 #za ta predmet povisamo st.

#predmet z najvec visanji
naj_zelena = None
for kaj, koliko in visanj.items():
    #ce se nimamo tega predmeta ali je imel trenutni vec visanj
    if naj_zelena is None or visanj[kaj] > visanj[naj_zelena]:
        naj_zelena = kaj

#izpis
for kaj, koliko in cene.items():
    print(kaj, "-", koliko)

print("Najdražji predmet je", max_kaj, "- za", najvisja_cena, "ga je kupila", max_kdo)

for kaj, koliko in cene.items():
    print(kaj, "-", koliko)

for kaj, koliko in visanj.items():
    print(kaj, "-", koliko)

print("Najbolj so se pulile za predmet", naj_zelena)

# ||||| opt + shift + ž
# slovarji:
# .get("Triglav", "ni hriba") -> če ni hriba "triglav", ga nastavi na "ni hriba"
# .setdefault("Kočna", 1000) -> če ne obstaja "kočna", ga doda v slovar in mu dodeli vrednost 1000
# sum(hribi.values()) -> vrne vrednsot
# hribi.items() -> vrne pare (ključ, vrednost)
# hribi.keys() -> vrne ključe NEUPORABNO; namesto tega napišemo samo for x in hribi: namesto for x in hribi.keys()

# list prebere iz slovarja njegove ključe