
from perhitungan import (
    hitung_persegi,
    hitung_persegi_panjang,
    hitung_segitiga,
    hitung_lingkaran
)


def menu():
    print("\n=== KALKULATOR GEOMETRI ===")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("4. Lingkaran")
    print("5. Keluar")


def input_positif(pesan):
    while True:
        try:
            nilai = float(input(pesan))
            if not (0 < nilai < float("inf")):
                print("Input harus angka positif lebih dari 0!")
                continue
            return nilai
        except ValueError:
            print("Input tidak valid! Masukkan angka.")


def main():
    while True:
        menu()
        pilihan = input("Pilih bangun datar (1-5): ")

        if pilihan == "1":
            sisi = input_positif("Masukkan panjang sisi: ")
            luas, keliling = hitung_persegi(sisi)

        elif pilihan == "2":
            panjang = input_positif("Masukkan panjang: ")
            lebar = input_positif("Masukkan lebar: ")
            luas, keliling = hitung_persegi_panjang(panjang, lebar)

        elif pilihan == "3":
            alas = input_positif("Masukkan alas: ")
            tinggi = input_positif("Masukkan tinggi: ")
            a = input_positif("Masukkan sisi pertama: ")
            b = input_positif("Masukkan sisi kedua: ")
            c = input_positif("Masukkan sisi ketiga: ")

            if a + b <= c or a + c <= b or b + c <= a:
                print("Ketiga sisi tidak membentuk segitiga!")
                continue

            luas, keliling = hitung_segitiga(
                alas, tinggi, a, b, c
            )

        elif pilihan == "4":
            jari_jari = input_positif("Masukkan jari-jari: ")
            luas, keliling = hitung_lingkaran(jari_jari)

        elif pilihan == "5":
            print("Terima kasih telah menggunakan program!")
            break

        else:
            print("Pilihan tidak tersedia!")
            continue

        print("\n--- HASIL PERHITUNGAN ---")
        print(f"Luas: {luas:.2f}")
        print(f"Keliling: {keliling:.2f}")


if __name__ == "__main__":
    main()
