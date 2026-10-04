# Tugas MK.Programming Lanjutan 
# Membuat program sederhana dari riwayat Music youtube
# tugas Uhamka

import time

print("================================")
print("=====Riwayat Music Youtube======")
print("=======By Wildan Malaki=========")
print("================================")

namaDepan = input("Masukkan Nama Depan Anda : ")
namaBelakang = input("Masukkan Nama Belakang Anda : ")
namaLengkap = namaDepan + " " + namaBelakang

print("Halo.. Selamat datang", namaLengkap, "di Riwayat Music Youtube guehhhh")

print("mengekstraksi data dari riwayat music youtube..")
time.sleep(2)
print("sabar yaa..")
time.sleep(2)
print("dowkaokdawok nungguin yaakk??")
time.sleep(5)
print("oke.. data berhasil di ekstrak dari riwayat music youtube..")

riwayatMusicWildan = {
    1: {
        "judul": "Ada titik-titik diujung doa",
        "artis": "Sel Priadi",
        "platform": "Youtube Music",
        "menit": "5.06"
    },
    2: {
        "judul": "Serana",
        "artis": "For Revenge",
        "platform": "youtube Music",
        "menit": "4.12"
    },
    3: {
        "judul": "Another Love",
        "artis": "Tom Odell",
        "platform": "Youtube Music",
        "menit": "4.08"
    },
    4: {
        "judul": "Wonderwall",
        "artis": "Oasis",
        "platform": "Youtube Music",
        "menit": "4.40"
    },
    5: {
        "judul": "Last Night on Earth",
        "artis": "Miller Hoffman",
        "platform": "Youtube Music",
        "menit": "3.57",
    },
    6: {
        "judul": "What if I call",
        "artis": "Alex Crichton",
        "platform": "Youtube Music",
        "menit": "2.41",
    },
    7: {
       "judul": "Serana (feat. Danindra Divide)",
       "artis": "For Revenge",
       "platform": "Youtube Music",
       "menit": "4.04",
    },
    8: {
        "judul": "Bring Me To Life",
        "artis": "Evanescence",
        "platform": "Youtube Music",
        "menit": "4.14"
    },
    9: {
        "judul": "Boulevard of Broken Dreams - Single Album Version",
        "artis": "Green Day",
        "platform": "Youtube Music",
        "menit": "4.48"
    },
    10: {
        "judul": "One More Light",
        "artis": "Linkin Park",
        "platform": "Youtube Music",
        "menit": "4.31"
    }
}

print("====================================)")
time.sleep(3)
print("Riwayat lagu-lagumu dari youtube music adalah :",riwayatMusicWildan[1]["judul"])
time.sleep(1)
print("Riwayat lagu-lagumu dari youtube music adalah :",riwayatMusicWildan[2]["judul"])
time.sleep(1)
print("Riwayat lagu-lagumu dari youtube music adalah :",riwayatMusicWildan[3]["judul"])
time.sleep(1)
print("Riwayat lagu-lagumu dari youtube music adalah :",riwayatMusicWildan[4]["judul"])
time.sleep(1)
print("Riwayat lagu-lagumu dari youtube music adalah :",riwayatMusicWildan[5]["judul"])
time.sleep(1)
print("Riwayat lagu-lagumu dari youtube music adalah :",riwayatMusicWildan[6]["judul"])
time.sleep(1)
print("Riwayat lagu-lagumu dari youtube music adalah :",riwayatMusicWildan[7]["judul"])
time.sleep(1)
print("Riwayat lagu-lagumu dari youtube music adalah :",riwayatMusicWildan[8]["judul"])
time.sleep(1)
print("Riwayat lagu-lagumu dari youtube music adalah :",riwayatMusicWildan[9]["judul"])
time.sleep(1)
print("Riwayat lagu-lagumu dari youtube music adalah :",riwayatMusicWildan[10]["judul"])
time.sleep(1)

pencet = input(f"Mas {namaLengkap} berikut adalah riwayat judul-judul yang kamu dengarkan tadi.. (pencet apa aja biar next yeee)")

for nomor in range(1, 11):
    lagu = riwayatMusicWildan[nomor]
    print(f"{nomor}. {lagu['judul']}")
    print(f"   Artis    : {lagu['artis']}")
    print(f"   Platform : {lagu['platform']}")
    print(f"   Durasi   : {lagu['menit']} menit")
    print("-" * 30)




