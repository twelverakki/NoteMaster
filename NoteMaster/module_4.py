import os
import json
import csv

def tampilkan_catatan(direktori="catatan"):
    """
    Menampilkan isi file catatan dalam format .txt, .csv, atau .json dari sebuah direktori.

    Parameter:
    - direktori: Nama direktori yang berisi catatan (default: "catatan").
    """
    if not os.path.exists(direktori):
        print(f"Direktori '{direktori}' tidak ditemukan.")
        return

    ekstensi_diizinkan = [".csv", ".txt", ".json"]

    print("File catatan yang tersedia:")
    file_tersedia = False
    semua_file = []

    for file_name in os.listdir(direktori):
        file_path = os.path.join(direktori, file_name)
        if os.path.isfile(file_path) and os.path.splitext(file_name)[1] in ekstensi_diizinkan:
            semua_file.append(file_name)
            print(f"- {file_name}")
            file_tersedia = True

    if not file_tersedia:
        print("Tidak ada file catatan yang tersedia dengan ekstensi yang didukung.")
        return

    file_name_input = input("Masukkan nama file catatan (tanpa ekstensi): ").strip()

    matching_files = [f for f in semua_file if f.startswith(file_name_input)]

    if len(matching_files) > 1:
        print(f"Ada beberapa file dengan nama '{file_name_input}' dengan ekstensi yang berbeda:")
        for i, file_name in enumerate(matching_files):
            print(f"{i + 1}. {file_name}")

        pilihan = input("Pilih file yang ingin ditampilkan (masukkan nomor atau ketik 'semua' untuk menampilkan semua): ").strip()

        if pilihan.lower() == 'semua':
            for file_name in matching_files:
                tampilkan_isi_file(direktori, file_name)
        else:
            try:
                index = int(pilihan) - 1
                if 0 <= index < len(matching_files):
                    tampilkan_isi_file(direktori, matching_files[index])
                else:
                    print("Pilihan tidak valid.")
            except ValueError:
                print("Masukkan nomor yang valid.")
    elif matching_files:
        tampilkan_isi_file(direktori, matching_files[0])
    else:
        print(f"Tidak ada file yang cocok dengan nama '{file_name_input}'.")


def tampilkan_isi_file(direktori, file_name):
    """
    Fungsi untuk menampilkan isi dari file sesuai dengan formatnya.
    """
    ekstensi = os.path.splitext(file_name)[1]
    file_path = os.path.join(direktori, file_name)

    try:
        if ekstensi == ".txt":
            with open(file_path, 'r', encoding='utf-8') as file:
                print(f"\nIsi dari {file_name}:\n")
                print(file.read())
        elif ekstensi == ".json":
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                print(f"\nIsi dari {file_name} (format JSON):\n")
                print(json.dumps(data, indent=4))
        elif ekstensi == ".csv":
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                print(f"\nIsi dari {file_name} (format CSV):\n")
                for row in reader:
                    print(", ".join(row))
    except Exception as e:
        print(f"Terjadi kesalahan saat membaca {file_name}: {e}")