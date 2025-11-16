#Izpiši najvišje temperature, izmerjene na vsaki posamični postaji.
# Odgovor: Murska Sobota 40, Črnomelj 40, Maribor 40, Brnik 38, Lisca 35, ...

podatki = {}
min_t, max_t = 373, -273

for vrstica in open("vremenske-postaje.txt"):

    kraj, datum, najvisja, najnizja = vrstica.strip().split(",")

    # castanje temperatur
    najnizja = int(najnizja)
    najvisja = int(najvisja)

    # če še ne obstaja kraj, ga dodaj
    if kraj not in podatki:
        podatki[kraj] = {"najnizja": min_t, "najvisja": max_t}

    # posodobimo, če so nove ekstremne temperature
    if podatki[kraj]["najnizja"] > najnizja:
        podatki[kraj]["najnizja"] = najnizja

    if podatki[kraj]["najvisja"] < najvisja:
        podatki[kraj]["najvisja"] = najvisja

for kraj in podatki:
    #print(f"{podatki["kraj"]}:\n  Najnizja: {podatki["najnizja"]}\n  Najvisja: {podatki["najvisja"]}")
    print(f"{kraj}:\n   Najnizja: {podatki[kraj]["najnizja"]}\n   Najvisja: {podatki[kraj]["najvisja"]}")

    # hugging face
    # lm studio