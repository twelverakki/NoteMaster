def tambahCatatan(self, note):
        """Fungsi untuk menambah catatan baru ke dalam daftar"""
        self.NotesMaster.append(note)
        print(f"Catatan berhasil ditambahkan: {note}")

def view_notes(self):
        """Fungsi untuk melihat semua catatan yang ada"""
        if not self.NotesMaster:
            print("Tidak ada catatan yang tersedia.")
        else:
            for i, note in enumerate(self.NoterMaster, 1):
                print(f"{i}. {note}")

def tambahCatatanExisting(self, index, note):
    """Fungsi untuk menambahkan catatan baru ke catatan yang sudah ada (di akhir)"""
    if index < 0 or index >= len(self.NotesMaster):
        print("Index catatan tidak valid.")
    else:
        self.NotesMaster[index] += "\n" + note
        print(f"Catatan berhasil ditambahkan ke catatan nomor {index+1}: {note}")