''' Methods strip(), lstrip() , rstrip() 

Method dari strip untuk menghapus kata yang diinginkan dari pyhton yang bisa diisi didalam method
1. nama = "DanDanDanWilganMalakiDanDanDan"
print(nama.strip(Dan))

2. Method dari .strip() yang bisa menghapus awalan whitespace dan akhir whitespace. bisa juga
menambahkan kata apa yang ingin dihapus didalam method strip  
nama = "    WildanMalaki    "
print(nama.strip())

3. Method dari lstrip(left) yang artinya untuk menghapus whitespace dari kiri string 
nama = "       WildanMalaki"
print(nama.lstrip())

4. Method dari rstrip(right) yang artinya untuk menghapus whitespace dari kanan string 
nama = "WildanMalaki        "
print(nama.rstrip())
'''

''' Methods startwith(), endwith()

1. Metode startswith() bertujuan untuk menemukan suatu kata pada awal string.
Metode ini mengembalikan nilai True.

print("WildanMalaki".startswith("Wildan"))

2. Methods endswith() bertunjuan menemukan suatu kata pada akhir string.
metode ini mengembalikan nilai true jika menemukan kata akhir

print("WildanMalaki".endswith("Malaki"))
'''

''' Methods .join(), .split() 

1. Methods .join() yang berfungsi untuk menggabungkan semua keseluruan string yang harus ditulis didalam
method .join(["contoh","Wildan","Uhamka"])

print(''.join(["Wildan","Malaki","Ganteng"]))

print("Ganteng".join(["Wildan","banget"]))

2. Methods .split() yang bertujuan untuk memisahkan string

print("Wildan Malaki Ganteng Banget".split())

print("Wildan Malaki belom mandi".split())

3. Menambahkan '\n' pada akhir .split() yang berfungsi memisahkan setiap baris pada string

print("""
Halo Nama saya wildan malaki
saya adalah seseorang mahasiswa uhamka
semester 3
yang sedang belajar coding
hehehe
""".split("\n"))

'''

''' Methods .replace() 
.replace() berfungsi untuk menggantikan elemen string didalamnya dengan elemen string lainnya..
contoh 1 = 
nama = "Nama aku adalah Yanto yang ingin belajar coding"
print(nama.replace("Yanto","Wildan"))

Contoh 2 =
string = "Nama aku adalah Naufal yang ingin pergi ke Bali"
print(string.replace("Naufal","Wildan").replace("Bali","Jakarta"))

'''

# ==== PENGECEKAN STRING ====

''' issuper(), islower(), isalpha(), isalnum(), isdecimal(), isspace(), istitle(), 

1. issuper() akan mengembalikan nilai 'true' jika didalam hurus string besar semua(kapital), jika ada
ada satupun huruf kecil, maka kondisinya akan menjadi 'false'

nama = "WILDAN"
print(nama.isupper())

outputnya = True. Karena huruf "WILDAN" besar semua.

coba gua ubah salah satu huruf dari string, maka akan terjadi false

nama = "WiLDAN"
print(nama.isupper())
outputnya akan = False karena Inya kecil

2. islower() akan mengembalikan nilai "true" jika didalamnya menggunakan huruf kecil semua. sebaliknya dari 
methods isupper(), jika ada huruf besar satu saja maka kondisinya akan "False"

nama = "wildanmalaki"

print(nama.islower())
output = akan "True" karena hurufnya kecil semua

jika kita rangkum dari isupper() dan islower()

print("hasil dari islower()")
#islower()
nama = "wildanmalaki"
print("islower() :",nama.islower())
print("isupper() :",nama.isupper())

#isupper()
print("hasil dari isupper()")
nama_2 = "WILDANMALAKI"
print("isupper() :",nama_2.isupper())
print("islower() :",nama_2.islower())

3. .isalpha() methods yang berfungsi untuk mengecek karakter didalam string adalah huruf ALFABET, 
jika ada huruf lain seperti angka, simbol . maka akan "false"

nama = "wildan"
print(nama.isalpha())
outputnya = True karena didalamnya hanyalah alfabet, tidak ada angka dan simbol didalamnya

nama = "W1ldan"
print(nama.isalpha())
outputnya = False karena terdapat angka didalamnya.

nama = nama = "Wild@n"
print(nama.isalpha())
outputnya = False karena terdapat simbol "@" didalamnya

4. .isalnum() Methods ini memeriksa apakah seluruh karakter dalam string hanya terdiri dari:
Huruf (A-Z, a-z)\
Angka (0-9)

nama = "Wildan123"
print(nama.isalnum())
outputnya = True, karena termasuk alfabet didalamnya.

nama = "wildan malaki"
print(nama.isalnum())
outputnya = False, karena terdapat spasi didalamnya

nama = "Wildan_Malaki"
print(nama.isalpha())
outputnya = False, karena ada simbol "underscore" pada isinya

5. .isdecimal() method untuk string yang berfungsi mengecek apakah ada nilai desimal didalam string, 
mengembalikan nilai True jika ada

print("Hanya berisi angka :")
angka = "123"
print(angka.isdecimal())
outpunya = True , karena hanya angka didalamnya.

print("Tidak ada angka didalamnya : ")
angka_2 = "wildan"
print(angka_2.isdecimal())

print("\nCoba kita gabungkan 'WildanMalaki123' kondisiya seperti apa")
A = "WildanMalaki123"
print("hasilnya : ",A.isdecimal())
outputnya = False, karena ada campuran WildanMalaki dan angka didalamnya.

6. .isspace() adalah methods yang mengembalikan kondisi True jika isinya hanyalah Whitespace,spasi,tab,
newline, dan karakter whitespace lainnya

x = "           "
print(x.isspace())
outputnya = True, Karena tidak isi. isinya hanyalah tab,spasi.

x = "   ___     "
print(x.isspace())
outpunya = False, karena ada Underscore 

7. istitle() adalah method untuk mengembalikan nilai true jika setiap katanya mempunyai huruf kapital 

# Huruf pertama besar (kapital)
nama = "Wildan"
print(nama.istitle())

# huruf pertama kecil 
nama_2 = "wildan"
print(nama_2.istitle())

'''

#Formatting pada STRING

'''
.zfill(), .rjust(), .ljust(), .center(), dll.

1. .zfill() adalah metods yang menambahkan nilai 0 didepan sebuah string dengan panjang tertentu.

#zfill() menambahkan teks tambahan sebesar 1 dari String "Wildan" yang berisi 6 huruf jadi totalnya 7
teks = "Wildan"
nambah_teks = teks.zfill(7)
print(nambah_teks)

#zfill() menambahkan teks tambahan sebesar 4 dari String "WildanMalaki" yang berisi 12 huruf jadi totalnya 16
teks_2 = "WildanMalaki"
teks_baru = teks_2.zfill(16)
print(teks_baru)

2. .rjust() Methods yang berfungsi untuk merapikan teks, dan memberi Whitespace pada awal String. bisa
ditambahkan huruf/angka yang lain

nama = "Wildan"
print(nama.rjust(10))
output:     Wildan, menghitung dari total angka yang diberi. pada output gua, ada 5 Whitespace 5 huruf.
kalo digambar, seperti ini _____Wildan. totalnya 10 

nama_depan = "Wildan"
nama_belakang = "Malaki"
print(nama_depan,nama_belakang.rjust(15))
outputnya = Wildan          Malaki

nama = "Wildan"
print(nama.rjust(20,"!"))
output = !!!!!!!!!!!!!!Wildan 

3. ljust() Methods ini mengembalikan dari metode rjust() yang bertujuan untuk membuat teks rata kiri

print("WildanMalaki".ljust(50))
output = WildanMalaki

4. center() menjadikan teks rata tengah,  Metode ini akan menambahkan whitespace di sebelah kiri dan 
kanan secara default. Anda juga bisa mengganti whitespace tersebut dengan karakter lain.

print("WildanMalaki".center(16,"-"))
outputnya = --WildanMalaki--

'''

##### String Literals #####

'''
\' Single quote
\" Double quote
\t Tab
\n Newline (line break)
\\ Backslash

1. contoh dari newline "\n" yang berfungsi untuk membuat garis kode baru dibawahnya.

print("Halo!\nPerkenalkan namaku Wildan Malaki\nSaya berasal dari Teknik Informatika\nUniversitas Uhamka!")
output = 

Halo!
Perkenalkan namaku Wildan Malaki
Saya berasal dari Teknik Informatika
Universitas Uhamka!
'''







