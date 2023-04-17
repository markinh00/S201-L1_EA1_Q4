from Televisao import Televisao
from SmartTV import SmartTV


tv = Televisao("LG")
smarttv = SmartTV("Samsung")

tv.aumentar_volume(70)
tv.diminuir_volume(27)
tv.trocar_canal("Canal #1")
tv.mostrar_info()
print("---------------------------")
smarttv.aumentar_volume(100)
smarttv.diminuir_volume(41)
smarttv.trocar_canal("Canal #6")
smarttv.conectar_internet("boa")
smarttv.mostrar_info()
