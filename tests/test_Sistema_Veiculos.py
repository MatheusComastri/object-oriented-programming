from codigo.Sistema_Veiculos import *

def test_criar_veiculo():
    veiculo = Veiculo(
        marca = 'Ford',
        modelo = 'Mustang',
        preco = 150,
    )

    assert veiculo.get_marca() == 'Ford'
    assert veiculo.get_modelo() == 'Mustang'
    assert veiculo.get_preco() == 150


def test_getters_setters():
    veiculo = Veiculo(
        marca = 'Ford',
        modelo = 'Mustang',
        preco = 150,
    )

    veiculo.set_marca('Fiat')
    veiculo.set_modelo('Uno')
    veiculo.set_preco(50)

    assert veiculo.get_marca() == 'Fiat'
    assert veiculo.get_modelo() == 'Uno'
    assert veiculo.get_preco() == 50

def test_calcular_custo_carro():
    veiculo = Carro(
        marca = 'Ford',
        modelo = 'Mustang',
        preco = 150,
    )

    custo = veiculo.calcular_custo()
    assert custo== 172.5

def test_calcular_custo_Moto():
    veiculo = Moto(
        marca = 'Honda',
        modelo = 'CG-Start',
        preco = 100,
    )

    custo = veiculo.calcular_custo()
    assert custo == 110

def test_calcular_custo_Bicicleta():
    veiculo = Bicicleta(
        marca = 'Croiser',
        modelo = 'TF-100',
        preco = 70,
    )

    custo = veiculo.calcular_custo()
    assert custo == 73.5