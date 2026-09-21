from codigo.exe01 import Veiculo

def test_getter_e_setter():
    veiculo = Veiculo(
        modelo="Civic",
        marca="Honda",
        ano=2020,
        velocidade_atual=50
    )

    # Altera os valores através dos setters
    veiculo.set_modelo("Corolla")
    veiculo.set_marca("Toyota")
    veiculo.set_ano(2022)
    veiculo.set_velocidade_atual(80)
    veiculo.set_ligado(True)

    # Verifica os valores através dos getters
    assert veiculo.get_modelo() == "Corolla"
    assert veiculo.get_marca() == "Toyota"
    assert veiculo.get_ano() == 2022
    assert veiculo.get_velocidade_atual() == 80
    assert veiculo.get_ligado() is True


def test_acelerar():
    veiculo = Veiculo(
        modelo="Civic",
        marca="Honda",
        ano=2020,
        velocidade_atual=50
    )

    veiculo.acelerar(30)

    assert veiculo.get_velocidade_atual() == 80

def test_frear():
    veiculo = Veiculo(
        modelo="Civic",
        marca="Honda",
        ano=2020,
        velocidade_atual=50
    )

    veiculo.frear(20)
    assert veiculo.get_velocidade_atual() == 30

def test_frear_zerano_velocidade():
    veiculo = Veiculo(
        modelo="Civic",
        marca="Honda",
        ano=2020,
        velocidade_atual=50
    )

    veiculo.frear(60)
    assert veiculo.get_velocidade_atual() == 0


def test_ligar():
    veiculo = Veiculo(
        modelo="Civic",
        marca="Honda",
        ano=2020
    )

    # O veículo começa desligado
    assert veiculo.get_ligado() is False

    # Liga o veículo
    veiculo.ligar()

    # Verifica se ficou ligado
    assert veiculo.get_ligado() is True


def test_desligar():
    veiculo = Veiculo(
        modelo="Civic",
        marca="Honda",
        ano=2020,
        velocidade_atual=50
    )


    veiculo.ligar()
    veiculo.desligar()
    assert veiculo.get_ligado() is False
    assert veiculo.get_velocidade_atual() == 0


def test_velocidade_alta(capsys):
    veiculo = Veiculo(
        modelo="Civic",
        marca="Honda",
        ano=2020,
        velocidade_atual=80
    )

    # Verifica a velocidade comparando com o limite de 60
    veiculo.velocidade_alta(60)

    # Captura o que foi exibido pelo print
    saida = capsys.readouterr()

    # Verifica se a mensagem correta apareceu
    assert "Velocidade acima do limite permitido" in saida.out


def test_velocidade_dentro_do_limite(capsys):
    veiculo = Veiculo(
        modelo="Civic",
        marca="Honda",
        ano=2020,
        velocidade_atual=50
    )


    veiculo.velocidade_alta(60)
    saida = capsys.readouterr()
    assert "Velocidade abaixo do limite permitido" in saida.out


def test_exibir_dados():
    veiculo = Veiculo(
        modelo="Civic",
        marca="Honda",
        ano=2020,
        velocidade_atual=50
    )

    # Guarda o texto retornado pelo metodo
    dados = veiculo.exibir_dados()

    # Verifica se os dados do veículo estão no retorno
    assert "Civic" in dados
    assert "Honda" in dados
    assert "50" in dados