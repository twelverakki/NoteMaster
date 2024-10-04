def cari_catatan(catatan_list, kata_kunci):

    hasil_pencarian = []

    kata_kunci = kata_kunci.lower()

    for catatan in catatan_list:
        judul = catatan.get('judul', '').lower()
        isi = catatan.get('isi', '').lower()

        # Periksa
        if kata_kunci in judul or kata_kunci in isi:
            hasil_pencarian.append(catatan)

    return hasil_pencarian


def pencarian_catatan(catatan_list, kata_kunci):

    # Cek spasi
    if kata_kunci and not kata_kunci.isspace():  # Pastikan tidak kosong
        # Mencari yang sesuai
        hasil = cari_catatan(catatan_list, kata_kunci)

        if hasil:
            print(f"\nHasil pencarian untuk kata kunci '{kata_kunci}':")
            for catatan in hasil:
                print(f"- {catatan['judul']}: {catatan['isi']}")
        else:
            print(f"\nTidak ada catatan yang ditemukan dengan kata kunci '{kata_kunci}'.")
    else:
        print("Kata kunci tidak boleh kosong atau hanya berisi spasi.")
