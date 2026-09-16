class ContaBancaria:
    def __init__(self, titular, numero_conta, saldo=0):
        self.__titular = titular
        self.__numero_conta = numero_conta
        self.__saldo = saldo

    # GET: consulta/retorna o valor atual do atributo privado __titular.
    def get_titular(self):
        return self.__titular

    # SET: altera o valor do atributo privado __titular.
    # Recebe um novo valor pelo parâmetro titular e coloca esse valor em __titular.
    #   Não altero __titular diretamente. Chamo o metodo set_titular() e ele faz a alteração dentro do atributo privado.
    def set_titular(self, titular):
        self.__titular = titular


    def get_numero_conta(self):
        return self.__numero_conta
    def set_numero_conta(self, numero_conta):
        self.__numero_conta = numero_conta


    def get_saldo(self):
        return self.__saldo
    def set_saldo(self, saldo):
        self.__saldo = saldo



    def depositar(self, valor):
        # self = representa a conta/objeto que está executando o metodo
        # valor = valor que será depositado

        while True:
            # Repete até o usuário informar o número correto da conta
            conta = int(input("Qual o número da conta que deseja depositar? "))

            # Pega o número da conta através do GET
            # get_numero_conta() → lê o atributo privado __numero_conta
            if conta == self.get_numero_conta():

                # GET → pega o saldo atual
                # valor → soma o dinheiro que será depositado
                # SET → coloca o novo saldo no atributo privado __saldo
                self.set_saldo(self.get_saldo() + valor)

                print("Depósito realizado com sucesso")
                break  # Sai do while porque o depósito deu certo

            else:
                # Se o número informado não for o da conta
                print("Conta não encontrada, digite novamente")



    def sacar(self, valor):
        # O while True cria um loop que continuará executando até encontrarmos um "break".
        # Nesse caso, ele serve para continuar tentando enquanto o número da conta estiver errado ou o valor do saque for maior que o saldo.
        while True:
            conta = int(input("Qual o número da conta que deseja sacar? "))

            # Comparamos o número digitado pelo usuário (conta)
            # com o número da conta armazenado no objeto.
            # get_numero_conta() é o metodo que criamos para acessar o atributo privado __numero_conta.
            # Os parênteses () são necessários porque estamos chamando/executando o metodo.
            if conta == self.get_numero_conta():

                # Verifica se o valor que o usuário deseja sacar é menor ou igual ao saldo atual da conta.
                # get_saldo() pega o valor atual do atributo privado __saldo. (get_saldo éo metodo criado para isso)
                if valor <= self.get_saldo():

                    # Primeiro pegamos o saldo atual usando get_saldo(). Depois diminuímos o valor que será sacado (usa esse nome get_saldo, pois foi o metodo criado para isso)
                    # Por fim, usamos set_saldo() para colocar o novo saldo dentro do atributo privado __saldo.
                    self.set_saldo(self.get_saldo() - valor)

                    print("Resgate realizado com sucesso")
                    break

                else:
                    # get_saldo() pega o saldo atual para mostrar quanto a pessoa possui.
                    print(
                        f"Saldo insuficiente, você possui apenas "
                        f"R${self.get_saldo()} e tentou sacar R${valor}"
                    )
                    valor = int(input("Por favor, digite outro valor:"))

            else:
                print("Conta não encontrada, digite novamente")


    def extrato(self):
        return (
            f"Operação realizada com sucesso, segue abaixo o extrato:\n"
            f"-----------------------------------\n"
            f"Extrato:\n"
                f"Titular: {self.get_titular()}\n"
                f"---Numero da conta: {self.get_numero_conta()}\n"
                f"---Saldo: R${self.get_saldo()}\n"
            f"-----------------------------------\n"
        )

# Executa este código somente quando o arquivo for executado diretamente,
# evitando que ele seja executado automaticamente quando for importado pelos testes.
if __name__ == "__main__":
    # Cria uma conta com titular, número e saldo inicial
    meu_extrato = ContaBancaria(
        titular="Matheus Comastri de Oliveira Leite",
        numero_conta=123,
        saldo=30
    )

    # Pede o valor que será depositado
    valor = int(input("Digite o valor que deseja depositar: "))
    meu_extrato.depositar(valor)
    # Realiza o depósito na conta

    # Pede o valor que será sacado
    valor = int(input("Digite o valor que deseja sacar: "))
    meu_extrato.sacar(valor)
    # Realiza o saque na conta

    # Mostra o extrato atualizado da conta
    print(meu_extrato.extrato())