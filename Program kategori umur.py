print("==== Selamat datang keprogram sederhanaku ====n")
print("==== Program mengkategorikan umur seseorang ====")
print("==== Program by Wildan Malaki ====")
print("==== #keluardarivibecoding ====\n")

input("Apakah kamu sudah dewasa ? ")
input("Apakah kamu masih bocil ? ")
print("Mari kita nilai HAHAAHA ..\n")

nama = input("Masukan nama kamu : ")
print("okee salam kenal", nama, )

while True:
    x = input("\nApakah kamu yakin kamu itu dewasa? ")
    
    if x == "yakin":
        print("\nokee, jika kamu dewasa")
        break
    else:
        print("jawab 'yakin' kalo udah dewasa ")

umur = int(input("Coba masukan umurmu donks : "))

if umur >= 20:
    hasil = "Kamu berarti beneran dewasa HAHAHAHAHAHA\n"
elif umur >= 17:
    hasil = "kamu masih remaja kocak\n"
else:
    hasil = "Sumpah, lu itu masih bocil. belajar yang bener ya dek\n"
    
print(nama, hasil)








