
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
  - Menghapus catatan tertentu berdasarkan judul
  - Menghapus file catatan secara keseluruhan berdasarkan nama file
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

### Membuat Catatan

```python
from NoteMaster import buat_catatan

buat_catatan("Ini adalah catatan baru.")
```

### Mengedit Catatan

```python
from NoteMaster import edit_catatan

edit_catatan("Judul Catatan", "Ini adalah konten yang diperbarui.", "catatan.txt")
```

### Mencari Catatan

```python
from NoteMaster import pencarian_catatan

pencarian_catatan(catatan_list, "kata kunci")
```

### Menghapus Catatan

```python
from NoteMaster import hapus_item_catatan, hapus_catatan, hapus_all

hapus_item_catatan("my_notes/catatan.json", "note1")
hapus_catatan("my_notes/catatan.json", "note1")
hapus_all("my_notes/")
```

### Menampilkan Catatan

```python
from NoteMaster import tampilkan_catatan

tampilkan_catatan("my_notes")
```

### Menyimpan Catatan

```python
from NoteMaster import (
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

#### `buat_catatan(judul: str, isi: str, tipe_data: str) -> dict/str`
Fungsi ini digunakan untuk membuat catatan dengan format yang sesuai berdasarkan tipe data yang dipilih.

**Parameter:**
- `judul`: String yang berisi judul catatan yang ingin dibuat.
- `isi`: String yang berisi isi catatan yang ingin dibuat.
- `tipe_data`: String yang menentukan tipe data untuk menyimpan catatan. Nilai yang valid adalah `'csv'`, `'json'`, atau `'txt'`.

**Contoh Penggunaan:**
```python
catatan_json = buat_catatan("Catatan Pertama", "Ini adalah isi dari catatan pertama.", "json")
print(catatan_json)
```

**Output:**
Outputnya adalah data dengan type dict yang telah diformat dan mempunyai key "judul" juga "isi":
```
{
    "judul": "Catatan Pertama",
    "isi": "Ini adalah isi dari catatan pertama."
}
```

Jika `tipe_data` tidak valid, outputnya adalah:
```
ValueError: Tipe data tidak valid. Pilih antara 'csv', 'json', atau 'txt'.
```

### Catatan modul create_catatan
- Pastikan untuk memilih tipe data yang valid saat memanggil fungsi `buat_catatan()`.
- Fungsi ini berguna untuk menyimpan catatan dalam berbagai format, sehingga pengguna dapat memilih format yang paling sesuai dengan kebutuhan mereka.


### `module_2`

#### `hapus_item_catatan(file_path, identifier) -> None`
Fungsi ini digunakan untuk menghapus item dari file JSON, CSV, atau TXT berdasarkan judul.

**Parameter:**
- `file_path (str)`: Path lengkap dari file.
- `identifier (str)`: Judul dari catatan yang ingin dihapus di dalam file.

**Raises:**
- `FileNotFoundError`: Jika file tidak ditemukan pada path yang diberikan.
- `Exception`: Kesalahan umum lainnya saat mencoba menghapus item dalam file.

**Contoh Penggunaan:**
```python
hapus_item_catatan('my_notes/catatan.json', 'note1')
hapus_item_catatan('my_notes/catatan.csv', 'note1')
hapus_item_catatan('my_notes/catatan.txt', 'note1')
```

**Output:**
```
Item dengan judul [identifier] berhasil dihapus dari [file_path].
```
Jika file tidak ditemukan atau terjadi kesalahan lain, pesan kesalahan akan dicetak.

#### `hapus_catatan(file_path) -> None`
Menghapus file JSON, CSV, atau TXT secara keseluruhan.

**Parameter**
- `file_path (str)`: Path lengkap dari file yang akan dihapus.

**Raises:**
- `FileNotFoundError`: Jika file tidak ditemukan.

**Contoh Penggunaan:**
```python
hapus_catatan('my_notes/catatan.json')
```

**Output:**
```
File [file_path] berhasil dihapus.
```

#### `hapus_all(directory_path: str) -> None`
Fungsi ini digunakan untuk menghapus semua file dengan ekstensi .json, .csv, dan .txt dalam direktori yang diberikan.

**Parameter:**
- `directory_path`: Path lengkap dari direktori tempat file disimpan.

**Raises:**
- `FileNotFoundError`: Jika direktori tidak ditemukan atau tidak valid.
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

#### `edit_catatan(judul: str, isi_baru: str, filename: str, directory: str or none) -> None`
Fungsi ini digunakan untuk mengedit catatan dalam file yang ditentukan.

**Parameter:**
- `judul (str)`: Judul catatan yang ingin diedit.
- `isi_baru (str)`: Isi baru yang akan menggantikan isi catatan.
- `filename (str)`: Nama file yang berisi catatan. Harus memiliki ekstensi .csv, .json, atau .txt.
- `directory (str or None)`: Nama direktori tempat file berada, atau None jika file ada di root.

**Raises:**
- `FileNotFoundError`: Jika file tidak ditemukan.
- `ValueError`: Jika format file tidak didukung.

**Contoh Penggunaan:**
```python
edit_catatan("Catatan Pertama", "Ini adalah isi baru untuk catatan pertama.", "catatan.json", "my_notes")
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

#### `tampilkan_catatan(directory: str) -> None`
Fungsi ini digunakan untuk menampilkan isi catatan dari file yang ada dalam package.

**Parameter:**
- `directory`: Direktori tempat file berada (example: "Penyimpanan").

**Contoh Penggunaan:**
```python
tampilkan_catatan("My_files")
```

**Output:**
Jika directory ditemukan, fungsi akan menampilkan daftar file catatan yang tersedia. Pengguna kemudian diminta untuk memasukkan nama file catatan (tanpa ekstensi). Jika file ditemukan, isi file akan ditampilkan. Jika tidak, pesan kesalahan akan dicetak.

Jika nama file yang sama ditemukan lebih dari satu dan berbeda ekstensi maka pengguna diminta memasukkan nomor dari catatan yang telah diurutkan, dan masukkan 'semua' untuk menampilkan semua isi dari catatan yang memiliki nama yang sama tersebut.

Contoh output saat file ditemukan:
```
File catatan yang tersedia:
- catatan.csv
- note.txt
- catatan.json

Masukkan nama file catatan (tanpa ekstensi): catatan
```
```
Ada beberapa file dengan nama 'catatan' dengan ekstensi yang berbeda:
1. catatan.csv
2. catatan.json
Pilih file yang ingin ditampilkan (masukkan nomor atau ketik 'semua' untuk menampilkan semua): semua
```
```
Menampilkan isi dari catatan.txt:

[Isi dari catatan.txt]
```

Jika directory tidak ditemukan, outputnya adalah:
```
Directory 'My_files' tidak ditemukan.
```

Jika tidak ada catatan ditemukan untuk nama file yang dimasukkan, outputnya adalah:
```
Tidak ada file yang cocok dengan nama '[nama_file]'.
```

### Catatan modul 4
- Pastikan direktori yang berisi catatan sudah ada dan dapat diakses.
- Fungsi ini tidak mengembalikan nilai, tetapi mencetak pesan status dan isi file ke konsol.


### `module_5`


#### `cari_catatan(directory: str, kata_kunci: str) -> None`
Fungsi ini digunakan untuk melakukan pencarian catatan berdasarkan kata kunci dari semua file di direktori.

**Parameter:**
- `directory`: Path direktori tempat catatan berada (misalnya, 'my_notes').
- `kata_kunci`: Kata kunci yang akan dicari dalam judul dan isi catatan.

**Returns:**
- Tidak ada: Hasil pencarian akan ditampilkan langsung di terminal/console.

**Contoh Penggunaan:**
```python
cari_catatan('my_notes', 'kedua')
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

### Catatan Modul
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