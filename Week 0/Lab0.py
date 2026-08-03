# TODO: import library yang diperlukan

import math

print("=" * 60)
print("SELAMAT DATANG DI SISTEM PENCATATAN PENDUDUK FLORIAN!")
print("=" * 60)

print("\n==== Data Penduduk ====")

# TODO: lengkapi input-input di bawah ini
nama = input("Masukkan nama penduduk: ")
tempat_lahir = input("Masukkan tempat lahir: ")
tanggal_lahir = input("Masukkan tanggal lahir (DD/MM/YYYY): ")
spesies = input("Masukkan spesies: ")
tinggi = float(input("Masukkan tinggi (dalam m): "))
berat = float(input("Masukkan berat (dalam kg): "))

# TODO: hitung tinggi dan luas rumah
# refer kembali ke rumus yang disediakan pada soal
tinggi_rumah = (tinggi + 0.85)
luas_rumah = (math.pi * math.pow(2, 0.5)) * tinggi * tinggi + berat/3

# TODO: tampilkan luaran sesuai dengan test case yang ada pada dokumen soal
# ingat bahwa bilangan dibulatkan dua angka di belakang koma
print("\n==== Ringkasan Data Penduduk ====")
print(f"Penduduk berspesies {spesies} dengan nama {nama} yang lahir tanggal {tanggal_lahir} di {tempat_lahir} berhasil terdaftar menjadi penduduk negeri Florian!")
print(f"\n{nama} berhak atas rumah dengan tinggi {tinggi_rumah} meter dan luas {round(luas_rumah, 2)} meter persegi")

print(f"\n{'=' * 60}")
print("TERIMA KASIH SUDAH MELAKUKAN PENCATATAN DATA PENDUDUK!")
print("=" * 60)