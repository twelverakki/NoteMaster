import os
import json
import csv

def baca_catatan(file_path):
    """
    Membaca catatan dari file JSON, CSV, atau TXT dan mengembalikan daftar catatan.

    Args:
        file_path (str): Path file yang akan dibaca.

    Returns:
        list: Daftar catatan dalam bentuk dictionary dengan kunci 'Judul' dan 'Isi'.
    """
    _, file_extension = os.path.splitext(file_path)
    catatan_list = []

    if file_extension == '.json':
        with open(file_path, 'r', encoding='utf-8') as file:
            catatan_list = json.load(file)

    elif file_extension == '.csv':
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                judul = row['Judul'].strip().lower()  # Menghapus spasi dan konversi ke lowercase
                isi = row['Isi'].strip().lower()
                catatan_list.append({'Judul': judul, 'Isi': isi})

            # print(catatan_list)

    elif file_extension == '.txt':
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                if ':' in line:
                    judul, isi = line.strip().split(':', 1)
                    catatan_list.append({'Judul': judul.strip(), 'Isi': isi.strip()})
                else:
                    print(f"Baris tidak sesuai format di {file_path}: '{line.strip()}'")

    return catatan_list


def cari_catatan(directory, kata_kunci):
    """
    Fungsi untuk melakukan pencarian catatan berdasarkan kata kunci dari semua file di direktori.

    Args:
        directory (str): Path direktori tempat catatan berada (my_notes).
        kata_kunci (str): Kata kunci yang akan dicari dalam judul dan isi catatan.

    Returns:
        None: Menampilkan hasil pencarian langsung di terminal.
    """
    kata_kunci = kata_kunci.strip().lower()

    if not kata_kunci:
        print("Kata kunci tidak boleh kosong atau hanya berisi spasi.")
        return

    semua_catatan = []

    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path) and file_name.endswith(('.json', '.csv', '.txt')):
            catatan_list = baca_catatan(file_path)
            semua_catatan.extend(catatan_list)

    hasil_pencarian = [
        catatan for catatan in semua_catatan
        if kata_kunci in catatan.get('Judul', '').lower() or kata_kunci in catatan.get('Isi', '').lower()
    ]

    if hasil_pencarian:
        print(f"\nHasil pencarian untuk kata kunci '{kata_kunci}':")
        for catatan in hasil_pencarian:
            print(f"- {catatan['Judul']}: {catatan['Isi']}")
            print("-" * 40)
    else:
        print(f"\nTidak ada catatan yang ditemukan dengan kata kunci '{kata_kunci}'.")