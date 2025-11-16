i = 0
predmet_po_vrsti = 0
trenutni_predmet = []
prejsni_predmet = None
prvi = 0
zadnji = 0

for vrstica in open("zapisnik.txt"):
    predmet, ime, cena = vrstica.split(",")
    cena = int(cena)

    trenutni_predmet.append((i, predmet_po_vrsti, predmet, int(cena)))  # to je zdaj tuple

    #kadar pridem do novega predmeta na drazbi
    if prejsni_predmet is not None and predmet != prejsni_predmet:
        prvi = i

        if predmet_po_vrsti == 0:
            if trenutni_predmet[i][0] - trenutni_predmet[i - 7][0] < 7:
                print(predmet, trenutni_predmet[i][3] - trenutni_predmet[prvi][3])
            else:
                print(predmet, trenutni_predmet[i][3] - trenutni_predmet[i - 7][3])

        predmet_po_vrsti += 1

        #ce je med zadnjim in prvim manj kot sedem mest
        if trenutni_predmet[i][0] - trenutni_predmet[i-7][0] < 7:
            print(predmet, trenutni_predmet[i][3] - trenutni_predmet[prvi][3])
        else:
            print(predmet, trenutni_predmet[i][3] - trenutni_predmet[i-7][3])

    prejsni_predmet = predmet
    i += 1



#for i, predmet_po_vrsti, predmet, cena in trenutni_predmet:    #tuki moram nastet vse elemente lista tudi ce jih ne bom uporabljal
#    if trenutni_predmet[i]
