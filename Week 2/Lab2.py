# Header
print("============================================================")
print("SISTEM PENCATATAN ANGGOTA KDMP FLORIAN")
print("============================================================")


def tentukan_paket(skor_usaha):
    # TODO: Menentukan paket berdasarkan skor usaha
    if ...:
        return "Paket Tunas"
    elif ...:
        return "Paket Mekar"
    else:
        return "Paket Mandiri"


# TODO: Meminta banyak anggota yang akan didaftarkan
daftar_anggota = []
banyak_anggota = ...

# TODO: Meminta data untuk setiap anggota
for nomor in range(..., ...):
    print(f"\n=== Data anggota {nomor} ===")
    # TODO: Mengambil input
    nama = ...
    kode_wilayah = ...
    skor_usaha = ...
    komoditas = ...

    # TODO: Mengubah kode wilayah menjadi nama wilayah
    if ...:
        wilayah = "Pegunungan"
    elif ...:
        wilayah = "Lembah"
    else:
        wilayah = "Pesisir"

    paket = tentukan_paket(...)

    # Data anggota disimpan sebagai tuple dengan urutan:
    # Nama, Wilayah, Skor Usaha, Komoditas, Paket
    data_anggota = (..., ..., ..., ..., ...)
    daftar_anggota.append(...)


# TODO: Menampilkan data anggota dalam bentuk tabel
jumlah_tunas = 0
jumlah_mekar = 0
jumlah_mandiri = 0

print("\n====================== DATA ANGGOTA KDMP ======================")
print(f"{'No':<3} {'Nama':<12} {'Wilayah':<11} {'Skor':>4} {'Komoditas':<12} {'Paket':<14}")

for i in range(...):
    anggota = daftar_anggota[...]
    nama, wilayah, skor_usaha, komoditas, paket = ...

    print(f"{...:<3} {nama:<12} {...:<11} {skor_usaha:>4} {...:<12} {paket:<14}")

    # TODO: Menghitung jumlah anggota pada setiap paket
    if ...:
        jumlah_tunas += 1
    elif ...:
        jumlah_mekar += 1
    else:
        jumlah_mandiri += 1


print("====================== RINGKASAN KDMP ======================")
print(f"Jumlah penerima Paket Tunas: {...}")
print(f"Jumlah penerima Paket Mekar: {...}")
print(f"Jumlah penerima Paket Mandiri: {...}")

# BONUS: uncomment dan lengkapi jika mengerjakan bonus
# def tampilkan_anggota_per_paket(daftar_anggota):
#     ...
#
# tampilkan_anggota_per_paket(daftar_anggota)

print("============================================================")
print("TERIMA KASIH SUDAH MEMBANTU KDMP FLORIAN!")
print("============================================================")