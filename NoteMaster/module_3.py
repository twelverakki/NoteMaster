import pandas as pd

def edit_catatan(judul, isi_baru, filename='catatan.csv'):
    try:
        df = pd.read_csv(filename)
    except FileNotFoundError:
        print("Tidak ada catatan yang ditemukan.")
        return

    if judul not in df['Judul'].values:
        print("Catatan dengan judul ini tidak ditemukan.")
        return

    df.loc[df['Judul'] == judul, 'Isi'] = isi_baru
    df.to_csv(filename, index=False)
    print("Catatan berhasil diedit.")

# if __name__ == "__main__":
#     judul_catatan = 'judul catatan'
#     isi_baru = 'isi baru'
    
#     edit_catatan(judul_catatan, isi_baru)