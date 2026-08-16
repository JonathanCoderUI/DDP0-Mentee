# Header 
print("============================================================")
print("KALKULATOR ANGGARAN PEMBANGUNAN INFRASTRUKTUR NEGERI FLORIAN")
print("============================================================")

# TODO: Meminta input awal
wilayah_asal = input("Masukkan wilayah geografis saat ini: ")
banyak_jalan = int(input("Masukkan banyak jalan yang akan dibangun: "))
sisa_anggaran = int(input("Masukkan rencana anggaran pembangunan jalan: "))
biaya_per_km = int(input("Masukkan biaya pembangunan jalan per kilometer: "))

# TODO: Memulai perulangan untuk setiap rute jalan
for i in range(1, banyak_jalan + 1):
    print(f"\n= Rute jalan {i} =")
    wilayah_tujuan = input("Wilayah geografis tujuan: ")
    panjang_jalan = int(input("Panjang jalan (km): "))
    
    # TODO: Logika percabangan untuk menentukan faktor pengali
    faktor_pengali = 1.0
    if wilayah_asal == wilayah_tujuan:
        faktor_pengali = 1.0
    elif (wilayah_asal == "G" and wilayah_tujuan == "L") or (wilayah_asal == "L" and wilayah_tujuan == "G"):
        faktor_pengali = 1.5
    elif (wilayah_asal == "G" and wilayah_tujuan == "P") or (wilayah_asal == "P" and wilayah_tujuan == "G"):
        faktor_pengali = 2.0
    elif (wilayah_asal == "L" and wilayah_tujuan == "P") or (wilayah_asal == "P" and wilayah_tujuan == "L"):
        faktor_pengali = 3.0
        
    # TODO: Kalkulasi biaya rute dan sisa anggaran
    biaya_rute_ini = int(panjang_jalan * biaya_per_km * faktor_pengali)
    sisa_anggaran -= biaya_rute_ini
    
    print(f"Biaya rute ini: {biaya_rute_ini}")
    print(f"Sisa anggaran: {sisa_anggaran}")

    # TODO: Kondisi jika sisa anggaran sudah bernilai negatif
    if sisa_anggaran < 0:
        break
    
    # Mengubah wilayah asal untuk rute berikutnya
    wilayah_asal = wilayah_tujuan

# TODO: Kondisi rencana memenuhi rancangan anggaran
print("=============================================================")
if sisa_anggaran >= 0:
    print("STATUS: RENCANA PEMBANGUNAN MEMENUHI RANCANGAN ANGGARAN")
else:
    print("STATUS: RENCANA PEMBANGUNAN TIDAK MEMENUHI RANCANGAN ANGGARAN")
print("=============================================================")