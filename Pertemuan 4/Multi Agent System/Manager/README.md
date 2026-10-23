# Simulasi Multi-Agent Foraging

Simulasi sederhana menggunakan **Python** untuk menggambarkan perilaku beberapa agen dalam mencari dan mengumpulkan resource pada lingkungan berbentuk grid. Program ini menggunakan pergerakan acak untuk menentukan tindakan agen, dengan mekanisme pemeriksaan posisi, pengambilan resource, dan perhitungan skor.

## Fitur Utama

* **Lingkungan Grid:** Membuat lingkungan berukuran 5×5 dengan resource yang ditempatkan secara acak.
* **Multi-Agent:** Menjalankan dua agen, yaitu Alpha dan Beta, dalam satu lingkungan yang sama.
* **Pergerakan Acak:** Agen bergerak satu sel ke arah atas, bawah, kiri, atau kanan.
* **Pengumpulan Resource:** Agen mengambil resource ketika berada pada koordinat yang sama dengan resource tersebut dan memperoleh satu poin.
* **Perhitungan Skor:** Menampilkan skor akhir dari setiap agen setelah simulasi selesai.
* **Visualisasi Terminal:** Menampilkan posisi agen, lokasi resource, dan jumlah resource yang tersisa pada setiap langkah.

## Komponen Program

Program terdiri dari tiga komponen utama:

* **Environment:** Mengatur ukuran grid, posisi resource, daftar agen, pemeriksaan batas lingkungan, dan tampilan simulasi.
* **ForagingAgent:** Mengelola posisi, skor, serta tindakan agen dalam mencari dan mengumpulkan resource.
* **Main Program:** Membuat lingkungan dan agen, menjalankan simulasi selama maksimal enam langkah, serta menampilkan hasil akhir.

## Representasi Grid

| Simbol | Keterangan |
| :---: | --- |
| `.` | Sel kosong |
| `$` | Resource yang belum dikumpulkan |
| `[A]` | Agen Alpha |
| `[B]` | Agen Beta |

## Alur Kerja

1. Program membuat lingkungan berukuran 5×5 dan menempatkan hingga lima resource pada koordinat acak.
2. Dua agen, Alpha dan Beta, dibuat dengan posisi awal yang ditentukan secara acak.
3. Pada setiap langkah, program menampilkan kondisi grid dan jumlah resource yang tersisa.
4. Setiap agen memeriksa apakah terdapat resource pada posisi saat ini.
5. Jika resource ditemukan, agen mengambilnya dan memperoleh satu poin. Jika tidak, agen mencoba bergerak ke salah satu sel yang berdekatan secara acak.
6. Simulasi berakhir setelah enam langkah atau ketika seluruh resource telah dikumpulkan.
7. Program menampilkan skor akhir masing-masing agen.

## Persyaratan

* Python 3.x
* Modul bawaan Python: `random`
* Tidak memerlukan instalasi library tambahan.

## Instalasi

### 1. Buka Terminal di VS Code dan Clone Repository

Jalankan perintah berikut pada terminal VS Code:

```bash
git clone https://github.com/DNALWANA/AI-EL1-09.git
```

### 2. Masuk ke Folder Proyek

```bash
cd AI-EL1-09/"Pertemuan 4/Multi Agent System/Manager"
```

### 3. Jalankan Program

```bash
python3 Gabungan.py
```

Jika perintah `python3` tidak dikenali pada Windows, gunakan:

```bash
python Gabungan.py
```

## Screenshot Hasil Program

Bagian ini berisi 21 screenshot yang mendokumentasikan hasil program. Gambar disusun dalam tiga kolom agar lebih mudah dilihat pada halaman repository GitHub.

**Catatan:** Simpan seluruh gambar di folder `assets` yang berada sejajar dengan file `README.md`. Nama file gambar harus sesuai dengan nama yang digunakan pada tabel berikut.

### Dokumentasi Hasil Simulasi

| Screenshot 1 | Screenshot 2 | Screenshot 3 |
| :---: | :---: | :---: |
| ![Screenshot 1](./assets/Screenshot_01.png) | ![Screenshot 2](./assets/Screenshot_02.png) | ![Screenshot 3](./assets/Screenshot_03.png) |
| Screenshot 4 | Screenshot 5 | Screenshot 6 |
| ![Screenshot 4](./assets/Screenshot_04.png) | ![Screenshot 5](./assets/Screenshot_05.png) | ![Screenshot 6](./assets/Screenshot_06.png) |
| Screenshot 7 | Screenshot 8 | Screenshot 9 |
| ![Screenshot 7](./assets/Screenshot_07.png) | ![Screenshot 8](./assets/Screenshot_08.png) | ![Screenshot 9](./assets/Screenshot_09.png) |
| Screenshot 10 | Screenshot 11 | Screenshot 12 |
| ![Screenshot 10](./assets/Screenshot_10.png) | ![Screenshot 11](./assets/Screenshot_11.png) | ![Screenshot 12](./assets/Screenshot_12.png) |
| Screenshot 13 | Screenshot 14 | Screenshot 15 |
| ![Screenshot 13](./assets/Screenshot_13.png) | ![Screenshot 14](./assets/Screenshot_14.png) | ![Screenshot 15](./assets/Screenshot_15.png) |
| Screenshot 16 | Screenshot 17 | Screenshot 18 |
| ![Screenshot 16](./assets/Screenshot_16.png) | ![Screenshot 17](./assets/Screenshot_17.png) | ![Screenshot 18](./assets/Screenshot_18.png) |
| Screenshot 19 | Screenshot 20 | Screenshot 21 |
| ![Screenshot 19](./assets/Screenshot_19.png) | ![Screenshot 20](./assets/Screenshot_20.png) | ![Screenshot 21](./assets/Screenshot_21.png) |

## Keterbatasan

### 1. Pergerakan Acak

Agen menentukan arah pergerakan secara acak tanpa menggunakan algoritma pencarian untuk menemukan resource secara efisien.

### 2. Interaksi Antar-Agen

Agen belum memiliki mekanisme komunikasi, berbagi informasi, atau koordinasi strategi dalam mengumpulkan resource.

### 3. Inisialisasi Acak

Posisi agen dan resource ditentukan secara acak. Beberapa resource dapat memiliki koordinat yang sama sehingga jumlah resource unik bisa kurang dari lima.

### 4. Jumlah Langkah Terbatas

Simulasi hanya berjalan selama maksimal enam langkah sehingga tidak menjamin seluruh resource dapat dikumpulkan.

## Pengembangan Selanjutnya

* Mengimplementasikan algoritma pencarian seperti Breadth-First Search (BFS) untuk membantu agen menemukan resource.
* Menambahkan memori agen untuk mencatat sel yang telah dikunjungi.
* Mengembangkan komunikasi dan koordinasi antar-agen.
* Mengevaluasi kinerja agen berdasarkan jumlah resource yang dikumpulkan dan langkah yang diperlukan.
* Menambahkan visualisasi grafis untuk menampilkan pergerakan agen secara langsung.
