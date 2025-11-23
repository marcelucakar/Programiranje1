import unittest
import os
import warnings

#tukaj je moja koda

#seznami
def unikati(s):
    s2 = []
    for ime in s:
        if ime not in s2:
            s2.append(ime)
    return s2

def skupnih(s, t):
    skupnih = 0
    s = unikati(s)
    t = unikati(t)
    
    for element in s:
        for e in t:
            if element == e:
                skupnih += 1
    return skupnih

# def vseh(s, t):
    i = 0
    skupek = []
    skupek = s + t
    skupek = unikati(skupek)
    print(len(skupek), skupek)
    return len(skupek)

def vseh(s, t):
    return len(unikati(s + t))

#procesiranje seznamov
def preberi_datoteko(ime_dat):
    v = []
    for vrstica in open(ime_dat):
        #st_elementov = vrstica.count(",") + 1  -- ce potrebujemo slucajno kdaj naslednjic st. elementov ki jih ima posamezna vrstica v datoteki
        v.append(vrstica.split(","))
    return v

def filtriran(s, stolpec, vrednost):
    tmp = []    #isto kot "v" pri prejsni funkciji, sam se mi zdi bolj kul uporabit tmp
    for vrstica in s:
        if vrstica[stolpec] == vrednost:
            tmp.append(vrstica)
    return tmp

def izlusci(s, vrednost):
    tmp = []
    for vrstica in s:
        tmp.append(vrstica[vrednost])
    return tmp

#drazbaaa

def predmeti(ime_dat, oseba):
    tmp = []
    koncni_tmp = [] # a se da to bolje optimizirat?? ni mi vsec, da potrebujem dva seznama...
    prejsnji = "1234567890"
    tmp = filtriran(preberi_datoteko(ime_dat), 1, oseba)
    for vrstica in tmp:
        if prejsnji != vrstica[0]:
            koncni_tmp.append(vrstica[0])
        prejsnji = vrstica[0]
    return koncni_tmp

def osebe(ime_dat, predmet):
    tmp = []
    koncni_tmp = []
    tmp = filtriran(preberi_datoteko(ime_dat), 0, predmet)
    for vrstica in tmp:
        if vrstica[1] not in koncni_tmp:
            koncni_tmp.append(vrstica[1])
    return koncni_tmp

def podobnost(s, t):
    return skupnih(s, t) / vseh(s, t)

def podobnost_oseb(ime_dat, oseba1, oseba2):
    return podobnost(predmeti(ime_dat, oseba1), predmeti(ime_dat, oseba2))


#def podobnost_oseb(ime_dat, oseba1, oseba2):
#    predmet1 = predmeti(ime_dat, oseba1)
#    predmet2 = predmeti(ime_dat, oseba2)
#    inter = unikati([x for x in predmet1 if x in predmet2])
#    uni = unikati(predmet1 + predmet2)
#    if len(uni) == 0:
#        return 1.0
#    return len(inter) / len(uni)

#dodatno iz predavanj



def podobnost_predmetov(ime_dat, predmet1, predmet2):
    oseba1 = osebe(ime_dat, predmet1)
    oseba2 = osebe(ime_dat, predmet2)
    uni = unikati(oseba1 + oseba2)
    if len(uni) == 0:
        return 1.0
    inter = unikati([x for x in oseba1 if x in oseba2])
    return len(inter) / len(uni)
#tukaj so pa testi



with open("zapisnik.txt", "wt", encoding="utf-8") as f:
    f.write("""slika,Berta,31
slika,Ana,33
slika,Berta,35
slika,Fanči,37
slika,Ana,40
slika,Fanči,45
pozlačen dežnik,Ema,29
Meldrumove vaze,Greta,44
Meldrumove vaze,Ana,46
Meldrumove vaze,Greta,48
Meldrumove vaze,Ana,53
Meldrumove vaze,Fanči,57
Meldrumove vaze,Ana,60
Meldrumove vaze,Greta,61
Meldrumove vaze,Ana,63
Meldrumove vaze,Cilka,67
Meldrumove vaze,Greta,71
Meldrumove vaze,Fanči,76
Meldrumove vaze,Cilka,78
skodelice,Dani,50
skodelice,Berta,55
skodelice,Dani,60
skodelice,Berta,61
skodelice,Dani,62
skodelice,Berta,65
skodelice,Dani,68
skodelice,Berta,70
skodelice,Dani,74
skodelice,Berta,76
skodelice,Dani,80
skodelice,Berta,83
kip,Cilka,30
kip,Ema,32
kip,Berta,37
kip,Ema,39
kip,Cilka,43
kip,Berta,44
kip,Cilka,45
kip,Dani,50
kip,Cilka,53
kip,Greta,55
kip,Dani,58
kip,Cilka,61
kip,Dani,63
kip,Greta,68
kip,Cilka,72
kip,Greta,76
kip,Ema,77
kip,Dani,81
kip,Greta,85
kip,Cilka,86
kip,Dani,90
kip,Greta,92
kip,Ema,94
kip,Dani,97
kip,Ema,98
kip,Greta,99
kip,Ema,100
kip,Greta,103
kip,Dani,107
čajnik,Berta,15
srebrn jedilni servis,Ema,27
srebrn jedilni servis,Helga,30
srebrn jedilni servis,Ema,35
srebrn jedilni servis,Cilka,39
srebrn jedilni servis,Helga,40
srebrn jedilni servis,Greta,45
srebrn jedilni servis,Ema,47
srebrn jedilni servis,Cilka,49
srebrn jedilni servis,Ema,53
srebrn jedilni servis,Greta,55
srebrn jedilni servis,Cilka,58
srebrn jedilni servis,Greta,59
srebrn jedilni servis,Cilka,62
srebrn jedilni servis,Greta,63
perzijska preproga,Fanči,16
perzijska preproga,Helga,21
""")

with open("druga-datoteka.txt", "wt") as f:
    f.write("Cube,12,51,212\nCube,15,76,135\nCanyon,12,77,235\nScott,35,124,4316\n")

class NoWarning(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)


class TestSeznami(NoWarning):
    def test_01_unikati(self):
        s = ["Ana", "Ana", "Berta", "Cilka", "Ana", "Berta", "Berta", "Berta", "Ema", "Dani", "Cilka"]
        t = s.copy()
        self.assertEqual(["Ana", "Berta", "Cilka", "Ema", "Dani"], unikati(s))
        self.assertEqual(t, s, "Pusti seznam, ki ga funkcija dobi kot argument, pri miru!")
        self.assertEqual([], unikati([]))
        self.assertEqual(["Ana"], unikati(["Ana"]))
        self.assertEqual([5, 8, 3], unikati([5, 8, 3]))
        self.assertEqual([5, 8, 3], unikati([5, 5, 5, 5, 8, 5, 8, 8, 8, 3, 3, 3, 5]))

    def test_02_skupnih(self):
        s = ["Ana", "Ana", "Berta", "Cilka", "Ana", "Berta", "Berta", "Berta", "Ema", "Dani", "Cilka"]
        sc = s.copy()
        t = ["Cilka", "Fanči", "Ana", "Ana", "Fanči", "Ana", "Cilka"]
        tc = t.copy()
        self.assertEqual(2, skupnih(s, t))
        self.assertEqual(2, skupnih(t, s))
        self.assertEqual(sc, s, "Pusti seznam, ki ga funkcija dobi kot argument, pri miru!")
        self.assertEqual(tc, t, "Pusti seznam, ki ga funkcija dobi kot argument, pri miru!")
        self.assertEqual(0, skupnih(s, ["Fanči", "Greta"]))
        self.assertEqual(1, skupnih(t, ["Fanči", "Greta"]))
        self.assertEqual(0, skupnih(s, []))
        self.assertEqual(0, skupnih([], []))

    def test_03_vseh(self):
        s = ["Ana", "Ana", "Berta", "Cilka", "Ana", "Berta", "Berta", "Berta", "Ema", "Dani", "Cilka"]
        sc = s.copy()
        t = ["Cilka", "Fanči", "Ana", "Ana", "Fanči", "Ana", "Cilka"]
        tc = t.copy()
        self.assertEqual(6, vseh(s, t))
        self.assertEqual(6, vseh(t, s))
        self.assertEqual(sc, s, "Pusti seznam, ki ga funkcija dobi kot argument, pri miru!")
        self.assertEqual(tc, t, "Pusti seznam, ki ga funkcija dobi kot argument, pri miru!")
        self.assertEqual(7, vseh(s, ["Fanči", "Greta"]))
        self.assertEqual(4, vseh(t, ["Fanči", "Greta"]))
        self.assertEqual(5, vseh(s, []))
        self.assertEqual(0, vseh([], []))


class TestProcesiranjeSeznamov(NoWarning):
    def test_01_preberi_datoteko(self):
        self.assertEqual([['slika', 'Berta', '31\n'],
                          ['slika', 'Ana', '33\n'],
                          ['slika', 'Berta', '35\n'],
                          ['slika', 'Fanči', '37\n'],
                          ['slika', 'Ana', '40\n']],
                         preberi_datoteko("zapisnik.txt")[:5])

        self.assertEqual([['Cube', '12', '51', '212\n'],
                          ['Cube', '15', '76', '135\n'],
                          ['Canyon', '12', '77', '235\n'],
                          ['Scott', '35', '124', '4316\n']
                          ], preberi_datoteko("druga-datoteka.txt"))

    def test_02_filter(self):
        s = [["Ana", 5, 9, "Berta"],
             ["Cilka", 5, 12, "Berta"],
             ["Ana", 5, 9, "Cilka"],
             ["Berta", 5, 1, "Ana"]]
        self.assertEqual(
            [["Ana", 5, 9, "Berta"],
             ["Ana", 5, 9, "Cilka"]], filtriran(s, 0, "Ana")
        )
        self.assertEqual(
            [["Ana", 5, 9, "Cilka"],
             ["Ana", 5, 9, "Berta"]], filtriran(s[::-1], 0, "Ana")
        )
        self.assertEqual(s, filtriran(s, 1, 5))
        self.assertEqual([], filtriran(s, 0, "Dani"))
        self.assertEqual([["Ana", 5, 9, "Cilka"]], filtriran(s, 3, "Cilka"))

    def test_03_izlusci(self):
        s = [["Ana", 5, 9, "Berta"],
             ["Cilka", 5, 12, "Berta"],
             ["Ana", 5, 9, "Cilka"],
             ["Berta", 5, 1, "Ana"]]
        self.assertEqual(["Ana", "Cilka", "Ana", "Berta"], izlusci(s, 0))
        self.assertEqual([5, 5, 5, 5], izlusci(s, 1))
        self.assertEqual([9, 12, 9, 1], izlusci(s, 2))


class TestDrazba(NoWarning):
    def test_01_predmeti(self):
        self.assertEqual(['slika', 'Meldrumove vaze'], predmeti("zapisnik.txt", "Ana"))
        self.assertEqual(['slika', 'skodelice', 'kip', 'čajnik'], predmeti("zapisnik.txt", "Berta"))
        self.assertEqual(['Meldrumove vaze', 'kip', 'srebrn jedilni servis'], predmeti("zapisnik.txt", "Cilka"))
        self.assertEqual([], predmeti("zapisnik.txt", "Benjamin"))

        try:
            os.rename("zapisnik.txt", "zapisnik-2.txt")
            self.assertEqual(['slika', 'Meldrumove vaze'], predmeti("zapisnik-2.txt", "Ana"))
        finally:
            os.rename("zapisnik-2.txt", "zapisnik.txt")

    def test_02_osebe(self):
        self.assertEqual(['Cilka', 'Ema', 'Berta', 'Dani', 'Greta'], osebe("zapisnik.txt", "kip"))
        self.assertEqual(['Fanči', 'Helga'], osebe("zapisnik.txt", "perzijska preproga"))
        self.assertEqual([], osebe("zapisnik.txt", "stol brez noge"))

    def test_03_podobnost_oseb(self):
        self.assertAlmostEqual(0.2, podobnost_oseb("zapisnik.txt", "Ana", "Berta"))
        self.assertAlmostEqual(0.5, podobnost_oseb("zapisnik.txt", "Cilka", "Ema"))
        self.assertAlmostEqual(0.25, podobnost_oseb("zapisnik.txt", "Ana", "Cilka"))
        self.assertAlmostEqual(1 / 6, podobnost_oseb("zapisnik.txt", "Berta", "Cilka"))
        self.assertAlmostEqual(1, podobnost_oseb("zapisnik.txt", "Berta", "Berta"))

    def test_04_podobnost_predmetov(self):
        self.assertAlmostEqual(0.4, podobnost_predmetov("zapisnik.txt", "kip", "skodelice"))
        self.assertAlmostEqual(1 / 7, podobnost_predmetov("zapisnik.txt", "kip", "slika"))
        self.assertAlmostEqual(0, podobnost_predmetov("zapisnik.txt", "kip", "perzijska preproga"))
        self.assertAlmostEqual(1, podobnost_predmetov("zapisnik.txt", "kip", "kip"))


class TestPriporocila(NoWarning):
    def test_01_priporoci_predmet(self):
        self.assertEqual("srebrn jedilni servis", priporoci_predmet("zapisnik.txt", "kip"))
        self.assertEqual("Meldrumove vaze", priporoci_predmet("zapisnik.txt", "slika"))

    def test_02_priporoci_prijatelja(self):
        self.assertEqual("Fanči", priporoci_prijatelja("zapisnik.txt", "Ana"))
        self.assertEqual("Dani", priporoci_prijatelja("zapisnik.txt", "Berta"))


if __name__ == "__main__":
    unittest.main()