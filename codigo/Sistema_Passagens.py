class Voo:

    # Construtor da classe Voo.
    # Recebe os dados que são comuns a todos os tipos de voo.
    def __init__(self, origem, distancia, destino, data_voo):
        self.__origem = origem
        self.__distancia = distancia
        self.__destino = destino
        self.__data_voo = data_voo

    # Getter: permite acessar a origem do voo.
    def get_origem(self):
        return self.__origem

    # Setter: permite alterar a origem do voo.
    def set_origem(self, origem):
        self.__origem = origem

    def get_distancia(self):
        return self.__distancia

    def set_distancia(self, distancia):
        self.__distancia = distancia

    def get_destino(self):
        return self.__destino

    def set_destino(self, destino):
        self.__destino = destino

    def get_data_voo(self):
        return self.__data_voo

    def set_data_voo(self, data_voo):
        self.__data_voo = data_voo

    # Metodo que será sobrescrito pelas classes filhas.
    # Cada tipo de voo terá sua própria forma de calcular o preço.
    def calcular_preco(self):
        return

    # Exibe os dados que são comuns a todos os tipos de voo.
    # O calcular_preco() será chamado de acordo com o tipo do objeto.
    def exibir_dados(self):
        return (
            f'Origem: {self.get_origem()}\n'
            f'Destino: {self.get_destino()}\n'
            f'Distância: {self.get_distancia()}\n'
            f'Data do voo: {self.get_data_voo()}\n'
            f'Preço: {self.calcular_preco()}\n'
        )


# ==========================================================================
# VooDomestico herda os atributos e métodos da classe Voo.
class VooDomestico(Voo):

    # Recebe os dados do voo doméstico e também o fator utilizado para calcular o preço.
    def __init__(self, origem, distancia, destino, data_voo, fator):

        # Chama o construtor da classe Voo para inicializar os atributos que são comuns aos dois tipos de voo.
        Voo.__init__(self, origem, distancia, destino, data_voo)

        self.__fator = fator

    def get_fator(self):
        return self.__fator

    def set_fator(self, fator):
        self.__fator = fator

    # Sobrescreve o metodo calcular_preco() da classe Voo.
    # O preço doméstico é calculado pela distância multiplicada pelo fator.
    def calcular_preco(self):
        return self.get_distancia() * self.get_fator()


# ==========================================================================

# VooInternacional herda os atributos e métodos da classe Voo.
class VooInternacional(Voo):

    # Além dos dados comuns, recebe o fator e a taxa de conversão.
    def __init__(self, origem, distancia, destino, data_voo, fator, taxa_conersao):

        # Chama o construtor da classe Voo para inicializar
        # origem, distância, destino e data do voo.
        Voo.__init__(self, origem, distancia, destino, data_voo)

        self.__fator = fator
        self.__taxa_conersao = taxa_conersao

    def get_fator(self):
        return self.__fator

    def set_fator(self, fator):
        self.__fator = fator

    def get_taxa_conersao(self):
        return self.__taxa_conersao

    def set_taxa_conersao(self, taxa_conersao):
        self.__taxa_conersao = taxa_conersao

    # Sobrescreve o metodo calcular_preco() da classe Voo.
    # Primeiro calcula o preço pela distância e pelo fator.
    # Depois aplica a taxa de conversão.
    def calcular_preco(self):
        preco = self.get_distancia() * self.get_fator()
        return preco * self.get_taxa_conersao()


# duvidas -> Pq n usar o set para os calculos e so o get? Como fica o def exibir dados, como ele sabe qual estou chamando?
