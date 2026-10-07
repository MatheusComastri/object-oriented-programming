from codigo.Sistema_ContaB import *

def test_criar_conta():
    conta = ContaBancaria(
        numero_conta=10,
        saldo=100,
        titular="Matheus"
    )

    assert conta.get_numero_conta() == 10
    assert conta.get_saldo() == 100
    assert conta.get_titular() == "Matheus"

def test_getters_setters():
    conta = ContaBancaria(
        numero_conta=10,
        saldo=100,
        titular="Matheus"
    )

    conta.set_numero_conta(12)
    conta.set_saldo(200)
    conta.set_titular("Lucas")

    assert conta.get_numero_conta() == 12
    assert conta.get_saldo() == 200
    assert conta.get_titular() == "Lucas"

def test_depositar_corrente():
    conta = ContaCorrente(
        numero_conta=10,
        saldo=100,
        titular="Matheus",
        valor=45,
        taxa=0.08
    )

    conta.depositar()
    assert conta.get_saldo() == 133.9

    # ou
    # preco = conta.depositar()
    # assert preco == 133.4
    # Como depositar() usa set_saldo() para modificar o objeto, podemos chamar o
    # metodo e depois verificar o saldo pelo getter, sem precisar guardar o retorno em uma variável.


def test_sacar_corrente():
    conta = ContaCorrente(
        numero_conta=10,
        saldo=100,
        titular="Matheus",
        valor=45,
        taxa=0.08
    )

    valor = conta.sacar()

    assert valor == 45
    assert conta.get_saldo() == 55


def test_sacar_corrente_sem_saldo():
    conta = ContaCorrente(
        numero_conta=10,
        saldo=30,
        titular="Matheus",
        valor=45,
        taxa=0.08
    )

    valor = conta.sacar()

    assert valor == "Sem saldo"
    assert conta.get_saldo() == 30




def test_depositar_poupanca_valor():
    conta = ContaPoupanca(
        numero_conta=10,
        saldo=100,
        titular="Matheus",
        valor=45,
        taxa=0.08
    )

    preco = conta.depositar()
    assert preco == 145


def test_sacar_poupanca():
    conta = ContaPoupanca(
        numero_conta=10,
        saldo=100,
        titular="Matheus",
        valor=45,
        taxa=0.08
    )

    valor = conta.sacar()

    assert valor == 45
    assert conta.get_saldo() == 55


def test_sacar_poupanca_sem_saldo():
    conta = ContaPoupanca(
        numero_conta=10,
        saldo=30,
        titular="Matheus",
        valor=45,
        taxa=0.08
    )

    valor = conta.sacar()

    assert valor == "Sem saldo"
    assert conta.get_saldo() == 30


def test_calcular_juros_poupanca():
    conta = ContaPoupanca(
        numero_conta=10,
        saldo=100,
        titular="Matheus",
        valor=45,
        taxa=0.08
    )

    conta.calcularjuros()
    assert conta.get_saldo() == 108