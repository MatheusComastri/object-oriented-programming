from codigo.SIstema_Pedido import *
from codigo.exe05 import Produto


def test_criar_produto():
    produto = Produtos(
        nome="Teclado", preco=100)

    assert produto.get_nome() == "Teclado"
    assert produto.get_preco() == 100

def test_getter_setter():
    produto = Produtos(
        nome="Teclado", preco=100
    )

    produto.set_nome("Mouse")
    produto.set_preco(50)
    assert produto.get_nome() == "Mouse"
    assert produto.get_preco() == 50


def test_calcular_preco_PE():
    produto = ProdutoEletronico(
        nome="Teclado", preco=100
    )

    preco = produto.CalcularPreco()
    assert preco == 90


def test_calcular_preco_PR():
    produto = ProdutoRoupa(
        nome="Camisa", preco=80
    )

    preco = produto.CalcularPreco()
    assert preco == 64


def test_calcular_preco_PL():
    produto = ProdutoLivro(
        nome="O Alquimista", preco=50
    )

    preco = produto.CalcularPreco()
    assert preco == 47.5