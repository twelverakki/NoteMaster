from pathlib import Path
import json
import csv
import os

def hapus_item_catatan(file_path, identifier):
    """
    Menghapus item dari file JSON, CSV, atau TXT berdasarkan judul.

    Args:
        file_path (str): Path lengkap dari file.
        identifier (str): Judul dari catatan yang ingin dihapus di dalam file.

    Raises:
        FileNotFoundError: Jika file tidak ditemukan pada path yang diberikan.
        Exception: Kesalahan umum lainnya saat mencoba menghapus item dalam file.
    """
    file_extension = os.path.splitext(file_path)[1]

    if file_extension == '.json':
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        updated_data = [note for note in data if note.get('Judul') != identifier]

        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(updated_data, file, indent=4)
        print(f"Item dengan judul '{identifier}' berhasil dihapus dari {file_path}.")


    elif file_extension == '.csv':
        updated_data = []
        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            updated_data = [row for row in reader if row['Judul'] != identifier]

        with open(file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['Judul', 'Isi'])
            writer.writeheader()
            writer.writerows(updated_data)
        print(f"Item dengan judul '{identifier}' berhasil dihapus dari {file_path}.")

    elif file_extension == '.txt':
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        updated_lines = [line for line in lines if not line.startswith(identifier + ':')]

        with open(file_path, 'w', encoding='utf-8') as file:
            file.writelines(updated_lines)

        print(f"Item dengan judul '{identifier}' berhasil dihapus dari {file_path}.")
    else:
        print(f"Format file '{file_extension}' tidak didukung untuk penghapusan item.")

def hapus_catatan(file_path):
    """
    Menghapus file JSON, CSV, atau TXT secara keseluruhan.

    Args:
        file_path (str): Path lengkap dari file yang akan dihapus.

    Raises:
        FileNotFoundError: Jika file tidak ditemukan.
        PermissionError: Jika tidak ada izin untuk menghapus file.
    """
    try:
        os.remove(file_path)
        print(f"File {file_path} berhasil dihapus.")
    except FileNotFoundError:
        print(f"File {file_path} tidak ditemukan.")
    except Exception as e:
        print(f"Gagal menghapus file {file_path}: {e}")

def hapus_all(directory_path):
    """
    Menghapus semua file dengan ekstensi .json, .csv, dan .txt dalam direktori yang diberikan.
    """
    path = Path(directory_path)

    try:
        file_extensions = ['*.json', '*.csv', '*.txt']
        for ext in file_extensions:
            for file in path.glob(ext):
                print(f"File {file} berhasil dihapus.") if file.unlink() else ''

    except FileNotFoundError:
        print(f"Direktori {directory_path} tidak ditemukan.")
    except Exception as e:
        print(f"Gagal menghapus file dalam direktori {directory_path}: {e}")
