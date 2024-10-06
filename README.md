
<h1 align="center">NoteMaster</h1>

NoteMaster adalah paket Python yang menyediakan serangkaian alat untuk membantu Anda mengelola catatan. Paket ini memungkinkan Anda untuk menambah, melihat, mengedit, mencari, menghapus, dan menyimpan catatan dalam berbagai format file seperti JSON, CSV, dan TXT.

## Fitur

- **Manajemen Catatan**:
  - Menambah catatan baru
  - Melihat semua catatan yang ada
  - Menambahkan catatan ke catatan yang sudah ada
- **Pengeditan Catatan**:
  - Mengedit konten catatan berdasarkan judul
- **Pencarian Catatan**:
  - Mencari catatan yang mengandung kata kunci tertentu
  - Menampilkan hasil pencarian
- **Penghapusan Catatan**:
  - Menghapus catatan tertentu berdasarkan ID
  - Menghapus semua catatan dalam direktori
- **Penyimpanan Catatan**:
  - Menyimpan catatan ke dalam format JSON, CSV, atau TXT
  - Membuat cadangan catatan ke direktori terpisah

## Instalasi

Untuk menginstal paket NoteMaster, gunakan pip:

```bash
pip install NoteMaster
```

## Cara Menggunakan

Berikut adalah beberapa contoh cara menggunakan paket NoteMaster:

### Menambah Catatan

```python
from NoteMaster.module_1 import tambah_catatan
tambah_catatan("Ini adalah catatan baru.")
```

### Mengedit Catatan

```python
from NoteMaster.module_3 import edit_catatan
edit_catatan("Judul Catatan", "Ini adalah konten yang diperbarui.", "catatan.txt")
```

### Mencari Catatan

```python
from NoteMaster.module_5 import pencarian_catatan
pencarian_catatan(catatan_list, "kata kunci")
```

### Menghapus Catatan

```python
from NoteMaster.module_2 import hapus_catatan
hapus_catatan("catatan.json", 1)
```

### Menampilkan Catatan

```python
from NoteMaster.module_4 import tampilkan_catatan
tampilkan_catatan("NoteMaster")
```

### Menyimpan Catatan

```python
from NoteMaster.module_6 import (
    simpan_catatan_json,
    simpan_catatan_txt,
    simpan_catatan_csv,
    backup_catatan
)

simpan_catatan_json(catatan_list, "catatan.json")
simpan_catatan_txt(catatan_list, "catatan.txt")
simpan_catatan_csv(catatan_list, "catatan.csv")
backup_catatan("catatan.json", "backup/catatan.json")
```

## Tentang Modul

Paket NoteMaster terdiri dari modul-modul berikut:

### `module_1`


#### `tambah_catatan(note: str) -> None`
Fungsi ini digunakan untuk menambah catatan baru ke dalam daftar.

**Parameter:**
- `note`: String yang berisi catatan yang ingin ditambahkan.

**Contoh Penggunaan:**
```python
tambah_catatan("Ini adalah catatan pertama.")
```

**Output:**
```
Catatan berhasil ditambahkan: Ini adalah catatan pertama.
```

#### `view_notes() -> None`
Fungsi ini digunakan untuk melihat semua catatan yang ada dalam daftar.

**Contoh Penggunaan:**
```python
view_notes()
```

**Output:**
```
1. Ini adalah catatan pertama.
```
Jika tidak ada catatan yang tersedia, outputnya adalah:
```
Tidak ada catatan yang tersedia.
```

#### `tambah_catatan_existing(index: int, note: str) -> None`
Fungsi ini digunakan untuk menambahkan catatan baru ke catatan yang sudah ada (di akhir).

**Parameter:**
- `index`: Indeks catatan yang ingin ditambahkan.
- `note`: String yang berisi catatan yang ingin ditambahkan ke catatan yang sudah ada.

**Contoh Penggunaan:**
```python
tambah_catatan_existing(0, "Ini adalah tambahan untuk catatan pertama.")
```

**Output:**
```
Catatan berhasil ditambahkan ke catatan nomor 1: Ini adalah tambahan untuk catatan pertama.
```
Jika indeks tidak valid, outputnya adalah:
```
Index catatan tidak valid.
```

### Catatan modul 1
- Pastikan untuk memanggil fungsi `tambah_catatan()` sebelum menggunakan `view_notes()` atau `tambah_catatan_existing()` agar ada catatan yang dapat dilihat atau ditambahkan.
- Indeks yang digunakan dalam `tambah_catatan_existing()` dimulai dari 0.

### `module_2`

#### `hapus_catatan(file_path: str, note_id: int) -> None`
Fungsi ini digunakan untuk menghapus catatan dari file berdasarkan ID catatan.

**Parameter:**
- `file_path`: Path lengkap dari file yang akan dihapus.
- `note_id`: ID catatan yang ingin dihapus.

**Raises:**
- `FileNotFoundError`: Jika file tidak ditemukan pada path yang diberikan.
- `PermissionError`: Jika tidak ada izin yang cukup untuk menghapus file.
- `Exception`: Kesalahan umum lainnya saat mencoba menghapus file.

**Contoh Penggunaan:**
```python
hapus_catatan('notes/catatan.json', 1)
```

**Output:**
```
File notes/catatan.json berhasil dihapus.
```
Jika file tidak ditemukan atau terjadi kesalahan lain, pesan kesalahan akan dicetak.

#### `hapus_all(directory_path: str) -> None`
Fungsi ini digunakan untuk menghapus semua file dengan ekstensi .json, .csv, dan .txt dalam direktori yang diberikan.

**Parameter:**
- `directory_path`: Path lengkap dari direktori tempat file disimpan.

**Raises:**
- `FileNotFoundError`: Jika direktori tidak ditemukan atau tidak valid.
- `PermissionError`: Jika tidak ada izin yang cukup untuk menghapus file.
- `Exception`: Kesalahan umum lainnya saat mencoba menghapus file.

**Contoh Penggunaan:**
```python
hapus_all('data/')
```

**Output:**
```
File data/catatan1.json berhasil dihapus.
File data/catatan2.csv berhasil dihapus.
File data/catatan3.txt berhasil dihapus.
```
Jika ada kesalahan dalam penghapusan file atau direktori tidak ditemukan, pesan kesalahan akan dicetak.

### Catatan modul 2
- Pastikan untuk memeriksa izin file dan direktori sebelum menggunakan fungsi ini untuk menghindari kesalahan izin.
- Fungsi ini tidak mengembalikan nilai, tetapi mencetak pesan status ke konsol.

### `module_3`

#### `edit_catatan(judul: str, isi_baru: str, filename: str) -> None`
Fungsi ini digunakan untuk mengedit catatan dalam file yang ditentukan.

**Parameter:**
- `judul`: Judul catatan yang ingin diedit.
- `isi_baru`: Isi baru yang akan menggantikan isi catatan.
- `filename`: Nama file yang berisi catatan. Harus memiliki ekstensi .csv, .json, atau .txt.

**Raises:**
- `FileNotFoundError`: Jika file tidak ditemukan.
- `ValueError`: Jika format file tidak didukung.

**Contoh Penggunaan:**
```python
edit_catatan("Catatan Pertama", "Ini adalah isi baru untuk catatan pertama.", "catatan.json")
```

**Output:**
```
Catatan berhasil diedit.
```
Jika catatan dengan judul yang diberikan tidak ditemukan, outputnya adalah:
```
Catatan dengan judul ini tidak ditemukan.
```
Jika file tidak ditemukan, outputnya adalah:
```
Tidak ada catatan yang ditemukan.
```
Jika format file tidak didukung, outputnya adalah:
```
Format file tidak didukung. Gunakan .csv, .json, atau .txt.
```

### Catatan modul 3
- Pastikan untuk memeriksa izin file sebelum menggunakan fungsi ini untuk menghindari kesalahan izin.
- Fungsi ini tidak mengembalikan nilai, tetapi mencetak pesan status ke konsol.

### `module_4`

#### `tampilkan_catatan(package_name: str, directory: str = ".") -> None`
Fungsi ini digunakan untuk menampilkan isi catatan dari file yang ada dalam package.

**Parameter:**
- `package_name`: Nama direktori yang berisi catatan.
- `directory`: Direktori tempat package berada (default: ".").

**Contoh Penggunaan:**
```python
tampilkan_catatan("CatatanSaya")
```

**Output:**
Jika package ditemukan, fungsi akan menampilkan daftar file catatan yang tersedia. Pengguna kemudian diminta untuk memasukkan nama file catatan (tanpa ekstensi). Jika file ditemukan, isi file akan ditampilkan. Jika tidak, pesan kesalahan akan dicetak.

Contoh output saat file ditemukan:
```
File catatan yang tersedia:
- catatan.csv
- catatan.txt
- catatan.json

Masukkan nama file catatan (tanpa ekstensi): catatan
Menampilkan isi dari catatan.txt:

[Isi dari catatan.txt]
```

Jika package tidak ditemukan, outputnya adalah:
```
Package 'CatatanSaya' tidak ditemukan di direktori .
```

Jika tidak ada catatan ditemukan untuk nama file yang dimasukkan, outputnya adalah:
```
Tidak ada catatan ditemukan untuk 'catatan' dengan ekstensi yang diizinkan.
```

### Catatan modul 4
- Pastikan direktori yang berisi catatan sudah ada dan dapat diakses.
- Fungsi ini tidak mengembalikan nilai, tetapi mencetak pesan status dan isi file ke konsol.


### `module_5`

#### `cari_catatan(catatan_list: list, kata_kunci: str) -> list`
Fungsi ini digunakan untuk mencari catatan yang sesuai dengan kata kunci.

**Parameter:**
- `catatan_list`: Daftar catatan, di mana setiap catatan adalah dictionary yang memiliki setidaknya kunci 'judul' dan 'isi'.
- `kata_kunci`: Kata kunci yang akan dicari di dalam judul dan isi catatan.

**Returns:**
- Daftar catatan yang mengandung kata kunci di judul atau isi.

**Contoh Penggunaan:**
```python
catatan_list = [
    {'judul': 'Catatan Pertama', 'isi': 'Ini adalah isi catatan pertama.'},
    {'judul': 'Catatan Kedua', 'isi': 'Ini adalah isi catatan kedua.'}
]

hasil = cari_catatan(catatan_list, 'pertama')
print(hasil)
```

**Output:**
```
[{'judul': 'Catatan Pertama', 'isi': 'Ini adalah isi catatan pertama.'}]
```

#### `pencarian_catatan(catatan_list: list, kata_kunci: str) -> None`
Fungsi ini digunakan untuk melakukan pencarian catatan berdasarkan kata kunci dan menampilkan hasilnya.

**Parameter:**
- `catatan_list`: Daftar catatan yang akan dicari, masing-masing catatan adalah dictionary dengan setidaknya kunci 'judul' dan 'isi'.
- `kata_kunci`: Kata kunci yang akan dicari dalam judul dan isi catatan.

**Returns:**
- Tidak ada: Hasil pencarian akan ditampilkan langsung di terminal/console.

**Contoh Penggunaan:**
```python
pencarian_catatan(catatan_list, 'kedua')
```

**Output:**
```
Hasil pencarian untuk kata kunci 'kedua':
- Catatan Kedua: Ini adalah isi catatan kedua.
----------------------------------------
```
Jika tidak ada catatan yang ditemukan, outputnya adalah:
```
Tidak ada catatan yang ditemukan dengan kata kunci 'kedua'.
```

### Catatan modul 5
- Pastikan kata kunci tidak kosong atau hanya berisi spasi sebelum melakukan pencarian.
- Fungsi ini tidak mengembalikan nilai, tetapi mencetak hasil pencarian ke konsol.

### `module_6`
#### `simpan_catatan_json(catatan_list: List[Dict[str, str]], file_path: str) -> None`
Menyimpan daftar catatan ke dalam file dengan format JSON.

**Parameter:**
- `catatan_list`: Daftar catatan yang akan disimpan. Setiap catatan adalah dictionary dengan kunci 'judul' dan 'isi'.
- `file_path`: Jalur file tempat catatan akan disimpan.

**Returns:**
- Tidak ada.

**Raises:**
- `FileNotFoundError`: Jika jalur file tidak ditemukan.
- `IOError`: Jika terjadi kesalahan I/O saat menyimpan catatan.

**Contoh Penggunaan:**
```python
catatan = [{"judul": "Catatan 1", "isi": "Ini adalah isi catatan 1."}]
simpan_catatan_json(catatan, "catatan.json")
```

#### `simpan_catatan_txt(catatan_list: List[Dict[str, str]], file_path: str) -> None`
Menyimpan daftar catatan ke dalam file dengan format TXT.

**Parameter:**
- `catatan_list`: Daftar catatan yang akan disimpan. Setiap catatan adalah dictionary dengan kunci 'judul' dan 'isi'.
- `file_path`: Jalur file tempat catatan akan disimpan.

**Returns:**
- Tidak ada.

**Raises:**
- `FileNotFoundError`: Jika jalur file tidak ditemukan.
- `IOError`: Jika terjadi kesalahan I/O saat menyimpan catatan.

**Contoh Penggunaan:**
```python
catatan = [{"judul": "Catatan 1", "isi": "Ini adalah isi catatan 1."}]
simpan_catatan_txt(catatan, "catatan.txt")
```

#### `simpan_catatan_csv(catatan_list: List[Dict[str, str]], file_path: str) -> None`
Menyimpan daftar catatan ke dalam file dengan format CSV.

**Parameter:**
- `catatan_list`: Daftar catatan yang akan disimpan. Setiap catatan adalah dictionary dengan kunci 'judul' dan 'isi'.
- `file_path`: Jalur file tempat catatan akan disimpan.

**Returns:**
- Tidak ada.

**Raises:**
- `FileNotFoundError`: Jika jalur file tidak ditemukan.
- `IOError`: Jika terjadi kesalahan I/O saat menyimpan catatan.

**Contoh Penggunaan:**
```python
catatan = [{"judul": "Catatan 1", "isi": "Ini adalah isi catatan 1."}]
simpan_catatan_csv(catatan, "catatan.csv")
```

### `backup_catatan(file_path: str, backup_path: str) -> None`
Membuat salinan cadangan dari file catatan.

**Parameter:**
- `file_path`: Jalur file catatan yang akan dicadangkan.
- `backup_path`: Jalur tempat cadangan akan disimpan.

**Returns:**
- Tidak ada.

**Raises:**
- `FileNotFoundError`: Jika file catatan tidak ditemukan.
- `Exception`: Jika terjadi kesalahan saat membuat backup.

**Contoh Penggunaan:**
```python
backup_catatan("catatan.json", "backup/catatan_backup.json")
```

### Catatan modul 6
- Pastikan untuk memeriksa izin file dan direktori sebelum menggunakan fungsi ini untuk menghindari kesalahan izin.
- Fungsi ini tidak mengembalikan nilai, tetapi mencetak pesan status ke konsol.


Paket ini dirancang untuk memudahkan pengelolaan catatan Anda dengan berbagai pilihan format penyimpanan dan fitur yang fleksibel untuk pencatatan dan manajemen catatan.

## Kontak
Untuk pertanyaan lebih lanjut, silakan hubungi:
- twelve.rakki@gmail.com.
- qhosans@gmail.com