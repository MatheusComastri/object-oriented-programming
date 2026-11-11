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

    def get_professor(self):
        return self.__professor
    def set_professor(self, professor):
        self.__professor = professor

    def get_alunos(self):
        return self.__alunos
    def set_alunos(self, alunos):
        self.__alunos = alunos

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



class Curso:
    def __init__(self):
        # inicializa uma lista vazia para armazenar os alunos matriculados no curso
        self.__alunos = []
        self.__professores = []


    def get_alunos(self):
        return self.__alunos
    def set_alunos(self, alunos):
        self.__alunos = alunos

    def get_professores(self):
        return self.__professores
    def set_professores(self, professores):
        self.__professores = professores


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

    def get_get_contratar_professores(self, professor): # errrado
        self.__professores.append(professor)

    def get_nomes_professores_turma(self):
        resultado = []
        for professor in self.__professores:
            resultado.append(professor.get_nome())

    # numero 8
    def verificar_aluno(self, aluno):
        # Recebe um objeto Aluno como parâmetro para verificar se ele está matriculado no curso.

        # Utiliza o operador 'in' para verificar se o objeto recebido está presente na lista de alunos (__alunos).
        # Retorna True caso o aluno esteja na lista ou False caso contrário.
        return aluno in self.__alunos


    # numero 12
    def desmatricular_aluno(self, aluno):
        self.__alunos.remove(aluno)


