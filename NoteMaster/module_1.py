import json

def buat_catatan(judul, isi, tipe_data):
    """
    Membuat catatan dengan format yang sesuai berdasarkan tipe data yang dipilih.

    Parameters:
    - judul (str): Judul catatan
    - isi (str): Isi catatan
    - tipe_data (str): Tipe data untuk menyimpan catatan ('csv', 'json', 'txt')

    Returns:
    - dict/str: Template catatan yang siap untuk disimpan
    """
    catatan = {
        "judul": judul,
        "isi": isi
    }

    if tipe_data == 'json':
        return json.dumps(catatan, indent=4)
    elif tipe_data == 'csv':
        output = f"judul,isi\n{judul},{isi}\n"
        return output
    elif tipe_data == 'txt':
        return f"judul:isi\n{judul}:{isi}"
    else:
        raise ValueError("Tipe data tidak valid. Pilih antara 'csv', 'json', atau 'txt'.")