# jenis-jenis makanan

# C (Create)
# instansiasi
# instansiasi adalah proses persiapan variabel yang akan dipakai
type_data = []

# CRUD
# add
type_data.append("nasi") # ini di akhir data
type_data.append("ikan")
type_data.append("ayam bakar")
type_data.append("semangka")
type_data.insert(1, "jagung") # awal data # insert(mau_diselipkan_ke_berapa,valuenya_berapa)

# Read
print(f"All list Data :{type_data}")
# read specific value
print(f"index ke 2 : {type_data[2]}")

# Update
type_data[4] = "Tomat"
print(f"All list Data  update index ke 4:{type_data}")

# Delete
del type_data[2]
print(f"All list Data delete index ke 2:{type_data}")


