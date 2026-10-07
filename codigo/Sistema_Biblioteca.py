from datetime import datetime, timedelta


class MaterialBiblioteca:
    def __init__(self, titulo, data_publicacao):
        self.__titulo = titulo
        self.__data_publicacao = data_publicacao


    def get_titulo(self):
        return self.__titulo
    def set_titulo(self, titulo):
        self.__titulo = titulo

    def get_data_publicacao(self):
        return self.__data_publicacao
    def set_data_publicacao(self, data_publicacao):
        self.__data_publicacao = data_publicacao


    def calcular_data_devolucao(self):
        return


class Livro(MaterialBiblioteca):
    def __init__(self, titulo, data_publicacao):
        MaterialBiblioteca.__init__(self, titulo, data_publicacao)

    def calcular_data_devolucao(self):
        data_aluguel = datetime.now().date()
        prazo = 15

        return data_aluguel + timedelta(days=prazo)



class Revista(MaterialBiblioteca):
    def __init__(self, titulo, data_publicacao):
        MaterialBiblioteca.__init__(self, titulo, data_publicacao)

    def calcular_data_devolucao(self):
        data_aluguel = datetime.now().date()
        prazo = 7

        return data_aluguel + timedelta(days=prazo)


class Filme(MaterialBiblioteca):
    def __init__(self, titulo, data_publicacao):
        MaterialBiblioteca.__init__(self, titulo, data_publicacao)

    def calcular_data_devolucao(self):
        data_aluguel = datetime.now().date()
        prazo = 5

        return data_aluguel + timedelta(days=prazo)


