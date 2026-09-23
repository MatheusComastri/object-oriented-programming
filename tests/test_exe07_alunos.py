from codigo.exe_07_heranca import *

# Testa se é possível alterar e recuperar o nome de Pessoa.
def test_retornar_nome_pessoa():
    # Cria um objeto Pessoa.
    pessoa = Pessoa(
        nome="Matheus",
        cpf=12345678
    )
    # Altera o nome através do setter.
    pessoa.set_nome("João")
    # Verifica se o getter retorna o novo nome.
    assert pessoa.get_nome() == "João"

# Testa se é possível alterar e recuperar o CPF.
def test_retornar_cpf_pessoa():
    pessoa = Pessoa(
        nome="Matheus",
        cpf=12345678
    )

    pessoa.set_cpf(87654321)
    assert pessoa.get_cpf() == 87654321



# ==================================================================================================

# Testa o nome herdado por Professor.
def test_retornar_nome_professor():
    professor = Professor(
        nome="Matheus",
        cpf=12345678,
        titulacao="Mestre"
    )

    # Usa o setter herdado de Pessoa.
    professor.set_nome("Bruno")
    assert professor.get_nome() == "Bruno"

# Testa o CPF herdado por Professor.
def test_retornar_cpf_professor():
    professor = Professor(
        nome="Matheus",
        cpf=12345678,
        titulacao="Mestre"
    )

    professor.set_cpf(456123789)
    assert professor.get_cpf() == 456123789


# Testa a titulação específica do Professor.
def test_retornar_titulacao_professor():
    professor = Professor(
        nome="Matheus",
        cpf=12345678,
        titulacao="Mestre"
    )

    professor.set_titulacao("Doutor")
    assert professor.get_titulacao() == "Doutor"


# Testa o metodo que exibe os dados do professor.
def test_exibir_dados_professor():
    professor = Professor(
        nome="Matheus",
        cpf=12345678,
        titulacao="Mestre"
    )

    # Guarda o texto retornado pelo metodo.
    dados = professor.exibir_dados_professor()

    # Verifica se o nome está no texto.
    assert "Matheus" in dados

    # Verifica se a titulação está no texto.
    assert "Mestre" in dados



# =======================================================================

# Testa o nome herdado por Aluno.
def test_retornar_nome_aluno():
    aluno = Aluno(
        nome="Matheus",
        cpf=12345678,
        matricula=123456789,
        escola_segundo_grau="Apogeu"
    )

    aluno.set_nome("Henrique")
    assert aluno.get_nome() == "Henrique"


# Testa o CPF herdado por Aluno.
def test_retornar_cpf_aluno():
    aluno = Aluno(
        nome="Matheus",
        cpf=12345678,
        matricula=123456789,
        escola_segundo_grau="Apogeu"
    )

    aluno.set_cpf(456123789)
    assert aluno.get_cpf() == 456123789


# Testa a matrícula do Aluno.
def test_retornar_matricula_aluno():
    aluno = Aluno(
        nome="Matheus",
        cpf=12345678,
        matricula=123456789,
        escola_segundo_grau="Apogeu"
    )

    aluno.set_matricula(456123789)
    assert aluno.get_matricula() == 456123789


# Testa a escola de segundo grau.
def test_retornar_escola_segundo_grau_aluno():
    aluno = Aluno(
        nome="Matheus",
        cpf=12345678,
        matricula=123456789,
        escola_segundo_grau="Apogeu"
    )

    aluno.set_escola_segundo_grau("Jesuitas")
    assert aluno.get_escola_segundo_grau() == "Jesuitas"


# Testa a situação um aluno do ensino médio aprovado.
def test_aproveitamento_escola_aluno_aprovado(): #
    aluno = AlunoEnsinoMedio(
        nome="Matheus",
        cpf=12345678,
        matricula=123456789,
        escola_segundo_grau="Apogeu"
    )

    # Calcula a média: (8 + 5) / 2 = 6.5. -> Passa os parametros 8 e 5 para metodo calcular
    resultado = aluno.aproveitamento_escola(8, 5)

    # Como 6.5 >= 6, deve ser aprovado.
    assert resultado == "Aprovado"


# Testa um aluno do ensino médio reprovado.
def test_aproveitamento_escola_aluno_reprovado():
    aluno = AlunoEnsinoMedio(
        nome="Matheus",
        cpf=12345678,
        matricula=123456789,
        escola_segundo_grau="Apogeu"
    )

    resultado = aluno.aproveitamento_escola(4, 5)

    assert resultado == "Reprovado"


# Testa a exibição dos dados do aluno do ensino médio.
def test_exibir_dados_escola_aluno():
    aluno = AlunoEnsinoMedio(
        nome="Matheus",
        cpf=12345678,
        matricula=145236987,
        escola_segundo_grau="Apogeu"
    )

    # Chama o metodo e guarda o texto retornado -> passando os parametros (pois no metodo pede o valores de nota)
    resultado = aluno.exibir_dados_escola(8, 5)

    # Verifica se o nome está no resultado.
    assert "Matheus" in resultado

    # Verifica se a matrícula está no resultado.
    assert "145236987" in resultado

    # Verifica se a situação está no resultado.
    assert "Aprovado" in resultado


def test_aproveitamento_aluno_graduacao_aprovado():
    aluno = AlunoGraduacao(
        nome="Matheus",
        cpf=12345678,
        matricula=123456789,
        escola_segundo_grau="Apogeu"
    )

    resultado = aluno.aproveitamento_graduacao(7, 9)
    assert resultado == "Aprovado"


# Testa um aluno da graduação aprovado.
def test_aproveitamento_aluno_graduacao_reprovado():
    aluno = AlunoGraduacao(
        nome="Matheus",
        cpf=12345678,
        matricula=123456789,
        escola_segundo_grau="Apogeu"
    )

    resusltado = aluno.aproveitamento_graduacao(3, 2)
    assert resusltado == "Reprovado"


# Testa a exibição dos dados do aluno da graduação.
def test_exibir_dados_graduacao_aluno():
    aluno = AlunoGraduacao(
        nome="Matheus",
        cpf=12345678,
        matricula=123456789,
        escola_segundo_grau="Apogeu"
    )

    reultado = aluno.exibir_dados_graduacao(8, 5)

    assert "Matheus" in reultado
    assert "123456789" in reultado
    assert "Reprovado" in reultado