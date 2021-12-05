Aturan Penggajian :
1. Baca inputan nama pegawai
2. Baca status nikah pegawai (A)
3. Jika A = yes, maka Baca inputan jumlah anak pegawai (B). Jika A = no, maka skip ke langkah selanjutnya
4. Jika A = yes, maka Tunjangan Keluarga adalah 20% dari C. Jika A = no, maka tidak ada Tunjangan Keluarga
5. Jika B = 1, maka Tunjangan anak sebesar 10% dari C untuk tiap anak, hingga maksimal 2 anak. Jika B >= 3, Maka Tunjangan anak maksimal sebesar 20%.
6. Print Gaji Pokok (C) pegawai sebesar Rp 1.500.000,-
7. Print Tunjangan Keluarga (jika A = no, maka Print Rp 0)
8. Print Tunjangan Anak (Jika A = no atau B = 0, maka Print Rp 0)
9. Print Total Semua Gaji Pokok + Tunjangan Keluarga + Tunjangan Anak
10. Baca inputan Looping Program (D)
11. Jika D = yes, maka ulangi program dari langkah 1
12. Jika D = no, maka print "Terima Kasih"

def soal_1() :
    
    name = input("Masukkan Nama : ")
    mariage = input("Sudah Menikah (Y/T) : ")

    gapok = 1500000

    if mariage == "Y" or mariage == "y":
        anak = int(input("Jumlah Anak : "))
        tukel = gapok * (20 / 100)
        
        if anak > 2 :
            tunakpersen = 2 * (10/100)
        else :
            tunakpersen = anak * (10/100)
        

        tunak = tunakpersen * gapok

    else :
        tukel = 0
        tunak = 0
    
    
    jutol = gapok + tukel + tunak
    
    print(f'''
Detail Gaji {name} : 
Gaji Pokok    : {gapok}
Tunj Keluarga : {tukel}
Tunj Anak     : {tunak}
Jumlah Total  : {tunak} ''')
    
    question = input("Apakah mau lagi (Y/T) : ")
    
    if question == "Y" :
        soal_1()
    else :
        print("Terima kasih.")

soal_1()