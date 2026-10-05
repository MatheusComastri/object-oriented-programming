class Veiculo:
    def __init__(self, marca, modelo, preco):
        self.__marca = marca
        self.__modelo = modelo
        self.__preco = preco

    def get_marca(self):
        return self.__marca
    def set_marca(self, marca):
        self.__marca = marca

    def get_modelo(self):
        return self.__modelo
    def set_modelo(self, modelo):
        self.__modelo = modelo

    def get_preco(self):
        return self.__preco
    def set_preco(self, preco):
        self.__preco = preco


    def calcular_custo(self):
        return

