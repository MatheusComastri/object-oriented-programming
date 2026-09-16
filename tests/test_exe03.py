from codigo.exe03 import Livro

def test_criar_livro():
    meu_livro = Livro(
        titulo="A Sociedade do Anel",
        autor="J.R.R. Tolkien",
        genero="Fantasia Épica",
        ano_publicacao=1954,
        numero_paginas=576
    )

    assert meu_livro.get_titulo() == "A Sociedade do Anel"
    assert meu_livro.get_autor() == "J.R.R. Tolkien"
    assert meu_livro.get_genero() == "Fantasia Épica"
    assert meu_livro.get_ano_publicacao() == 1954
    assert meu_livro.get_numero_paginas() == 576

# ----------------------------------------------------------------------------------------------------------------------------

def test_abrir_livro(monkeypatch, capsys):
    meu_livro = Livro(
        titulo="A Sociedade do Anel",
        autor="J.R.R. Tolkien",
        genero="Fantasia Épica",
        ano_publicacao=1954,
        numero_paginas=576
    )

    # Faz o input() responder "Sim" automaticamente.
    monkeypatch.setattr("builtins.input", lambda _: "Sim")

    # Chama o metodo abrir() para executar o teste.
    meu_livro.abrir()

    # Captura o que foi impresso pelo print().
    saida = capsys.readouterr()

    # Verifica se a mensagem esperada foi impressa na tela.
    assert "Você começou a leitura do livro: A Sociedade do Anel" in saida.out


# teste if - nao para metodo abrir
def test_nao_abrir_livro(monkeypatch, capsys):
    meu_livro = Livro(
        titulo="A Sociedade do Anel",
        autor="J.R.R. Tolkien",
        genero="Fantasia Épica",
        ano_publicacao=1954,
        numero_paginas=576
    )

    monkeypatch.setattr("builtins.input", lambda _: "Nao")

    meu_livro.abrir()

    saida = capsys.readouterr()

    assert "Até outra hora então" in saida.out



# teste else para metodo abrir
def test_abrir_livro_resposta_invalida(monkeypatch, capsys):
    meu_livro = Livro(
        titulo="A Sociedade do Anel",
        autor="J.R.R. Tolkien",
        genero="Fantasia Épica",
        ano_publicacao=1954,
        numero_paginas=576
    )

    # Cria uma sequência de respostas que serão usadas pelo input().
    entradas = iter(["Talvez", "Sim"])

    # Substitui temporariamente o input() para usar as respostas acima.
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    meu_livro.abrir()

    saida = capsys.readouterr()

    assert "Não entendi a sua resposta, digite novamente" in saida.out
    assert "Você começou a leitura do livro: A Sociedade do Anel" in saida.out

# ---------------------------------------------------------------------------------------------------------------



def test_fechar_livro(monkeypatch, capsys):
    meu_livro = Livro(
        titulo="A Sociedade do Anel",
        autor="J.R.R. Tolkien",
        genero="Fantasia Épica",
        ano_publicacao=1954,
        numero_paginas=576
    )

    monkeypatch.setattr("builtins.input", lambda _: "Sim")
    meu_livro.fechar()
    saida = capsys.readouterr()
    assert "Livro fechado, até outra hora!"


def test_nao_fechar_livro(monkeypatch, capsys):
    meu_livro = Livro(
        titulo="A Sociedade do Anel",
        autor="J.R.R. Tolkien",
        genero="Fantasia Épica",
        ano_publicacao=1954,
        numero_paginas=576
    )

    monkeypatch.setattr("builtins.input", lambda _: "Nao")
    meu_livro.fechar()
    saida = capsys.readouterr()
    assert "Certo, continue sua leitura!"


def test_fechar_livro_resposta_invalida(monkeypatch, capsys):
    meu_livro = Livro(
        titulo="A Sociedade do Anel",
        autor="J.R.R. Tolkien",
        genero="Fantasia Épica",
        ano_publicacao=1954,
        numero_paginas=576
    )

    entradas = iter([ "Talves", "Sim"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))
    meu_livro.fechar()
    saida = capsys.readouterr()
    assert "Não entendi a sua resposta, digite novamente" in saida.out
    assert "Livro fechado, até outra hora!" in saida.out

# -----------------------------------------------------------------------------------------------------------------------





def test_marcar_pagina(monkeypatch, capsys):
    meu_livro = Livro(
        titulo="A Sociedade do Anel",
        autor="J.R.R. Tolkien",
        genero="Fantasia Épica",
        ano_publicacao=1954,
        numero_paginas=576
    )

    # Cria as respostas que serão usadas pelos dois input().
    entradas = iter(["Sim", "100"])

    # Faz o input() usar as respostas acima.
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    # Executa o metodo.
    meu_livro.marcar_pagina()

    # Captura o que foi impresso.
    saida = capsys.readouterr()

    # Verifica se a página foi alterada para 100.
    assert meu_livro.get_pagina_atual() == 100

    # Verifica se a mensagem correta foi impressa.
    assert "Você parou na página 100! de 576" in saida.out


def test_nao_marcar_pagina(monkeypatch, capsys):
    meu_livro = Livro(
        titulo="A Sociedade do Anel",
        autor="J.R.R. Tolkien",
        genero="Fantasia Épica",
        ano_publicacao=1954,
        numero_paginas=576
    )

    monkeypatch.setattr("builtins.input", lambda _: "Nao")
    meu_livro.marcar_pagina()
    saida = capsys.readouterr()
    assert "Certo, caso queira marcar, é só dizer"


def test_marcar_pagina_resposta_invalida(monkeypatch, capsys):
    meu_livro = Livro(
        titulo="A Sociedade do Anel",
        autor="J.R.R. Tolkien",
        genero="Fantasia Épica",
        ano_publicacao=1954,
        numero_paginas=576
    )

    entradas = iter([ "Talves", "Nao"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))
    meu_livro.marcar_pagina()
    saida = capsys.readouterr()
    assert "Não entendi sua resposta, digite novamente" in saida.out
    assert "Certo, caso queira marcar, é só dizer" in saida.out

# ----------------------------------------------------------------------------------------------------------------------------------------


def test_avancar_pagina(monkeypatch, capsys):
    meu_livro = Livro(
        titulo="A Sociedade do Anel",
        autor="J.R.R. Tolkien",
        genero="Fantasia Épica",
        ano_publicacao=1954,
        numero_paginas=576,
        pagina_atual = 100 # estou add esse atributo para começar na pagina desejada
    )

    # Faz o input() responder "Sim".
    monkeypatch.setattr("builtins.input", lambda _: "Sim")

    # Executa o metodo.
    meu_livro.avancar_pagina()

    # Captura o que foi impresso.
    saida = capsys.readouterr()

    # Verifica se a página avançou para 101.
    assert meu_livro.get_pagina_atual() == 101

    # Verifica a mensagem impressa.
    assert "Você está na página 101!" in saida.out


def test_avancar_paginna_ultima(monkeypatch, capsys):
    meu_livro = Livro(
        titulo="A Sociedade do Anel",
        autor="J.R.R. Tolkien",
        genero="Fantasia Épica",
        ano_publicacao=1954,
        numero_paginas=576,
        pagina_atual=576  # estou add esse atributo para começar na ultima pagina
    )

    # Faz o input() responder "Sim".
    monkeypatch.setattr("builtins.input", lambda _: "Sim")

    # Executa o metodo.
    meu_livro.avancar_pagina()

    # Captura o que foi impresso.
    saida = capsys.readouterr()

    # Verifica se a página continuou sendo 576.
    assert meu_livro.get_pagina_atual() == 576

    # Verifica a mensagem do else.
    assert "Você já está na última página" in saida.out


def test_nao_avancar_pagina(monkeypatch, capsys):
    meu_livro = Livro(
        titulo="A Sociedade do Anel",
        autor="J.R.R. Tolkien",
        genero="Fantasia Épica",
        ano_publicacao=1954,
        numero_paginas=576,
    )

    monkeypatch.setattr("builtins.input", lambda _: "Nao")
    meu_livro.avancar_pagina()
    saida = capsys.readouterr()
    assert "Okay, caso queira é só falar"


def test_nao_avancar_pagina_resposta_invalida(monkeypatch, capsys):
    meu_livro = Livro(
        titulo="A Sociedade do Anel",
        autor="J.R.R. Tolkien",
        genero="Fantasia Épica",
        ano_publicacao=1954,
        numero_paginas=576,
    )

    entradas = iter([ "Talves", "Nao"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))
    meu_livro.avancar_pagina()
    saida = capsys.readouterr()
    assert "Não entendi sua resposta, digite novamente" in saida.out
    assert "Okay, caso queira é só falar" in saida.out

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------