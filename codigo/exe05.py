class Produto:
    def __init__(self, nome, preco, quantidade_estoque, categoria):
        self.nome = nome
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque
        self.categoria = categoria


    def adicionar_estoque(self, quantidade):
        self.quantidade_estoque += quantidade
        print(f"Foram cadastradas {quantidade} unidades ao estoque")
        print(f"Estoque atual: {self.quantidade_estoque} unidades")


    def remover_estoque(self, quantidade):
        if quantidade <= self.quantidade_estoque:
            self.quantidade_estoque -= quantidade
            print(f"Foram removidas {quantidade} unidades do estoque")
            print(f"Estoque atual: {self.quantidade_estoque} unidades")
        else:
            print("O estoque não possui a quantidade desejada para a remoção")



    def aplicar_desconto(self, porcentagem):
        self.preco -= self.preco * (porcentagem/100)


    def exibir_dados(self):
        return (
            f"-------------------------\n"
            f"Nome: {self.nome}\n"
            f"Preço: R${self.preco:.2f}\n"
            f"Estoque: {self.quantidade_estoque}\n"
            f"Categoria: {self.categoria}\n"
            f"-------------------------"
        )

# cadastrar produtos
def cadastrar_produtos(produtos):
    nome = input("Digite o nome do produto: ")
    preco = int(input("Digite o valor do produto: "))
    quantidade_estoque = int(input("Digite o quantidade de estoque desse produto: "))
    categoria = input("Digite o categoria do produto: ")

    # verificação existencia do produto
    for produto in produtos:
        if produto.nome.lower() == nome.lower():
            print("Produto já está cadastrado")
            produto.adcionar_estoque(quantidade_estoque)
            return

    # se não encontrou, cria um nogo
    novo_produto = Produto(
        nome=nome,
        preco=preco,
        quantidade_estoque=quantidade_estoque,
        categoria=categoria
    )

    #Adiciona o objeto na lista
    produtos.append(novo_produto)
    print("Produto cadastrado com sucesso!")


# exibir produtos
def exibir_produtos(produtos):
    if len(produtos) == 0:
        print("\nNenhum produto cadastrado")
        return
    print("\n=======Produtos cadastrados=======\n")
    for produto in produtos:
        print(produto.exibir_dados())



def encontrar_produtos(produtos):

    nome = input("Digite o nome do produto: ")
    for produto in produtos:
        if produto.nome.lower() == nome.lower():
            return produto
    return None


# Menu Principal
def menu():
    produtos = []
    while True:
        print("============================")
        print("  Sistema de Produtos"  )
        print("1 - Cadastrar Produtos")
        print("2 - Adcionar ao estoque")
        print("3 - Remover do estoque")
        print("4 - Aplicar desconto")
        print("5 - Exibir Produtos")
        print("6 - Sair")


        opcao = input("Escolha uma opção: ")

        # cadastrar produtos
        if opcao == "1":
            cadastrar_produtos(produtos)

        # adcionar produtos
        elif opcao == "2":
            produto = encontrar_produtos(produtos)

            if produto is not None:

                quantidade = int(
                    input("Digite a quantidade para adicionar: ")
                )
                produto.adicionar_estoque(quantidade)

            else:
                print("\nProduto não encontrado.")

        # remover produtos
        elif opcao == "3":
            produto = encontrar_produtos(produtos)

            if produto is not None:
                quantidade = int(
                    input("Digite a quantidade para remover: ")
                )
                produto.remover_estoque(quantidade)
            else:
                print("\nProduto não encontrado.")

        # aplicar desconto
        elif opcao == "4":
            produto = encontrar_produtos(produtos)

            if produto is not None:
                quantidade = int(
                    input("Digite a porcentagem do desconto: ")
                )
                produto.aplicar_desconto(quantidade)
            else:
                print("\nProduto não encontrado.")

        # exibir produtos
        elif opcao == "5":
            exibir_produtos(produtos)

        # sair
        elif opcao == "6":
            print("\nPrograma finalizado com sucesso!")
            break

        else:
            print("\nOpção não encontrada, digite noamente")

menu()


