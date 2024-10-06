from typing import List, Dict  

# Daftar untuk menyimpan catatan  
catatan_list: List[Dict[str, str]] = []  

def tambah_catatan(judul: str, isi: str) -> None:  
    """Fungsi untuk menambah catatan baru ke dalam daftar."""  
    catatan = {"judul": judul, "isi": isi}  
    catatan_list.append(catatan)  
    print(f"Catatan berhasil ditambahkan: {judul}")  

def lihat_catatan() -> None:  
    """Fungsi untuk melihat semua catatan yang ada."""  
    if not catatan_list:  
        print("Tidak ada catatan yang tersedia.")  
    else:  
        for i, catatan in enumerate(catatan_list, 1):  
            print(f"{i}. Judul: {catatan['judul']}\n   Isi: {catatan['isi']}\n")