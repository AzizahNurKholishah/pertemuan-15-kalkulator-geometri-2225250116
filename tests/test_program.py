
import sys
import os
import math
import unittest

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../src"))
)

from perhitungan import (
    hitung_persegi,
    hitung_persegi_panjang,
    hitung_segitiga,
    hitung_lingkaran
)


class TestKalkulatorGeometri(unittest.TestCase):

    def test_01_persegi(self):
        self.assertEqual(hitung_persegi(5), (25, 20))

    def test_02_persegi_panjang(self):
        self.assertEqual(hitung_persegi_panjang(6, 4), (24, 20))

    def test_03_segitiga(self):
        self.assertEqual(hitung_segitiga(6, 4, 5, 5, 6), (12, 16))

    def test_04_lingkaran(self):
        luas, keliling = hitung_lingkaran(7)
        self.assertAlmostEqual(luas, math.pi * 49)
        self.assertAlmostEqual(keliling, 14 * math.pi)

    def test_05_persegi_desimal(self):
        self.assertEqual(hitung_persegi(2.5), (6.25, 10))

    def test_06_persegi_panjang_desimal(self):
        self.assertEqual(hitung_persegi_panjang(2.5, 4), (10, 13))

    def test_07_lingkaran_desimal(self):
        luas, keliling = hitung_lingkaran(0.5)
        self.assertAlmostEqual(luas, math.pi * 0.25)
        self.assertAlmostEqual(keliling, math.pi)


if __name__ == "__main__":
    unittest.main()
