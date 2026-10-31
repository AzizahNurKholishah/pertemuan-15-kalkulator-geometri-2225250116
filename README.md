# Kalkulator Geometri Bangun Datar - Proyek Akhir Pertemuan 15

| **Keterangan** | **Data** |
|---|---|
| **Nama** | Azizah Nur Kholishah |
| **NIM** | 2225250116 |
| **Kelas** | 3-E |
| **Jurusan** | Pendidikan Matematika |

## Deskripsi

Kalkulator Geometri Bangun Datar merupakan program sederhana berbasis Python yang digunakan untuk menghitung luas dan keliling beberapa jenis bangun datar. Program ini dijalankan melalui terminal dengan menyediakan pilihan menu sehingga pengguna dapat memilih bangun datar, memasukkan ukuran, dan memperoleh hasil perhitungan secara otomatis.

Program ini ditujukan bagi siswa yang sedang mempelajari materi geometri, khususnya luas dan keliling persegi, persegi panjang, segitiga, serta lingkaran.

Proyek ini merupakan pengembangan dari rancangan Pertemuan 14 yang dilanjutkan pada Pertemuan 15 melalui implementasi program, pengujian, debugging, dan dokumentasi.

## Fitur

- Menghitung luas dan keliling persegi berdasarkan panjang sisi.
- Menghitung luas dan keliling persegi panjang berdasarkan panjang dan lebar.
- Menghitung luas dan keliling segitiga berdasarkan alas, tinggi, dan tiga sisi.
- Menghitung luas dan keliling lingkaran berdasarkan jari-jari.
- Memvalidasi ukuran bangun datar agar bernilai positif atau lebih dari nol.
- Menangani input nonangka menggunakan `try-except ValueError`.
- Memeriksa syarat ketiga sisi segitiga agar membentuk segitiga yang valid.
- Menampilkan hasil perhitungan dengan dua angka desimal.
- Menyediakan menu berulang sehingga pengguna dapat melakukan perhitungan kembali tanpa menjalankan ulang program.

## Persyaratan

- Python 3.x (tanpa library tambahan)

## Cara Menjalankan

```bash
git clone https://github.com/AzizahNurKholishah/pertemuan-15-kalkulator-geometri-2225250116.git
cd pertemuan-15-kalkulator-geometri-2225250116
python src/main.py
```

Di Windows, gunakan `python src/main.py`. Jika menggunakan sistem yang mengenali perintah `python3`, gunakan `python3 src/main.py`.

Menjalankan seluruh test case otomatis:

```bash
python -m unittest discover -s tests -v
```

## Struktur Folder

```text
pertemuan-15-analisis-proyek/
|-- README.md
|-- .gitignore
|-- src/
|   |-- main.py
|   `-- perhitungan.py
|-- tests/
|   |-- test_case.md
|   `-- test_program.py
`-- docs/
    `-- bug_log.md
```

Keterangan:

- `README.md`: Dokumentasi proyek dan panduan penggunaan program.
- `.gitignore`: Mengatur file sementara yang tidak perlu diunggah ke GitHub.
- `src/main.py`: Mengatur menu, input, validasi, dan tampilan hasil perhitungan.
- `src/perhitungan.py`: Berisi fungsi perhitungan luas dan keliling setiap bangun datar.
- `tests/test_case.md`: Berisi tabel pengujian dan hasil yang diperoleh.
- `tests/test_program.py`: Berisi pengujian otomatis menggunakan `unittest`.
- `docs/bug_log.md`: Berisi catatan bug, penyebab, dan perbaikan yang dilakukan.


## Test Case

Pengujian dilakukan untuk memastikan fungsi perhitungan menghasilkan nilai yang benar serta program mampu menangani input tidak valid. Pengujian mencakup kondisi normal, bilangan desimal, input batas, dan input yang tidak sesuai.

| ID | Fitur | Input | Expected | Actual | Status |
|---|---|---|---|---|---|
| TC01 | Persegi | Sisi = 5 | Luas 25, keliling 20 | Luas 25, keliling 20 | PASS |
| TC02 | Persegi panjang | Panjang = 6, lebar = 4 | Luas 24, keliling 20 | Luas 24, keliling 20 | PASS |
| TC03 | Segitiga | Alas = 6, tinggi = 4, sisi = 5, 5, 6 | Luas 12, keliling 16 | Luas 12, keliling 16 | PASS |
| TC04 | Lingkaran | Jari-jari = 7 | Luas ≈153.94, keliling ≈43.98 | Luas ≈153.94, keliling ≈43.98 | PASS |
| TC05 | Persegi desimal | Sisi = 2.5 | Luas 6.25, keliling 10 | Luas 6.25, keliling 10 | PASS |
| TC06 | Persegi panjang desimal | Panjang = 2.5, lebar = 4 | Luas 10, keliling 13 | Luas 10, keliling 13 | PASS |
| TC07 | Lingkaran desimal | Jari-jari = 0.5 | Luas ≈0.79, keliling ≈3.14 | Luas ≈0.79, keliling ≈3.14 | PASS |
| TC08 | Input nonangka | abc | Pesan input tidak valid | Input tidak valid! Masukkan angka. | PASS |
| TC09 | Input nol | 0 | Pesan input harus lebih dari nol | Input harus angka positif lebih dari 0! | PASS |
| TC10 | Pilihan menu tidak valid | 9 | Pesan pilihan tidak tersedia | Pilihan tidak tersedia! | PASS |
| TC11 | Segitiga tidak valid | Sisi = 1, 2, 5 | Pesan segitiga tidak valid | Ketiga sisi tidak membentuk segitiga! | PASS |

Hasil pengujian yang dicatat menunjukkan 7 pengujian otomatis dan 4 pengujian manual berhasil, dengan total 11 test case berstatus PASS.

Dokumentasi pengujian selengkapnya tersedia pada [tests/test_case.md](tests/test_case.md).

### Bug yang Ditemukan

| ID | Ringkasan | Status |
|---|---|---|
| BUG-01 | Input huruf menyebabkan `ValueError` karena konversi langsung menggunakan `float(input())` tanpa penanganan kesalahan | Closed |

Perbaikan dilakukan dengan menambahkan fungsi `input_positif()` yang menggunakan `try-except ValueError`. Setelah diperbaiki, program dapat menampilkan pesan kesalahan dan meminta pengguna memasukkan nilai kembali.

Detail debugging dan pengujian ulang terdapat pada [docs/bug_log.md](docs/bug_log.md).

## Known Issues

Berdasarkan pengujian yang telah dilakukan, tidak ditemukan bug utama yang menghambat fungsi perhitungan. Namun, program masih memiliki beberapa keterbatasan:

- Program hanya mendukung empat jenis bangun datar.
- Program masih menggunakan terminal dan belum memiliki antarmuka grafis.
- Hasil perhitungan belum dapat disimpan ke file.
- Pada perhitungan segitiga, program sudah memvalidasi syarat ketiga sisi, tetapi belum memeriksa sepenuhnya kesesuaian antara alas, tinggi, dan tiga sisi yang dimasukkan.

## Anggota dan Kontribusi

Proyek dikerjakan secara individu.

| Nama | NIM | Kontribusi |
|---|---|---|
| Azizah Nur Kholishah | 2225250116 | Perancangan, implementasi program, pengujian, debugging, dokumentasi, dan pengelolaan repository GitHub |

## Referensi/Bantuan

- Dokumentasi resmi Python 3 dan VS Code.
- Think Python (Downey, 2015).
- Bantuan AI untuk menyusun struktur proyek, contoh kode, dan dokumentasi. Algoritma, fungsi utama, test case, dan bug yang diperbaiki sudah saya baca dan pahami.