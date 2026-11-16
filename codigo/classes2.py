class Pessoa:
    def __init__(self):
        self.__nome = None

    def get_nome(self):
        return self.__nome
    def set_nome(self, nome):
        self.__nome = nome


class Aluno(Pessoa):
    def __init__(self):
        Pessoa.__init__(self)



class Professor(Pessoa):
    def __init__(self):
        Pessoa.__init__(self)



class Turma:
    def __init__(self):
        self.__professor = None
        self.__alunos = []
        self.__disciplina = None

    def get_professor(self):
        return self.__professor
    def set_professor(self, professor):
        self.__professor = professor

    def get_alunos(self):
        return self.__alunos
    def set_alunos(self, alunos):
        self.__alunos = alunos

    def get_disciplina(self):
        return self.__disciplina
    def set_disciplina(self, disciplina):
        self.__disciplina = disciplina


    # numero 1
    def get_nome_professor(self):
        if self.__professor is None:
            return "Turma sem professor"
        else:
            return self.__professor.get_nome()

    # numero 2
    def get_matricular(self, aluno):
        self.__alunos.append(aluno)


    def get_nome_aluno_turma(self):
        resultado = []
        for aluno in self.__alunos:
            resultado.append(aluno.get_nome())
        return resultado

    # numero 7
    def get_verificar_aluno_turma(self, aluno):
        # Recebe um objeto Aluno como parâmetro para verificar se ele está matriculado no curso.

        # Utiliza o operador 'in' para verificar se o objeto recebido está presente na lista de alunos (__alunos).
        # Retorna True caso o aluno esteja na lista ou False caso contrário.
        return aluno in self.__alunos


    def get_desmatricular_aluno_turma(self, aluno):
        self.__alunos.remove(aluno)



class Disciplina:
    def __init__(self):
        self.__nome = None

    def get_nome(self):
        return self.__nome
    def set_nome(self, nome):
        self.__nome = nome


class Curso:
    def __init__(self):
        # inicializa uma lista vazia para armazenar os alunos matriculados no curso
        self.__alunos = []
        self.__professores = []
        self.__turmas = []


    def get_alunos(self):
        return self.__alunos
    def set_alunos(self, alunos):
        self.__alunos = alunos

    def get_professores(self):
        return self.__professores
    def set_professores(self, professores):
        self.__professores = professores

    def get_turmas(self):
        return self.__turmas
    def set_turmas(self, turmas):
        self.__turmas = turmas


    def matricular(self, aluno):
        # Recebe um objeto Aluno pelo parâmetro 'aluno'.
        # Adiciona esse objeto ao final da lista __alunos do curso.
        self.__alunos.append(aluno) # recebe um aluno e guarda ele na lista alunos

    # numero 5
    def get_nomes_alunos(self):
        # Cria uma lista vazia chamada resultado.
        # Ela será utilizada para armazenar os nomes dos alunos, e não os objetos Aluno completos.
        resultado = []

        # Percorre a lista __alunos, acessando um aluno por vez.
        # A cada repetição, a variável 'aluno' recebe um dos objetos Aluno que estão armazenados na lista.
        for aluno in self.__alunos:
            # Acessa o metodo get_nome() do objeto Aluno atual.
            # O metodo retorna o nome desse aluno.
            # Em seguida, append() adiciona esse nome à lista resultado.
            resultado.append(aluno.get_nome()) # armazeno cada nome de aluno (aluno in alunos) em resultado

        # Depois que todos os alunos forem percorridos,
        # retorna a lista resultado contendo somente os nomes.
        return resultado

    def adcionar_turmas(self, turmas):
        self.__turmas.append(turmas)

    def get_contratar_professores(self, professor): # errrado
        self.__professores.append(professor)

    def get_nomes_professores_turma(self):
        resultado = []
        for turma in self.__turmas:
            resultado.append(turma.get_professor().get_nome())
        return resultado

    # numero 8
    def verificar_aluno(self, aluno):
        # Recebe um objeto Aluno como parâmetro para verificar se ele está matriculado no curso.

        # Utiliza o operador 'in' para verificar se o objeto recebido está presente na lista de alunos (__alunos).
        # Retorna True caso o aluno esteja na lista ou False caso contrário.
        return aluno in self.__alunos


    # numero 12
    def desmatricular_aluno(self, aluno):
        self.__alunos.remove(aluno)

    # numero 4
    def get_nomes_alunos_turmas_curso(self):
        # Cria uma lista vazia para armazenar os nomes dos alunos
        resultado = []

        # Percorre todas as turmas cadastradas no curso.
        # Utilizamos dois FOR porque o curso possui várias turmas
        # e cada turma pode possuir vários alunos.
        # Primeiro precisamos acessar cada turma para depois
        # percorrer os alunos que pertencem a ela.
        for turma in self.__turmas:

            # Percorre individualmente os alunos da turma atual.
            # O metodo get_alunos() retorna a lista de alunos da turma.
            for aluno in turma.get_alunos():
                # Obtém o nome do aluno atual através do get_nome()
                # e adiciona esse nome à lista resultado.
                resultado.append(aluno.get_nome())
        return resultado


    # numero 6
    def get_nome_disciplina_turma_curso(self):
        resultado = []

        # Percorre todas as turmas cadastradas no curso.
        for turma in self.__turmas:
            # Acessa a disciplina da turma atual,
            # obtém seu nome e adiciona à lista.
            resultado.append(turma.get_disciplina().get_nome())

        # Retorna os nomes das disciplinas encontradas.
        return resultado

    # numero 9
    def get_verificar_turma_curso(self, turma):
        return turma in self.__turmas

    # numero 11
    def get_excluir_turma_curso(self, turma):
        self.__turmas.remove(turma)