class Veiculo:
    def __init__ (self, modelo, marca, ano, velocidade_atual=0):
        # self representa um objeto em particular (cada objeto da class)
        self.__modelo = modelo
        self.__marca = marca
        self.__ano = ano
        self.__velocidade_atual = velocidade_atual
        self.__ligado = False

    def get_modelo(self):
        return self.__modelo
    def set_modelo(self, modelo):
        self.__modelo = modelo

    def get_marca(self):
        return self.__marca
    def set_marca(self, marca):
        self.__marca = marca

    def get_ano(self):
        return self.__ano
    def set_ano(self, ano):
        self.__ano = ano

    def get_velocidade_atual(self):
        return self.__velocidade_atual
    def set_velocidade_atual(self, velocidade_atual):
        self.__velocidade_atual = velocidade_atual

    def get_ligado(self):
        return self.__ligado
    def set_ligado(self, ligado):
        self.__ligado = ligado





    def acelerar(self, quantidade):
        self.set_velocidade_atual(
            self.get_velocidade_atual() + quantidade)


    def frear(self, quantidade):
        if quantidade <= self.get_velocidade_atual():
            self.set_velocidade_atual(
                self.get_velocidade_atual() - quantidade)
        else:
            self.set_velocidade_atual(0)


    def ligar(self):
        # Liga o veículo somente se ele estiver desligado
        if not self.get_ligado():
            self.set_ligado(True)


    def desligar(self):
        # Desliga o veículo somente se ele estiver ligado
        if self.get_ligado:
            self.set_ligado(False)

            # Ao desligar, a velocidade também volta para zero
            self.set_velocidade_atual(0)

    def velocidade_alta(self, velocidade_permitida):
        if self.get_velocidade_atual() > velocidade_permitida:
            print("Velocidade acima do limite permitido")
        else:
            print("Velocidade abaixo do limite permitido")

    def exibir_dados(self):
        return (
            f"--- DADOS DO VEÍCULO ---\n"
            f"Modelo: {self.get_modelo()}\n"
            f"Marca: {self.get_marca()}\n"
            f"Velocidade atual: {self.get_velocidade_atual()} km/h"
        )


# # o de letra minuscula representa o objeto, o maiuscula representa a class (já com seus componentes)
# meu_carro = Veiculo("Civic", "Honda", 20)
# meu_carro.acelerar(int(input("Digite quanto o carro irá acelerar: "))) #acelerar recebe 20 como parametro para quantidade (quantidade é 20)
# meu_carro.frear(int(input("Digite quanto o carro irá frear: ")))
# meu_carro.velocidade_alta(60)
# print(meu_carro.exibir_dados())
