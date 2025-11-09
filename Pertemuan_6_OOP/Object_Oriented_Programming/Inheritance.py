# Case
# Mobil

class Mobil : 
    warna = "Putih"
    _pelek_ban = "T37" 
    __logo_mobil = "Mitsubisi" 

    def __init__(self,merek, jenis, warna):
         self.warna = warna
         self.merek = merek
         self.jenis = jenis

    def getProfile(self): 
          print(f"merek : {self.merek}")
          print(f"warna : {self.warna}")
          print(f"jenis: {self.jenis}")
          print(f"pelek : {self._pelek_ban}")
          print(f"logo Mobil : {self.__logo_mobil}")

    def setPelek(self,nama_pelek):
         self._pelek_ban = nama_pelek

class Mitsubisi(Mobil): # inheritance
     def __init__(self,merek, jenis, warna):
          super().__init__(merek, jenis, warna)

    # self itu artinya dia menggunakan object yang ada pada semua kelas
    
     def kenalpot(self):
          print("Jumlah Kenalpot : 4 silinder")

lancer = Mitsubisi("Mitsubisi","Lancer","Hitam") 
lancer.getProfile() # ini tidak ada pada class nya tapi ada pada kelas atasnya
print(f"====================")
lancer.setPelek("Lancer Ring")
lancer.getProfile()
lancer.kenalpot()