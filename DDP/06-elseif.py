nilai = int(input("Masukkan nilai :"))
grade = ""
if(nilai < 60):
    grade = "F"
elif(nilai < 70):
    grade = "D"
elif(nilai < 80):
    grade = "C"
elif(nilai < 90):
    grade = "B"
else:
    grade = "A"

print("grade = %s" % grade)
