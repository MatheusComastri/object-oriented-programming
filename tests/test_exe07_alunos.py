from codigo.exe_07_heranca import *


# ===============================================================
# TESTES DA CLASSE PESSOA

def test_retornar_nome_pessoa():
    pessoa = Pessoa(
        nome="Matheus",
        cpf=12345678
    )

    pessoa.set_nome("João")

    assert pessoa.get_nome() == "João"


def test_retornar_cpf_pessoa():
    pessoa = Pessoa(
        nome="Matheus",
        cpf=12345678
    )

    pessoa.set_cpf(87654321)

    assert pessoa.get_cpf() == 87654321


# ===============================================================
# TESTES DA CLASSE PROFESSOR

def test_retornar_nome_professor():
    professor = Professor(
        nome="Matheus",
        cpf=12345678,
        titulacao="Mestre"
    )

    professor.set_nome("Bruno")

    assert professor.get_nome() == "Bruno"


def test_retornar_cpf_professor():
    professor = Professor(
        nome="Matheus",
        cpf=12345678,
        titulacao="Mestre"
    )

    professor.set_cpf(456123789)

    assert professor.get_cpf() == 456123789


def test_retornar_titulacao_professor():
    professor = Professor(
        nome="Matheus",
        cpf=12345678,
        titulacao="Mestre"
    )

    professor.set_titulacao("Doutor")

    assert professor.get_titulacao() == "Doutor"


def test_exibir_dados_professor():
    professor = Professor(
        nome="Matheus",
        cpf=12345678,
        titulacao="Mestre"
    )

    dados = professor.exibir_dados_professor()

    assert "Matheus" in dados
    assert "Mestre" in dados


# ===============================================================
# TESTES DA CLASSE ALUNO

def test_retornar_nome_aluno():
    aluno = Aluno(
        nome="Matheus",
        cpf=12345678,
        matricula=123456789,
        escola_segundo_grau="Apogeu",
        nota1=8,
        nota2=5
    )

    aluno.set_nome("Henrique")

    assert aluno.get_nome() == "Henrique"


def test_retornar_cpf_aluno():
    aluno = Aluno(
        nome="Matheus",
        cpf=12345678,
        matricula=123456789,
        escola_segundo_grau="Apogeu",
        nota1=8,
        nota2=5
    )

    aluno.set_cpf(456123789)

    assert aluno.get_cpf() == 456123789


def test_retornar_matricula_aluno():
    aluno = Aluno(
        nome="Matheus",
        cpf=12345678,
        matricula=123456789,
        escola_segundo_grau="Apogeu",
        nota1=8,
        nota2=5
    )

    aluno.set_matricula(456123789)

    assert aluno.get_matricula() == 456123789


def test_retornar_escola_segundo_grau_aluno():
    aluno = Aluno(
        nome="Matheus",
        cpf=12345678,
        matricula=123456789,
        escola_segundo_grau="Apogeu",
        nota1=8,
        nota2=5
    )

    aluno.set_escola_segundo_grau("Jesuitas")

    assert aluno.get_escola_segundo_grau() == "Jesuitas"


def test_retornar_nota1_aluno():
    aluno = Aluno(
        nome="Matheus",
        cpf=12345678,
        matricula=123456789,
        escola_segundo_grau="Apogeu",
        nota1=8,
        nota2=5
    )

    aluno.set_nota1(9)

    assert aluno.get_nota1() == 9


def test_retornar_nota2_aluno():
    aluno = Aluno(
        nome="Matheus",
        cpf=12345678,
        matricula=123456789,
        escola_segundo_grau="Apogeu",
        nota1=8,
        nota2=5
    )

    aluno.set_nota2(7)

    assert aluno.get_nota2() == 7


def test_calcular_media_aluno():
    aluno = Aluno(
        nome="Matheus",
        cpf=12345678,
        matricula=123456789,
        escola_segundo_grau="Apogeu",
        nota1=8,
        nota2=6
    )

    resultado = aluno.calcular_media()

    assert resultado == 7


# ===============================================================
# TESTES DA CLASSE ALUNO ENSINO MÉDIO

def test_aproveitamento_escola_aluno_aprovado():
    aluno = AlunoEnsinoMedio(
        nome="Matheus",
        cpf=12345678,
        matricula=123456789,
        escola_segundo_grau="Apogeu",
        nota1=8,
        nota2=5
    )

    resultado = aluno.aproveitamento_escola()

    assert resultado == "Aprovado"


def test_aproveitamento_escola_aluno_reprovado():
    aluno = AlunoEnsinoMedio(
        nome="Matheus",
        cpf=12345678,
        matricula=123456789,
        escola_segundo_grau="Apogeu",
        nota1=4,
        nota2=5
    )

    resultado = aluno.aproveitamento_escola()

    assert resultado == "Reprovado"


def test_calcular_aprovacao_ensino_medio_aprovado():
    aluno = AlunoEnsinoMedio(
        nome="Matheus",
        cpf=12345678,
        matricula=145236987,
        escola_segundo_grau="Apogeu",
        nota1=8,
        nota2=5
    )

    resultado = aluno.calcular_aprovacao()

    assert resultado == "Aprovado"


def test_exibir_dados_ensino_medio():
    aluno = AlunoEnsinoMedio(
        nome="Matheus",
        cpf=12345678,
        matricula=145236987,
        escola_segundo_grau="Apogeu",
        nota1=8,
        nota2=5
    )

    resultado = aluno.exibir_dados()

    assert "Matheus" in resultado
    assert "145236987" in resultado
    assert "Aprovado" in resultado


# ===============================================================
# TESTES DA CLASSE ALUNO GRADUAÇÃO

def test_aproveitamento_graduacao_aluno_aprovado():
    aluno = AlunoGraduacao(
        nome="Matheus",
        cpf=12345678,
        matricula=123456789,
        escola_segundo_grau="Apogeu",
        nota1=7,
        nota2=9
    )

    resultado = aluno.aproveitamento_graduacao()

    assert resultado == "Aprovado"


def test_aproveitamento_graduacao_aluno_reprovado():
    aluno = AlunoGraduacao(
        nome="Matheus",
        cpf=12345678,
        matricula=123456789,
        escola_segundo_grau="Apogeu",
        nota1=3,
        nota2=2
    )

    resultado = aluno.aproveitamento_graduacao()

    assert resultado == "Reprovado"


def test_calcular_aprovacao_graduacao_aprovado():
    aluno = AlunoGraduacao(
        nome="Matheus",
        cpf=12345678,
        matricula=123456789,
        escola_segundo_grau="Apogeu",
        nota1=8,
        nota2=7
    )

    resultado = aluno.calcular_aprovacao()

    assert resultado == "Aprovado"


def test_exibir_dados_graduacao():
    aluno = AlunoGraduacao(
        nome="Matheus",
        cpf=12345678,
        matricula=123456789,
        escola_segundo_grau="Apogeu",
        nota1=8,
        nota2=5
    )

    resultado = aluno.exibir_dados()

    assert "Matheus" in resultado
    assert "123456789" in resultado
    assert "Reprovado" in resultado