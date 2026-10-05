from datetime import datetime, timedelta


class MaterialBiblioteca:
    def __init__(self, titulo, data_publicacao, prazo, data_aluguel):
        self.__titulo = titulo
        self.__data_publicacao = data_publicacao
        self.__prazo = prazo
        self.__data_aluguel = data_aluguel

    def get_titulo(self):
        return self.__titulo
    def set_titulo(self, titulo):
        self.__titulo = titulo

    def get_data_publicacao(self):
        return self.__data_publicacao
    def set_data_publicacao(self, data_publicacao):
        self.__data_publicacao = data_publicacao

    def get_prazo(self):
        return self.__prazo
    def set_prazo(self, prazo):
        self.__prazo = prazo

    def get_data_aluguel(self):
        return self.__data_aluguel
    def set_data_aluguel(self, data_aluguel):
        self.__data_aluguel = data_aluguel


    def calcular_data_devolucao(self):
        return


class Livro(MaterialBiblioteca):
    def __init__(self, titulo, data_publicacao, prazo, data_aluguel):
        MaterialBiblioteca.__init__(self, titulo, data_publicacao, prazo, data_aluguel)


    def calcular_data_devolucao(self):
        self.set_data_aluguel(datetime.now().date())
        prazo = self.get_data_aluguel() + timedelta(days=self.get_prazo())
        return prazo


class Revista(MaterialBiblioteca):
    def __init__(self, titulo, data_publicacao, prazo, data_aluguel):
        MaterialBiblioteca.__init__(self, titulo, data_publicacao, prazo, data_aluguel)

    def calcular_data_devolucao(self):
        self.set_data_aluguel(datetime.now().date())
        prazo = self.get_data_aluguel() + self.get_prazo()
        return prazo

class Filme(MaterialBiblioteca):
    def __init__(self, titulo, data_publicacao, prazo, data_aluguel):
        MaterialBiblioteca.__init__(self, titulo, data_publicacao, prazo, data_aluguel)

    def calcular_data_devolucao(self):
        self.set_data_aluguel(datetime.now().date())
        prazo = self.get_data_aluguel() + timedelta(days=self.get_prazo())
        return prazo

