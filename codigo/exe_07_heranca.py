class Pessoa:
    # Construtor -> recebe os dados iniciais da classe Pessoa
    def __init__(self, nome, cpf):
        # Atributos privados da classe
        self.__nome = nome
        self.__cpf = cpf

    # Retorna o nome armazenado
    def get_nome(self):
        return self.__nome

    # Altera o nome armazenado
    def set_nome(self, nome):
        self.__nome = nome

    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, cpf):
        self.__cpf = cpf


# ===============================================================

# A classe Professor herda os atributos e métodos de Pessoa.
# Professor também possui seus próprios atributos.

class Professor(Pessoa):
    def __init__(self, nome, cpf, titulacao):

        # Inicializa nome e cpf usando o construtor da classe Pessoa.
        Pessoa.__init__(self, nome, cpf)

        # Atributo específico de Professor
        self.__titulacao = titulacao

    def get_titulacao(self):
        return self.__titulacao

    def set_titulacao(self, titulacao):
        self.__titulacao = titulacao

    # Retorna os dados principais do professor
    def exibir_dados_professor(self):
        return (
            f"Nome do professor: {self.get_nome()}\n"
            f"Titulação do professor: {self.get_titulacao()}\n"
        )


# ===============================================================

# Aluno também herda da classe Pessoa.
# Assim como Professor, ele reutiliza os atributos de Pessoa.

class Aluno(Pessoa):
    def __init__(self, nome, cpf, matricula, escola_segundo_grau, nota1, nota2):

        # Inicializando nome e cpf da classe Pessoa
        Pessoa.__init__(self, nome, cpf)

        self.__matricula = matricula
        self.__escola_segundo_grau = escola_segundo_grau
        self.__nota1 = nota1
        self.__nota2 = nota2

    def get_matricula(self):
        return self.__matricula

    def set_matricula(self, matricula):
        self.__matricula = matricula

    def get_escola_segundo_grau(self):
        return self.__escola_segundo_grau

    def set_escola_segundo_grau(self, escola_segundo_grau):
        self.__escola_segundo_grau = escola_segundo_grau

    def get_nota1(self):
        return self.__nota1

    def set_nota1(self, nota1):
        self.__nota1 = nota1

    def get_nota2(self):
        return self.__nota2

    def set_nota2(self, nota2):
        self.__nota2 = nota2

    # Calcula a média usando as notas que já foram armazenadas
    # no objeto pelo construtor.
    def calcular_media(self):
        return (self.__nota1 + self.__nota2) / 2

    # Exibe os dados do aluno e sua situação.
    def exibir_dados(self):
        return (
            # get_nome() vem da classe Pessoa
            f"Nome do aluno: {self.get_nome()}\n"

            # get_matricula() vem da classe Aluno
            f"Matricula do aluno: {self.get_matricula()}\n"

            # Chama o metodo calcular_aprovacao().
            # Esse metodo será definido pelas classes filhas. -> superclasse pode pegar metodos das subclasses
            f"Situação do aluno: {self.calcular_aprovacao()}\n"
        )


# ===============================================================

# AlunoEnsinoMedio herda de Aluno.
# Como não possui atributos próprios, o __init__ apenas
# chama o __init__ de Aluno para inicializar os atributos herdados.

class AlunoEnsinoMedio(Aluno):

    # Como Aluno agora precisa receber nota1 e nota2,
    # também precisamos recebê-las aqui para passá-las para Aluno.
    def __init__(self, nome, cpf, matricula, escola_segundo_grau, nota1, nota2):

        # Chama o construtor de Aluno e passa todos os dados.
        Aluno.__init__(
            self,
            nome,
            cpf,
            matricula,
            escola_segundo_grau,
            nota1,
            nota2
        )

    # Calcula a aprovação do aluno do Ensino Médio.
    # As notas já estão armazenadas no objeto,
    # por isso não precisamos recebê-las novamente.
    def calcular_aprovacao(self):

        if self.calcular_media() >= 6:
            return "Aprovado"
        else:
            return "Reprovado"

    def aproveitamento_escola(self):
        return self.calcular_aprovacao()


# ===============================================================

# AlunoGraduacao também herda de Aluno.
# A diferença é que a média mínima para aprovação é 7.

class AlunoGraduacao(Aluno):

    def __init__(self, nome, cpf, matricula, escola_segundo_grau, nota1, nota2):

        # Chama o construtor de Aluno e passa todos os dados.
        Aluno.__init__(
            self,
            nome,
            cpf,
            matricula,
            escola_segundo_grau,
            nota1,
            nota2
        )

    def calcular_aprovacao(self):

        if self.calcular_media() >= 7:
            return "Aprovado"
        else:
            return "Reprovado"

    def aproveitamento_graduacao(self):
        return self.calcular_aprovacao()