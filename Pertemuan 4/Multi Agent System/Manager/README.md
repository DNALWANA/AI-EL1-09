# 🌱 Multi-Agent Foraging Simulation

Simulasi sederhana **Multi-Agent System (MAS)** menggunakan Python, di mana beberapa agen bergerak dalam suatu lingkungan untuk mencari dan mengumpulkan resource. Program ini menerapkan konsep dasar *agent-based simulation*, *environment*, *perception*, dan *action* dalam Artificial Intelligence (AI).

## 📌 Deskripsi Proyek

Proyek ini mensimulasikan dua agen, yaitu **Alpha** dan **Beta**, yang berada di dalam lingkungan berbentuk grid berukuran 5 × 5. Setiap agen memiliki posisi awal acak dan berusaha menemukan resource yang tersebar secara acak di lingkungan.

Agen akan memeriksa apakah terdapat resource pada posisi saat ini. Jika resource ditemukan, agen mengambilnya dan memperoleh satu poin. Jika tidak, agen bergerak secara acak ke salah satu arah yang berdekatan, selama posisi tujuan masih berada di dalam batas lingkungan.

Simulasi berlangsung selama maksimal enam langkah atau berhenti lebih awal jika seluruh resource berhasil dikumpulkan.

## 🎯 Tujuan

- Memahami konsep dasar Multi-Agent System dalam Artificial Intelligence.
- Mengimplementasikan agen yang dapat mengamati lingkungan dan melakukan tindakan.
- Memahami interaksi antara agen dan environment.
- Mensimulasikan pergerakan agen dalam grid dua dimensi.
- Menghitung skor berdasarkan resource yang berhasil dikumpulkan.

## ⚙️ Teknologi yang Digunakan

- **Bahasa pemrograman:** Python 3
- **Library:** `random` (standard library Python)
- **Konsep AI:** Multi-Agent System, Agent-Based Simulation, Perception and Action
- **Visualisasi:** Output berbasis teks pada terminal

## 🧠 Konsep dan Komponen Program

### 1. Environment

Class `Environment` merepresentasikan dunia tempat agen beroperasi.

Fungsi utamanya:
- Menentukan ukuran grid berdasarkan `width` dan `height`.
- Menempatkan lima resource pada koordinat acak.
- Menyimpan daftar agen yang berpartisipasi dalam simulasi.
- Memeriksa apakah posisi masih berada dalam batas grid.
- Menampilkan kondisi lingkungan pada setiap langkah simulasi.

### 2. ForagingAgent

Class `ForagingAgent` merepresentasikan agen yang bertugas mencari dan mengumpulkan resource.

Setiap agen memiliki:
- `name`: nama agen.
- `env`: referensi ke environment.
- `x` dan `y`: koordinat posisi agen.
- `score`: jumlah resource yang berhasil dikumpulkan.

Metode `perceive_and_act()` mengatur perilaku agen:

1. Memeriksa apakah terdapat resource pada posisi saat ini.
2. Mengambil resource jika tersedia.
3. Menambahkan skor sebanyak satu poin.
4. Bergerak secara acak jika tidak menemukan resource.
5. Memastikan perpindahan tidak keluar dari batas grid.

### 3. Main Program

Fungsi `main()` menjalankan keseluruhan simulasi dengan tahapan berikut:

1. Membuat environment berukuran 5 × 5.
2. Membuat dua agen, Alpha dan Beta.
3. Menambahkan agen ke dalam environment.
4. Menjalankan simulasi selama maksimal enam langkah.
5. Menampilkan kondisi grid dan aktivitas agen.
6. Menghentikan simulasi jika seluruh resource habis.
7. Menampilkan skor akhir setiap agen.

## 🗺️ Simbol Visualisasi

| Simbol | Keterangan |
|---|---|
| `.` | Sel kosong |
| `$` | Resource yang belum dikumpulkan |
| `[A]` | Posisi agen Alpha |
| `[B]` | Posisi agen Beta |

**Catatan:** Jika agen berada pada koordinat yang sama dengan resource, simbol agen akan diprioritaskan dalam tampilan grid.

## 🚀 Cara Menjalankan Program

### Prasyarat

Pastikan Python 3 telah terinstal pada komputer.

Periksa instalasi Python melalui terminal:

```bash
python --version
```

### Langkah 1 — Clone Repository

Ganti `USERNAME` dan `REPOSITORY` dengan informasi repository GitHub milikmu.

```bash
git clone https://github.com/USERNAME/REPOSITORY.git
```

### Langkah 2 — Masuk ke Folder Proyek

```bash
cd REPOSITORY
```

### Langkah 3 — Jalankan Program

Jika file Python bernama `foraging_simulation.py`, jalankan perintah:

```bash
python foraging_simulation.py
```

Tidak diperlukan instalasi library tambahan karena program hanya menggunakan modul bawaan Python.

## 📊 Contoh Output

Berikut ilustrasi format output yang akan ditampilkan di terminal. Posisi agen dan resource pada eksekusi sebenarnya akan berbeda karena ditentukan secara acak.

```text
--- Simulasi Langkah ke-1 ---
  .    $    .    .    .
  .   [A]   .    .    .
  .    .    .   [B]   .
  $    .    .    .    .
  .    .    $    .    .
Sisa Resource di Environment: 5

[Alpha] Menemukan dan mengambil resource di (1, 1)! Skor: 1

--- Hasil Akhir Simulasi ---
Skor Alpha: 1
Skor Beta: 0
```

*Output di atas hanya contoh ilustratif, bukan hasil eksekusi aktual.*

## 🔄 Alur Kerja Simulasi

```text
Mulai
  |
  v
Inisialisasi Environment
  |
  v
Buat Agen Alpha dan Beta
  |
  v
Tampilkan Kondisi Grid
  |
  v
Agen Mengamati Posisi Saat Ini
  |
  v
Apakah Ada Resource?
  |
  +---- Ya ----> Ambil Resource dan Tambah Skor
  |
  +---- Tidak -> Bergerak Secara Acak
  |
  v
Apakah Semua Resource Habis?
  |
  +---- Ya ----> Tampilkan Skor Akhir -> Selesai
  |
  +---- Tidak -> Lanjut ke Langkah Berikutnya
```

## ⚠️ Batasan Program

Beberapa batasan pada implementasi saat ini:

- Pergerakan agen dilakukan secara acak, tanpa algoritma pencarian jalur.
- Agen tidak memiliki memori mengenai lokasi yang telah dikunjungi.
- Agen tidak berkomunikasi atau berkoordinasi secara eksplisit.
- Posisi awal agen dan resource ditentukan secara acak.
- Simulasi memiliki batas maksimal enam langkah.
- Resource dapat menempati koordinat yang sama pada proses pembangkitan awal, sehingga jumlah resource unik bisa kurang dari lima.
- Agen dapat berada pada koordinat yang sama karena tidak ada mekanisme pencegahan tabrakan.

## 🔮 Pengembangan Selanjutnya

Proyek ini dapat dikembangkan dengan menambahkan beberapa fitur:

- **Intelligent Search:** Menggunakan algoritma BFS, DFS, atau A* untuk mencari resource.
- **Agent Memory:** Menyimpan riwayat pergerakan dan lokasi resource yang pernah ditemukan.
- **Cooperation:** Membuat agen berbagi informasi untuk meningkatkan efisiensi pengumpulan resource.
- **Performance Evaluation:** Membandingkan jumlah resource yang dikumpulkan, langkah yang diperlukan, dan tingkat keberhasilan agen.
- **Visualization:** Membuat animasi pergerakan agen menggunakan Pygame atau Matplotlib.
- **Reproducible Simulation:** Menggunakan random seed agar hasil percobaan dapat diulang.

## 📚 Konsep Artificial Intelligence yang Dipelajari

Proyek ini memperkenalkan implementasi dasar beberapa konsep AI:

- Intelligent Agents
- Agent–Environment Interaction
- Perception and Action
- Multi-Agent Systems
- Randomized Decision Making
- Agent-Based Modeling and Simulation

*Proyek pembelajaran Artificial Intelligence — simulasi dasar Multi-Agent Foraging menggunakan Python.*
