class Produtos:

    # Construtor da classe Produtos.
    def __init__(self, nome, preco_unitario, quantidade_estoque, quantidade_vendida):
        self.__nome = nome
        self.__preco_unitario = preco_unitario
        self.__quantidade_estoque = quantidade_estoque
        self.__quantidade_vendida = quantidade_vendida

    # Getter: permite acessar o nome do produto.
    def get_nome(self):
        return self.__nome

    # Setter: permite alterar o nome do produto.
    def set_nome(self, nome):
        self.__nome = nome


    def get_preco_unitario(self):
        return self.__preco_unitario
    def set_preco_unitario(self, preco_unitario):
        self.__preco_unitario = preco_unitario

    def get_quantidade_estoque(self):
        return self.__quantidade_estoque
    def set_quantidade_estoque(self, quantidade_estoque):
        self.__quantidade_estoque = quantidade_estoque

    def get_quantidade_vendida(self):
        return self.__quantidade_vendida
    def set_quantidade_vendida(self, quantidade_vendida):
        self.__quantidade_vendida = quantidade_vendida

    def calcular_preco(self):
        return

    # Realiza a venda somente se houver estoque suficiente.
    def vender(self, quantidade):

        # Verifica se a quantidade solicitada está disponível no estoque.
        if quantidade <= self.get_quantidade_estoque():

            # Diminui do estoque a quantidade que foi vendida.
            self.set_quantidade_estoque(
                self.get_quantidade_estoque() - quantidade
            )

            # Registra a quantidade vendida.
            self.set_quantidade_vendida(quantidade)

            # True indica que a venda foi realizada.
            return True

        # False indica que não havia estoque suficiente.
        return False

    def exibir_dados(self):
        return (
            f'Nome: {self.get_nome()}\n'
            f'Preço unitário: {self.get_preco_unitario()}\n'
            f'Quantidade em estoque: {self.get_quantidade_estoque()}\n'
            f'Quantidade vendida: {self.get_quantidade_vendida()}\n'
            f'Preço total: {self.calcular_preco()}\n'
        )

# ==========================================================================
class ProdutoEletronico:

    def __init__(self, nome, preco_unitario, quantidade_estoque, quantidade_vendida):
        Produtos.__init__(
            self,
            nome,
            preco_unitario,
            quantidade_estoque,
            quantidade_vendida
        )

    # Sobrescreve o metodo calcular_preco() da classe Produtos.
    # O preço total é o preço unitário multiplicado pela quantidade vendida.
    def calcular_preco(self):
        return self.get_preco_unitario() * self.get_quantidade_vendida()


# ==========================================================================
class ProdutoRoupa(Produtos):

    def __init__(self, nome, preco_unitario, quantidade_estoque, quantidade_vendida):
        # Chama o construtor da classe Produtos para inicializar
        # os atributos que são comuns aos produtos.
        Produtos.__init__(
            self,
            nome,
            preco_unitario,
            quantidade_estoque,
            quantidade_vendida
        )

    # Se forem vendidas mais de 5 unidades, aplica 20% de desconto.
    def calcular_preco(self):

        # 0.80 representa os 80% restantes depois do desconto de 20%.
        if self.get_quantidade_vendida() > 5:
            return (self.get_preco_unitario() * self.get_quantidade_vendida()) * 0.80

        # Se forem 5 unidades ou menos, não existe desconto.
        else:
            return self.get_preco_unitario() * self.get_quantidade_vendida()


# ==========================================================================
class ProdutoAlimento(Produtos):

    def __init__(self, nome, preco_unitario, quantidade_estoque, quantidade_vendida):
        Produtos.__init__(
            self,
            nome,
            preco_unitario,
            quantidade_estoque,
            quantidade_vendida
        )

    # O preço total é o preço por quilo multiplicado pela quantidade vendida.
    def calcular_preco(self):
        return self.get_preco_unitario() * self.get_quantidade_vendida()