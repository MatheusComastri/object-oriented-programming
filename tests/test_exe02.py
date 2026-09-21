from codigo.exe02 import ContaBancaria


def test_getters_e_setters():
    conta = ContaBancaria(titular="Matheus Comastri de Oliveira Leite", numero_conta=123, saldo=20 )
    conta.set_titular("Duda")

    assert conta.get_titular() == "Duda"


def test_deve_modificar_numero_conta():
    conta = ContaBancaria("Matheus", 123, 30)
    conta.set_numero_conta(456)

    assert conta.get_numero_conta() == 456


def test_deve_modificar_saldo():
    conta = ContaBancaria("Matheus", 123, 30)
    conta.set_saldo(100)

    assert conta.get_saldo() == 100


def test_deve_depositar(monkeypatch):
    conta = ContaBancaria("Matheus", 123, 30)

    # Simula o usuário digitando o número da conta: 123 -> ignora o input do user (basicamente subsitui os inputs por esses valores prédefinidos para realizar o test)
    monkeypatch.setattr("builtins.input", lambda _: "123")
    conta.depositar(50)

    # Saldo inicial = 30
    # Depósito = 50
    # Saldo esperado = 80
    assert conta.get_saldo() == 80


def test_deve_sacar(monkeypatch):
    conta = ContaBancaria("Matheus", 123, 100)

    # Simula o usuário digitando o número da conta: 123
    monkeypatch.setattr("builtins.input", lambda _: "123")
    conta.sacar(30)

    # Saldo inicial = 100
    # Saque = 30
    # Saldo esperado = 70
    assert conta.get_saldo() == 70


def test_deve_mostrar_extrato():
    conta = ContaBancaria("Matheus", 123, 30)
    # Chama o metodo extrato() da classe ContaBancaria usando o objeto conta.
    extrato = conta.extrato()

    assert "Matheus" in extrato
    assert "123" in extrato
    assert "30" in extrato






