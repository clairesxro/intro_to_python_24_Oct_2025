# Case 
# mobil

class Mobil :  # Mobil disebut name class dan ini contoh class
    # property public
    # object yang mudah diganti dan boleh diganti oleh siapapun
    warna = "Putih" # warna disebut object
    # property private
    # object yang tidak mudah diganti tetapi diperbolehkan
    _pelek_ban = "T37"
    # property protected
    # object yang tidak bisa diubah di luar kelas tersebut
    __logo_mobil = "Mitsubisi"

    def __init__(self,merek, jenis, warna):
         self.warna = warna
         self.merek = merek
         self.jenis = jenis

    def getProfile(self): # ini sebutannya method
          print(f"merek : {self.merek}")
          print(f"warna : {self.warna}")
          print(f"jenis: {self.jenis}")
          print(f"pelek : {self._pelek_ban}")
          print(f"logo Mobil : {self.__logo_mobil}")



honda = Mobil("Honda","Civic","Hitam") 
honda.getProfile()
print(f"====================")
# contoh perubah object
honda.merek = "Mitsubisi" # di sini merubah objectnya
honda.jenis = "Lancer"
honda.getProfile()
