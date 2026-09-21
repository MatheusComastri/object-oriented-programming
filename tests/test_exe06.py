from codigo.exe06 import Funcionario

def test_getter_e_setter():
    funcionario = Funcionario(
        nome="Mateus",
        cargo="Dev-Júnior",
        salario=3000,
        departamento="Desenvolvimento"
    )

    funcionario.set_nome("Lucas")
    funcionario.set_cargo("Dev-Sênior")
    funcionario.set_salario(5000)
    funcionario.set_departamento("Desenvolvimento")

    assert funcionario.get_nome() == "Lucas"
    assert funcionario.get_cargo() == "Dev-Sênior"
    assert funcionario.get_salario() == 5000
    assert funcionario.get_departamento() == "Desenvolvimento"


def test_receber_aumento():
    funcionario = Funcionario(
        nome="Mateus",
        cargo="Dev-Júnior",
        salario=3000,
        departamento="Desenvolvimento"
    )

    funcionario.receber_aumento(10)

    assert funcionario.get_salario() == 3300




def test_mudar_departamento_mesmo(monkeypatch, capsys):
    funcionario = Funcionario(
        nome="Mateus",
        cargo="Dev-Júnior",
        salario=3000,
        departamento="Desenvolvimento"
    )

    # Define as respostas que o input() vai receber
    respostas = iter(["Sim", "Desenvolvimento"])

    # Substitui o input() pelas respostas acima
    monkeypatch.setattr("builtins.input",lambda _: next(respostas))

    # Executa o metodo que estamos testando
    funcionario.mudar_departamento()

    # Captura o texto exibido pelos print()
    saida = capsys.readouterr().out

    # Verifica se o departamento continuou o mesmo
    assert funcionario.get_departamento() == "Desenvolvimento"

    # Verifica se a mensagem correta foi exibida
    assert "O funcionário já está alocado a este departamento" in saida


def test_mudar_departamento_sucesso(monkeypatch, capsys):
    funcionario = Funcionario(
        nome="Mateus",
        cargo="Dev-Júnior",
        salario=3000,
        departamento="Desenvolvimento"
    )

    respostas = iter(["Sim", "Ciência de dados"])
    monkeypatch.setattr("builtins.input",lambda _: next(respostas))
    funcionario.mudar_departamento()
    saida = capsys.readouterr().out

    assert funcionario.get_departamento() == "Ciência de dados"
    assert "Departamento alterado para Ciência de dados" in saida


def test_nao_mudar_departamento_sucesso(monkeypatch, capsys):
    funcionario = Funcionario(
        nome="Mateus",
        cargo="Dev-Júnior",
        salario=3000,
        departamento="Desenvolvimento"
    )

    monkeypatch.setattr("builtins.input", lambda _: "Nao")
    funcionario.mudar_departamento()
    saida = capsys.readouterr().out

    assert "Certo, quando quiser realizar a mudança é só me chamar" in saida