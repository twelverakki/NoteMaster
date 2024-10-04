from pathlib import Path
import json
import csv
import os

def delete_note(file_path, note_id):
	"""
    Menghapus file teks (.txt) yang disimpan di sistem file.

    Args:
        file_path (str): Path lengkap dari file .txt yang akan dihapus.

    Raises:
        FileNotFoundError: Jika file tidak ditemukan pada path yang diberikan.
        PermissionError: Jika tidak ada izin yang cukup untuk menghapus file.
        Exception: Kesalahan umum lainnya saat mencoba menghapus file.

    Example:
        >>> delete_txt_file('notes/catatan.txt')
        File notes/catatan.txt berhasil dihapus.

    Jika file ditemukan, fungsi ini akan menghapus file dan mencetak pesan berhasil.
    Jika file tidak ditemukan atau terjadi kesalahan lain, pesan kesalahan akan dicetak.
    """
	# Deteksi ekstensi file
	file_extension = os.path.splitext(file_path)[1]

	# Proses berdasarkan ekstensi file
	if file_extension == '.json':
		# Proses file JSON
		with open(file_path, 'r') as file:
			data = json.load(file)

		# Hapus catatan dengan note_id yang sesuai
		data = [note for note in data if note.get('id') != note_id]

		# Simpan perubahan
		with open(file_path, 'w') as file:
			json.dump(data, file, indent=4)

	elif file_extension == '.csv':
		# Proses file CSV
		updated_data = []
		with open(file_path, 'r') as file:
			reader = csv.DictReader(file)
			updated_data = [row for row in reader if row['id'] != str(note_id)]

		# Simpan perubahan
		with open(file_path, 'w', newline='') as file:
			writer = csv.DictWriter(file, fieldnames=updated_data[0].keys())
			writer.writeheader()
			writer.writerows(updated_data)

	elif file_extension == '.txt':
		try:
			os.remove(file_path)  # Menghapus file dari sistem
			print(f"File {file_path} berhasil dihapus.")
		except FileNotFoundError:
			print(f"File {file_path} tidak ditemukan.")
		except PermissionError:
			print(f"Tidak memiliki izin untuk menghapus file {file_path}.")
		except Exception as e:
			print(f"Gagal menghapus file {file_path}: {e}")

	else:
		print("Format file tidak didukung")

# Contoh penggunaan
# delete_note('catatan.json', 1)
# delete_note('catatan.csv', 2)
# delete_note('catatan.txt', 3)

def delete_all_notes(directory_path):
    """
    Menghapus semua file dengan ekstensi .json, .csv, dan .txt dalam direktori yang diberikan.

    Args:
        directory_path (str): Path lengkap dari direktori tempat file disimpan.

    Raises:
        FileNotFoundError: Jika direktori tidak ditemukan atau tidak valid.
        PermissionError: Jika tidak ada izin yang cukup untuk menghapus file.
        Exception: Kesalahan umum lainnya saat mencoba menghapus file.

    Example:
        >>> delete_all_notes('data/')
        File data/catatan1.json berhasil dihapus.
        File data/catatan2.csv berhasil dihapus.
        File data/catatan3.txt berhasil dihapus.

    Fungsi ini mencari semua file dengan ekstensi .json, .csv, dan .txt dalam direktori yang diberikan,
    kemudian menghapus file-file tersebut satu per satu. Jika ada kesalahan dalam penghapusan
    file atau direktori tidak ditemukan, pesan kesalahan akan dicetak.
    """
    path = Path(directory_path)

    try:
        # Dapatkan semua file dengan ekstensi yang ditentukan
        file_extensions = ['*.json', '*.csv', '*.txt']
        for ext in file_extensions:
            for file in path.glob(ext):
                file.unlink()  # Menghapus file
                print(f"File {file} berhasil dihapus.")

    except FileNotFoundError:
        print(f"Direktori {directory_path} tidak ditemukan.")
    except PermissionError:
        print(f"Tidak memiliki izin untuk menghapus file dalam direktori {directory_path}.")
    except Exception as e:
        print(f"Gagal menghapus file dalam direktori {directory_path}: {e}")

# Contoh penggunaan
# delete_all_notes('data/')