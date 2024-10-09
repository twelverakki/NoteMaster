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
    for file_name in os.listdir(direktori):
        file_path = os.path.join(direktori, file_name)
        if os.path.isfile(file_path) and os.path.splitext(file_name)[1] in ekstensi_diizinkan:
            print(f"- {file_name}")
            file_tersedia = True

    if not file_tersedia:
        print("Tidak ada file catatan yang tersedia dengan ekstensi yang didukung.")
        return

    # Meminta pengguna memasukkan nama file
    file_name = input("Masukkan nama file catatan (tanpa ekstensi): ").strip()

    # Periksa file di setiap ekstensi yang diizinkan
    for ekstensi in ekstensi_diizinkan:
        file_path = os.path.join(direktori, file_name + ekstensi)
        if os.path.exists(file_path):
            print(f"\nMenampilkan isi dari {file_name + ekstensi}:\n")

            # Membaca dan menampilkan isi file sesuai formatnya
            try:
                if ekstensi == ".txt":
                    with open(file_path, 'r', encoding='utf-8') as file:
                        print(file.read())
                elif ekstensi == ".json":
                    with open(file_path, 'r', encoding='utf-8') as file:
                        data = json.load(file)
                        print(json.dumps(data, indent=4))  # Tampilkan JSON dengan rapi
                elif ekstensi == ".csv":
                    with open(file_path, 'r', encoding='utf-8') as file:
                        reader = csv.reader(file)
                        for row in reader:
                            print(", ".join(row))  # Tampilkan CSV sebagai tabel
                return
            except Exception as e:
                print(f"Terjadi kesalahan saat membaca {file_name + ekstensi}: {e}")
                return

    # Jika file tidak ditemukan
    print(f"Tidak ada catatan ditemukan untuk '{file_name}' dengan ekstensi yang diizinkan.")