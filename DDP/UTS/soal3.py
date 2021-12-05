baris = int(input("Jumlah Bintang : "))
print("." * baris, end="\n")
x = (baris // 2) - 1
y = 2
while x != 0:
    while y <= (baris - 2):
        print("." * x, end="")
        print("*" * y, end="")
        print("." * x, end="\n")
        x = x - 1
        y = y + 2
print("*" * baris)