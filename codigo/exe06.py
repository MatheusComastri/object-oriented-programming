class Funcionario:
    def __init__(self, nome, cargo, salario, departamento):
        self.__nome = nome
        self.__cargo = cargo
        self.__salario = salario
        self.__departamento = departamento


    def get_nome(self):
        return self.__nome
    def set_nome(self, nome):
        self.__nome = nome

    def get_cargo(self):
        return self.__cargo
    def set_cargo(self, cargo):
        self.__cargo = cargo

    def get_salario(self):
        return self.__salario
    def set_salario(self, salario):
        self.__salario = salario

    def get_departamento(self):
        return self.__departamento
    def set_departamento(self, departamento):
        self.__departamento = departamento



    def receber_aumento(self, valor):
        self.set_salario(
            self.get_salario() + self.get_salario() * (valor / 100)
        )



    def mudar_departamento(self):
        resposta = input("Deseja mudar o departamento? ('Sim' ou Nao') ").strip().capitalize()
        if resposta == 'Sim':
            novo_departamento = input("Qual o novo departamento? ")
            if novo_departamento ==  self.get_departamento():
                print("O funcionário já está alocado a este departamento")
            else:
                #  setter é uma função e precisa receber o novo valor como argumento
                # O novo departamento é diferente do atual, então ppode fazer a alteração.
                self.set_departamento(novo_departamento)
                print(f"Departamento alterado para {self.get_departamento()}")
        elif resposta == 'Nao':
            print("Certo, quando quiser realizar a mudança é só me chamar")

        else:
            print("Resposta não encontrada")



    def exibir_dados(self):
        return (
            f"\n-----------------------------\n"
            f"\n Ficha do Funcionário:"
            f"Nome: {self.get_nome()}\n"
            f"Cargo: {self.get_cargo()}\n"
            f"Salário: R${self.get_salario():.2f}\n"
            f"Departamento: {self.get_departamento()}\n"
            f"-----------------------------"
        )



