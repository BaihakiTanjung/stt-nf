
print(("======Program mencari akar persamaan kuadrat======="))


a = int(input("Masukkan bilangan a (tidak boleh bernilai 0): "))
b = int(input("Masukkan bilangan b: "))
c = int(input("Masukkan bilangan c: "))


def persamaanKuadrat(a, b, c):
    # variabel d adalah deskriminan
    # d = deskriminan

    d = (b*b) - 4*a*c
    print(f"Deskriminan = {d}")
    if d > 0:
        x1 = (-b + (d**2)) / (2*a)
        x2 = (-b - (d**2)) / (2*a)
        print(f"Deskriminan positif, maka memiliki dua akar namun berbeda")
        print(f"x1 = {int(x1)}")
        print(f"x2 = {int(x2)}")
    elif d == 0:
        x1 = x2 = (-b + (d**2)) / (2*a)
        print(f"Hanya memiliki asatu akar tunggal, yaitu x1 = x2 = {int(x1)}")
    else:
        print("Akar tidak real atau imajier")


persamaanKuadrat(a, b, c)
