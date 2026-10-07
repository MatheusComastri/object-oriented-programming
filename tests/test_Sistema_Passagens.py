from codigo.Sistema_Passagens import *

def test_criar_voo():
    passagem = Voo(
        origem="Brasil",
        distancia=9800,
        destino="Suiça",
        data_voo='Fevereiro'
    )

    assert passagem.get_origem() == "Brasil"
    assert passagem.get_distancia() == 9800
    assert passagem.get_destino() == "Suiça"
    assert passagem.get_data_voo() == "Fevereiro"

def test_getter_setter():
    passagem = Voo(
        origem="Brasil",
        distancia=9800,
        destino="Suiça",
        data_voo='Fevereiro'
    )

    passagem.set_origem("França")
    passagem.set_distancia(6000)
    passagem.set_destino("EUA")
    passagem.set_data_voo("Março")

    assert passagem.get_origem() == "França"
    assert passagem.get_distancia() == 6000
    assert passagem.get_destino() == "EUA"
    assert passagem.get_data_voo() == "Março"


def test_calcular_preco_voo_domestico():
    passagem = VooDomestico(
        origem="Juiz de Fora",
        distancia=479,
        destino="São Paulo",
        data_voo='Fevereiro',
        fator= 0.30
    )

    preco = passagem.calcular_preco()
    assert preco == 143.7

def test_calcular_preco_voo_internacional():
    passagem = VooInternacional(
        origem="Brasil",
        distancia=9800,
        destino="Suiça",
        data_voo='Fevereiro',
        fator= 1,
        taxa_conversao= 0.5
    )

    preco = passagem.calcular_preco()
    assert round(preco, 2) == 4900