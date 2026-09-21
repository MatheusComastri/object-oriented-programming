class Pessoa:
    def __init__(self, nome, idade, altura, peso):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura
        self.__peso = peso

    # GET: consulta/retorna o valor atual do atributo privado __nome.
    def get_nome (self):
        return self.__nome

    # SET: altera o valor do atributo privado __nome.
    # Recebe um novo valor pelo parâmetro nome e coloca esse valor em __nome.
    #   Não altero __nome diretamente. Chamo o metodo set_nome() e ele faz a alteração dentro do atributo privado.
    def set_nome(self, nome):
        self.__nome = nome

    def get_idade(self):
        return self.__idade
    def set_idade(self, idade):
        self.__idade = idade

    def get_altura(self):
        return self.__altura
    def set_altura(self, altura):
        self.__altura = altura

    def get_peso(self):
        return self.__peso
    def set_peso(self, peso):
        self.__peso = peso



    def envelhecer(self):
        self.set_idade(self.get_idade() + 1)
        print(f"Parabéns, agora você tem {self.get_idade()} anos.")


    def crescer(self):
        if self.__idade <= 21:
            self.set_altura(self.get_altura() + 1)
            print(f"Sua altura aumentou para {self.get_altura()}cm")


    def ganhar_peso(self, quilos):
        self.set_peso(self.get_peso() + quilos)
        print(f"Você ganhou {quilos}kg e agora está pesando {self.get_peso()}kg")


    def perder_peso(self, quilos):
        self.set_peso(self.get_peso() - quilos)
        print(f"Você perdeu {quilos}kg e agora está pesando {self.get_peso()}kg")


    def exibir_dados(self):
        return (
            f"--- DADOS DA PESSOA ---\n"
            f"Nome: {self.get_nome()}\n"
            f"Idade: {self.get_idade()} anos\n"
            f"Altura: {self.get_altura()} cm\n"
            f"Peso: {self.get_peso()} kg\n"
            f"------------------------"
        )

