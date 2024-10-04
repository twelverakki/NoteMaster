def cari_catatan(catatan_list, kata_kunci):
    """
    Fungsi untuk mencari catatan yang sesuai dengan kata kunci.

    Args:
        catatan_list (list): Daftar catatan, di mana setiap catatan adalah dictionary
        yang memiliki setidaknya kunci 'judul' dan 'isi'.
        kata_kunci (str): Kata kunci yang akan dicari di dalam judul dan isi catatan.

    Returns:
        list: Daftar catatan yang mengandung kata kunci di judul atau isi.
    """
    hasil_pencarian = []
    kata_kunci = kata_kunci.lower().strip()  # Menghapus spasi di awal dan akhir kata kunci

    for catatan in catatan_list:
        judul = catatan.get('judul', '').lower()
        isi = catatan.get('isi', '').lower()

        # Periksa apakah kata kunci ada di dalam judul atau isi
        if kata_kunci in judul or kata_kunci in isi:
            hasil_pencarian.append(catatan)

    return hasil_pencarian


def pencarian_catatan(catatan_list, kata_kunci):
    """
    Fungsi untuk melakukan pencarian catatan berdasarkan kata kunci dan menampilkan hasilnya.

    Args:
        catatan_list (list): Daftar catatan yang akan dicari, masing-masing catatan adalah dictionary
        dengan setidaknya kunci 'judul' dan 'isi'.
        kata_kunci (str): Kata kunci yang akan dicari dalam judul dan isi catatan.

    Returns:
        None: Hasil pencarian akan ditampilkan langsung di terminal/console.
    """
    kata_kunci = kata_kunci.strip()  # Menghapus spasi di awal dan akhir

    if kata_kunci:  # Pastikan kata kunci tidak kosong setelah di-strip
        hasil = cari_catatan(catatan_list, kata_kunci)

        if hasil:
            print(f"\nHasil pencarian untuk kata kunci '{kata_kunci}':")
            for catatan in hasil:
                print(f"- {catatan['judul']}: {catatan['isi']}")
                print("-" * 40)  # Garis pemisah antar catatan
        else:
            print(f"\nTidak ada catatan yang ditemukan dengan kata kunci '{kata_kunci}'.")
    else:
        print("Kata kunci tidak boleh kosong atau hanya berisi spasi.")
