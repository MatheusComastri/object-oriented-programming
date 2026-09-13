class ContaBancaria:
    def __init__(self, titular, numero_conta, saldo=0):
        self.titular = titular
        self.numero_conta = numero_conta
        self.saldo = saldo

    def depositar(self, valor):
        while True:
            conta = int(input("Qual o número da conta que deseja depositar?"))

            if conta == self.numero_conta:
                self.saldo += valor
                print("Depósito realizado com sucesso0")
                break
            else:
                print("Conta não encontrada, digite novamente")


    def sacar(self, valor):
        while True:
            conta = int(input("Qual o número da conta que deseja sacar?"))
            if conta == self.numero_conta:
                if valor <= self.saldo:
                    self.saldo -= valor
                    print("Resgate realizado com sucesso")
                    break
                else:
                    print(f"Saldo insuficiente, você possui apenas R${self.saldo} e tentou sacar R${valor}")
                    valor = int(input("Por favor, digite outro valor:"))

            else:
                print("Conta não encontrada, digite novamente")


    def extrato(self):
        return (
            f"Operação realizada com sucesso, segue abaixo o extrato:\n"
            f"-----------------------------------\n"
            f"Extrato:\n"
                f"Titular: {self.titular}\n"
                f"---Numero da conta: {self.numero_conta}\n"
                f"---Saldo: R${self.saldo}\n"
            f"-----------------------------------\n"
        )

meu_extrato = ContaBancaria(titular= "Matheus Comastri de Oliveira Leite", numero_conta= 123, saldo= 30 )
meu_extrato.depositar(int(input("Digite o valor que deseja depositar: ")))
meu_extrato.sacar(int(input("Digite o valor que deseja sacar: ")))
print(meu_extrato.extrato())