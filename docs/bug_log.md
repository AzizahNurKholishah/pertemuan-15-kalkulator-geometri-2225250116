
# Bug Log

## Kalkulator Geometri Bangun Datar — Pertemuan 15

| ID | Gejala | Test | Lokasi | Penyebab | Perbaikan | Status |
|---|---|---|---|---|---|---|
| BUG-01 | Program berhenti dan menampilkan ValueError ketika pengguna memasukkan huruf seperti "abc" pada input ukuran bangun datar. | TC08 | `src/main.py`, input ukuran | Fungsi `float(input())` tidak dapat mengubah input huruf menjadi angka dan belum memiliki penanganan kesalahan. | Membuat fungsi `input_positif()` dengan `try-except ValueError` agar program menampilkan pesan kesalahan dan meminta input ulang. | Closed |

## Bukti Perbaikan

Pada versi awal Pertemuan 14, program menggunakan:

`float(input("Masukkan panjang sisi: "))`

Jika pengguna memasukkan huruf, program berhenti karena ValueError.

Pada Pertemuan 15, kode diperbaiki dengan menambahkan fungsi `input_positif()` yang menggunakan `try-except` dan perulangan untuk menangani input tidak valid.

## Pengujian Ulang

Setelah perbaikan, dilakukan pengujian ulang terhadap input tidak valid dan fungsi perhitungan.

- TC08: Input huruf "abc" berhasil ditangani.
- TC09: Input angka 0 ditolak sesuai validasi.
- TC10: Pilihan menu 9 menampilkan pesan kesalahan.
- TC11: Panjang sisi 1, 2, dan 5 ditolak karena tidak membentuk segitiga.

Selain itu, 7 pengujian otomatis dijalankan kembali untuk memastikan fungsi perhitungan tetap berjalan.

## Kesimpulan

Perbaikan dilakukan pada bagian validasi input tanpa mengubah fungsi utama kalkulator geometri. Dengan penambahan penanganan kesalahan, program lebih stabil dan dapat memberikan pesan yang jelas ketika pengguna memasukkan input tidak valid.
