# Dasar-Dasar Pemrograman — Pertemuan 6

Halo! Saya **Diego**, dan selamat datang di repository latihan Python saya.

Repository ini berisi empat latihan dari mata kuliah **Dasar-Dasar Pemrograman (DDP)** pada pertemuan ke-6. Latihan ini bertujuan untuk memahami penggunaan variabel, tipe data, input/output, f-string, serta operasi aritmetika dasar menggunakan Python.

## Informasi Mahasiswa

- **Nama:** Komang Christdiego Anadika Junior
- **NIM:** 2601010002
- **Program Studi:** Sistem Informasi
- **Kelas:** SI Pagi A

## Daftar Latihan

### 1. Biodata — `latihan1_biodata.py`

Program untuk menampilkan informasi biodata yang disimpan dalam variabel, meliputi nama, NIM, program studi, dan hobi.

**Konsep:** Variabel, string, `print()`, dan f-string.

### 2. Persegi Panjang — `latihan2_persegi_panjang.py`

Program untuk menghitung luas dan keliling persegi panjang berdasarkan input panjang dan lebar dari pengguna.

**Rumus:**
- Luas = Panjang × Lebar
- Keliling = 2 × (Panjang + Lebar)

**Contoh:** Panjang 8 m dan lebar 5 m menghasilkan luas 40 m² serta keliling 26 m.

Program ini juga dilengkapi **trace table** dalam bentuk komentar pada bagian akhir file untuk menjelaskan perubahan nilai variabel selama eksekusi.

### 3. Konversi Suhu — `latihan3_konversi_suhu.py`

Program untuk mengonversi suhu dari Celsius ke Fahrenheit dan Kelvin.

**Rumus:**
- Fahrenheit = (Celsius × 9/5) + 32
- Kelvin = Celsius + 273.15

**Konsep:** Input pengguna, tipe data numerik, dan operasi aritmetika.

### 4. Total Belanja — `latihan4_total_belanja.py`

Program sederhana untuk menghitung total pembayaran berdasarkan nama barang, harga satuan, dan jumlah barang, termasuk PPN 11% sesuai ketentuan latihan.

**Rumus:**
- Subtotal = Harga × Jumlah
- PPN = Subtotal × 0.11
- Total Bayar = Subtotal + PPN

**Contoh:** Pembelian 3 buku dengan harga Rp25.000 per buku menghasilkan subtotal Rp75.000, PPN Rp8.250, dan total pembayaran Rp83.250.

## Cara Menjalankan Program

### 1. Persiapan

Pastikan Python 3 sudah terinstal. Git juga diperlukan jika ingin melakukan clone repository.

### 2. Clone Repository

Buka terminal atau Git Bash, kemudian jalankan:

```bash
git clone https://github.com/itskaizendev/ddp-python-2601010002.git
```

Masuk ke folder project:

```bash
cd ddp-python-2601010002
```

### 3. Jalankan Program

Gunakan salah satu perintah berikut:

```bash
# Latihan 1: Biodata
python latihan1_biodata.py

# Latihan 2: Persegi Panjang
python latihan2_persegi_panjang.py

# Latihan 3: Konversi Suhu
python latihan3_konversi_suhu.py

# Latihan 4: Total Belanja
python latihan4_total_belanja.py
```

**Catatan:** Pada Windows, jika perintah `python` tidak dikenali, coba gunakan `py`.

## Struktur Repository

```text
ddp-python-2601010002/
├── latihan1_biodata.py
├── latihan2_persegi_panjang.py
├── latihan3_konversi_suhu.py
├── latihan4_total_belanja.py
└── README.md
```

## Versi

**v1.0-beta — Initial Release**

Versi awal yang mencakup empat latihan dasar Python beserta dokumentasi penggunaannya.

## Penutup

Repository ini merupakan bagian dari proses pembelajaran saya dalam memahami dasar-dasar pemrograman menggunakan Python.

Setiap latihan dikerjakan untuk melatih pemahaman terhadap logika program, pengolahan input, perhitungan, dan penyajian output.

---

**Author:** Diego

**Language:** Python 3

**Version:** v1.0-beta
