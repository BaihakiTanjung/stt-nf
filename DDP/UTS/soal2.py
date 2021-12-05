daftar_pegawai = [
    {"nama": "Budi", "gaji": 1500000},
    {"nama": "Cici", "gaji": 2000000}
]

print("|","Nama","|","Gaji","  ","|")
for i in range(len(daftar_pegawai)):
    print("|",daftar_pegawai[i]["nama"],"|",daftar_pegawai[i]["gaji"],"|")