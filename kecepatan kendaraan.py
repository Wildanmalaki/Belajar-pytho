print("=== PENGUKURAN KECEPATAN ===")

tipe = input("Mobilmu apa mereknya: ")
kecepatan = int(input("Kecepatan kamu membawa mobil berapa : "))

if kecepatan > 105:
    print("Buset. ngabers lu ?")
elif kecepatan > 80:
    print("udah lumayan kenceng")
elif kecepatan > 50:
    print("kamu nyantai banget ya")
else:
    print("Pelan banget, ini mah jalan kaki!")