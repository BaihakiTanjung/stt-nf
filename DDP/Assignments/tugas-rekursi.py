# Tugas 1
# faktorial
# recursive
# def faktorial_recursive(x):
#     hasil = 1
#     for i in range(2, x + 1):
#         hasil *= i
#     return hasil


# print(faktorial_recursive(10))


# iterasi
# def faktorial_iterasi(n):
#     if n == 0:
#         return 1
#     else:
#         return n * faktorial_iterasi(n-1)


# print(faktorial_iterasi(10))

# tugas 2
# recursive
# def fibonacci (n):
#     if n < 1:
#       return [n]
#     return fibonacci(n - 1) + [n]

# print(fibonacci(5))


# iterasi
# def fibonacci_iterasi(n):
#     fib = [0, 1]
#     for i in range(2, n):
#         fib.append(fib[i-1] + fib[i-2])
#     return fib

# print(fibonacci_iterasi(10))

# tugas 3

def jumlah(n):
    if n == 0:
        return 0
    else:
        return n + jumlah(n-1)


print(jumlah(5))

# tugas 4


def jumlah(n):
    if n == 0:
        return 0
    else:
        return n + jumlah(n-1)


print(jumlah(6))
