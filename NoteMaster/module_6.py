import json  
import csv  
import shutil  
from typing import List, Dict  

FIELDNAMES = ["judul", "isi"]  

def simpan_catatan_json(catatan_list: List[Dict[str, str]], file_path: str) -> None:  
    """  
    Menyimpan daftar catatan ke dalam file dengan format JSON.  

    Args:  
        catatan_list (List[Dict[str, str]]): Daftar catatan yang akan disimpan. Setiap catatan adalah dictionary dengan kunci 'judul' dan 'isi'.  
        file_path (str): Jalur file tempat catatan akan disimpan.  

    Returns:  
        None  

    Raises:  
        FileNotFoundError: Jika jalur file tidak ditemukan.  
        IOError: Jika terjadi kesalahan I/O saat menyimpan catatan.  

    Example:  
        catatan = [{"judul": "Catatan 1", "isi": "Ini adalah isi catatan 1."}]  
        simpan_catatan_json(catatan, "catatan.json")  
    """  
    if not catatan_list:  
        print("Daftar catatan tidak boleh kosong.")  
        return  
    try:  
        with open(file_path, 'w', encoding='utf-8') as file:  
            json.dump(catatan_list, file, ensure_ascii=False, indent=4)  
        print(f"Catatan berhasil disimpan ke {file_path}.")  
    except FileNotFoundError:  
        print(f"File tidak ditemukan: {file_path}")  
    except IOError as e:  
        print(f"Kesalahan I/O saat menyimpan catatan: {e}")  

def simpan_catatan_txt(catatan_list: List[Dict[str, str]], file_path: str) -> None:  
    """  
    Menyimpan daftar catatan ke dalam file dengan format TXT.  

    Args:  
        catatan_list (List[Dict[str, str]]): Daftar catatan yang akan disimpan. Setiap catatan adalah dictionary dengan kunci 'judul' dan 'isi'.  
        file_path (str): Jalur file tempat catatan akan disimpan.  

    Returns:  
        None  

    Raises:  
        FileNotFoundError: Jika jalur file tidak ditemukan.  
        IOError: Jika terjadi kesalahan I/O saat menyimpan catatan.  

    Example:  
        catatan = [{"judul": "Catatan 1", "isi": "Ini adalah isi catatan 1."}]  
        simpan_catatan_txt(catatan, "catatan.txt")  
    """  
    if not catatan_list:  
        print("Daftar catatan tidak boleh kosong.")  
        return  
    try:  
        with open(file_path, 'w', encoding='utf-8') as file:  
            for catatan in catatan_list:  
                file.write(f"{catatan['judul']}\n{catatan['isi']}\n\n")  
        print(f"Catatan berhasil disimpan ke {file_path}.")  
    except FileNotFoundError:  
        print(f"File tidak ditemukan: {file_path}")  
    except IOError as e:  
        print(f"Kesalahan I/O saat menyimpan catatan: {e}")  

def simpan_catatan_csv(catatan_list: List[Dict[str, str]], file_path: str) -> None:  
    """  
    Menyimpan daftar catatan ke dalam file dengan format CSV.  

    Args:  
        catatan_list (List[Dict[str, str]]): Daftar catatan yang akan disimpan. Setiap catatan adalah dictionary dengan kunci 'judul' dan 'isi'.  
        file_path (str): Jalur file tempat catatan akan disimpan.  

    Returns:  
        None  

    Raises:  
        FileNotFoundError: Jika jalur file tidak ditemukan.  
        IOError: Jika terjadi kesalahan I/O saat menyimpan catatan.  

    Example:  
        catatan = [{"judul": "Catatan 1", "isi": "Ini adalah isi catatan 1."}]  
        simpan_catatan_csv(catatan, "catatan.csv")  
    """  
    if not catatan_list:  
        print("Daftar catatan tidak boleh kosong.")  
        return  
    try:  
        with open(file_path, 'w', newline='', encoding='utf-8') as file:  
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)  
            writer.writeheader()  
            writer.writerows(catatan_list)  
        print(f"Catatan berhasil disimpan ke {file_path}.")  
    except FileNotFoundError:  
        print(f"File tidak ditemukan: {file_path}")  
    except IOError as e:  
        print(f"Kesalahan I/O saat menyimpan catatan: {e}")  

def backup_catatan(file_path: str, backup_path: str) -> None:  
    """  
    Membuat salinan cadangan dari file catatan.  

    Args:  
        file_path (str): Jalur file catatan yang akan dicadangkan.  
        backup_path (str): Jalur tempat cadangan akan disimpan.  

    Returns:  
        None  

    Raises:  
        FileNotFoundError: Jika file catatan tidak ditemukan.  
        Exception: Jika terjadi kesalahan saat membuat backup.  

    Example:  
        backup_catatan("catatan.json", "backup/catatan_backup.json")  
    """  
    try:  
        shutil.copy(file_path, backup_path)  
        print(f"Backup berhasil dibuat di {backup_path}.")  
    except FileNotFoundError:  
        print(f"File {file_path} tidak ditemukan.")  
    except Exception as e:  
        print(f"Terjadi kesalahan saat membuat backup: {e}")