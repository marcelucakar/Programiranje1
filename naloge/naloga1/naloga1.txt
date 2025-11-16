# za prve tri tocke
st_prodanih = 0
naj_cena = 0
skupna_cena = 0
koncna_skupna_cena = 0
# 4. tocka
ana_kupila_predmetov = 0
berta_kupila_predmetov = 0
# 5. tocka
ana_porabila = 0
berta_porabila = 0
# ostale spremenljivke
ana_na_vrsti = True

for vnos in open("datoteka.txt"):
    vnos = int(vnos)

    if(vnos > naj_cena):
        naj_cena = vnos

    if(vnos == -1):
        # ko pride do konca prodaje izdelka, se prejsna prodaja shrane in pocisti vrednosti
        koncna_skupna_cena += skupna_cena

        if(not ana_na_vrsti):
            ana_porabila += skupna_cena # to ne dela pravilno ne vem zakaj (5. tocka)
            ana_kupila_predmetov += 1
        else: # elif(not berta_na_vrsti):
            berta_porabila += skupna_cena # to ne dela pravilno ne vem zakaj (5. tocka)
            berta_kupila_predmetov += 1

        skupna_cena = 0
        st_prodanih += 1
        ana_na_vrsti = True

    else:
        skupna_cena = vnos

        ana_na_vrsti = not ana_na_vrsti


print(f"St. prodanih: {st_prodanih}")
print(f"Najvisja dosezena cena je {naj_cena}.")
print(f"Skupna cena prodajnih predmetov je {koncna_skupna_cena}.")
print(f"Ana je kupila {ana_kupila_predmetov}, Berta pa {berta_kupila_predmetov}.")
print(f"Ana je porabila {ana_porabila}, Berta {berta_porabila}.")