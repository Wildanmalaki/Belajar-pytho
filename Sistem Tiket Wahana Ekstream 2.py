print("==== SISTEM TIKET WAHANA EKSTREM ====")
print("==== PERINGATAN!!, ANDA HARUS BERUSIA MINIMAL 12 TAHUN ====")
print("==== DAN HARUS MEMPUNYAI KARTU VIP ====\n")

input("Tekan enter untuk melanjutkan ..")
print()

nama = input("Silahkan masukan nama anda: ")
umur = int(input("Silahkan masukan umur anda: "))
tinggi = float(input("Silahkan masukan tinggi anda: "))
while True:
    kartu_ktp = input("apakah kamu mempunyai kartu vip ? :")

    if umur >= 12 and tinggi >= 145:
        print("Selamat kamu bisa masuk reguler")
        break
    elif umur >= 12 and tinggi >= 175 and kartu_ktp == "punya":
        print("Selamat kamu mendapatkan diskon 10%")
        break
    else:
        print("Maaf anda tidak memenuhi syarat..")
