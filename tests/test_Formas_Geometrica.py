from codigo.Formas_Geometricas import *

def test_criar_formas_geometrica():
    forma = FormaGeometrica("Quadrado")
    assert forma.get_nome() == "Quadrado"

def test_getter_setter():
    forma = FormaGeometrica("Quadrado")

    forma.set_nome("Circulo")
    assert forma.get_nome() == "Circulo"

def test_calcuar_area_circulo():
    circulo = Circulo("Circulo", 5)

    area = circulo.calcular_area()
    assert round(area, 2) == 78.54

def test_calcular_perimetro_circulo():
    circulo = Circulo("Circulo", 5)

    perimetro = circulo.calcular_perimetro()
    assert round(perimetro, 2) == 31.42


def test_exibir_dados_circulo():
    circulo = Circulo("Círculo", 5)

    dados = circulo.exibir_dados()

    assert "Círculo" in dados
    assert "Área:" in dados
    assert "Perímetro:" in dados





def test_caculaar_area_retangulo():
    retangulo = Retangulo("Retangulo", 4, 2)

    area = retangulo.calcular_area()
    assert round(area, 2) == 8

def test_cacular_perimetro_retangulo():
    retangulo = Retangulo("Retangulo", 4, 2)

    perimetro = retangulo.calcular_perimetro()
    assert round(perimetro, 2) == 12


def test_exibir_dados_retangulo():
    retangulo = Retangulo("Retângulo", 10, 5)

    dados = retangulo.exibir_dados()

    assert "Retângulo" in dados
    assert "Área:" in dados
    assert "Perímetro:" in dados

