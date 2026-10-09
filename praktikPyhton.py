''' Praktik '''
#Praktik 1
lebar = 55

print(lebar * "=")
print("Praktik 1".center(lebar))
print("Belajar Fundamental Programming".center(lebar))
print(lebar * "=")

#judul program
print("Database perusahaan WMfilms")
database = {
    1: {
        "ID": 1000,
        "user": "Wildan",
        "merk": "Canon",
        "tipe": "750D",
        "baterai": "LPE17",
        "lensa_pertama" : "Tamron 150-600 SP",
        "lensa_kedua" : "Canon 70-200",
        "Flash": "Godox"
        
    },
    2: {
        "ID": 2,
        "user": "Alvito",
        "merk": "Canon",
        "tipe": "EOS R",
        "baterai": "LPE6",
        "lensa_pertama" : "Tamron 150-600 SP",
        "lensa_kedua" : "Canon 70-200"
    },
    3: {
        "ID": 3,
        "user": "Faqih",
        "merk": "Canon",
        "tipe": "EOS R6",
        "baterai": "LPE6NH",
        "lensa_pertama" : "Tamron 150-600 SP",
        "lensa_kedua" : "Canon 70-200"
    },
    4: {
        "ID": 4,
        "user": "Yoga",
        "merk": "Canon",
        "tipe": "EOS R1",
        "baterai": "LPE19",
        "lensa_pertama" : "Tamron 150-600 SP",
        "lensa_kedua" : "Canon 70-200"
    },
}

#mengganti ID diluar dari Dictionary
database[1]["ID"] = 1

for nomor in range(1,5):
    peralataan = database[nomor]
    print(nomor, f"Peralatan Tempur {peralataan["user"]}")
    print(f"ID            : {peralataan["ID"]}")
    print(f"User          : {peralataan["user"]}")
    print(f"Merk          : {peralataan["merk"]}")
    print(f"Tipe          : {peralataan["tipe"]}")
    print(f"Baterai       : {peralataan["baterai"]}")
    print(f"Lensa pertama : {peralataan["lensa_pertama"]}")
    print(F"Lensa Kedua   : {peralataan["lensa_kedua"]}")
    print(F"Flash         : {peralataan.get("Flash", "Tidak ada")}")

#Praktik 2
lebar = 55

print(lebar * "=")
print("Praktik 2".center(lebar))
print("Belajar Fundamental Programming".center(lebar))
print(lebar * "=")