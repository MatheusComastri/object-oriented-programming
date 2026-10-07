from codigo.Sistema_Pagamento import *

def test_criar_funcionario():
    funcionario = Funcionario(
        nome="Pedro",
        salarioMensal=2000
    )

    assert funcionario.get_nome() == "Pedro"
    assert funcionario.get_salarioMensal() == 2000


def test_getter_setter():
    funcionario = Funcionario(
        nome="Pedro",
        salarioMensal=2000
    )

    funcionario.set_nome("Lucas")
    funcionario.set_salarioMensal(3000)
    assert funcionario.get_nome() == "Lucas"
    assert funcionario.get_salarioMensal() == 3000


def test_calcular_pagamento_funcionario():
    funcionario = FuncionarioComum(
        nome="Pedro",
        salarioMensal=2000
    )

    pagamento = funcionario.calcularPagamento()
    assert pagamento == 2000


def test_exibir_dados_funcionario_comum():
    funcionario = FuncionarioComum(
        nome="Pedro",
        salarioMensal=2000
    )

    dados = funcionario.exibir_dados()

    assert "Pedro" in dados
    assert "2000" in dados


def test_calcular_pagamento_gerente():
    funcionario = Gerente(
        nome="Pedro",
        salarioMensal=2000
    )

    pagamento = funcionario.calcularPagamento()
    assert pagamento == 4000


def test_exibir_dados_gerente():
    funcionario = Gerente(
        nome="Pedro",
        salarioMensal=2000,
    )

    dados = funcionario.exibir_dados()
    assert "Pedro" in dados
    assert "4000" in dados


def test_calcular_pagamento_diretor():
    funcionario = Diretor(
        nome="Pedro",
        salarioMensal=2000,
        lucroMensal=50000
    )

    pagamento = funcionario.calcularPagamento()
    assert pagamento == 7000

def test_getter_setter_lucro_diretor():
    funcionario = Diretor(
        nome="Pedro",
        salarioMensal=2000,
        lucroMensal=50000
    )

    assert funcionario.get_lucroMensal() == 50000

    funcionario.set_lucroMensal(60000)

    assert funcionario.get_lucroMensal() == 60000


def test_exibir_dados_diretor():
    funcionario = Diretor(
        nome="Pedro",
        salarioMensal=2000,
        lucroMensal=50000
    )

    dados = funcionario.exibir_dados()

    assert "Pedro" in dados
    assert "7000" in dados