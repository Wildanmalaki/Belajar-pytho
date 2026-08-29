### Operasi pada List, Set, String pada Pyhton 

''' len(), set(), min(), max(), .count()

# len() Berfungsi untuk menghitung banyaknya element dari list, set dan String
 
list = [1,2,3,4,5,6,7,8,9,10]
print(list)
print(len(list))

- Implementasi len() dengan Integer

list_string = ["a","b","c","d","e","f","g"]
print(list_string)
print(len(list_string))

- Implementasi len() dengan string

nama = "WildanMalaki"
print(nama)
print(len(nama))

output = 12

# set() berfungsi untuk menghapus element yang terduplikat. 

angka = set([1,2,3,3,3,3,3,4,4,5,6,7,8,8,8,9,9])

print(angka)
print(len(angka))

# min() method yang berfungsi untuk mengetahui nilai minimum pada suatu variabel, sedangkan max() berfungsi
sebaliknya, mengetahui nilai tertinggi.

angka = [102,92,87,100,67,120,112,500,400,93]

print(angka)
print("Angka terkecil adalah")
print(min(angka)) #outputnya 67
print("Angka terbesar adalah")
print(max(angka)) #outputnya 500

# .count() method yang berfungsi untuk mengetahui berapa kali objek muncul dalam list.

implementasi .count() ke integer.

angka = [1,2,3,3,1,4,5,6,7,7,8,9]
print(angka.count(7)) #output = 2

implementasi .count() ke String. 
nama = ["Wildan Malaki", 1,2,"Wildan Malaki","Wildan Malaki"]
print(nama.count("Wildan Malaki")) #output = 3

implementasi .count() untuk mencari huruf "a"

kalimat = "aku suka kamu, tapi kamunya enggak\npadahal aku cinta kamu, tapi kamunya nggak\nyaudah tapi mau gimana"
sub_a = "a"
sub_b = "m"

print("Kata 'a' pada kalimat mempunyai :")
print(kalimat.count(sub_a),"kalimat") #output = 23 Kalimat
print(kalimat.count(sub_b),"Kalimat") #output = 6 Kalimat

====== Operator In not in ========
Operator In, Not in berfungsi untuk mengetahui nilai yang ada pada suatu object apakah ada didalam list atau
tidak..

kalimat = "Belajar fudamental coding tanpa vibecoding"

print("coding" in kalimat) #output : True
print("fudamental" in kalimat) #output : True
print("tidak" in kalimat) #output : false
print("wildan" in kalimat) #output : False

====== Multiple Variabel ========
Variabel yang bisa ditambahkan dengan nilai tertentu untuk membuat multi variabel. 

#Variabel yang bernama "data" yang berisi list diantaranya "Wildan Malaki","Umur 24 tahun","Universitas Muhammadiyah Prof Hamka"
data = ["Wildan Malaki","Umur 24 tahun","Universitas Muhammadiyah Prof Hamka"] 
nama,umur,univ = data #membuat multi variabel untuk mengisi antar list yang ada divariabel "data", agar terpisah

print(data) #outputnya ["Wildan Malaki","Umur 24 tahun","Universitas Muhammadiyah Prof Hamka"]
print(nama) #outputnya Wildan Malaki
print(umur) #umur 24 tahun
print(univ) #Universitas Muhammadiyah Prof Hamka

#Contoh 2

data = ["Wildan malaki",24,"tahun", 2026]

nama,integer24,tahun,inttahun = data

print(data)
print(nama)
print(integer24)
print(tahun)
print(inttahun)

================== UJIAN ==========================

# KUIS OPERASI LIST
var_list = [792564, 465231, 203748, 981037, 857219, 314092, 608345, 123907, 736890, 985026, 
179430, 450218, 680934, 543187, 978260, 283045, 617902, 405826, 820913, 731095, 
592403, 109237, 874956, 605132, 214978, 674519, 391047, 825160, 509317, 768490, 
950283, 307491, 487610, 532198, 605132, 160984, 609873, 245016, 879043, 734126, 
351809, 670594, 920873, 605132, 596410, 135890, 804512, 683420, 290753, 931560, 
175430, 950672, 378490, 284105, 746098, 503624, 605132, 167432, 974810, 519463, 
407835, 740326, 281709, 630921, 953284, 605132, 429731, 183607, 369012, 541380, 
605132, 217605, 496803, 827309, 153607, 605132, 720459, 381904, 594031, 810235, 
673925, 492157, 835096, 260481, 956024, 540329, 806295, 320158, 751903, 980465, 
235780, 857943, 605132, 125094, 620493, 913250
]

panjang = (len(var_list))
maksimal = (max(var_list))
minimal = (min(var_list))
banyak = (var_list.count(605132))

print (panjang, maksimal, minimal, banyak) #output 96 985026 109237 8 

'''






