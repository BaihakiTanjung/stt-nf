# tugas 1

# seq = [10, 20, 15, 75, 90, 65]
# max = 65  # elemen yang dicari
# imax = -1  # posisi elemen yang dicari

# for i in range(len(seq)):
#     if seq[i] == max:
#         imax = i
#         break

# if imax == -1:
#     print('hasil: max = ', max, 'tidak ada di posisi')
# else:
#     print('hasil: max = ', max, 'di posisi imax = ', imax)

# tugas 2

# hasil_akhir = [
#     {'nama': 'Reza', 'nilai': 70},
#     {'nama': 'Ciut', 'nilai': 63},
#     {'nama': 'Dian', 'nilai': 80},
#     {'nama': 'Badu', 'nilai': 40}
# ]


# def find_by_name(nama, hasil_akhir):
#     for i in hasil_akhir:
#         if i['nama'] == nama:
#             return i
#     return None


# print(find_by_name('Dian', hasil_akhir))

# tugas 3

# def binary_search_recursive(list, target, start, end):
#     if start > end:
#         return -1

#     mid = (start + end) // 2
#     if target == list[mid]:
#         return mid

#     if target < list[mid]:
#         return binary_search_recursive(list, target, start, mid-1)
#     else:
#         return binary_search_recursive(list, target, mid+1, end)


# target = 18
# list = [1, 2, 5, 7, 13, 15, 16, 18, 24, 28, 29]

# print("Searching for {}".format(target))
# print("Index of {} : {}".format(
#     target, binary_search_recursive(list, target, 0, len(list))))
