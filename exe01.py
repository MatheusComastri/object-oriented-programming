class Veiculo:
    def __init__ (self, modelo, marca, velocidade_atual=0):
        # self representa um objeto em particular (cada objeto da class)
        self.modelo = modelo
        self.marca = marca
        self.velocidade_atual = velocidade_atual


    def acelerar(self, quantidade):
        self.velocidade_atual += quantidade #pq eu preciso enviar utilizando o self. quando eu estou usando um valor que eu já defini



    def frear(self, quantidade):
        if quantidade <= self.velocidade_atual:
            self.velocidade_atual -= quantidade
        else:
            self.velocidade_atual = 0


    def velocidade_alta(self, velocidade_permitida):
        if self.velocidade_atual > velocidade_permitida:
            print("Velocidade acima do limite permitido")
        else:
            print("Velocidade a baixo do limite permitido")

    def exibir_dados(self):
        return (
            f"--- DADOS DO VEÍCULO ---\n"
            f"Modelo: {self.modelo}\n"
            f"Marca: {self.marca}\n"
            f"Velocidade atual: {self.velocidade_atual} km/h"
        )


# o de letra minuscula representa o objeto, o maiuscula representa a class (já com seus componentes)
meu_carro = Veiculo("Civic", "Honda", 20)
meu_carro.acelerar(int(input("Digite quanto o carro irá acelerar: "))) #acelerar recebe 20 como parametro para quantidade (quantidade é 20)
meu_carro.frear(int(input("Digite quanto o carro irá frear: ")))
meu_carro.velocidade_alta(60)
print(meu_carro.exibir_dados())
