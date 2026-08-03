import math

# Input Data
waktu = int(input("Waktu (Menit): "))
pusat_x = int(input("Koordinat Titik Pusat X: "))
pusat_y = int(input("Koordinat Titik Pusat Y: "))
jari_jari = int(input("Jari-jari Bianglala (Meter): "))
sudut_awal = int(input("Sudut Awal Bianglala (Derajat): "))

# Menghitung Sudut
kecepatan = 6
sudut_akhir = sudut_awal + (kecepatan * waktu)

# Menghitung Koordinat Titik Akhir
x_akhir = pusat_x + jari_jari * math.cos(math.radians(sudut_akhir)) # sebenarnya bisa lebih singkat sih kalau radians nya dihitung dulu kemudian dibikin variabel baru
y_akhir = pusat_y + jari_jari * math.sin(math.radians(sudut_akhir))

# Output
print(f"{x_akhir:.2f}, {y_akhir:.2f}")