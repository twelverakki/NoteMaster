def buat_catatan(judul, isi, tipe_data):
    """
    Membuat catatan dengan format yang sesuai berdasarkan tipe data yang dipilih.

    Parameters:
    - judul (str): Judul catatan
    - isi (str): Isi catatan
    - tipe_data (str): Tipe data untuk menyimpan catatan ('csv', 'json', 'txt')

    Returns:
    - dict: Template catatan yang siap untuk disimpan
    """
    catatan = {
        "judul": judul,
        "isi": isi
    }

    if tipe_data == 'json' or tipe_data == 'csv' or tipe_data == 'txt':
        return catatan
    else:
        raise ValueError("Tipe data tidak valid. Pilih antara 'csv', 'json', atau 'txt'.")