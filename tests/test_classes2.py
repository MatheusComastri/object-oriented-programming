from codigo.classes2 import *

# ============================= Numero 1 =============================

def test_retornar_nome_professor():
    professor = Professor()
    professor.set_nome("Carlos")

    turma = Turma()
    turma.set_professor(professor)
    assert turma.get_nome_professor() == "Carlos"


def test_nao_retornar_nome_professor():
    turma = Turma()
    assert turma.get_nome_professor() == "Turma sem professor"

# ====================================================================


# =============================== Numero 5 ===================================
def test_retornar_alunos_curso():
    curso = Curso()
    aluno1 = Aluno()
    aluno2 = Aluno()
    curso.matricular(aluno1)
    curso.matricular(aluno2)
    assert curso.get_alunos() == [aluno1, aluno2] # Teste inicial, verifica apenas se os alunos foram registrados


def test_retornar_nomes_alunos_curso():
    # Cria um objeto Curso.
    curso = Curso()

    # Cria o primeiro objeto Aluno e define seu nome.
    aluno1 = Aluno()
    aluno1.set_nome("Matheus")

    # Cria o segundo objeto Aluno e define seu nome.
    aluno2 = Aluno()
    aluno2.set_nome("Bernardo")

    # Matricula os dois objetos Aluno no curso.
    # Os objetos são adicionados à lista interna __alunos.
    curso.matricular(aluno1)
    curso.matricular(aluno2)

    # Verifica se o metodo get_nomes_alunos() retorna
    # uma lista contendo os nomes dos alunos matriculados,
    # respeitando a mesma ordem em que foram adicionados.
    assert curso.get_nomes_alunos() == ["Matheus", "Bernardo"]

# ============================================================================


# =============================== Numero 8 ===================================

def test_encontrar_aluno():
    # Cria um objeto Aluno.
    aluno = Aluno()

    # Cria um objeto Curso.
    curso = Curso()

    # Matricula o aluno no curso, adicionando seu objeto à lista interna de alunos (__alunos).
    # passo o objeto aluno para o metodo da clsse
    curso.matricular(aluno)

    # Passa o objeto Aluno criado anteriormente como argumento para o metodo. -> passaa parametro para verificar-aluno na class curso
    # Dentro da classe Curso, esse objeto será recebido pelo parâmetro 'aluno',
    # permitindo verificar se ele está presente na lista de alunos matriculados.
    assert curso.verificar_aluno(aluno) == True


def test_nao_encontrar_aluno():
    # Cria um objeto Aluno.
    aluno = Aluno()

    # Cria um objeto Curso com a lista de alunos inicialmente vazia.
    curso = Curso()

    # Verifica se o metodo verificar_aluno() retorna False, pois o aluno ainda não foi matriculado no curso.
    assert curso.verificar_aluno(aluno) == False

# ============================================================================



# =============================== Numero 12 ===================================

def test_remover_aluno_curso():
    # Cria um objeto Aluno.
    aluno = Aluno()

    # Cria um objeto Curso.
    curso = Curso()

    # Matricula o aluno no curso, adicionando seu objeto à lista __alunos.
    curso.matricular(aluno)

    # Passa o objeto Aluno como argumento para o metodo desmatricular_aluno().
    # Dentro da classe Curso, o parâmetro receberá esse objeto
    # para identificar qual aluno deverá ser removido da lista.
    curso.desmatricular_aluno(aluno)

    # Verifica se a lista de alunos do curso está vazia,
    # confirmando que o aluno foi removido corretamente.
    assert curso.get_alunos() == []

# ============================================================================

# =============================== Numero 2 ===================================

def test_retornar_alunos_turma():
    turma = Turma()
    aluno1 = Aluno()
    aluno2 = Aluno()

    turma.get_matricular(aluno1)
    turma.get_matricular(aluno2)
    assert turma.get_alunos() == [aluno1, aluno2]


def test_retonar_nomes_alunos_turma():
    turma = Turma()
    aluno1 = Aluno()
    aluno1.set_nome("Matheus")

    aluno2 = Aluno()
    aluno2.set_nome("Bernardo")

    turma.get_matricular(aluno1)
    turma.get_matricular(aluno2)

    assert turma.get_nome_aluno_turma() == ["Matheus", "Bernardo"]

# ================================ Numero 3 =======================================

# Teste para verificar se as turmas são adicionadas e retornadas corretamente pelo curso.
def test_retornar_turmas():
    curso = Curso()

    # Cria duas turmas.
    turmaA = Turma()
    turmaB = Turma()

    # Adiciona as duas turmas à lista de turmas do curso.
    curso.adcionar_turmas(turmaA)
    curso.adcionar_turmas(turmaB)

    # Verifica se o metodo retorna as mesmas turmas, na ordem em que foram adicionadas.
    assert curso.get_turmas() == [turmaA, turmaB]


# Teste para verificar se os professores são adicionados e retornados corretamente pelo curso.
def test_retornar_professores_turmas():
    curso = Curso()

    # Cria dois objetos da classe Professor.
    professor1 = Professor()
    professor2 = Professor()

    # Adiciona os dois professores à lista de professores do curso.
    curso.get_contratar_professores(professor1)
    curso.get_contratar_professores(professor2)

    # Verifica se o metodo retorna os mesmos professores, na ordem em que foram adicionados.
    assert curso.get_professores() == [professor1, professor2]


# Teste para verificar se é possível obter os nomes dos professores que lecionam nas turmas do curso.
def test_retornar_nomes_professores_turmas_curso():
    curso = Curso()

    # Cria o primeiro professor e define seu nome.
    professor1 = Professor()
    professor1.set_nome("Bruno")

    # Cria o segundo professor e define seu nome.
    professor2 = Professor()
    professor2.set_nome("Marcos")

    # Cria duas turmas.
    turmaA = Turma()
    turmaB = Turma()

    # Associa cada professor à sua respectiva turma.
    turmaA.set_professor(professor1)
    turmaB.set_professor(professor2)

    # Adiciona as duas turmas ao curso.
    curso.adcionar_turmas(turmaA)
    curso.adcionar_turmas(turmaB)

    # Verifica se o metodo retorna os nomes dos professores das turmas.
    assert curso.get_nomes_professores_turma() == ["Bruno", "Marcos"]

# ================================ Numero 4 =======================================

def test_retornar_nomes_alunos_turma_curso():
    # Cria um objeto da classe Curso.
    # Esse objeto será utilizado para armazenar as turmas.
    curso = Curso()

    # Cria o primeiro objeto da classe Aluno.
    aluno1 = Aluno()

    # Define o nome do primeiro aluno utilizando o metodo set_nome().
    aluno1.set_nome("Matheus")

    # Cria o segundo objeto da classe Aluno.
    aluno2 = Aluno()

    # Define o nome do segundo aluno.
    aluno2.set_nome("Bernardo")

    # Cria um objeto da classe Turma.
    # Essa turma terá os dois alunos cadastrados nela.
    turmaA = Turma()

    # Adiciona o primeiro aluno à lista de alunos da turma.
    # Utilizamos get_matricular() porque esse metodo utiliza append()
    # para adicionar o aluno à lista existente, sem substituir seu conteúdo.
    turmaA.get_matricular(aluno1)

    # Adiciona o segundo aluno à mesma lista.
    # Assim, a turma passa a ter os dois alunos cadastrados.
    turmaA.get_matricular(aluno2)

    # Adiciona a turmaA à lista de turmas do curso.
    # Dessa forma, o curso passa a ter acesso à turma e aos alunos dela.
    curso.adcionar_turmas(turmaA)

    # Verifica se o metodo get_nomes_alunos_turmas_curso()
    # retorna uma lista com os nomes dos alunos cadastrados
    # nas turmas pertencentes ao curso.
    # O resultado esperado é uma lista com os nomes Matheus e Bernardo.
    assert curso.get_nomes_alunos_turmas_curso() == ["Matheus", "Bernardo"]


def test_retornar_nomes_alunos_de_varias_turmas():
    curso = Curso()

    # Cria os alunos
    aluno1 = Aluno()
    aluno1.set_nome("Matheus")

    aluno2 = Aluno()
    aluno2.set_nome("Bernardo")

    aluno3 = Aluno()
    aluno3.set_nome("João")

    # Cria duas turmas
    turmaA = Turma()
    turmaB = Turma()

    # Adiciona dois alunos na primeira turma
    turmaA.get_matricular(aluno1)
    turmaA.get_matricular(aluno2)

    # Adiciona um aluno na segunda turma
    turmaB.get_matricular(aluno3)

    # Adiciona as duas turmas ao curso
    curso.adcionar_turmas(turmaA)
    curso.adcionar_turmas(turmaB)

    # Verifica se o metodo retorna os alunos das duas turmas
    assert curso.get_nomes_alunos_turmas_curso() == [
        "Matheus", "Bernardo", "João"
    ]


def test_retornar_lista_vazia_sem_turmas():
    # Cria um curso sem adicionar nenhuma turma
    curso = Curso()

    # Como não existem turmas nem alunos para percorrer,
    # o resultado esperado é uma lista vazia.
    assert curso.get_nomes_alunos_turmas_curso() == []

# ================================ Numero 6 =======================================


def test_retornar_nomes_disciplina_turma_curso():
    # Cria um objeto da classe Curso.
    # Ele será responsável por armazenar as turmas.
    curso = Curso()

    # Cria o primeiro objeto da classe Disciplina.
    disciplina1 = Disciplina()

    # Define o nome da primeira disciplina.
    disciplina1.set_nome("Orientação a objetos")

    # Cria o segundo objeto da classe Disciplina.
    disciplina2 = Disciplina()

    # Define o nome da segunda disciplina.
    disciplina2.set_nome("Análise de Sistema")

    # Cria dois objetos da classe Turma.
    # Cada turma terá uma disciplina associada.
    turmaA = Turma()
    turmaB = Turma()

    # Associa a primeira disciplina à turma A.
    # O metodo set_disciplina() armazena o objeto Disciplina
    # no atributo __disciplina da turma.
    turmaA.set_disciplina(disciplina1)

    # Associa a segunda disciplina à turma B.
    turmaB.set_disciplina(disciplina2)

    # Adiciona a turma A à lista de turmas do curso.
    curso.adcionar_turmas(turmaA)

    # Adiciona a turma B à lista de turmas do curso.
    curso.adcionar_turmas(turmaB)

    # Verifica se o metodo retorna os nomes das disciplinas
    # associadas às turmas cadastradas no curso.
    # A lista retornada deve conter os nomes na ordem
    # em que as turmas foram adicionadas.
    assert curso.get_nome_disciplina_turma_curso() == ["Orientação a objetos", "Análise de Sistema"]


def test_retornar_lista_vazia_sem_turmas_curso():
    curso = Curso()

    assert curso.get_nome_disciplina_turma_curso() == []

# ================================ Numero 7 =======================================


def test_verificar_verificar_aluno_turma():
    # Cria um objeto da classe Turma.
    turma = Turma()

    # Cria um objeto da classe Aluno.
    aluno = Aluno()

    # Adiciona o aluno à lista de alunos da turma.
    # O metodo get_matricular() utiliza append()
    # para inserir o aluno na lista __alunos.
    turma.get_matricular(aluno)

    # Verifica se o metodo get_verificar_aluno_turma()
    # identifica que o aluno está cadastrado na turma.
    # Como o aluno foi adicionado anteriormente,
    # o resultado esperado é True.
    assert turma.get_verificar_aluno_turma(aluno) == True


def test_nao_verificar_aluno_turma():
    # Cria um objeto da classe Turma.
    turma = Turma()

    # Cria um objeto da classe Aluno.
    aluno = Aluno()

    # Não adicionamos o aluno à turma.
    # Portanto, a lista __alunos permanece vazia.

    # Verifica se o metodo get_verificar_aluno_turma()
    # identifica que o aluno não pertence à turma.
    # Como ele não foi cadastrado, o resultado esperado é False.
    assert turma.get_verificar_aluno_turma(aluno) == False

# ================================ Numero 9 =======================================

def test_verificar_turma_curso():
    # Cria um objeto da classe Turma.
    turma = Turma()

    # Cria um objeto da classe Curso.
    curso = Curso()

    # Adiciona o objeto turma à lista de turmas do curso.
    # Nesse momento, o objeto turma passa a fazer parte da lista __turmas que pertence ao objeto curso.
    curso.adcionar_turmas(turma)

    # Verifica se o objeto turma está presente na lista __turmas do curso.
    # É necessário passar turma novamente porque estamos chamando outro metodo,
    # com uma finalidade diferente: o primeiro adiciona o objeto à lista, enquanto este recebe o objeto que deve ser procurado.
    # O metodo retorna True se encontrar a turma na lista ou False caso contrário.
    assert curso.get_verificar_turma_curso(turma) == True


def test_nao_verificar_turma_curso():
    # Cria um objeto da classe Turma.
    turma = Turma()

    # Cria um objeto da classe Curso.
    curso = Curso()

    # Não adicionamos a turma ao curso.
    # Portanto, a lista __turmas permanece vazia.

    # Verifica se a turma está cadastrada no curso.
    # Como ela não foi adicionada, o resultado esperado é False.
    assert curso.get_verificar_turma_curso(turma) == False



# ================================ Numero 10 =======================================

def test_remover_aluno_turma():
    # Cria um objeto da classe Turma.
    turma = Turma()

    # Cria um objeto da classe Aluno.
    aluno = Aluno()

    # Matricula o objeto aluno na turma, adicionando-o à lista de alunos (__alunos).
    turma.get_matricular(aluno)

    # Remove o objeto aluno da lista de alunos da turma.
    # É necessário passar aluno como parâmetro para indicar qual objeto deve ser removido.
    turma.get_desmatricular_aluno_turma(aluno)

    # Verifica se a lista de alunos da turma está vazia após a remoção.
    # O resultado esperado é [], pois o único aluno matriculado foi removido.
    assert turma.get_alunos() == []


# ================================ Numero 11 =======================================

def test_remover_turma_curso():
    # Cria um objeto da classe Turma.
    turma = Turma()

    # Cria um objeto da classe Curso.
    curso = Curso()

    # Adiciona o objeto turma à lista de turmas (__turmas) do curso.
    curso.adcionar_turmas(turma)

    # Remove o objeto turma da lista de turmas do curso.
    # O parâmetro turma indica exatamente qual turma deve ser removida.
    curso.get_excluir_turma_curso(turma)

    # Verifica se a lista de turmas do curso está vazia após a remoção.
    # O resultado esperado é [], pois a única turma adicionada foi removida.
    assert curso.get_turmas() == []