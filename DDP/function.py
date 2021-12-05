def getAverageWithCountLen(daftar_bilangan):
    count = len(daftar_bilangan)
    sum = 0
    
    if(count == 0):
        return 0

    for bilangan in daftar_bilangan:
        count += 1
        sum += bilangan

    return sum/count


def getAverage(daftar_bilangan):
    count = 0
    sum = 0
    for bilangan in daftar_bilangan:
        count += 1
        sum += bilangan
    if(count == 0):
        return 0
    return sum/count


daftar = [1000, 2, 3, 17, 50]
avg = getAverageWithCountLen(daftar)
print(f"Average value is {avg}")
