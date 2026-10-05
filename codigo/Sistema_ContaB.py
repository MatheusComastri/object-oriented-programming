class ContaBancaria:
    def __init__ (self, numero_conta, saldo, titular):

        self.__numero_conta = numero_conta
        self.__saldo = saldo
        self.__titular = titular

    def get_numero_conta(self):
        return self.__numero_conta
    def set_numero_conta(self, numero_conta):
        self.__numero_conta = numero_conta

    def get_saldo(self):
        return self.__saldo
    def set_saldo(self, saldo):
        self.__saldo = saldo

    def get_titular(self):
        return self.__titular
    def set_titular(self, titular):
        self.__titular = titular


    def depositar(self):
        return

    def sacar(self):
        return

    def calcularjuros(self):
        return


class ContaCorrente(ContaBancaria):
    def __init__ (self, numero_conta, saldo, titular, valor, taxa):
        ContaBancaria.__init__(self, numero_conta, saldo, titular)

        self.__valor = valor
        self.__taxa = taxa

    def get_valor(self):
        return self.__valor
    def set_valor(self, valor):
        self.__valor = valor

    def get_taxa(self):
        return self.__taxa
    def set_taxa(self, taxa):
        self.__taxa = taxa

    def depositar(self):
        novo_saldo = (self.get_valor() + self.get_saldo()) - self.get_taxa()
        self.set_saldo(novo_saldo)
        return self.get_saldo()

    def sacar(self):
        if self.get_valor() <= self.get_saldo():
            self.set_saldo(self.get_saldo() - self.get_valor())
            return self.get_valor()
        else:
            return "Sem saldo"



class ContaPoupanca(ContaBancaria):
    def __init__ (self, numero_conta, saldo, titular, valor, taxa):
        ContaBancaria.__init__(self, numero_conta, saldo, titular)

        self.__valor = valor
        self.__taxa = taxa

    def get_valor(self):
        return self.__valor
    def set_valor(self, valor):
        self.__valor = valor

    def get_taxa(self):
        return self.__taxa
    def set_taxa(self, taxa):
        self.__taxa = taxa


    def depositar(self):
        novo_saldo = self.get_valor() + self.get_saldo()
        self.set_saldo(novo_saldo)
        return self.get_saldo()

    def sacar(self):
        if self.get_valor() <= self.get_saldo():
            self.set_saldo(self.get_saldo() - self.get_valor())
            return self.get_valor()
        else:
            return "Sem saldo"

    def calcularjuros(self):
        juros = self.get_saldo() * self.get_taxa()
        self.set_saldo(self.get_saldo() + juros)
        return self.get_saldo()

# a diferença e usar o get e o set para esses caso
# self.get saldo() - self.get_valor