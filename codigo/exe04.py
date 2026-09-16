class Pessoa:
    def __init__(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso

    def envelhecer(self):
        self.idade += 1
        print(f"Parabéns, agora você tem {self.idade} anos.")

    def crescer(self):
        if self.idade <= 21:
            self.altura += 1
            print(f"Sua altura aumentou para {self.altura}cm")

    def ganhar_peso(self, quilos):
        self.peso += quilos
        print(f"Você ganhou {quilos}kg e agora está pesando {self.peso}kg")

    def perder_peso(self, quilos):
        self.peso -= quilos
        print(f"Você perdeu {quilos}kg e agora está pesando {self.peso}kg")

    def imc(self):
        imc =  self.peso / ((self.altura/100) ** 2)
        if imc < 18.5:
            print("O seu peso está menor do que o consideráel saudável")
        elif imc >= 18.5 and imc <= 24.9:
            print("O seu peso está ideal")
        elif imc >= 25 and imc <= 29.9:
            print("Você está com sobrepeso")
        elif imc >= 30 and imc <= 34.9:
            print("Excesso de peso, requer ateção")
        elif imc >= 35 and imc <= 39.9:
            print("Obesidade moderada e severa")
        elif imc >= 40:
            print("Você está obeso")

    def exibir_dados(self):
        return (
            f"--- DADOS DA PESSOA ---\n"
            f"Nome: {self.nome}\n"
            f"Idade: {self.idade} anos\n"
            f"Altura: {self.altura} cm\n"
            f"Peso: {self.peso} kg\n"
            f"------------------------"
        )

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura em centimentos: "))
peso = float(input("Digite seu peso em quilogramas: "))


pessoa = Pessoa(
    nome=nome,
    idade=idade,
    altura=altura,
    peso=peso)

pessoa.envelhecer()
pessoa.crescer()
pessoa.ganhar_peso(5)
pessoa.perder_peso(1)
pessoa.imc()

print(pessoa.exibir_dados())
