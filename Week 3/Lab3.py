import turtle
import random
import time




DAFTAR_WARNA = ["red","green","blue","yellow","purple","orange"]




def setup_background():
  """
  Mengatur judul canvas dan mengubah tampilannya dengan warna hitam agar terlihat
  seperti malam hari.
  """
  turtle.setup(800,600)
  turtle.bgcolor("black")
  turtle.title("Penampilan Kembang Api Pesta Rakyat Florian")
  turtle.hideturtle() # Menyembunyikan icon turtle
  turtle.tracer(0) # Mematikan animasi turtle, sehingga gambar akan langsung muncul sekaligus


def rocket_animation(x_target, y_target):
  """
  Menganimasikan pergerakan roket kembang api saat meluncur ke langit
  """


  # TODO: Pindahkan turtle ke koordinat (x_target, -250)
  # (angkat pena terlebih dahulu agar tidak meninggalkan jejak)
  turtle.penup()
  turtle.goto(x_target, -250)
  turtle.pendown()


  # TODO: Atur warna pena menjadi warna abu-abu ("gray") dan atur ketebalan garis menjadi 2
  turtle.pencolor("gray")
  turtle.pensize(2)


  # Nyalakan tracer turtle khusus di dalam fungsi ini saja
  turtle.tracer(1, 10)
  turtle.speed(3)


  # TODO: Pindahkan turtle ke koordinat ledakan (x_target, y_target)
  turtle.goto(x_target, y_target)


  # Matikan lagi tracernya
  turtle.tracer(0)


def starburst_animation(x_target, y_target):
  """
  Menganimasikan proses meledaknya kembang api di langit
  """
   panjang_percikan = random.randint(50, 150) # TODO: Memilih integer acak dalam interval [50, 150]
  jumlah_percikan = random.randint(15, 30) # TODO: Memilih integer acak dalam interval [15, 30]
  warna = DAFTAR_WARNA[random.randint(0, 5)] # TODO: Mengambil warna dengan memilih indeks acak dalam interval [0, 5]
  sudut = 360/jumlah_percikan # TODO: Hitung sudut antar percikan (360 derajat dibagi jumlah percikan)


  # TODO: Atur ketebalan garis ledakan sebesar 3 dan atur warna sesuai dengan warna yang dipilih
  turtle.pensize(3)
  turtle.pencolor(warna)


  for current_radius in range(10, panjang_percikan+1, 10):
      for i in range(jumlah_percikan):
          # Kembalikan posisi turtle ke koordinat titik ledak setiap akan menggambarkan percikan baru
          turtle.penup()
          turtle.goto(x_target, y_target)


          # Atur arah/sudut pergerakan turtle sesuai urutan kelopak percikan
          turtle.setheading(i * sudut)
          turtle.pendown()


          # Gambar kelopak percikan sesuai dengan panjang radius saat ini
          turtle.forward(current_radius)
    
      turtle.update()
      time.sleep(0.02)


def draw_firework():
  x_target = random.randint(-250, 250) # TODO: Memilih integer acak dalam interval [-250, 250]
  y_target = random.randint(50, 200) # TODO: Memilih integer acak dalam interval [50, 200]


  # TODO: Lengkapi parameter fungsi untuk menampilkan roket yang meluncur ke atas
  rocket_animation(x_target, y_target)


  turtle.clear()   
  turtle.update()   
  time.sleep(0.1)   


  # TODO: Lengkapi parameter fungsi untuk menampilkan ledakan kembang api
  starburst_animation(x_target, y_target)


  time.sleep(0.5)
  turtle.clear()
  turtle.update()


def main():
  print("============================================================")
  print("Penampilan Kembang Api - Pesta Rakyat Florian")
  print("============================================================\n")




  banyak_peluncuran = int(input("Masukkan banyaknya peluncuran kembang api: "))




  print("\nSihir dipersiapkan... Saksikan pertunjukan kembang api di langit Florian!")
  setup_background()




  for _ in range(banyak_peluncuran):
      draw_firework()




  print("\nPertunjukan selesai! Klik jendela turtle untuk menutup.")
  turtle.exitonclick()




if __name__ == "__main__":
  main()