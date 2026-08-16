# Header 
print("============================================================")
print("KALKULATOR ANGGARAN PEMBANGUNAN INFRASTRUKTUR NEGERI FLORIAN")
print("============================================================")

# TODO: Meminta input awal
wilayah_asal = ...
banyak_jalan = ...
sisa_anggaran = ...
biaya_per_km = ...

# TODO: Memulai perulangan untuk setiap rute jalan
for ... in range(..., ...):
    print(f"\n=== Rute jalan {...} ===")
    wilayah_tujuan = ...
    panjang_jalan = ...
    
    # TODO: Logika percabangan untuk menentukan faktor pengali
    faktor_pengali = 1.0
    if ...:
        faktor_pengali = 1.0
    elif (...):
        faktor_pengali = 1.5
    elif (...):
        faktor_pengali = 2.0
    elif (...):
        faktor_pengali = 3.0
        
    # TODO: Kalkulasi biaya rute dan sisa anggaran
    biaya_rute_ini = ...
    sisa_anggaran -= ...
    
    print(f"Biaya rute ini: {biaya_rute_ini}")
    print(f"Sisa anggaran: {sisa_anggaran}")

    # TODO: Kondisi jika sisa anggaran sudah bernilai negatif
    if (...):
        ...
    
    print("Visualisasi medan geografis:")
    # TODO: Mencetak Visualisasi Medan Geografis (BONUS)
    ...

# TODO: Kondisi rencana memenuhi rancangan anggaran
print("=============================================================")
if sisa_anggaran >= 0:
    print("STATUS: RENCANA PEMBANGUNAN MEMENUHI RANCANGAN ANGGARAN")
else:
    print("STATUS: RENCANA PEMBANGUNAN TIDAK MEMENUHI RANCANGAN ANGGARAN")
print("=============================================================")