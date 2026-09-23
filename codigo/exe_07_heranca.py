class Pessoa:
    # Costrutor -> recebe os dados iniciais da classe pessoa
    def __init__(self, nome, cpf):
        # Atributos privados da classe
        self.__nome = nome
        self.__cpf = cpf

    # retorna o nome armazenado
    def get_nome(self):
        return self.__nome
    # altera o nome armazenado
    def set_nome(self, nome):
        self.__nome = nome

    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, cpf):
        self.__cpf = cpf


# ===============================================================

# a classe professor herda os atributos e metodos de pessoa (profesor tabém posui seus próprios atributos)

class Professor(Pessoa):
    def __init__(self, nome, cpf, titulacao):

        # inicializa nome e cpf usando o construtor a classe pessoa -> pois em pessoa eu coloquei como obrigatório inicializar com os dados
        Pessoa.__init__(self, nome, cpf)

        # atributos espcificos de professor
        self.__titulacao = titulacao

    def get_titulacao(self):
        return self.__titulacao

    def set_titulacao(self, titulacao):
        self.__titulacao = titulacao

    # função para retornar os dados principais de professor
    def exibir_dados_professor(self):
        return (
            f"Nome do professor:{self.get_nome()}\n"
            f"Titulação do professor:{self.get_titulacao()}\n"
        )

# ===============================================================
# Aluno também herda da classe Pessoa.
# Assim como Professor, ele reutiliza os atributos de Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, cpf, matricula, escola_segundo_grau):

        Pessoa.__init__(self, nome, cpf) # inicializando nome e cpf da classe pessoa

        self.__matricula = matricula
        self.__escola_segundo_grau = escola_segundo_grau

    def get_matricula(self):
        return self.__matricula

    def set_matricula(self, matricula):
        self.__matricula = matricula

    def get_escola_segundo_grau(self):
        return self.__escola_segundo_grau

    def set_escola_segundo_grau(self, escola_segundo_grau):
        self.__escola_segundo_grau = escola_segundo_grau


# ===============================================================

# AlunoEnsinoMedio herda de Aluno. Como ela não possui atributos próprios,
# o __init__ apenas chama o __init__ de Aluno para inicializar os atributos herdados.

class AlunoEnsinoMedio(Aluno):

    # Construtor da classe.
    # Como não existem atributos novos, ele apenas chama o construtor de Aluno.
    def __init__(self, nome, cpf, matricula, escola_segundo_grau):

        # chama o construtor de aluno para incializar seus aributos
        Aluno.__init__(self, nome, cpf, matricula, escola_segundo_grau) #

    # calcula a media de duas notas e verifica a aprovação
    def aproveitamento_escola(self, nota1, nota2):

        media = (nota1 + nota2) / 2

        if media >= 6:
            return "Aprovado"
        else:
            return "Reprovado"
        # return dados

    # exibe os dados de aluno e sua situação
    def exibir_dados_escola(self, nota1, nota2):

        return (
            # gett_nome() vem a classe pessoa
            f"Nome do aluno:{self.get_nome()}\n "
            
            # get_matricula() vem da classe aluno
            f"Matricula do aluno:{self.get_matricula()}\n "
            
            # Chama o metodo que calcula a situação do aluno.
            # Como esse metodo possui um return, ele devolve o resultado ("Aprovado" ou "Reprovado") para esta chamada.
            # Assim, o resultado retornado pode ser usado diretamente na mensagem. -> O return volta para onde fiz a chamada da funçãao 
            f"Situação do aluno: {self.aproveitamento_escola(nota1, nota2)}\n" #

        )

# ===============================================================
# Herda de aluno
# Acontece o mesmo que em alunoescola

class AlunoGraduacao(Aluno):
    def __init__(self, nome, cpf, matricula, escola_segundo_grau):
        Aluno.__init__(self, nome, cpf, matricula, escola_segundo_grau)


    def aproveitamento_graduacao(self, nota1, nota2):

        media = (nota1 + nota2) / 2

        if media >= 7:
            return "Aprovado"
        else:
            return "Reprovado"


    def exibir_dados_graduacao(self, nota1, nota2):

        return (
            f"Nome do aluno:{self.get_nome()}\n"
            f"Matricula do aluno:{self.get_matricula()}\n"
            f"Situação do aluno: {self.aproveitamento_graduacao(nota1, nota2)}\n"

        )
