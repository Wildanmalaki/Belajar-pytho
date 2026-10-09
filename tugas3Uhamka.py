print("Wildan Malaki - 2503015089")

# nilai dari NIM 2503015089
a = 89
b = 50
c = 1

# cek dulu kalau ketiganya sama
if a == b and b == c:
    print("a, b, dan c nisalnya sama")
# kalau ada dua yang sama dan lebih besar dari yang ketiga
elif a == b and a > c:
    print("a and b nilanya besar")
elif a == c and a > b:
    print("a and c nilainya besar")
elif b == c and b > a:
    print("b and c nilainya besar")
# kalau tidak ada yang sama, cari satu yang paling besar
elif a > b and a > c:
    print("a nilainya besar")
elif b > a and b > c:
    print("b nilainya besar")
# sisanya pasti c yang paling besar
else:
    print("c nilainya besar")