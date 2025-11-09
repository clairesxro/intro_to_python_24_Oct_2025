kondisi_1 = 10
kondisi_2 = 12

# lebih besar
hasil_kondisi = (kondisi_1 > kondisi_2)
print(f"Apakah nilai {kondisi_1} lebih besar (>) dari {kondisi_2} adalah {hasil_kondisi}")

# lebih kecil
hasil_kondisi = (kondisi_1 < kondisi_2)
print(f"Apakah nilai {kondisi_1} lebih kecil (<) dari {kondisi_2} adalah {hasil_kondisi}")

kondisi_1 = 12
kondisi_2 = 12

# besar dari
hasil_kondisi = (kondisi_1 >= kondisi_2)
print(f"Apakah nilai {kondisi_1} lebih besar sama dengan (>=) dari {kondisi_2} adalah {hasil_kondisi}")

# kecil dari
kondisi_1 = 12
kondisi_2 = 12

# lebih besar
hasil_kondisi = (kondisi_1 <= kondisi_2)
print(f"Apakah nilai {kondisi_1} lebih kecil sama dengan (<=) dari {kondisi_2} adalah {hasil_kondisi}")

# gerbang logika
# and
# dipakai saat punya 2 atau lrbih kondisi
hasil_kondisi = (kondisi_1 <= kondisi_2) and (kondisi_1 < kondisi_2)
print(f"Apakah kondisi pertama dan ke dua benar : {hasil_kondisi}")
# or
# salah satu kondisi bernilai benar baru akan dijalankan
hasil_kondisi = (kondisi_1 <= kondisi_2) or (kondisi_1 < kondisi_2)
print(f"Apakah kondisi pertama dan ke dua benar : {hasil_kondisi}")

kondisi_1 = "Hasil"
kondisi_2 = "hasil"
hasil_kondisi = (kondisi_1 == kondisi_2)
print(f"Apakah nilai {kondisi_1} sama dengan (==) {kondisi_2} adalah {hasil_kondisi}")

# logika not (!=)
kondisi_1 = True
hasil_kondisi = kondisi_1 != True
print(f"Apakah nilai {kondisi_1} tidak ssama dengan (!=) {True} adalah {hasil_kondisi}")




