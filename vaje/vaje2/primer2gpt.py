podatki = {}
min_t, max_t = 373, -273

for vrstica in open("vremenske-postaje.txt"):
    kraj, datum, najvisja, najnizja = vrstica.strip().split(",")
    najnizja = int(najnizja)
    najvisja = int(najvisja)

    # če kraj še ne obstaja v podatkih, ga dodaj
    if kraj not in podatki:
        podatki[kraj] = {"najnizja": min_t, "najvisja": max_t}

    # posodobi, če so nove ekstremne temperature
    if podatki[kraj]["najnizja"] > najnizja:
        podatki[kraj]["najnizja"] = najnizja

    if podatki[kraj]["najvisja"] < najvisja:
        podatki[kraj]["najvisja"] = najvisja

# izpis
for kraj in podatki:
    print(f"{kraj}: najnižja = {podatki[kraj]['najnizja']}, najvišja = {podatki[kraj]['najvisja']}")
