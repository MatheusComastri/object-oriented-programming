from codigo.exe04 import Pessoa

def test_getters_e_setters():
    pessoa = Pessoa(
        nome="Matheus",
        idade=24,
        altura=180,
        peso=80
    )

    pessoa.set_nome("João")
    pessoa.set_idade(30)
    pessoa.set_altura(175)
    pessoa.set_peso(75)

    assert pessoa.get_nome() == "João"
    assert pessoa.get_idade() == 30
    assert pessoa.get_altura() == 175
    assert pessoa.get_peso() == 75



def test_envelhecer(capsys):
    pessoa = Pessoa(
        nome="Matheus",
        idade=24,
        altura=180,
        peso=80
    )

    pessoa.envelhecer()

    saida = capsys.readouterr()

    assert pessoa.get_idade() == 25
    assert "Parabéns, agora você tem 25 anos" in saida.out


def test_crescer(capsys):
    pessoa = Pessoa(
        nome="Matheus",
        idade=20, # alterei idade para 20 para que a condição seja atendida (so crescer se for menor que 21)
        altura=180,
        peso=80
    )


    pessoa.crescer()

    resposta = capsys.readouterr()

    assert pessoa.get_altura() == 181
    assert "Sua altura aumentou para 181cm" in resposta.out


def test_ganhar_peso(capsys):
    pessoa = Pessoa(
        nome="Matheus",
        idade=24,
        altura=180,
        peso=80
    )

    pessoa.ganhar_peso(10) # ganhar peso recebe o parametro de quilos, logo, preciso informar quantos quilos a pessoa vai ganhar (chamando a função)
    saida = capsys.readouterr()

    assert pessoa.get_peso() == 90
    assert "Você ganhou 10kg e agora está pesando 90kg" in saida.out


def test_perder_peso(capsys):
    pessoa = Pessoa(
        nome="Matheus",
        idade=24,
        altura=180,
        peso=80
    )

    pessoa.perder_peso(5)
    saida = capsys.readouterr()

    assert pessoa.get_peso() == 75
    assert "Você perdeu 5kg e agora está pesando 75kg" in saida.out


def test_exibir_dados():
    pessoa = Pessoa(
        nome="Matheus",
        idade=24,
        altura=180,
        peso=80
    )

    dados = pessoa.exibir_dados()

    assert "Matheus" in dados
    assert "24" in dados
    assert "180" in dados
    assert "80" in dados

