# Union
set1 = {1, 2, 3, 4, 5}
set2 = {2, 4, 6}
set3 = set1.union(set2)
# print(set3)

# update
set1 = {1, 2, 3}
set2 = {2, 4, 6}
set3 = set2.update(set1)
# print(set3)


# Dictonary
data_diri = {
    "nama": "Rizki",
    "matpel": "DDP",
}

data_diri["semester"] = 1
print(data_diri["semester"])

# akses dengan key
x = data_diri.get("nama")

# mengubah value
data_diri["nama"] = "Rizki"

# menambah entri
data_diri["alamat"] = "Jl. Kebon Kacang"

# menghapus key 
data_diri.pop("semester")

# mengecek keberadaan key
if "semester" in data_diri:
    print("ada")
