''' KOMPARASI LOGIC DAN OPERASI OR AND NOT 
    Wildan Malaki ANTI VIBECODING 1 '''

# Input nama user
nama_depan = input("Masukan nama depan anda: ")
nama_belakang = input("Masukan nama belakang anda: ")

# Variabel lengkap disimpan
namaLengkap = nama_depan + " " + nama_belakang

# Input umur
while True:
    umur_input = input("Masukan umur : ")
    # Membersihkan kata "tahun" dan spasi di sekitarnya
    isUmur = umur_input.lower().replace("", "").strip()
    try:
        umur = int(isUmur)
        break
    except ValueError:
        print("Input salah bos!, silahkan masukan umurmu lagi : ")

# Input isMarried
isMarried = input("Apakah sudah menikah ? (y/n) : ").lower()

# Logic validasi input
while isMarried != "y" and isMarried != "n":
    print("Input salah! silahkan masukan (y/n) :")
    isMarried = input("Apakah sudah menikah ? (y/n) : ").lower()

# Konversi status menikah ke boolean
if isMarried == "y":    
    isMarried = True
else:
    isMarried = False

# Logic validasi umur (mengubah angka umur menjadi status boolean)
if umur >= 18:
    status_umur = True
else:
    status_umur = False
    
# Komparasi logika AND
if status_umur and isMarried:
    print(f"\nSelamat kepada {namaLengkap}\nAnda lolos pada tahap ini")
else:
    print(f"Maaf kepada {namaLengkap} tidak lolos pada tahap ini. Coba lagi nanti")