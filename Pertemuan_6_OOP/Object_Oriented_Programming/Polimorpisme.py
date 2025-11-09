# Case
# Mobil

class Mobil() : 
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

    def klaksonMobil(self):
         pass 
    
class Mitsubisi(Mobil):
     def __init__(self,merek, jenis, warna):
          super().__init__(merek, jenis, warna)
    
     def kenalpot(self):
          print("Jumlah Kenalpot : 4 silinder")

     def klaksonMobil(self): 
          print("Tuuuttt")

class Honda(Mobil):
     def __init__(self,merek, jenis, warna):
          super().__init__(merek, jenis, warna)
    
     def kenalpot(self):
          print("Jumlah Kenalpot : 2 silinder")

     def klaksonMobil(self): 
          print("Teeeettttt")

class Toyota(Mobil):
     def __init__(self,merek, jenis, warna):
          super().__init__(merek, jenis, warna)
    
     def kenalpot(self):
          print("Jumlah Kenalpot : 1 silinder")

     def klaksonMobil(self): 
          print("Pakai Strobo")

def getKlakson(Mobil): #polymorpisme
     Mobil.klaksonMobil()

lancer = Mitsubisi("Mitsubisi","Lancer","Hitam") 
getKlakson(lancer)
civic = Honda("Honda","Civic","Hitam")
getKlakson(civic)
toyota = Toyota("Toyota","Avanza","Hitam")
getKlakson(toyota)