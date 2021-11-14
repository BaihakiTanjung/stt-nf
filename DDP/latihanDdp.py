# # Soal 1

# string = ""
# bar = 1

# x = int(input("Masukkan angka :"))

# # Looping Baris
# while bar <= x:
# 	# Looping Kolom Spasi Kosong
# 	kol = bar
# 	while kol > 1:
# 		string = string + "   "
# 		kol = kol - 1

# 	# Looping Kolom Bintang
# 	kanan = 0
# 	while kanan <= (x - bar):
# 		string = string + " * "
# 		kanan = kanan + 1

# 	string = string + "\n"
# 	bar = bar + 1
# print (string)


# # Soal 2

# string = ""
# bar = 1

# x = int(input("Masukkan angka :"))
# print("\n")
# # Looping Baris
# while bar <= x:
#     kol = bar
#     # Looping Kolom Spasi Kosong
#     while kol > 1:
#         string = string + " "
#         kol = kol - 1
#     # Looping Kolom Bintang Sisi Kiri
#     kiri = 0
#     while kiri <= (x - bar):
#         string = string + "*"
#         kiri = kiri + 1
#     # Looping Kolom Bintang Sisi Kanan
#     kanan = kiri
#     while kanan > 1:
#         string = string + "*"
#         kanan = kanan - 1

#     string = string + "\n\n"
#     bar = bar + 1
# print(string)

# # Soal 3

# string = ""
# bar = 1

# x = int(input("Masukkan angka :"))
# print("\n")
# # Looping Baris
# while bar <= x:
#     kol = bar
#     # Looping Kolom Spasi Kosong
#     while kol > 1:
#         string = string + "   "
#         kol = kol - 1
#     # Looping Kolom Bintang Sisi Kiri
#     kiri = 0
#     while kiri <= (x - bar):
#         string = string + " * "
#         kiri = kiri + 1
#     # Looping Kolom Bintang Sisi Kanan
#     kanan = kiri
#     while kanan > 1:
#         string = string + " * "
#         kanan = kanan - 1

#     string = string + "\n\n"
#     bar = bar + 1
# print(string)

# Soal 4
for i in range(0, 17):
    if i % 2 == 1:
        print(" ", ' '*15, " ")
    elif i > 0 and i < 16:
        if i == 4:
            print("|", " - "*5, "|")
        else : 
            print("|", ' '*15, "|")
    else:
        print("- "*10)

# Soal 5
for i in range(0, 1):
    for c in range(1, 4):
        print(c, end=" ")
            

            
