from Televisao import Televisao


class SmartTV(Televisao):
    def __init__(self, modelo):
        super().__init__(modelo)
        self.__internet = ""

    def conectar_internet(self, internet: str):
        self.__internet = internet

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Internet: {self.__internet}")
