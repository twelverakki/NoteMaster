import os
import json
import csv

def edit_catatan(judul, isi_baru, file_name, directory=None):
    """
    Mengedit catatan dalam file CSV, JSON, atau TXT di dalam atau luar direktori yang ditentukan.

    Args:
        judul (str): Judul catatan (atau ID untuk JSON) yang ingin diedit.
        isi_baru (str): Isi baru yang akan menggantikan isi catatan.
        file_name (str): Nama file yang berisi catatan.
        directory (str or None): Nama direktori tempat file berada, atau None jika file ada di root.

    Returns:
        None: Fungsi ini tidak mengembalikan nilai, tetapi mencetak pesan status ke konsol.
    """
    # Buat path lengkap jika directory disertakan
    if directory:
        file_path = os.path.join(directory, file_name)
    else:
        file_path = file_name

    # Periksa apakah file ada
    if not os.path.isfile(file_path):
        print(f"File '{file_path}' tidak ditemukan.")
        return

    # Deteksi ekstensi file
    file_extension = os.path.splitext(file_path)[1].lower()

    try:
        if file_extension == '.csv':
            # Buka dan edit file CSV
            with open(file_path, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                data = list(reader)

                # Cek apakah kolom yang dibutuhkan ada di CSV
                if 'Judul' not in reader.fieldnames or 'Isi' not in reader.fieldnames:
                    raise ValueError("File CSV tidak memiliki kolom yang sesuai (Judul, Isi).")

            # Edit catatan yang sesuai
            found = False
            for row in data:
                if row['Judul'] == judul:
                    row['Isi'] = isi_baru
                    found = True
                    break

            if not found:
                print(f"Catatan dengan judul '{judul}' tidak ditemukan.")
                return

            # Tulis ulang file CSV dengan perubahan
            with open(file_path, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=['Judul', 'Isi'])
                writer.writeheader()
                writer.writerows(data)

        elif file_extension == '.json':
            # Buka dan edit file JSON (berdasarkan ID)
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)

            # Cari catatan berdasarkan ID (bukan judul)
            found = False
            for item in data:
                if item['id'] == judul:  # Di JSON, 'judul' adalah ID
                    item['isi'] = isi_baru
                    found = True
                    break

            if not found:
                print(f"Catatan dengan ID '{judul}' tidak ditemukan.")
                return

            # Tulis ulang file JSON dengan perubahan
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4)

        elif file_extension == '.txt':
            # Buka dan edit file TXT
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()

            # Edit catatan yang sesuai
            found = False
            for i, line in enumerate(lines):
                if line.startswith(judul + ':'):
                    lines[i] = f"{judul}: {isi_baru}\n"
                    found = True
                    break

            if not found:
                print(f"Catatan dengan judul '{judul}' tidak ditemukan.")
                return

            # Tulis ulang file TXT
            with open(file_path, 'w', encoding='utf-8') as file:
                file.writelines(lines)

        else:
            print(f"Format file '{file_extension}' tidak didukung.")
            return

        print(f"Catatan dengan judul '{judul}' berhasil diedit.")

    except FileNotFoundError:
        print(f"File '{file_path}' tidak ditemukan.")
    except PermissionError:
        print(f"Tidak ada izin untuk mengakses file '{file_path}'.")
    except ValueError as e:
        print(f"Kesalahan format file: {e}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")