
class Estado:
    def __init__(self, nome):
        self.__nome = nome


    def get_nome(self):
        return self.__nome
    def set_nome(self, nome):
        self.__nome = nome



class Cidade:
    def __init__(self):
        # A cidade começa sem um estado associado.
        # None significa que ainda não existe um objeto Estado guardado.
        self.__estado = None
        self.__nome = ""

    # Retorna o objeto Estado associado à cidade.
    def get_estado(self):
        return self.__estado

    # Recebe um objeto Estado e guarda sua referência na cidade.
    def set_estado(self, estado):
        self.__estado = estado


    def get_cidade(self):
        return self.__nome

    def set_cidade(self, nome):
        self.__nome = nome


    # Retorna o nome do estado associado à cidade.
    def get_nome_estado(self):
        # Verifica se existe um estado associado.
        if self.__estado is None:
            return "Cidade sem estado"
        else:
            # Acessa o objeto Estado guardado em __estado
            # e chama o metodo get_nome() da classe Estado.
            return self.__estado.get_nome()

    # Resumo:
    # Estado = nome da classe.
    # estado = nome do parâmetro que recebe o objeto.
    # self.__estado = atributo que guarda a referência ao objeto.
    # get_estado() retorna o objeto Estado.
    # get_nome_estado() retorna apenas o nome desse estado.


    def get_estado_escola_cidade(self):
        return self.get_nome_estado()




class Escolaridade:
    def __init__(self):
        self.__nome = ""

    def get_nome(self):
        return self.__nome
    def set_nome(self, nome):
        self.__nome = nome




class Pessoa:
    def __init__(self):
        self.__escolaridade = None # guarda escolaridade recebida
        self.__naturalidade = None # ?
        self._nome = ""

    def get_escolaridade(self):
        return self.__escolaridade

    def set_escolaridade(self, escolaridade):
        # Recebe um objeto pelo parâmetro escolaridade. -> Vem do test (professor.set._escolaridade)
        # Guarda esse objeto no atributo __escolaridade da Pessoa.
        self.__escolaridade = escolaridade


    def get_naturalidade(self):
        return self.__naturalidade

    def set_naturalidade(self, naturalidade):
        self.__naturalidade = naturalidade

    def get_nome(self):
        return self._nome
    def set_nome(self, nome):
        self._nome = nome

    def get_nome_escolaridade(self):
        # Verifica se a pessoa tem algum objeto de escolaridade guardado.
        if self.__escolaridade is None:
            # Se não tiver, retorna esta mensagem.
            return "Pessoa sem escolaridade"
        else:
            # Se tiver um objeto guardado, chama o metodo get_nome() desse objeto para obter o nome da escolaridade.
            return self.__escolaridade.get_nome()

    def get_nome_naturalidade(self):
        if self.__naturalidade is None:
            return "Pessoa sem naturalidade"
        else:
            return self.__naturalidade.get_nome_estado()


    def get_nome_cidade(self):
        if self.__naturalidade is None:
            return "Pessoa sem naturalidade"
        else:
            return self.__naturalidade.get_cidade()


 # Resumo:
    # O metodo set_escolaridade() (da classe Pessoa) recebe um objeto pelo parâmetro escolaridade e guarda esse objeto no atributo self.__escolaridade (da classe Pessoa).
    # Esse objeto é criado a partir da classe Escolaridade e passado pelo código que chama o metodo. Depois, o metodo get_nome_escolaridade() (da classe Pessoa) verifica se existe um objeto guardado e,
    # se existir, chama o metodo get_nome() (da classe Escolaridade) desse objeto para retornar o nome armazenado no atributo __nome (da classe Escolaridade).




class Professor(Pessoa):
    def __init__(self):
        Pessoa.__init__(self)
        self.__curso = None
        self.__escola = None

    def get_curso(self):
        return self.__curso
    def set_curso(self, curso):
        self.__curso = curso

    def get_escola(self):
        return self.__escola
    def set_escola(self, escola):
        self.__escola = escola


    def get_nome_cordenador_professor(self):
        if self.__curso is None:
            return "Professor sem curso"
        else:
            return self.__curso.get_nome_cordenador()

    def get_tipo_ensino_contratacao_curso(self):
        if self.__curso is None:
            return "Professor sem contratação"
        else:
            return self.__curso.get_tipo_ensino_contratacao() # retorno par a classe curso
        # Não precisei criar uma nova associação com Curso, pois Professor já possui o atributo __curso.
        # Assim, basta acessar o objeto Curso existente para chegar ao TipoEnsino associado a ele.

    def get_diretor_escola(self): # letra i
        if self.__escola is None:
            return "Professor sem escola"
        else:
            return self.__escola.get_nome_diretor()


class Aluno(Pessoa):
    def __init__(self):
        Pessoa.__init__(self)
        self.__curso = None

    def get_curso(self):
        return self.__curso

    def set_curso(self, curso):
        self.__curso = curso

    def get_estado_escola(self):
        if self.__curso is None:
            return "Aluno sem curso"
        else:
            return self.__curso.get_estado_escola_curso()

    def get_cordenador_curso(self):
        if self.__curso is None:
            return "Aluno sem curso"
        else:
            return self.__curso.get_nome_cordenador()
        # Verifica se o aluno possui um curso associado.
        # Caso possua, acessa o objeto Curso e chama o metodo get_nome_cordenador(), que retorna o nome do professor responsável pela coordenação daquele curso.
        # Assim, o metodo percorre a associação Aluno → Curso → Professor. Já possuo as outras associações



class TipoEnsino:
    def __init__(self):
        self.__nome = None

    def get_nome(self):
        return self.__nome
    def set_nome(self, nome):
        self.__nome = nome



class Curso:
    def __init__(self):
        self.__cordenador = None
        self.__escola = None
        self.__tipo_ensino = None

    def get_cordenador(self):
        return self.__cordenador
    def set_cordenador(self, cordenador):
        self.__cordenador = cordenador

    def get_escola(self):
        return self.__escola
    def set_escola(self, escola):
        self.__escola = escola

    def get_tipo_ensino(self):
        return self.__tipo_ensino
    def set_tipo_ensino(self, tipo_ensino):
        self.__tipo_ensino = tipo_ensino

    def get_nome_cordenador(self):
        if self.__cordenador is None:
            return "Curso sem cordenador"
        else:
            # Acessa o objeto Professor associado ao curso.
            # Como Professor herda de Pessoa, pode utilizar get_nome().
            # Assim, retorna o nome do professor coordenador.
            return self.__cordenador.get_nome()

    def get_escolaridade_cordenador(self):
        if self.__cordenador is None:
            return "Curso sem cordenador"
        else:
            return self.__cordenador.get_nome_escolaridade()
            # self.__cordenador acessa o objeto Professor armazenado no atributo da classe Curso -> É o atributo cordenador (antes none)
            # get_nome_escolaridade() é um metodo definido na classe Pessoa.
            # Como Professor herda de Pessoa, o objeto armazenado em self.__cordenador também pode executar esse metodo.


    def get_estado_escola_curso(self):
        if self.__escola is None:
            return "Curso sem escola"
        else:
            return self.__escola.get_estado_escola_escola()

    def get_tipo_ensino_contratacao(self):
        if self.__tipo_ensino is None:
            return "Curso sem tipo ensino"
        else:
            return self.__tipo_ensino.get_nome() # retorno para a classe tipo ensino
        # Curso guarda uma referência para TipoEnsino.
        # Por meio dessa referência, consegue acessar o metodo get_nome()
        # da classe TipoEnsino e retornar o nome do ensino associado.



class Escola:
    def __init__(self):
        self.__diretor = None
        self.__cidade = None

    def get_diretor(self):
        return self.__diretor
    def set_diretor(self, diretor):
        self.__diretor = diretor

    def get_cidade(self):
        return self.__cidade
    def set_cidade(self, cidade):
        self.__cidade = cidade

    def get_escolaridade_diretor(self):
        if self.__diretor is None:
            return "Escola sem diretor"
        else:
            return self.__diretor.get_nome_escolaridade()

    def get_estado_escola_escola(self):
        if self.__cidade is None:
            return "Escola sem cidade"
        else:
            return self.__cidade.get_estado_escola_cidade()

    def get_nome_diretor(self): # letra i
        if self.__diretor is None:
            return "Escola sem diretor"
        else:
            return self.__diretor.get_nome() # associado a professor, herda get_nome de pessoa
