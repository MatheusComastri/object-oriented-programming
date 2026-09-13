class Livro:
    def __init__(self, titulo, autor, genero, ano_publicacao=0, numero_paginas=0,pagina_atual=0):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.ano_publicacao = ano_publicacao
        self.numero_paginas = numero_paginas
        self.pagina_atual = pagina_atual


    def abrir(self):
        while True:
            pergunta = input("Você quer começar a ler o livro? (Digite 'Sim' ou 'Nao'): ").strip().capitalize()
            if pergunta == 'Sim':
                print(f"Você começou a leitura do livro: {self.titulo}")
                break
            elif pergunta == 'Nao':
                print("Até outra hora então")
                break
            else:
                print("Não entendi a sua resposta, digite novamente")


    def fechar(self):
        while True:
            pergunta = input("Você deseja continuar a leitura? (Digite 'Sim' ou 'Nao'): ").strip().capitalize()
            if pergunta == 'Sim':
                print("Certo, boa leitura!")
                break
            elif pergunta == 'Nao':
                print("Ótimo, descanse e continue de onde parou em outro momento!")
                break
            else:
                print("Não entendi a sua resposta, digite novamente")


    def marcar_pagina(self):
        while True:
            resposta = input("Você deseja marcar em qual página parou? (Digite 'Sim' ou 'Nao'): ").strip().capitalize()
            if resposta == 'Sim':
                pagina = int(input("Em qual página você parou? "))
                while pagina < 0 or pagina > self.numero_paginas:
                    print("Página não encontrada")
                    pagina = int(input("Digite outra páina: "))

                self.pagina_atual = pagina
                print(f"Você parou na página {self.pagina_atual}! de {self.numero_paginas}")
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
                if self.pagina_atual < self.numero_paginas:
                    self.pagina_atual += 1
                    print(f"Você está na página {self.pagina_atual}!")
                else:
                    print("Você já está na última página")
                    break

            elif resposta == 'Nao':
                print("Okay, caso queira é só falar")
                break

            else:
                print("Não entendi sua resposta, digite novamente")


    def retrocer_pagina(self):
        while True:
            resposta = input("Deseja retrocer a página? (Digite 'Sim' ou 'Nao'): ").strip().capitalize()
            if resposta == 'Sim':
                if self.pagina_atual > 0:
                    self.pagina_atual -= 1
                    print(f"Você voltou para a página {self.pagina_atual}!")
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
            f"Título: {self.titulo}\n"
            f"Autor: {self.autor}\n"
            f"Gênero literário: {self.genero}\n"
            f"Ano de publicação: {self.ano_publicacao}\n"
            f"Número de páginas: {self.numero_paginas}\n"
            f"Página atual: {self.pagina_atual}\n"
            f"-----------------------------------"
        )

meu_livro = Livro(titulo="A Sociedade do Anel", autor="J.R.R. Tolkien", genero="Fantasia Épica", ano_publicacao=1954, numero_paginas=576 )

meu_livro.abrir()
meu_livro.fechar()
meu_livro.marcar_pagina()
meu_livro.avancar_pagina()
meu_livro.retrocer_pagina()
print(meu_livro.ficha_catalografica())