import math


# ===============================================================
# Classe base
#
# FormaGeometrica será a classe pai de Circulo e Retangulo.
# Ela possui os métodos que as classes filhas deverão implementar.
# ===============================================================

class FormaGeometrica:

    def __init__(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome
    def set_nome(self, nome):
        self.__nome = nome

    # Este metodo existe na classe pai, mas cada classe filha rá fazer o cálculo da sua própria maneira
    def calcular_area(self):
        return

    def calcular_perimetro(self):
        return


    # Ele usa os métodos calcular_area() e calcular_perimetro(),
    # que serão implementados de forma diferente em cada filha.
    def exibir_dados(self):
        return (
            f"Nome: {self.get_nome()}\n"
            f"Área: {self.calcular_area()}\n"
            f"Perímetro: {self.calcular_perimetro()}\n"
        )

# ===============================================================
# Círculo
#
# Circulo herda de FormaGeometrica.
# ===============================================================

class Circulo(FormaGeometrica):

    def __init__(self, nome, raio):

        # Inicializa o atributo nome da classe FormaGeometrica.
        FormaGeometrica.__init__(self, nome)

        # Atributo específico do círculo.
        self.__raio = raio

    def get_raio(self):
        return self.__raio
    def set_raio(self, raio):
        self.__raio = raio

    # Sobrescreve o metodo calcular_area() da classe pai.
    # Aqui o cálculo é específico do círculo.
    def calcular_area(self):
        return math.pi * (self.__raio ** 2)

    # Sobrescreve o metodo calcular_perimetro() da classe pai.
    def calcular_perimetro(self):
        return 2 * math.pi * self.__raio



# ===============================================================
# Retângulo
#
# Retangulo também herda de FormaGeometrica.
# Possui largura e altura como atributos próprios.
# ===============================================================

class Retangulo(FormaGeometrica):

    def __init__(self, nome, largura, altura):

        # Inicializa o atributo nome da classe FormaGeometrica.
        FormaGeometrica.__init__(self, nome)

        self.__largura = largura
        self.__altura = altura

    def get_largura(self):
        return self.__largura
    def set_largura(self, largura):
        self.__largura = largura

    def get_altura(self):
        return self.__altura
    def set_altura(self, altura):
        self.__altura = altura


    def calcular_area(self):
        return self.__largura * self.__altura


    def calcular_perimetro(self):
        return 2 * (self.__largura + self.__altura)

