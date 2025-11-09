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
        "nama_lengkap" : "Siska",
        "divisi" : "Programmer" 
    },
    {
        "nama_lengkap" : "Jono",
        "divisi" : "Product Manager"
     },
]

# format dasar fungsi
# def namaFunction{parameter}:
# Kegiatan apa yang mau kamu lakukan

# function void
# function yang tidak mengeluarkan apa pun hasilnya
def cetak_profile(nama,divisi):
    print(f"Nama : {nama}")
    print(f"divisi : {divisi}")
    print(f"============")

print(f"=====List Divisi=====")
cetak_profile(data_karyawan [0]["nama_lengkap"],data_karyawan [0]["divisi"])
cetak_profile(data_karyawan [1]["nama_lengkap"],data_karyawan [1]["divisi"])
cetak_profile(data_karyawan [2]["nama_lengkap"],data_karyawan [2]["divisi"])
cetak_profile(data_karyawan [3]["nama_lengkap"],data_karyawan [3]["divisi"])
cetak_profile(data_karyawan [4]["nama_lengkap"],data_karyawan [4]["divisi"])

# function non void
def luas_persegi_panjang(panjang,lebar):
    hasil = panjang * lebar
    return hasil #ini yang disebutnya mengeluarkan nilai


hasil_penjumlahan_luas_persegi = luas_persegi_panjang(2,5)
print(f"Luas dari persegi dengan lebar 2 dan panjang 5 adalah {hasil_penjumlahan_luas_persegi}")