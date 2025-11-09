# komentar / pagar (#
# tipe data yang tidak akan pernah dieksekusi sama program
# digunakan untuk menandai atau mematikan tulisan dalam coding sementara

# tipe data numeric
# integer
a = 10
print("Contoh tipe data integer: {0}".format(a))
b = 3.14
print("Contoh tipe data float: {0}".format(b))
c = 2 + 3j # j bilangan imajiner
print("Contoh tipe data complex (complex): {0}".format(c))

# tipe sequence
# list
d = [1,2,3,4,5,6,7,8]
print("Contoh tipe data list (list): {0}".format(d))
# truplet
e = (4,5,6)
print("Contoh tipe data truplet (list): {0}".format(e))
# range
f = range(1,5)
print("Contoh tipe data range (range): {0}".format(f))

# type String
nama_lengkap = "Clara Desratinola"
print("Contoh tipe data string (str): {0}".format(nama_lengkap))

# type maping
profile = {
    "nama" : "Clara Desratinola",
    "usia" : 17,
}
print("Contoh tipe data maping (dict): {0}".format(profile))

# type set
g = {1,2,3}
print("Contoh tipe data set (set): {0}".format(g))
h = frozenset ({4,5,6,7})
print("Contoh tipe data frozenset (frozenset): {0}".format(h))

# type boolean
# cuma bisa diisi salah satu True (1) or False (0)
kondisi_badan = True
print("Contoh tipe data boolean (bol): {0}".format(kondisi_badan))

# type Binary
i = 0b01000001
desimal = int(i)
char = chr(desimal)
print(char)
j = bytearray (d)
print (j)
k = memoryview (j)
print (k)