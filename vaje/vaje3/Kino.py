# to je tuple
filmi = [
    ('Poletje v skoljki 2', 6.1),
    ('Ne cakaj na maj', 7.3),
    ('Pod njenim oknom', 7.1),
    ('Kekec', 8.1),
    ('Poletje v skoljki', 7.2),
    ('To so gadi', 7.7),
]

#imena vseh filmov z oceno vsaj 7.0
print("imena vseh filmov z oceno nad 7.0:")
for ime, ocena in filmi:
    if ocena > 7.0:
        print(ime)

#ime filma z najvisjo oceno
naj_oc = 0
naj_film = []
for ime, ocena in filmi:
    if ocena > naj_oc:
        naj_oc = ocena
        naj_film = ime, ocena
print(f"\nFilm z najvisjo oceno je {naj_film[0]}.")

#povprecna cena vseh filmov
filmov = 0
sestevek_ocen = {}
for ime, ocena in filmi:
    sestevek_ocen.setdefault(ocena, 0)
    filmov += 1
    sestevek_ocen[ocena] += ocena

print(f"Povprecna ocena vseh filmov je {sum(sestevek_ocen.values()) / filmov}.")

#ime prvega filma v seznamu z oceno vsaj 7,0
najden_film = []
for ime, ocena in filmi:
    if ocena > 7.0:
        najden_film = ime, ocena
        break

print(f"Prvi film z oceno nad 7.0 je {najden_film[0]}.")