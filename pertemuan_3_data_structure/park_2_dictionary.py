# case
# kelas
data_kelas = {
    "kelas" : 12,
    "jurusan" : ["IPA", "IPS"], # ini tipe datanya list
    "nama_ketua" : "Udin"
}

# Read
print(f"List Dictionary:{data_kelas}")
# read specific
print(f"Nama dari ketua kelas : {data_kelas["nama_ketua"]}")
print(f"Cara mengambil jurusan IPS : {data_kelas["jurusan"][1]}")

# add value
data_kelas["jumlah_siswa"] = 40
print(f"List Dictionary setelah di add : {data_kelas}")
# update
data_kelas["jurusan"] = "IPS"
print(f"List Dictionary setelah di add : {data_kelas}")
# delete
del data_kelas["jumlah_siswa"]
print(f"List Dictionary setelah di delete : {data_kelas}")

