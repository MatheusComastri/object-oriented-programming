from codigo.Sistema_Biblioteca import *
from datetime import datetime, timedelta, date

def test_criar_Material_Biblioteca():
    material = MaterialBiblioteca(
        titulo='Batman: O longo dia das bruxas',
        data_publicacao=date(1996, 12,12)
    )

    assert material.get_titulo() == 'Batman: O longo dia das bruxas'
    assert material.get_data_publicacao() == date(1996, 12, 12)


def test_getters_setters():
    material = MaterialBiblioteca(
        titulo='Batman: O longo dia das bruxas',
        data_publicacao=date(1996, 12, 12)
    )

    material.set_titulo("A Sociedade do Anel")
    material.set_data_publicacao(date(1954, 7, 29))

    assert material.get_titulo() == "A Sociedade do Anel"
    assert material.get_data_publicacao() == date(1954, 7, 29)


def test_data_devolucao_Livro():
    material = Livro(
        titulo='A Sociedade do Anel',
        data_publicacao=date(1954, 7, 29)
    )

    data = material.calcular_data_devolucao()
    assert data == date(2026, 10, 22)

def test_data_deolucao_Revista():
    material = Revista(
        titulo='Batman: O longo dia das bruxas',
        data_publicacao=date(1996, 12, 12)
    )

    data = material.calcular_data_devolucao()
    assert data == date(2026, 10, 14)

def test_data_devolucao_Filme():
    material = Filme(
        titulo="A Casa Monstro",
        data_publicacao=date(2006, 7, 21)
    )

    data = material.calcular_data_devolucao()
    assert data == date(2026, 10, 12)