from codigo.Sistema_Pagamento import Diretor
from codigo.ex_classes import *


def test_retornar_escolaridade_professor():
    # Cria um objeto da classe Escolaridade.
    # Passa "Doutorado" para o parâmetro nome do __init__().
    escolaridade = Escolaridade() # é obrigatório passar um nome para escolraide devido ao init
    escolaridade.set_nome("Doutorado")

    # Cria um objeto da classe Professor.
    # Professor herda os métodos da classe Pessoa.
    professor = Professor() # professor é para realizar o teste

    # Chama set_escolaridade(), metodo herdado por professor da classe Pessoa.
    # Passa o objeto da classe Escolaridade que contém o nome "Doutorado",como argumento para o metodo.
    # O metodo guarda uma referência para esse objeto no atributo __escolaridade do objeto professor, da classe Professor.
    professor.set_escolaridade(escolaridade) # -> Basicamente, serve só para enviar o objeto escolaridade para a classe

    # Chama get_nome_escolaridade(), metodo herdado por professor da classe Pessoa.
    # Esse metodo acessa o objeto de Escolaridade guardado no atributo __escolaridade da Pessoa.
    # Em seguida, chama get_nome(), metodo da classe Escolaridade, para obter o nome armazenado no atributo __nome.
    assert professor.get_nome_escolaridade() == "Doutorado"
    # O objeto guardado em __escolaridade é da classe Escolaridade e contém o nome "Doutorado" -> contém tudo da classe, não só o nome
    # Por isso, get_nome(), da classe Escolaridade, é chamado para retornar esse texto,
    # em vez de retornar o objeto inteiro.


# Testa se o metodo get_nome_escolaridade() retorna a mensagem
def test_retornar_pessoa_sem_escolaridade():

    # Cria um objeto da classe Professor.
    # O construtor da classe Professor chama o construtor da classe Pessoa, que inicializa o atributo __escolaridade com o valor None.
    # Por isso, não é necessário passar uma escolaridade na criação do objeto.
    professor = Professor()

    # Chama get_nome_escolaridade(), metodo da classe Pessoa, herdado pela classe Professor.
    # Esse metodo verifica o atributo __escolaridade do objeto professor.
    # Como o valor é None, significa que nenhum objeto da classe Escolaridade foi associado ao objeto professor.
    # Por isso, o metodo retorna "Pessoa sem escolaridade". O assert verifica se o resultado é igual ao texto esperado.
    assert professor.get_nome_escolaridade() == "Pessoa sem escolaridade"


def test_retornar_nome_estado_cidade():
    # Cria um objeto Estado com o nome "MG".
    estado = Estado("MG")

    # Cria um objeto da classe Cidade.
    cidade = Cidade()

    # Associa o objeto estado à cidade usando o méeodo set_estado() em cidade.
    cidade.set_estado(estado)

    # Verifica se o metodo get_nome_estado() retorna "MG".
    assert cidade.get_nome_estado() == "MG"


def test_nao_retornar_nome_cidade():
    cidade = Cidade()
    assert cidade.get_nome_estado() == "Cidade sem estado"



# Testa se é possível obter o estado da naturalidade de um aluno.
def test_retonar_pessoa_natualidade():

    # Cria um objeto da classe Estado, passando "MG"
    # como argumento para o parâmetro nome do construtor __init__().
    estado = Estado("MG")

    # Cria um objeto da classe Cidade.
    cidade = Cidade()

    # Chama set_estado(), metodo da classe Cidade.
    # Passa o objeto estado, da classe Estado, como argumento. O objeto é associado ao atributo __estado da cidade.
    cidade.set_estado(estado)

    # Cria um objeto da classe Aluno.
    # Como Aluno herda de Pessoa, o atributo __naturalidade começa com o valor None, conforme o construtor de Pessoa.
    aluno = Aluno()

    # Chama set_naturalidade(), metodo da classe Pessoa, herdado pela classe Aluno.
    # Passa o objeto cidade, da classe Cidade, como argumento.
    # O objeto cidade fica associado ao atributo __naturalidade do aluno.
    aluno.set_naturalidade(cidade)

    # Chama get_nome_naturalidade(), metodo da classe Aluno ou herdado de Pessoa, dependendo de onde ele foi definido.
    # O metodo deve acessar a cidade associada ao aluno e obter o nome do estado associado a essa cidade.
    # O assert verifica se o resultado é igual ao texto esperado.
    assert aluno.get_nome_naturalidade() == "MG"

def test_retornar_aluno_sem_estado_naturalidade():
    aluno = Aluno()
    assert aluno.get_nome_naturalidade() == "Pessoa sem naturalidade"





def test_retornar_curso_sem_cordenador():
    curso = Curso()
    assert curso.get_nome_cordenador() == "Curso sem cordenador"
    # como eu não passei nenhum nome para codernador dara certo
    # não passei pois não chamei a classe professor (que hera set nome de pessoa) sem ela é impossível add um nome e ficará sempre none


def test_retornar_nome_cordenador_curso():
    # cria um objeto da classe Professor. O nome da variável poderia ser qualquer um, como professor, p1 ou cordenador.
    cordenador = Professor()

    # Define o nome do professor coordenador como "Bruno".
    # O metodo set_nome() é herdado da classe Pessoa.
    cordenador.set_nome("Bruno")

    # cria um objeto da classe Curso porque é nele que está o atributo __cordenador. Assim, poderá associar um professor a esse curso.
    curso = Curso()

    # Associa o objeto Professor ao objeto Curso como coordenador. -> cordenador possui o nome, curso possui cordenador

    # depois eu associo o objeto cordenador (possui a classe professor e tem o nome bruno) a variavel cordenador da classe curso -> curso.set_cordenador(cordenador),
    # ou seja, o curso.set_cordenador muda a variavel cordenador (antes parenteses) e passa o objeto cordenador como parametro (depois parenteses) -> o que antes era none agora e preenchido
    curso.set_cordenador(cordenador)  # serve para passar todos esses objetos que estao em cordenador (objeto) para a variavel codernador na classe curso

    # Verifica se o metodo get_nome_cordenador() retorna "Bruno".
    # O resultado esperado é o nome do professor associado ao curso.
    assert curso.get_nome_cordenador() == "Bruno"





def test_retornar_professor_sem_curso():
    professor = Professor()
    assert professor.get_nome_cordenador_professor() == "Professor sem curso"
    # não chamei a classe curso para add um curso a um professor, sem curso ele é none



def test_retornar_nome_cordenador_professor():
    cordenador = Professor()
    cordenador.set_nome("Bruno")
    curso = Curso()
    curso.set_cordenador(cordenador)
    professor = Professor()
    professor.set_curso(curso)
    assert professor.get_nome_cordenador_professor() == "Bruno"
    # aqui tem um passo a mais, pois preciso setar o curso em professor (pois na classe e none)
    #   professor.set_curso vai ter: o objeto curso (precisei da classe curso pelo cordenador - atributo), que possui o objeto corenador
    #       e cordenador tem o nome Bruno (precisei da classe professor pelo set nome)
    # o primeiro objeto professor vai ter o nome associado (cordneador) e o segundo objeto professor vai ter o curso associado -> PQ?




# oBS: Diferença entre os os dois
# Começado pelo curso: Aqui você começa pelo curso, associa um professor a ele e consulta o nome desse professor.

# Começando pelo professor: Aqui você começa por um professor, associa um curso a ele e, por meio desse curso, chega ao coordenador e consulta seu nome.
#   Só um detalhe importante: no segundo caso, você precisa criar dois objetos Professor:
#       Um é o coordenador, que tem o nome Bruno.
#       O outro é o professor que possui o curso associado.



def test_retornar_curso_sem_cordenador_escolaridade():
    curso = Curso()
    # curso = Curso() cria um novo curso -> quero saber a escolaridade de umm cordenador, e ele pertence a classe Curso e como ele é um professor, consigo acessar a escolaridade (herda e pessoa)
    # Como nenhum coordenador foi definido, o atributo __coordenador começa com None.
    assert curso.get_escolaridade_cordenador() == "Curso sem cordenador"

def test_retornar_cordenador_escolaridade():
    cordenador = Professor() # professor que tem a escolaridade herdada -> criei um objeto cordenador pra a classe Professor

    escolaridade = Escolaridade()
    escolaridade.set_nome("Mestrado")
    # criei uma escolaridade e defini seu nome, mas o pg não sabe quem é essa escolaridade

    cordenador.set_escolaridade(escolaridade)
    # associei escolaridade a um professor

    curso = Curso()
    curso.set_cordenador(cordenador)
    # associei professor a um curso, pois é na clase curso que verificamos a escolridade de um cordenaador

    assert curso.get_escolaridade_cordenador() == "Mestrado"


    # primeiro eu criei o metodo get_escolaridade_cordenador na classe curso, pois o exercicio pede a escolaridde de um cordenador de um curso (so por causa disso?)

    # return self.__cordenador.get_nome_escolaridade() -> essa parte serve para ir ate a classe escolaridade e pegar seu metodo get_nome escolaridade?

    # após isso, eu fiz o teste de sw:
    # primeiro eu criei um objeto professor para acessar a classe Curso, pois é ele quem possui escolaridade associada (herda de pessoa)
    # Segundo eu criei um objeto escolaridade para a classe Escolaridade, e setei o nome dela como Mestrado (devido ao set_nome)

    # Após isso, associei uma escolaridade a im professor pelo metodo cordenaador.set_escolaridade(escolridade) -> Lembrando que: cordenador é um objeto de Professor e profesor herda de Pessoa, logo set_escolaridde é um metodo de pessoa e (ecolaridade) é o escolaridade que possui as informções de set_nome (mestrado) -> evita que escolaridade seja none

    # Após isso criei um objeto curso para  a classe Curso, afinal o metodo para verificar a classe está em curso
    # Depois disso associei o cordenador (professor) a um curso -> Lebrando que, (cordenador) possui todas as iformações anteriores de escolaridade e set_corenador é um metodo de curso e vai evitar que curso seja none




def test_retornar_escola_sem_diretor():
    escola = Escola()
    assert escola.get_escolaridade_diretor() == "Escola sem diretor"

def test_retornar_escolaridade_diretor():
    diretor = Professor()
    escolaridade = Escolaridade()
    escolaridade.set_nome("Doutorado")
    diretor.set_escolaridade(escolaridade)
    escola = Escola()
    escola.set_diretor(diretor)
    assert escola.get_escolaridade_diretor() == "Doutorado"


def test_retornar_pessoa_sem_naturalidade_professor():
    # Cria um objeto da classe Professor.
    professor = Professor()

    # Verifica se o professor não possui uma cidade de naturalidade associada.
    # Como o atributo __naturalidade começa com None, deve retornar a mensagem padrão.
    assert professor.get_nome_cidade() == "Pessoa sem naturalidade"

def test_retornar_naturalidade_pessoa_professor():
    # Cria um objeto da classe Professor.
    # Professor herda de Pessoa -> também possui os métodos get_naturalidade() e set_naturalidade(). -> para chegar em cidade
    professor = Professor()


    # Esse objeto representa a naturalidade (cidade) que será associada ao professor.
    cidade = Cidade()

    # Define o nome da cidade no atributo da classe Cidade.
    cidade.set_cidade("Juiz de Fora")

    # Associa o objeto Cidade ao objeto Professor.
    # O metodo set_naturalidade() é herdado da classe Pessoa -> atributo naturalidade recebe o objeto cidade -> naturalidade em pessoa deixar de ser none
    professor.set_naturalidade(cidade)

    # Acessa o metodo get_nome_cidade() da classe Pessoa, herdado por Professor
    # Esse metodo acessa a naturalidade do professor e chama get_cidade() no objeto Cidade para retornar seu nome.
    assert professor.get_nome_cidade() == "Juiz de Fora"
    # OBS:
    #   A associação acontece quando o objeto Cidade é passado para set_naturalidade() e sua referência é armazenada no atributo __naturalidade da classe Pessoa.
    #   Assim, get_nome_cidade() consegue acessar o objeto Cidade armazenado em __naturalidade e chamar seu metodo get_cidade() para retornar o nome da cidade.




def test_nao_retornar_estado_escola_aluno():
    # Cria apenas o objeto aaluno
    aluno = Aluno()
    # chama get_estdo... Como aluno ainda não tem curso associado, retornar none
    assert aluno.get_estado_escola() == "Aluno sem curso"

def test_retoarnar_estado_escola_aluno():
    aluno = Aluno()
    curso = Curso()
    escola = Escola()
    cidade = Cidade()
    estado = Estado("Minas Gerais")

    cidade.set_estado(estado)
    escola.set_cidade(cidade)
    curso.set_escola(escola)
    aluno.set_curso(curso)
    assert aluno.get_estado_escola() == "Minas Gerais"

# A cadeia de relações começa com o objeto Aluno, que possui um Curso associado. O Curso possui uma Escola associada
# Escola possui uma Cidade associada. A Cidade, por sua vez, possui um Estado associado.

# Para descobrir o estado em que o aluno estuda, o metodo get_estado_escola() da classe Aluno acessa o objeto Curso por meio de get_curso().

# Em seguida, o Curso acessa a Escola associada e chama seu metodo get_estado_escola_escola(). A Escola acessa a Cidade associada e chama get_estado_escola_cidade().

# Por fim, a Cidade acessa o objeto Estado armazenado em seu atributo __estado e chama get_nome() para retornar o nome do estado.

# Dessa forma, cada classe acessa o objeto relacionado a ela e repassa a chamada até chegar ao Estado, permitindo descobrir onde o aluno estuda.

# OBS: # É necessário realizar todas as associações para que o aluno consiga acessar, por meio dos objetos relacionados, o Estado da cidade onde sua escola está localizada.

# Teste: # Cria os objetos e associa cada um ao próximo para que o aluno consiga acessar o estado por toda a cadeia de relações.


def test_nao_retornar_ensino_contratacao():
    professor = Professor()
    assert professor.get_tipo_ensino_contratacao_curso() == "Professor sem contratação"

def test_retornar_ensino_contratacao():
    professor = Professor()
    curso = Curso()
    tipo_ensino = TipoEnsino()
    tipo_ensino.set_nome("Superior")
    curso.set_tipo_ensino(tipo_ensino)
    professor.set_curso(curso)
    assert professor.get_tipo_ensino_contratacao_curso() == "Superior"
    # Primeiro, crio um Professor, um Curso e um TipoEnsino.
    # Defino o nome do TipoEnsino como "Superior".
    # Depois, associo TipoEnsino ao Curso e Curso ao Professor.
    # Por fim, verifico se Professor consegue acessar o Curso associado,
    # chegar ao TipoEnsino e retornar seu nome.



def test_retornar_cordenador_curso():
    aluno = Aluno()
    curso = Curso()
    professor = Professor()

    professor.set_nome("Marcos")
    # Associa o objeto Professor ao atributo coordenador do Curso.
    curso.set_cordenador(professor)

    # Associa o objeto Curso ao Aluno.
    aluno.set_curso(curso)

    # Verifica se o Aluno consegue acessar o nome do coordenador
    # percorrendo as associações entre Aluno, Curso e Professor.
    assert aluno.get_cordenador_curso() == "Marcos"

def test_retornar_cordenador_curso_sem_curso():
    aluno = Aluno()
    assert aluno.get_cordenador_curso() == "Aluno sem curso"


def test_retornar_cordenador_curso_sem_cordenador():
    aluno = Aluno()
    curso = Curso()

    aluno.set_curso(curso)
    assert aluno.get_cordenador_curso() == "Curso sem cordenador"



def test_retornar_diretor_escola():
    professor = Professor()
    diretor = Professor()
    escola = Escola()

    diretor.set_nome("Carlos")
    escola.set_diretor(diretor)
    professor.set_escola(escola)
    assert professor.get_diretor_escola() == "Carlos"


def test_retornar_diretor_sem_escola():
    professor = Professor()
    assert professor.get_diretor_escola() == "Professor sem escola"


def test_retornar_diretor_escola_sem_diretor():
    professor = Professor()
    escola = Escola()

    professor.set_escola(escola)
    assert professor.get_diretor_escola() == "Escola sem diretor"








































#---------------------------------------------------ESCOLARIDADE-----------------------------------------------------------------------------

# O caso de teste cria um objeto da classe Escolaridade, armazenando o texto "Doutorado" no atributo __nome desse objeto.
# A variável escolaridade, pertencente ao caso de teste, guarda uma referência para o objeto da classe Escolaridade.

# Em seguida, o caso de teste cria um objeto da classe Professor.
# Como a classe Professor herda da classe Pessoa, o objeto professor pode utilizar os métodos definidos na classe Pessoa.

# O caso de teste chama o metodo set_escolaridade(), definido na classe Pessoa e herdado pela classe Professor.
#  O objeto da classe Escolaridade, guardado na variável escolaridade do caso de teste, é passado como argumento para o parâmetro escolaridade desse metodo.

# Dentro do metodo set_escolaridade(), o objeto da classe Escolaridade é guardado no atributo __escolaridade do objeto professor, da classe Professor.
# Dessa forma, o objeto professor passa a ter uma referência para o objeto da classe Escolaridade.

# Depois, o caso de teste chama o metodo get_nome_escolaridade(), definido na classe Pessoa e herdado pela classe Professor.
# Esse metodo verifica se o atributo __escolaridade do objeto professor contém um objeto da classe Escolaridade ou se está vazio (None).

# Como o objeto da classe Escolaridade já foi guardado no atributo __escolaridade do objeto professor,
# o metodo get_nome_escolaridade() acessa esse objeto e chama o metodo get_nome(), pertencente à classe Escolaridade.

# O metodo get_nome(), da classe Escolaridade, retorna o valor do atributo __nome do objeto da classe Escolaridade.
#  Nesse caso, o valor retornado é o texto "Doutorado".

# Por fim, o assert do caso de teste verifica se o resultado retornado pelo metodo get_nome_escolaridade(),
#  da classe Pessoa e herdado pela classe Professor, é igual ao texto "Doutorado". Como os valores são iguais, o teste passa.

# Resumindo: o metodo set_escolaridade(), da classe Pessoa,  guarda no objeto professor uma referência para o objeto da classe Escolaridade.
#  Depois, o metodo get_nome_escolaridade(), também da classe Pessoa, acessa esse objeto e utiliza o metodo get_nome(),
#   da classe Escolaridade, para recuperar o nome "Doutorado". O assert confirma que essa comunicação entre os objetos funciona como esperado.

#-------------------------------------------------------------------------------------------------------------------------------------------------------


#--------------------------------------------------NATURALIDADE---------------------------------------------------------------------------------------

# Primeiro, crio um objeto da classe Estado e passo "MG" como parâmetro para o construtor.
# Depois, crio um objeto da classe Cidade e chamo o metodo set_estado(), da classe Cidade, passando o objeto estado como argumento.
# Esse metodo associa o objeto estado ao atributo que guarda o estado dentro de cidade, que antes estava vazio (None).

# Em seguida, crio um objeto da classe Aluno. Como a classe Aluno herda da classe Pessoa, o atributo que guarda a naturalidade começa vazio (None).
# Então, chamo o metodo set_naturalide() e passo o objeto cidade como argumento.
# Dessa forma, o objeto cidade, que já tem um objeto estado associado a ele, fica associado ao atributo de naturalidade do objeto aluno.

# Por fim, chamo o metodo get_nome_naturalidade() do objeto aluno.
#  Como a naturalidade não está vazia, o metodo acessa a cidade (atributo passado que contem estado) associada ao aluno
#  e chama o metodo get_nome_naturlidade da classe Pessoa (aluno herda pessoa), como naturlidade nao esta vio, ele chama
#  get_nome_estado(), da classe Cidade.  Como o estado também não está vazio, esse metodo obtém o nome do estado associado à cidade, retornando "MG".
#  Assim, o assert verifica se o resultado retornado é igual a "MG".

# -----------------------------------------------------------------------------------------------------------------------------------------



