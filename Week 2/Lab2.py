# Header
print("============================================================")
print("SISTEM PENCATATAN ANGGOTA KDMP FLORIAN")
print("============================================================")


def tentukan_paket(skor_usaha):
    # TODO: Menentukan paket berdasarkan skor usaha
    if skor_usaha <= 49:
        return "Paket Tunas"
    elif skor_usaha <= 79:
        return "Paket Mekar"
    else:
        return "Paket Mandiri"


# TODO: Meminta banyak anggota yang akan didaftarkan
daftar_anggota = []
banyak_anggota = int(input("Masukkan banyak anggota: "))

# TODO: Meminta data untuk setiap anggota
for nomor in range(1, banyak_anggota + 1):
    print(f"\n=== Data anggota {nomor} ===")
    # TODO: Mengambil input
    nama = input("Nama Anggota: ")
    kode_wilayah = input("Cabang KDMP (G/L/P): ")
    skor_usaha = int(input("Skor Usaha: "))
    komoditas = input("Komoditas Unggulan: ")

    # TODO: Mengubah kode wilayah menjadi nama wilayah
    if kode_wilayah.upper() == "G":
        wilayah = "Pegunungan"
    elif kode_wilayah.upper() == "L":
        wilayah = "Lembah"
    else:
        wilayah = "Pesisir"

    paket = tentukan_paket(skor_usaha)

    # Data anggota disimpan sebagai tuple dengan urutan:
    # Nama, Wilayah, Skor Usaha, Komoditas, Paket
    data_anggota = (nama, wilayah, skor_usaha, komoditas, paket)
    daftar_anggota.append(data_anggota)


# TODO: Menampilkan data anggota dalam bentuk tabel
jumlah_tunas = 0
jumlah_mekar = 0
jumlah_mandiri = 0

print("\n====================== DATA ANGGOTA KDMP ======================")
print(f"{'No':<3} {'Nama':<12} {'Wilayah':<11} {'Skor':>4} {'Komoditas':<12} {'Paket':<14}")

for i in range(len(daftar_anggota)):
    anggota = daftar_anggota[i]
    nama, wilayah, skor_usaha, komoditas, paket = anggota

    print(f"{i+1:<3} {nama:<12} {wilayah:<11} {skor_usaha:>4} {komoditas:<12} {paket:<14}")

    # TODO: Menghitung jumlah anggota pada setiap paket
    if paket == "Paket Tunas":
        jumlah_tunas += 1
    elif paket == "Paket Mekar":
        jumlah_mekar += 1
    else:
        jumlah_mandiri += 1


print("====================== RINGKASAN KDMP ======================")
print(f"Jumlah penerima Paket Tunas: {jumlah_tunas}")
print(f"Jumlah penerima Paket Mekar: {jumlah_mekar}")
print(f"Jumlah penerima Paket Mandiri: {jumlah_mandiri}")

# BONUS: uncomment dan lengkapi jika mengerjakan bonus
# def tampilkan_anggota_per_paket(daftar_anggota):
#     ...
#
# tampilkan_anggota_per_paket(daftar_anggota)

print("============================================================")
print("TERIMA KASIH SUDAH MEMBANTU KDMP FLORIAN!")
print("============================================================")