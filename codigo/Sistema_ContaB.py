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
        self__saldo = saldo

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
    def __init__ (self, numero_conta, saldo, titular):
        ContaBancaria.__init__(self, numero_conta, saldo, titular)

    def depositar(self):