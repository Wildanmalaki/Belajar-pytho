#Judul program
lebar = 55

print("=" * lebar)
print("Kalkulator Sederhana".center(lebar))
print("Dibuat oleh: Wildan Malaki".center(lebar))
print("Program untuk belajar fundamental programming".center(lebar))
print("Tanpa VibeCoding :D".center(lebar))
print("=" * lebar)
print()

#perulangan program
while True:

#Deklarasi + inisial
    angka_1 = float(input("Silahkan masukan angka pertama   : "))
    aritmatika = input("Operator (+,-,x,/)               : ")
    angka_2 = float(input("Silahkan masukan angka kedua     : "))

#conditional
    if aritmatika == "+":
        hasil = angka_1 + angka_2
        print(f"Hasilnya adalah: {hasil}")
    elif aritmatika == "-":
        hasil = angka_1 - angka_2
        print(f"Hasilnya adalah: {hasil} ")
    elif aritmatika == "x" or aritmatika == "*":
        hasil = angka_1 * angka_2
        print(f"hasilnya adalah: {hasil}")
    elif aritmatika == "/":
        hasil = angka_1 / angka_2
        print(f"hasilnya adalah: {hasil}")
    else:
        print("Yang bener kamu mas..")

    print("Terima kasih sudah menggunakan kalkulator sederhanaku!")
    print("By Wildan Malaki")


