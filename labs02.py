print("Proram Menentukan bilangan terbesar dari 3 buah bilangan")
print("-"*25)
print("Nama : Ahmad Hapizhudin/n")
print("NIM  : 312210370/n")
print("Kelas: TI.22.A4/n")

bil1 = int(input("Masukan bilangan ke 1 : "))
bil2 = int(input("Masukan bilangan ke 2 : "))
bil3 = int(input("Masukan bilangan ke 3 : "))

bilangan_terbesar = bil1
if bil2 > bilangan_terbesar:
    bilangan_terbesar = bil2
    print("Bilangan terbesar adalah : ",bilangan_terbesar)
elif bil3 > bilangan_terbesar:
    bilangan_terbesar = bil3
    print("Bilangan terbesar adalah : ",bilangan_terbesar)
elif bil2 == bilangan_terbesar & bil3 == bilangan_terbesar:
    print("semua bilangan sama besarnya")
else:
    False

