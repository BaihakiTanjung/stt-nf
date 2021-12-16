# tugas 1
hasil_akhir = [
    {'nama': 'Reza', 'nilai': 70},
    {'nama': 'Ciut', 'nilai': 63},
    {'nama': 'Dian', 'nilai': 80},
    {'nama': 'Badu', 'nilai': 40}
]


def find_by_name(nama, hasil_akhir):
    for i in hasil_akhir:
        if i['nama'] == nama:
            return i
    return None


print(find_by_name('Dian', hasil_akhir))


# tugas 2