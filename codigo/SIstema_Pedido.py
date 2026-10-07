class Produtos:
    # Construtor da classe: recebe os dados iniciais do produto.
    def __init__(self, nome, preco=0):
        # Atributos privados do produto.
        self.__nome = nome
        self.__preco = preco

    # Getter: permite acessar o nome que está armazenado no objeto.
    def get_nome(self):
        return self.__nome

    # Setter: permite alterar o nome que está armazenado no objeto -> para calcular o desconto,
    # não usarei o set para alterar preco base, apenas o get para mostrar o preço com desconto
    def set_nome(self, nome):
        self.__nome = nome

    def get_preco(self):
        return self.__preco

    def set_preco(self, preco):
        self.__preco = preco


    # Cada tipo de produto terá uma forma diferente de calcular o preço (Poliformismo).
    def CalcularPreco(self, desconto):
        return self.get_preco() - (self.get_preco() * desconto)


# ==========================================================================

# ProdutoEletronico herda os atributos e métodos da classe Produtos.
class ProdutoEletronico(Produtos):

    # O construtor recebe nome e preço e passa esses dados
    # para o construtor da classe Produtos.
    def __init__(self, nome, preco=0):
        Produtos.__init__(self, nome, preco)


    # Sobrescreve o metodo CalcularPreco() da classe Produtos.
    # Aqui o produto eletrônico recebe 10% de desconto.
    def CalcularPreco(self):
        desconto = 0.10
        return Produtos.CalcularPreco(self, desconto)


# ==========================================================================

class ProdutoRoupa(Produtos):

    def __init__(self, nome, preco=0):
        Produtos.__init__(self, nome, preco)


    def CalcularPreco(self):
        desconto = 0.20
        return Produtos.CalcularPreco(self, desconto)


# ==========================================================================

class ProdutoLivro(Produtos):

    def __init__(self, nome, preco=0):
        Produtos.__init__(self, nome, preco)

    def CalcularPreco(self):
        desconto = 0.05
        return Produtos.CalcularPreco(self, desconto)