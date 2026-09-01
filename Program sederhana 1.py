print("===== Program sederhana =====\n")
print("Menentukan nilai murid dari hasil nilai")
print("IF,ELIF,ELSE,Operator aritmatika\n")
print("===== By Wildan Malaki =====\n")

nama = input("Masukan nama kamu : ")
print("\nHalo selamat datang",nama,", program ini adalah program untuk menentukan kamu lulus atau tidak")

input("Pencet ENTER untuk melanjutkan..\n")

nilai = int(input("Masukan nilai kamu : "))

if nilai >= 80 :
    grade = "Grade A"
elif nilai >= 70:
    grade = "Grade B"
elif nilai >= 60:
    grade = "Grade C"
elif nilai < 60:
    grade = "Grade D"

print("\nSelamat, kamu mendapatkan", grade)
print("\nJangan patah semangat, keep doing!!!")
print()
print("===== Program by Wildan Malaki =====")
print("Praktik python dari mahaguru ChatGPT")