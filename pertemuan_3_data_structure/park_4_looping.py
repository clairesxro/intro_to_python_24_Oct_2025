# for
print("=====for range=====")
for index in range(1,5+1):
    print(f"{index},Tidak akan mengulang kesalahan kembali")



data_karyawan =[
    { 
        "nama_lengkap" : "Udin",
        "divisi" : "Programmer"
    },
    {   
        "nama_lengkap" : "Tono",
        "divisi" : "Programmer"
    },
    {
        "nama_lengkap" : "Toni",
        "divisi" : "Programmer"
    },
    {
        "nama_lengkap" : "Siti",
        "divisi" : "Programmer"
    },
    {
        "nama_lengkap" : "Siska",
        "divisi" : "Programmer" 
    },
    {
        "nama_lengkap" : "Jono",
        "divisi" : "Product Manager"
     },
]

def cetak_profile(nama,divisi):
    print(f"Nama : {nama}")
    print(f"divisi : {divisi}")
    print(f"============")

print("=====foreach=====")
for value in data_karyawan:
    cetak_profile(value["nama_lengkap"],value["divisi"])



print("=====while=====")
# kondisi akan dilihat terlebih dahulu dan memahami syarat yang diberikan 
count = 0
while count < 5:
    print("ini akan muncul terus menerus")
    count += 1

print("=====break and continue=====")
count = 0
while count <= 100:
    if count % 2 == 0:
        count += 1
        continue # digunakan untuk melakukan skip (melewati) 1 putaran
    print(count)
    count += 1
    if count == 30:
        break # memaksa untuk memberhentikan putaran