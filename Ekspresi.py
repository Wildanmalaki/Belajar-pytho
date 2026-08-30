''' Ekpresi adalah data yang disimpan didalam variabel yang akan dioperasikan untuk menghasilkan apa
yang diinginkan

#ekpresi aritmatika 
A = 5
x = 2
Z = 10
hasil = A * x + Z 
print(hasil) #20

#Ekpresi pergabunga "LIST"
angka = [1,2,3,4,5]
huruf = ["W","i","l","d","a","n"]

print("Angka diatas, huruf dibawah")
print(angka + huruf) #output : [1, 2, 3, 4, 5, 'W', 'i', 'l', 'd', 'a', 'n']

huruf = ["W","i","l","d","a","n"]
angka = [1,2,3,4,5]

print("huruf diatas, angka dibawah")
print(huruf + angka) #output : ['W', 'i', 'l', 'd', 'a', 'n', 1, 2, 3, 4, 5]

#Ekpresi replika pada list 

nama = ["W","i","l","d","a","n"]
print("===== REPLIKA LIST =====")
print(nama * 2) 

nama_depan = ["W","i","l","d","a","n"]
nama_belakang = ["M","a","l","a","k","i"]
print("===== REPLIKA + PERGABUNGAN LIST =====")
print(nama_depan * 2, nama_belakang *2)

output : 
===== REPLIKA LIST =====
['W', 'i', 'l', 'd', 'a', 'n', 'W', 'i', 'l', 'd', 'a', 'n']
===== REPLIKA + PERGABUNGAN LIST =====
['W', 'i', 'l', 'd', 'a', 'n', 'W', 'i', 'l', 'd', 'a', 'n'] ['M', 'a', 'l', 'a', 'k', 'i', 'M', 'a', 'l', 'a', 'k', 'i']
'''

''' - Ekspresi biner merupakan jenis yang memiliki dua operan. Operatornya meliputi penjumlahan (+), pengurangan (-),perkalian (*), 
    pembagian (/), perpangkatan (**), lebih kecil dari (<), lebih kecil dari sama dengan (<=), lebih besar dari (>), 
    lebih besar dari sama dengan (>=), modulus (%), sama dengan (==), dan tidak sama dengan (!=).
    - ekspresi uner adalah jenis ekspresi yang memiliki bentuk dasar operasi dengan satu operan.Contohnya adalah increment (x+=1), 
    decrement (x-=1), dan negasi (not x).


============= CONTOH EKPRESI UNER ========================
A = True
A = not A
print(A)

b = 6
b -= 1
print(b)

c = 6
c += 1
print(c)

d = 99
print(-d)

#penambahan ekpresi biner 
hasil = A + b * c / d
print("hasilnya adalah : ",hasil)

output = 

False
5
7
-99
hasilnya adalah :  0.35353535353535354

#SOAL CUSTOM
A = 57
A -= 30
B = 30
B += 20
C = 100
C *= 2

hasil = A + C * B
final = hasil + 10000

print(final) #output 20027

Didalam ekpresi terdapat 3 ekpresi yaitu 
Ekpresi Aritmatika : jenis ekpresi numerik yang menghasilkan numerik print(2+2) = 4
Ekpresi Relasional : Jenis Ekpresi Relasional yang menghasilkan nilai logika/boolean print(2>10) = False
Ekpresi Logika     : Jenis Ekpresi logika dan menghasilkan nilai logika print(True or False) = True

======== OPERATOR ARITMATIKA ========
x = 10
y = 5

print(x + y) #Penjumlahan 
print(x * y) #Perkalian 
print(x // y) #Pembagian bulat
print(x / y) #pembagian Rill
print(x & y) #modulo
print(x ** y) #pangkat

======= OPERATOR RELASIONAL =======
x = 10
y = 5

print(x > y) #lebih besar dari
print(x < y) #lebih kecil dari
print(x >= y) #lebih besar sama dengan
print(x <= y) #kurang dari sama dengan
print(x == y) #sama dengan
print(x != y) #tidak sama dengan

====== OPERATOR LOGIKA ======
AND menghasilkan nilai true jika keduanya menghasilkan nilai TRUE
print(True and True) output = True
print(True and False) output = False
print(False and True) output = False
print(False and False) output = False

OR mengembalikan nilai True jika salah satu menghasilkan nilai True
print(True or False) output = True
print(True or True) output = True
print(False or True) output = True
print(False or False) output = False

NOT operator NOT akan membalikkan nilai boolean dari operan aslinya atau disebut sebagai negasi
print(not True) = False
print(not False) = True

====== Operator Assignment ======
Operator ini bertujuan untuk melakukan proses assignment atau pemberian nilai pada suatu variabel dengan nilai tetap.
#Tambah 
A = 11
A += 5
print("Operasi Assignment tambah")
print(A)

#kurang 
B = 11
B -= 5
print("Operasi Assignment kurang")
print(B)

#kali
C = 11
C *= 5
print("Operasi Assignment kali")
print(C)

#bagi 
D = 11
D /= 5
print("Operasi Assignment bagi")
print(D)

#Modulo 
E = 11
E &= 5
print("Operasi Assignment Modulo")
print(E)

#perbedaan antara operasi Assigment dan operasi Aritmatika
X = 10
Y = 5
H = X + Y
print("Operasi ARITMATIKA")
print(H)

A = 10
A += 5
print("Operasi Assigment")
print(A)

====================== UJIAN ==========================
"""
TODO:
Anda diharuskan membuat program diskon untuk sebuah toko belanja dengan ketentuan berikut.
- Jika pelanggan berbelanja lebih dari 500.000 ribu, mereka akan mendapat potongan harga 10%.
- Seorang pelanggan bernama Dico telah berbelanja senilai 750.000 ribu.
- Buat operasi aritmetika untuk menghitung total harga belanja Dico setelah mendapatkan diskon, 
  dan simpan dalam variabel bernama "total_harga".

Tips:
- Ingat yang dicari adalah total harga belanja setelah diskon, bukan besaran potongan harga.
"""
# Jangan ubah kode ini
dico = 750000

# TODO: Silakan buat kode Anda di bawah ini.

dico = 750000
if dico > 500000:
    diskon = dico * 0.10
    total_harga = dico - diskon
    print(total_harga)
else:
    print("maaf kamu tidak mendapatkan diskon")
'''










