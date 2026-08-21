print("==== SISTEM TIKET WAHANA EKSTREM ====")
print("==== PERINGATAN!!, ANDA HARUS BERUSIA MINIMAL 12 TAHUN ====")
print("==== DAN HARUS MEMPUNYAI KARTU VIP ====\n")

input("Tekan enter untuk melanjutkan ..")
print()

nama = input("Masukan nama anda : ")
umur = int(input("Masukan umur anda : "))
tinggi = float(input("Masukan tinggi badan anda : "))
vip = input("Apakah kamu punya kartu VIP? ")

if (umur >= 12 and tinggi >= 145) or (vip == "punya" and umur >= 12 and tinggi >= 145):
    print("Selamat anda bisa masuk")
else:
    print("Maaf anda tidak memenuhi syarat..")


