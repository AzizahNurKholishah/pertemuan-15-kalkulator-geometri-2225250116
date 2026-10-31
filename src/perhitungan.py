import math

# Menghitung luas dan keliling persegi
def hitung_persegi(sisi):
    luas = sisi * sisi
    keliling = 4 * sisi
    return luas, keliling


# Menghitung luas dan keliling persegi panjang
def hitung_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    return luas, keliling


# Menghitung luas dan keliling segitiga
def hitung_segitiga(alas, tinggi, a, b, c):
    luas = 0.5 * alas * tinggi
    keliling = a + b + c
    return luas, keliling


# Menghitung luas dan keliling lingkaran
def hitung_lingkaran(jari_jari):
    luas = math.pi * jari_jari ** 2
    keliling = 2 * math.pi * jari_jari
    return luas, keliling