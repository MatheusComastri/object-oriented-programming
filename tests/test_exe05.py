from codigo.exe05 import Produto

def test_getters_e_setters():
    produto = Produto(
        nome="Teclado",
        preco=145,
        quantidade_estoque=6,
        categoria="Eletrônico"
    )

    produto.set_nome("Mouse")
    produto.set_preco(80)
    produto.set_quantidade_estoque(10)
    produto.set_categoria("Periférico")

    assert produto.get_nome() == "Mouse"
    assert produto.get_preco() == 80
    assert produto.get_quantidade_estoque() == 10
    assert produto.get_categoria() == "Periférico"


def test_adicionar_estoque(capsys):
    produto = Produto(
        nome='Teclado',
        preco=145,
        quantidade_estoque= 6,
        categoria = 'Eletrônico'
    )

    produto.adicionar_estoque(3)
    produto.adicionar_estoque(2)
    saida = capsys.readouterr()

    assert produto.get_quantidade_estoque() == 11

    assert "Foram cadastradas 3 unidades ao estoque" in saida.out
    assert "Estoque atual: 9 unidades" in saida.out

    assert "Foram cadastradas 2 unidades ao estoque" in saida.out
    assert "Estoque atual: 11 unidades" in saida.out




def test_remover_estoque(capsys):
    produto = Produto(
        nome='Teclado',
        preco=145,
        quantidade_estoque=6,
        categoria='Eletrônico'
    )

    produto.remover_estoque(4)
    saida = capsys.readouterr()

    assert produto.get_quantidade_estoque() == 2
    assert "Foram removidas 4 unidades do estoque" in saida.out
    assert "Estoque atual: 2 unidades" in saida.out


def test_remover_estoque_insuficiente(capsys):
    produto = Produto(
        nome='Teclado',
        preco=145,
        quantidade_estoque=6,
        categoria='Eletrônico'
    )

    produto.remover_estoque(10)
    saida = capsys.readouterr()

    assert produto.get_quantidade_estoque() == 6 # testa se vai continuar a mesma quantidade, pois o codigo não rodda, visto que, não possui estoque suficente para a quantidade a ser removida
    assert "O estoque não possui a quantidade desejada para a remoção" in saida.out



def test_aplicar_desconto():
    produto = Produto(
        nome='Teclado',
        preco=145,
        quantidade_estoque=6,
        categoria='Eletrônico'
    )

    produto.aplicar_desconto(10)

    assert produto.get_preco() == 130.50


def test_exibir_dados():
    produto = Produto(
        nome='Teclado',
        preco=145,
        quantidade_estoque=6,
        categoria='Eletrônico'
    )

    estoque = produto.exibir_dados()

    assert "Teclado" in estoque
    assert "145" in estoque
    assert "6" in estoque
    assert "Eletrônico" in estoque