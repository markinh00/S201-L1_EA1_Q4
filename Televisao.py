class Televisao:
    def __init__(self, modelo: str):
        self.modelo = modelo
        self.__volume = 0
        self.__canal = ""

    def aumentar_volume(self, valor: float):
        self.__volume += valor

    def diminuir_volume(self, valor: float):
        self.__volume -= valor

    def trocar_canal(self, canal: str):
        self.__canal = canal

    def mostrar_info(self):
        print(f"Modelo: {self.modelo}")
        print(f"Volume: {self.__volume}")
        print(f"Canal atual: {self.__canal}")
