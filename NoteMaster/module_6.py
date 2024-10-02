import json
import csv
import shutil

def simpan_catatan_json(catatan_list, file_path: str) -> None:
    """
    Menyimpan catatan ke file dalam format JSON.
    Args:
        catatan_list (list): Daftar catatan yang akan disimpan.
        file_path (str): Jalur file tempat catatan akan disimpan.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(catatan_list, file, ensure_ascii=False, indent=4)
        print(f"Catatan berhasil disimpan ke {file_path}.")
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan catatan: {e}")

def simpan_catatan_txt(catatan_list, file_path: str) -> None:
    """
    Menyimpan catatan ke file dalam format TXT.
    Args:
        catatan_list (list): Daftar catatan yang akan disimpan.
        file_path (str): Jalur file tempat catatan akan disimpan.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            for catatan in catatan_list:
                file.write(f"{catatan['judul']}\n{catatan['isi']}\n\n")
        print(f"Catatan berhasil disimpan ke {file_path}.")
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan catatan: {e}")

def simpan_catatan_csv(catatan_list, file_path: str) -> None:
    """
    Menyimpan catatan ke file dalam format CSV.
    Args:
        catatan_list (list): Daftar catatan yang akan disimpan.
        file_path (str): Jalur file tempat catatan akan disimpan.
    """
    try:
        with open(file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["judul", "isi"])
            writer.writeheader()
            writer.writerows(catatan_list)
        print(f"Catatan berhasil disimpan ke {file_path}.")
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan catatan: {e}")

def backup_catatan(file_path: str, backup_path: str) -> None:
    """
    Membuat salinan cadangan dari file catatan.
    Args:
        file_path (str): Jalur file catatan yang akan dicadangkan.
        backup_path (str): Jalur tempat cadangan akan disimpan.
    """
    try:
        shutil.copy(file_path, backup_path)
        print(f"Backup berhasil dibuat di {backup_path}.")
    except FileNotFoundError:
        print(f"File {file_path} tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan saat membuat backup: {e}")




# tambah id bde
# Contoh penggunaan
import os
if __name__ == "__main__":
    # Minta pengguna untuk memasukkan jalur folder
    folder_path = input("Masukkan jalur folder untuk menyimpan catatan (misal: catatan_folder): ")

    # Buat folder jika belum ada
    os.makedirs(folder_path, exist_ok=True)

    # Catatan yang akan disimpan
    catatan_list = [
        {"judul": "Catatan Pertama", "isi": "Ini adalah isi catatan pertama."},
        {"judul": "Catatan Kedua", "isi": "Ini adalah isi catatan kedua."}
    ]

    # Simpan catatan dalam format JSON, TXT, dan CSV
    json_file_path = os.path.join(folder_path, "catatan.json")
    txt_file_path = os.path.join(folder_path, "catatan.txt")
    csv_file_path = os.path.join(folder_path, "catatan.csv")

    simpan_catatan_json(catatan_list, json_file_path)
    simpan_catatan_txt(catatan_list, txt_file_path)
    simpan_catatan_csv(catatan_list, csv_file_path)

    # Buat backup untuk setiap file yang disimpan
    backup_catatan(json_file_path, os.path.join(folder_path, "catatan_backup.json"))
    backup_catatan(txt_file_path, os.path.join(folder_path, "catatan_backup.txt"))
    backup_catatan(csv_file_path, os.path.join(folder_path, "catatan_backup.csv"))