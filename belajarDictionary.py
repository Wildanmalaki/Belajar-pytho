lebar = 50
print(lebar * "-")
print("Belajar Dictionary".center(lebar))
print("Fundamental Programming".center(lebar))
print(lebar * "-")

# Variabel Dictionary "biodata"
biodata = {
    "namaDepan": "Wildan",
    "namaBelakang": "Malaki",
    "umur": 24,
}

#menambahkan variabel baru dan key kedalam variabel "biodata"
#secara manual
biodata["kota"] = "jakarta"
#mengubah lagi valuenya ke "bandung"
biodata["kota"] = "bandung"

# merubah value umur dengan memanggil variabel dictionary dan keynya
biodata["umur"] = 25

#ouput dari program dengan memanggil variabel dictionary dan valuenya.
print("Nama lengkapku adalah" ,biodata["namaDepan"], biodata["namaBelakang"])
print("Umurku saat ini adalah", biodata["umur"], "tahun")
print("Saat ini aku tinggal di", biodata["kota"])

# mencoba fungsi .get() pada dictionary
# fungsi .get() ini berfungsi untuk mengambil key yang tidak ada, jika error maka bisa diganti
print("Saat ini aku tinggal di", biodata.get("makanan", "tidak diketahui"))
print()

'''Praktik'''
#Praktik Dictionary
lebar = 50
print(lebar * "-")
print("Praktik Dictionary".center(lebar))
print("Wildan Malaki".center(lebar))
print(lebar * "-")

#judul program praktik
print("List Buku Dictionary")

#Dictionary
buku = {
    "judul": "Atomic Habits",
    "penulis": "James Clear",
    "halaman": 352,
    "tahun": "18 Oktober 2018"
}

#mengubah nilai dari variabel dictionary dan memanggil key buku
#dan mengubah valuenya dari 352 menjadi 400
buku["halaman"] = 400

#output dari program dictionary, menggunakan F string dan fungsi get.()
print(f"judul : {buku["judul"]}")
print(f"Penulis : {buku['penulis']}")
print(f"Total halaman : {buku["halaman"]}")
print(f"tahun terbit : {buku['tahun']}")
print(f"Penerbit : {buku.get("penerbit", "belum ada")}")