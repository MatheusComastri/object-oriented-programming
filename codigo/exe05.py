class Produto:
    def __init__(self, nome, preco, quantidade_estoque, categoria):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade_estoque = quantidade_estoque
        self.__categoria = categoria


    def get_nome(self):
        return self.__nome
    def set_nome(self, nome):
        self.__nome = nome

    def get_preco(self):
        return self.__preco
    def set_preco(self, preco):
        self.__preco = preco

    def get_quantidade_estoque(self):
        return self.__quantidade_estoque
    def set_quantidade_estoque(self, quantidade_estoque):
        self.__quantidade_estoque = quantidade_estoque

    def get_categoria(self):
        return self.__categoria
    def set_categoria(self, categoria):
        self.__categoria = categoria




    def adicionar_estoque(self, quantidade):
        self.set_quantidade_estoque(self.get_quantidade_estoque() + quantidade)
        print(f"Foram cadastradas {quantidade} unidades ao estoque")
        print(f"Estoque atual: {self.get_quantidade_estoque()} unidades")


    def remover_estoque(self, quantidade):
        if quantidade <= self.get_quantidade_estoque():
            self.set_quantidade_estoque(self.get_quantidade_estoque() - quantidade)
            print(f"Foram removidas {quantidade} unidades do estoque")
            print(f"Estoque atual: {self.get_quantidade_estoque()} unidades")
        else:
            print("O estoque não possui a quantidade desejada para a remoção")



    def aplicar_desconto(self, porcentagem):
        self.set_preco(
            self.get_preco() - self.get_preco() * (porcentagem/100)
        )


    def exibir_dados(self):
        return (
            f"-------------------------\n"
            f"Nome: {self.get_nome()}\n"
            f"Preço: R${self.get_preco():.2f}\n"
            f"Estoque: {self.get_quantidade_estoque()}\n"
            f"Categoria: {self.get_categoria()}\n"
            f"-------------------------"
        )
