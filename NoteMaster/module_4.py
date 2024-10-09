import os
import json
import csv

def tampilkan_catatan(direktori="catatan"):
    """
    Menampilkan isi file catatan dalam format .txt, .csv, atau .json dari sebuah direktori.

    Parameter:
    - direktori: Nama direktori yang berisi catatan (default: "catatan").
    """
    # Pastikan direktori ada
    if not os.path.exists(direktori):
        print(f"Direktori '{direktori}' tidak ditemukan.")
        return

    ekstensi_diizinkan = [".csv", ".txt", ".json"]

    # Tampilkan file yang tersedia di direktori
    print("File catatan yang tersedia:")
    file_tersedia = False
    semua_file = []

    # Cek setiap file dalam direktori dan simpan yang memiliki ekstensi sesuai
    for file_name in os.listdir(direktori):
        file_path = os.path.join(direktori, file_name)
        if os.path.isfile(file_path) and os.path.splitext(file_name)[1] in ekstensi_diizinkan:
            semua_file.append(file_name)
            print(f"- {file_name}")
            file_tersedia = True

    if not file_tersedia:
        print("Tidak ada file catatan yang tersedia dengan ekstensi yang didukung.")
        return

    # Meminta pengguna memasukkan nama file
    file_name_input = input("Masukkan nama file catatan (tanpa ekstensi): ").strip()

    # Filter file berdasarkan nama yang dimasukkan oleh pengguna (tanpa ekstensi)
    matching_files = [f for f in semua_file if f.startswith(file_name_input)]

    # Jika ada lebih dari satu file dengan nama yang sama namun ekstensi berbeda
    if len(matching_files) > 1:
        print(f"Ada beberapa file dengan nama '{file_name_input}' dengan ekstensi yang berbeda:")
        for i, file_name in enumerate(matching_files):
            print(f"{i + 1}. {file_name}")

        pilihan = input("Pilih file yang ingin ditampilkan (masukkan nomor atau ketik 'semua' untuk menampilkan semua): ").strip()

        if pilihan.lower() == 'semua':
            # Menampilkan semua file yang cocok
            for file_name in matching_files:
                tampilkan_isi_file(direktori, file_name)
        else:
            try:
                # Tampilkan satu file yang dipilih
                index = int(pilihan) - 1
                if 0 <= index < len(matching_files):
                    tampilkan_isi_file(direktori, matching_files[index])
                else:
                    print("Pilihan tidak valid.")
            except ValueError:
                print("Masukkan nomor yang valid.")
    elif matching_files:
        # Jika hanya ada satu file yang cocok, langsung ditampilkan
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
                print(json.dumps(data, indent=4))  # Tampilkan JSON dengan rapi
        elif ekstensi == ".csv":
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                print(f"\nIsi dari {file_name} (format CSV):\n")
                for row in reader:
                    print(", ".join(row))  # Tampilkan CSV sebagai tabel
    except Exception as e:
        print(f"Terjadi kesalahan saat membaca {file_name}: {e}")