import os

def tampilkan_catatan(package_name, directory="."):
    """
    Menampilkan isi catatan dari file yang ada dalam package.

    Parameters:
    - package_name: Nama direktori yang berisi catatan.
    - directory: Direktori tempat package berada (default: ".").
    """
    package_dir = os.path.join(directory, package_name)

    if not os.path.exists(package_dir):
        print(f"Package '{package_name}' tidak ditemukan di direktori {directory}")
        return

    ekstensi_diizinkan = [".csv", ".txt", ".json"]

    # Menampilkan daftar file yang ada
    print("File catatan yang tersedia:")
    for ekstensi in ekstensi_diizinkan:
        file_path = os.path.join(package_dir, f"catatan{ekstensi}")
        if os.path.exists(file_path):
            print(f"- catatan{ekstensi}")

    # Meminta pengguna untuk memasukkan nama file
    file_name = input("Masukkan nama file catatan (tanpa ekstensi): ")
    for ekstensi in ekstensi_diizinkan:
        file_path = os.path.join(package_dir, file_name + ekstensi)
        if os.path.exists(file_path):
            print(f"\nMenampilkan isi dari {file_name + ekstensi}:\n")
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    print(file.read())
                    return
            except Exception as e:
                print(f"Terjadi kesalahan saat membaca {file_name + ekstensi}: {e}")

    print(f"Tidak ada catatan ditemukan untuk '{file_name}' dengan ekstensi yang diizinkan.")