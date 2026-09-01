''' KOMPARASI LOGIC DAn OPERASI OR AND NOT 
    Wildan Malaki ANTI VIBECODING 1 '''

#Input nama user
nama_depan = input("Masukan nama depan anda: ")
nama_belakang = input("Masukan nama belakang anda: ")

#Variabel lengkap disimpah
namaLengkap = (nama_depan + " " + nama_belakang)

#input umur
umur = int(input("Masukan umur : "))
#input isMarried
isMarried = input("Apakah sudah menikah ? (y/n) :").strip().lower()
#logic validasi input
while isMarried != "y" and isMarried != "n":
    print("Input salah! silahkan masukan (y/n) :")
    isMarried = input("Apakah sudah menikah ? (y/n) :")

if isMarried == "y":    
    isMarried = True
else:
    isMarried = False
#logic validasi 
if umur >= 18:
    umur = True
else:
    umur = False
    
if umur and isMarried:
    print(f"\nSelamat kepada {namaLengkap}\nAnda lolos pada tahap ini")
else:
    print(f"Maaf kepada {namaLengkap} tidak lolos pada tahap ini . coba lagi nanti")


