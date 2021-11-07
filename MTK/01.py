def soal_3() :
    temp = 1
    for i in range(4, 9) :
        temp *= i - 3

    print(temp)

def soal_2() :
    temp = 0

    for i in range(5, 11) :
        npangkat = i * i
        temp += npangkat + (2 * i) - 1
    print(temp)

def soal_1() :
    temp = 0
    for i in range(13, 18) :
        temp += (5 * i) + 2
    print(temp)

soal_1()
soal_2()
soal_3()