import csv
import glob
import os

def kodirnik_postaj():
    postaje = {}
    folder = os.path.join(os.path.dirname(__file__), "vreme")
    for filepath in glob.glob(os.path.join(folder, "*.csv")):

        with open(filepath, "r") as f:
            reader = csv.DictReader(f)
            row = next(reader)
            postaja = row.get("STATION", "").strip()
            ime = row.get("NAME", "").strip()

            ime = ime.split(",")[0].title()
            postaje[ime] = postaja
    
    return postaje

def popravi(kodirnik):
    popravki = {
        'Murska Sobota Rakican': 'Murska Sobota',
        'Crnomelj Doblice': 'Črnomelj',
        'Letalisce Edvarda Rusjana Mari': 'Maribor',
        'Letalisce Jozeta Pucnika Ljubl': 'Brnik',
        'Ljubljana Bezigrad': 'Ljubljana',
        'Kocevje': 'Kočevje',
        'Smartno Pri Slovenj Gradcu': 'Smartno pri Slovenj Gradcu',
        'Kredarica': 'Kredarica',
        'Veliki Dolenci': 'Veliki Dolenci',
        'Novo Mesto': 'Novo mesto',
        'Nova Vas Na Blokah': 'Bloke',
        'Celje Medlog': 'Celje',
        'Portoroz Letalisce': 'Portorož',
        'Topol Pri Medvodah': 'Topol pri Medvodah',
        'Ratece Planica': 'Rateče'
    }
    for stari in list(kodirnik.keys()):
        if stari in popravki:
            nov = popravki[stari]
            kodirnik[nov] = kodirnik.pop(stari)
    return kodirnik


def preberi_meritve(ime_postaje, kodirnik):
    temperature = {}
    sifra = kodirnik.get(ime_postaje)

    dat = os.path.join(os.path.dirname(__file__), "vreme")

    for filepath in glob.glob(os.path.join(dat, "*.csv")):
        with open(filepath, "r") as f:
            reader = csv.DictReader(f)
            #row = next(reader)
            for row in reader:
                postaja = row.get("STATION", "").strip()
                if postaja != sifra:
                    continue
                
                datum_raw = row.get("DATE", "").strip()
                tmax = row.get("TMAX", "").strip()
                leto, mesec, dan = map(int, datum_raw.split("-"))
                datum = (leto, mesec, dan)

                if tmax == "":
                    continue
                else:
                    tmax = float(tmax)
                    tmax = tmax / 10.0

                temperature[datum] = tmax

    return temperature


def mrzli_silvester(podatki):
    silvester_slovar = {}
    for datum in podatki:
        if datum[1] == 12 and datum[2] == 31:
            silvester_slovar[datum[0]] = podatki[datum]
    najhladnejsi = min(silvester_slovar, key=silvester_slovar.get)
    return najhladnejsi

import unittest
import warnings


class Test(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)

    def test_01_kodirnik_postaj(self):
        self.assertEqual({'Bilje': 'SIE00115106',
                          'Celje Medlog': 'SIE00115176',
                          'Crnomelj Doblice': 'SIE00114856',
                          'Kocevje': 'SIE00114956',
                          'Kredarica': 'SIE00105938',
                          'Lesce': 'SIE00114966',
                          'Letalisce Edvarda Rusjana Mari': 'SIE00115156',
                          'Letalisce Jozeta Pucnika Ljubl': 'SIE00115146',
                          'Lisca': 'SIE00115186',
                          'Ljubljana Bezigrad': 'SIM00014015',
                          'Murska Sobota Rakican': 'SIE00115196',
                          'Nova Vas Na Blokah': 'SIE00115066',
                          'Novo Mesto': 'SIE00115126',
                          'Portoroz Letalisce': 'SIE00115166',
                          'Postojna': 'SIE00115076',
                          'Ratece Planica': 'SIE00115206',
                          'Smartno Pri Slovenj Gradcu': 'SIE00115136',
                          'Topol Pri Medvodah': 'SIE00115006',
                          'Veliki Dolenci': 'SIE00115096',
                          'Vojsko': 'SIE00115016'}
,                         kodirnik_postaj())

    def test_02_popravki(self):
        kodirnik = {'Bilje': 'SIE00115106',
                    'Celje Medlog': 'SIE00115176',
                    'Crnomelj Doblice': 'SIE00114856',
                    'Kocevje': 'SIE00114956',
                    'Kredarica': 'SIE00105938',
                    'Lesce': 'SIE00114966',
                    'Letalisce Edvarda Rusjana Mari': 'SIE00115156',
                    'Letalisce Jozeta Pucnika Ljubl': 'SIE00115146',
                    'Lisca': 'SIE00115186',
                    'Ljubljana Bezigrad': 'SIM00014015',
                    'Murska Sobota Rakican': 'SIE00115196',
                    'Nova Vas Na Blokah': 'SIE00115066',
                    'Novo Mesto': 'SIE00115126',
                    'Portoroz Letalisce': 'SIE00115166',
                    'Postojna': 'SIE00115076',
                    'Ratece Planica': 'SIE00115206',
                    'Smartno Pri Slovenj Gradcu': 'SIE00115136',
                    'Topol Pri Medvodah': 'SIE00115006',
                    'Veliki Dolenci': 'SIE00115096',
                    'Vojsko': 'SIE00115016'}
        popravi(kodirnik)
        self.assertEqual({'Bilje': 'SIE00115106',
                          'Bloke': 'SIE00115066',
                          'Brnik': 'SIE00115146',
                          'Celje': 'SIE00115176',
                          'Kočevje': 'SIE00114956',
                          'Kredarica': 'SIE00105938',
                          'Lesce': 'SIE00114966',
                          'Lisca': 'SIE00115186',
                          'Ljubljana': 'SIM00014015',
                          'Maribor': 'SIE00115156',
                          'Murska Sobota': 'SIE00115196',
                          'Novo mesto': 'SIE00115126',
                          'Portorož': 'SIE00115166',
                          'Postojna': 'SIE00115076',
                          'Rateče': 'SIE00115206',
                          'Smartno pri Slovenj Gradcu': 'SIE00115136',
                          'Topol pri Medvodah': 'SIE00115006',
                          'Veliki Dolenci': 'SIE00115096',
                          'Vojsko': 'SIE00115016',
                          'Črnomelj': 'SIE00114856'}, kodirnik)

    def test_03_preberi_meritve(self):
        kodirnik = kodirnik_postaj()
        popravi(kodirnik)
        podatki = preberi_meritve("Kredarica", kodirnik)
        self.assertAlmostEqual(14.4, podatki[(2023, 8, 13)])
        self.assertAlmostEqual(11.1, podatki[(2023, 10, 1)])
        self.assertNotIn((2023, 10, 4), podatki)

    def test_04_mrzli_silvester(self):
        kodirnik = kodirnik_postaj()
        popravi(kodirnik)

        podatki = preberi_meritve("Kredarica", kodirnik)
        self.assertEqual(1968, mrzli_silvester(podatki))

        podatki = preberi_meritve("Črnomelj", kodirnik)
        self.assertEqual(1996, mrzli_silvester(podatki))

        podatki = preberi_meritve("Ljubljana", kodirnik)
        self.assertEqual(1906, mrzli_silvester(podatki))

        podatki = preberi_meritve("Bloke", kodirnik)
        self.assertEqual(1996, mrzli_silvester(podatki))

        podatki = preberi_meritve("Bilje", kodirnik)
        self.assertEqual(2005, mrzli_silvester(podatki))


if __name__ == "__main__":
    unittest.main()
