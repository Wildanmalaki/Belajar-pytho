''' KOMPARASI LOGIC DAn OPERASI OR AND NOT 
            Wildan Malaki '''

#Input nama user
nama_depan = input("Masukan nama depan anda: ")
nama_belakang = input("Masukan nama belakang anda: ")

#Variabel lengkap disimpah
namaLengkap = (nama_depan + " " + nama_belakang)

#input umur
umur = int(input("Masukan umur : "))
#input isMarried
isMarried = input("Apakah sudah menikah ? ('Sudah' atau 'Belum) :")
#logic validasi input
while isMarried != "Sudah" and isMarried != "Belum":
    print("Input salah! silahkan masukan 'Sudah' atau 'Belum' :")
    isMarried = input("Apakah sudah menikah ? ('sudah' atau 'belum) ")

if isMarried == "Sudah":    
    isMarried = True
else:
    isMarried = False
#logic validasi 
if umur >= 18:
    umur = True
else:
    umur = False
    
if umur and isMarried:
    print(f"Selamat kepada {namaLengkap}\nAnda lolos pada tahap ini")
else:
    print(f"Maaf kepada {namaLengkap} tidak lolos pada tahap ini . coba lagi nanti")


