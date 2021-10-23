def tampilkan(nama, nilai):
    status = ""
    if nilai > 70:
        status = "Lulus"
    else:
        status = "Mengulang"

    print(f"siswa bernama {nama} memiliki nilai {nilai}, {status}")

tampilkan("Baihaki", 60)
