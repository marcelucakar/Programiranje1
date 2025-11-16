#Kateri sta najvišja in najnižja temperatura, izmerjeni kadarkoli v Sloveniji
# (na eni od teh vremenskih postaj, ne drugo)?
# Odgovor: najvišja: 40, najnižja: -32

maks = -278
minimum = 100

#podatki = {}

for vrstica in open("vremenske-postaje.txt"):

    kraj, datum, najvisja, najnizja = vrstica.strip().split(",")
    # strip se uporabi, kadar je zadnja spremenljivka tipa string, ker vsebuje "\n"
    # ce zadnjo spremenljivko castamo v int, tega koraka ni potrebno narediti

    najnizja = int(najnizja)
    najvisja = int(najvisja)


    if minimum > najnizja:
        minimum = najnizja

    if maks < najvisja:
        maks = najvisja

print(f"Najnizja: {minimum}\nNajvisja: {maks}")
