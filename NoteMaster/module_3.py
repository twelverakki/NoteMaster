import json
import csv
import os

def edit_catatan(judul, isi_baru, filename):
    """
    Mengedit catatan dalam file yang ditentukan.

    Fungsi ini mencari catatan berdasarkan judul yang diberikan dan
    memperbarui isinya dengan isi baru. Mendukung format file CSV,
    JSON, dan TXT. Pengguna harus menentukan nama file yang ingin
    diedit.

    Args:
        judul (str): Judul catatan yang ingin diedit.
        isi_baru (str): Isi baru yang akan menggantikan isi catatan.
        filename (str): Nama file yang berisi catatan.
        Harus memiliki ekstensi .csv, .json, atau .txt.

    Raises:
        FileNotFoundError: Jika file tidak ditemukan.
        ValueError: Jika format file tidak didukung.

    Returns:
        None: Fungsi ini tidak mengembalikan nilai,
        tetapi mencetak pesan status ke konsol.
    """
    file_extension = os.path.splitext(filename)[1].lower()

    if file_extension == '.csv':
        try:
            with open(filename, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                data = list(reader)
        except FileNotFoundError:
            print("Tidak ada catatan yang ditemukan.")
            return

        found = False
        for row in data:
            if row['Judul'] == judul:
                row['Isi'] = isi_baru
                found = True
                break

        if not found:
            print("Catatan dengan judul ini tidak ditemukan.")
            return

        with open(filename, mode='w', newline='') as file:
            fieldnames = ['Judul', 'Isi']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        print("Catatan berhasil diedit.")

    elif file_extension == '.json':
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            print("Tidak ada catatan yang ditemukan.")
            return

        if judul not in data:
            print("Catatan dengan judul ini tidak ditemukan.")
            return

        data[judul] = isi_baru
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        print("Catatan berhasil diedit.")

    elif file_extension == '.txt':
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
        except FileNotFoundError:
            print("Tidak ada catatan yang ditemukan.")
            return

        found = False
        for i, line in enumerate(lines):
            if line.startswith(judul + ':'):
                lines[i] = f"{judul}: {isi_baru}\n"
                found = True
                break

        if not found:
            print("Catatan dengan judul ini tidak ditemukan.")
            return

        with open(filename, 'w') as file:
            file.writelines(lines)
        print("Catatan berhasil diedit.")

    else:
        print("Format file tidak didukung. Gunakan .csv, .json, atau .txt.")