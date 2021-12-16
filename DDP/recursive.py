# def jumlah(n):
#     hasil = 0
#     if n <= 0:
#         hasil = 0
#     else:
#         hasil = n + jumlah(n-1)

#     print("n = %d" % n)
#     print("hasil = %d" % hasil)
#     return hasil


# print(jumlah(5))


hasil = {}


def fib(n):
    if n < 1:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    result = fib(n-1) + fib(n-2)
    return result


for i in range(1, 10):
    print(fib(i))
