class Livro:
    def __init__(self, titulo, autor, genero, ano_publicacao=0, numero_paginas=0,pagina_atual=0):
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
        self.__ano_publicacao = ano_publicacao
        self.__numero_paginas = numero_paginas
        self.__pagina_atual = pagina_atual

    def get_titulo(self):
        return self.__titulo
    def set_titulo(self, titulo):
        self.__titulo = titulo

    def get_autor(self):
        return self.__autor
    def set_autor(self, autor):
        self.__autor = autor

    def get_genero(self):
        return self.__genero
    def set_genero(self, genero):
        self.__genero = genero

    def get_ano_publicacao(self):
        return self.__ano_publicacao
    def set_ano_publicacao(self, ano_publicacao):
        self.__ano_publicacao = ano_publicacao

    def get_numero_paginas(self):
        return self.__numero_paginas
    def set_numero_paginas(self, numero_paginas):
        self.__numero_paginas = numero_paginas

    def get_pagina_atual(self):
        return self.__pagina_atual
    def set_pagina_atual(self, pagina_atual):
        self.__pagina_atual = pagina_atual




    def abrir(self):
        while True:
            pergunta = input("Você quer começar a ler o livro? (Digite 'Sim' ou 'Nao'): ").strip().capitalize()
            if pergunta == 'Sim':
                print(f"Você começou a leitura do livro: {self.get_titulo()}")
                break
            elif pergunta == 'Nao':
                print("Até outra hora então")
                break
            else:
                print("Não entendi a sua resposta, digite novamente")


    def fechar(self):
        while True:
            pergunta = input("Você deseja fechar o livro? (Digite 'Sim' ou 'Nao'): ").strip().capitalize()
            if pergunta == 'Sim':
                print("Livro fechado, até outra hora!")
                break
            elif pergunta == 'Nao':
                print("Certo, continue sua leitura!")
                break
            else:
                print("Não entendi a sua resposta, digite novamente")


    def marcar_pagina(self):
        while True:
            resposta = input("Você deseja marcar em qual página parou? (Digite 'Sim' ou 'Nao'): ").strip().capitalize()
            if resposta == 'Sim':
                pagina = int(input("Em qual página você parou? "))
                while pagina < 0 or pagina > self.get_numero_paginas():
                    print("Página não encontrada")
                    pagina = int(input("Digite outra página: "))

                self.set_pagina_atual(pagina)
                print(f"Você parou na página {self.get_pagina_atual()}! de {self.get_numero_paginas()}")
                break

            elif resposta == 'Nao':
                print("Certo, caso queira marcar, é só dizer")
                break

            else:
                print("Não entendi sua resposta, digite novamente")


    def avancar_pagina(self):
        while True:
            resposta = input("Deseja avançar a página? (Digite 'Sim' ou 'Nao'): ").strip().capitalize()
            if resposta == 'Sim':
                if self.get_pagina_atual() < self.get_numero_paginas():
                    self.set_pagina_atual(self.get_pagina_atual() + 1 )
                    print(f"Você está na página {self.get_pagina_atual()}!")
                    break
                else:
                    print("Você já está na última página")
                    break

            elif resposta == 'Nao':
                print("Okay, caso queira é só falar")
                break

            else:
                print("Não entendi sua resposta, digite novamente")


    def retroceder_pagina(self):
        while True:
            resposta = input("Deseja retrocer a página? (Digite 'Sim' ou 'Nao'): ").strip().capitalize()
            if resposta == 'Sim':
                if self.get_pagina_atual() > 0:
                    self.set_pagina_atual(self.get_pagina_atual() - 1)
                    print(f"Você voltou para a página {self.get_pagina_atual()}!")
                else:
                    print("Você está na primeira página")
                    break
            elif resposta == 'Nao':
                print("Okay, caso queira é só falar")
                break
            else:
                print("Não entendi sua resposta, digite novamente")

    def ficha_catalografica(self):
        return (
            f"Abaixo estão as informações do livro:\n"
            f"-----------------------------------\n"
            f"Título: {self.get_titulo()}\n"
            f"Autor: {self.get_autor()}\n"
            f"Gênero literário: {self.get_genero()}\n"
            f"Ano de publicação: {self.get_ano_publicacao()}\n"
            f"Número de páginas: {self.get_numero_paginas()}\n"
            f"Página atual: {self.get_pagina_atual()}\n"
            f"-----------------------------------"
        )

# meu_livro = Livro(titulo="A Sociedade do Anel", autor="J.R.R. Tolkien", genero="Fantasia Épica", ano_publicacao=1954, numero_paginas=576 )

#meu_livro.abrir()
#meu_livro.marcar_pagina()
# meu_livro.avancar_pagina()
#meu_livro.retroceder_pagina()
# print(meu_livro.ficha_catalografica())