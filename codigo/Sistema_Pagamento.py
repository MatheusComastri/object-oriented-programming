class Funcionario:
    # Construtor da classe pai.
    def __init__(self, nome, salarioMensal):
        self.__nome = nome
        self.__salarioMensal = salarioMensal

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_salarioMensal(self):
        return self.__salarioMensal

    def set_salarioMensal(self, salarioMensal):
        self.__salarioMensal = salarioMensal


    def calcularPagamento(self):
        return

    # Ele chama o calcularPagamento() de cada tipo de funcionário.
    def exibir_dados(self):
        return (
            f"Nome: {self.get_nome()}\n"
            f"Pagamento: {self.calcularPagamento()}\n"
        )


# ==========================================================================

class FuncionarioComum(Funcionario):

    # Chama o construtor da classe pai.
    def __init__(self, nome, salarioMensal):
        Funcionario.__init__(self, nome, salarioMensal)

    # Funcionário comum recebe somente o salário.
    def calcularPagamento(self):
        return self.get_salarioMensal()


# ==========================================================================

class Gerente(Funcionario):

    def __init__(self, nome, salarioMensal):
        Funcionario.__init__(self, nome, salarioMensal)

    # Gerente recebe salário + bônus de R$ 2.000.
    def calcularPagamento(self):
        bonus = 2000
        return self.get_salarioMensal() + bonus


# ==========================================================================

class Diretor(Funcionario):

    # Além do nome e salário, o diretor precisa saber o lucro mensal.
    def __init__(self, nome, salarioMensal, lucroMensal):
        Funcionario.__init__(self, nome, salarioMensal)

        # Atributo específico do Diretor.
        self.__lucroMensal = lucroMensal

    def get_lucroMensal(self):
        return self.__lucroMensal
    def set_lucroMensal(self, lucroMensal):
        self.__lucroMensal = lucroMensal


    # Diretor recebe salário + 10% dos lucros.
    def calcularPagamento(self):
        participacao = self.get_salarioMensal() + self.__lucroMensal * 0.10

        return self.get_salarioMensal() + participacao
        # O lucro é armazenado no objeto para que o metodo exibir_dados() herdado possa chamar calcularPagamento()
        # sem precisar receber o lucro como parâmetro self.__lucroMensal = lucroMensal


