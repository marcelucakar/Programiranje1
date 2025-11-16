# naloge resuj nad tem komentarjem

# Napiši funkcijo argmax(s), ki prejme seznam in vrne indeks največjega elementa seznama.

def argmax(s):
    m = None
    i = 0
    naj_i = None
    for element in s:

        if m is None or m < element:
            m = element
            naj_i = i
        i += 1

    return naj_i

# Ugani, kaj mora narediti funkcija argmin(s) :) in jo napiši.
def argmin(s):
    m = None
    i = 0
    min_i = None
    for element in s:
        if m is None or m > element:
            m = element
            min_i = i
        i += 1
    return min_i

# Napiši funkcijo span(s), ki prejme seznam števil in vrne razliko med največjim in
# najmanjšim členom podanega zaporedja.
# def span(s):
    m = None
    n = None
    for element in s:
        if m is None and n is None:
            m = element
            n = element
        if m > element:
            m = element
        elif n < element:
            n = element
    return n - m

def span(s):
    return s[argmax(s)] - s[argmin(s)]

def sami_sodi(s):
    return s == [] or (s[0]%2 == 0 and sami_sodi(s[1:]))



#tukaj nadaljuj

import unittest


class TestSeznami(unittest.TestCase):
    def test_argmax(self):
        self.assertEqual(0, argmax([1]))
        self.assertEqual(1, argmax([1, 2]))
        self.assertEqual(2, argmax([1, 0, 3, -5, 2]))
        self.assertEqual(4, argmax([1, 2, 3, 5, 10, 0, 2]))

    def test_argmin(self):
        self.assertEqual(0, argmin([1]))
        self.assertEqual(1, argmin([2, 1]))
        self.assertEqual(3, argmin([1, 0, 3, -5, 2]))
        self.assertEqual(5, argmin([1, 2, 3, 5, 10, 0, 2]))

    def test_span(self):
        self.assertEqual(0, span([1]))
        self.assertEqual(1, span([2, 1]))
        self.assertEqual(8, span([1, 0, 3, -5, 2]))
        self.assertEqual(10, span([1, 2, 3, 5, 10, 0, 2]))

    def test_sami_sodi(self):
        self.assertTrue(sami_sodi([]))
        self.assertTrue(sami_sodi([2]))
        self.assertTrue(sami_sodi([2, 4]))
        self.assertTrue(sami_sodi([2, 4, 0, -2]))

        self.assertFalse(sami_sodi([1]))
        self.assertFalse(sami_sodi([1, 2]))
        self.assertFalse(sami_sodi([1, 4, 3, 2]))

    def test_sodi_lihi(self):
        self.assertTrue(sodi_lihi([]))
        self.assertTrue(sodi_lihi([2, 1, 4, 1]))
        self.assertTrue(sodi_lihi([6, 3, 4, 9]))

        self.assertFalse(sodi_lihi([1]))
        self.assertFalse(sodi_lihi([1, 2, 4]))
        self.assertFalse(sodi_lihi([3, 6, 9, 4]))



class TestDrazba(unittest.TestCase):
    def setUp(self):
        with open("zapisnik1.txt", "w") as f:
            f.write(
                """slika,Berta,31
slika,Ana,33
slika,Berta,35
slika,Fanči,37
slika,Ana,40
slika,Fanči,45
pozlačen dežnik,Ema,29
Meldrumove vaze,Greta,44
Meldrumove vaze,Ana,53
Meldrumove vaze,Fanči,76
Meldrumove vaze,Cilka,78
skodelice,Dani,50
skodelice,Berta,55
skodelice,Dani,60
skodelice,Berta,61
skodelice,Berta,76
skodelice,Dani,80
skodelice,Berta,83        
"""
            )

    def test_ponudbe(self):
        self.assertListEqual(
            [31, 33, 35, 37, 40, 45], ponudbe("zapisnik1.txt", "slika")
        )
        self.assertListEqual([29], ponudbe("zapisnik1.txt", "pozlačen dežnik"))
        self.assertListEqual(
            [44, 53, 76, 78], ponudbe("zapisnik1.txt", "Meldrumove vaze")
        )
        self.assertListEqual(
            [50, 55, 60, 61, 76, 80, 83], ponudbe("zapisnik1.txt", "skodelice")
        )

    def test_najboljsa_ponudba(self):
        self.assertEqual(45, najboljsa_ponudba("zapisnik1.txt", "slika"))
        self.assertEqual(29, najboljsa_ponudba("zapisnik1.txt", "pozlačen dežnik"))
        self.assertEqual(78, najboljsa_ponudba("zapisnik1.txt", "Meldrumove vaze"))
        self.assertEqual(83, najboljsa_ponudba("zapisnik1.txt", "skodelice"))

    def test_stevilo_ponudb(self):
        self.assertEqual(6, stevilo_ponudb("zapisnik1.txt", "slika"))
        self.assertEqual(1, stevilo_ponudb("zapisnik1.txt", "pozlačen dežnik"))
        self.assertEqual(4, stevilo_ponudb("zapisnik1.txt", "Meldrumove vaze"))
        self.assertEqual(7, stevilo_ponudb("zapisnik1.txt", "skodelice"))

    def test_visanje(self):
        self.assertEqual(45 - 31, visanje("zapisnik1.txt", "slika"))
        self.assertEqual(0, visanje("zapisnik1.txt", "pozlačen dežnik"))
        self.assertEqual(78 - 44, visanje("zapisnik1.txt", "Meldrumove vaze"))
        self.assertEqual(83 - 50, visanje("zapisnik1.txt", "skodelice"))

    def test_ponudniki(self):
        self.assertDictEqual(
            {
                'Ana': 3,
                'Berta': 6,
                'Cilka': 1,
                'Dani': 3,
                'Ema': 1,
                'Fanči': 3,
                'Greta': 1
            },
            ponudniki("zapisnik1.txt"),
        )


if __name__ == "__main__":
    unittest.main()
