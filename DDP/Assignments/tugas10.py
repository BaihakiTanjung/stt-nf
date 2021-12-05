# Tugas 1
hasil_akhir = [
    {'nama': 'Reza', 'nilai': 70},
    {'nama': 'Ciut', 'nilai': 63},
    {'nama': 'Dian', 'nilai': 80},
    {'nama': 'Badu', 'nilai': 40},
]


def GraduatedStudents(hasil_akhir):
    array = []
    for i in hasil_akhir:
        if i['nilai'] > 65:
            array.append(i['nama'])

    print(array)

# GraduatedStudents(hasil_akhir)


# Tugas 2
fruits = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']


def reversed(a_list):
    new = a_list[::-1]
    print(new)


# reversed(fruits)

# Tugas 3
array = []


def duplicate(a_list):
    for item in a_list:
        for i in range(2):
            array.append(item)
    print(array)


# duplicate(fruits)

# Tugas 4
name = "Nurul Fikri"
consonant = ['a', 'i', 'u', 'e', 'o']


def removeConsonant(name):
    for i in name:
        if i in consonant:
            name = name.replace(i, '')
        name = name.replace(" ", '')
    print(name)


removeConsonant(name)
