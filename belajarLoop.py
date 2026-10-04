#output membuat string menjadi 3 baris
print("Memahami kerja loop dari")
for i in range(3):
    print("hallo namaku Wildan Malaki!")

#output untuk mengetahui kerja dari variabel "i", jika print dengan memanggil langsung variabel "i" maka 
#program menghitung 0-2
# angka 0 itu kehitung, karena pyhton membaca angka itu dari 0,
print("Loop dengan memanggil variabel i")
for i in range(3):
    print(i)

#mencoba mengubah nama variabel "i" 
#konsepnya tetap sama.
print("mencoba mengubah nama variabel 'i' ")
for wildan in range(3):
    print(wildan)

'''mencoba eksperiment 1'''
print("== mencoba eksperiment ke-1 ==\n")
umur = 24
pekerjaan = "Sofware Engineer"
isMarried = False

for wildan in range(3):
    print(wildan, "Namaku adalah Wildan")
    print("Aku saat ini lagi belajar loop!")
    print(f"Umurku saat ini adalah {umur}")
    print(f"Pekerjaanku sebagai {pekerjaan}")
    print(f"sudah menikah/belom : {isMarried}\n")

'''mencoba eksperiment 2'''
print("== mencoba eksperiment ke-2 ==")

#deklarasi + inisiasi  
namaDepan = "Wildan"
namaBelakang = "Malaki"
umur = 24
pekerjaan = "Network Engineer"
lamaBekerja = 5
isMarried = False

#fungsi loop
for nomor in range(5):
    print(f"Perkenalkan, nama lengkapku {namaDepan} {namaBelakang}")
    print(f"saat ini saya berumur {umur} tahun")
    print(f"pekerjaanku sebagai {pekerjaan} selama {lamaBekerja} tahun")
    print(f"Status pernikahan : {isMarried}")

print()

'''mencoba eksperiment 3'''
print("== mencoba eksperiment ke-3 ==")

#fungsi loop menghitung loop dari 1 sampai 5 menggunakan F string
print("fungsi loop menghitung loop dari 1 sampai 5 menggunakan F string")
for nomor in range(5):
    print(f"ini adalah baris : {nomor + 1}")

print()

#fungsi loop menghitung 1-5 dari fungsi "range"
print("fungsi loop menghitung 1-5 dari fungsi 'range'")
for nomor in range(1,6):
    print(f"ini adalah baris : {nomor}")

print()

#membuat kesimpukan
print("membuat kesimpulan fungsi loop..")
for nomor in range(1,4):
    print(f"putaran ke-{nomor}")