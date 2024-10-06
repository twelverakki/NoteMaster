Catatan = []  

def tambah_catatan(note):  
    """Fungsi untuk menambah catatan baru ke dalam daftar"""  
    Catatan.append(note)  
    print(f"Catatan berhasil ditambahkan: {note}")  

def view_notes():  
    """Fungsi untuk melihat semua catatan yang ada"""  
    if not Catatan:  
        print("Tidak ada catatan yang tersedia.")  
    else:  
        for i, note in enumerate(Catatan, 1):  
            print(f"{i}. {note}")  

def tambah_catatan_existing(index, note):  
    """Fungsi untuk menambahkan catatan baru ke catatan yang sudah ada (di akhir)"""  
    if index < 0 or index >= len(Catatan):  
        print("Index catatan tidak valid.")  
    else:  
        Catatan[index] += "\n" + note  
        print(f"Catatan berhasil ditambahkan ke catatan nomor {index + 1}: {note}")  


