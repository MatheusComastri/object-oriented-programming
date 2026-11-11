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



