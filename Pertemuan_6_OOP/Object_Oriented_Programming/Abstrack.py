# Case
# Mobil

from abc import ABC, abstractclassmethod

class Mobil(ABC) : 
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

    @abstractclassmethod
    def klaksonMobil(self):
         pass # abstract
    
class Mitsubisi(Mobil):
     def __init__(self,merek, jenis, warna):
          super().__init__(merek, jenis, warna)
    
     def kenalpot(self):
          print("Jumlah Kenalpot : 4 silinder")

     def klaksonMobil(self): # overrider method menulis ulang method abstract agar untuk masing-masing class
          print("Tuuuttt")

lancer = Mitsubisi("Mitsubisi","Lancer","Hitam") 
lancer.getProfile() 
lancer.kenalpot()
lancer.klaksonMobil()