# class Funcionario:
#     def __init__(self, nome, cargo, salario, departamento):
#         self.nome = nome
#         self.cargo = cargo
#         self.salario = salario
#         self.departamento = departamento
#
#
#
#     def receber_aumento(self, valor):
#         self.salario += self.salario * (valor / 100)
#
#
#
#
#     def mudar_departamento(self):
#         resposta = input("Deseja mudar o departamento? ('Sim' ou Nao') ").strip().capitalize()
#         if resposta == 'Sim':
#             novo_departamento = input("Qual o novo departamento? ")
#             if novo_departamento ==  self.departamento:
#                 print("O funcionário já está alocado a este departamento")
#             else:
#                 self.departamento = novo_departamento
#                 print(f"Departamento alterado para {self.departamento}")
#         elif resposta == 'Nao':
#             print("Certo, quando quiser realizar a mudança é só me chamar")
#
#         else:
#             print("Resposta não encontrada")
#
#
#
#     def exibir_dados(self):
#         return (
#             f"\n-----------------------------\n"
#             f"\n Ficha do Funcionário:"
#             f"Nome: {self.nome}\n"
#             f"Cargo: {self.cargo}\n"
#             f"Salário: R${self.salario:.2f}\n"
#             f"Departamento: {self.departamento}\n"
#             f"-----------------------------"
#         )
#
# def novo_funcionario(funcionarios):
#     nome = input("\nQual o nome do funcionário? ")
#     cargo = input("Qual o cargo? ")
#     salario = int(input("Qual o salário do funcionário? "))
#     departamento = input("Em qual o departamento ele irá trabalhar? ")
#
#     for funcionario in funcionarios:
#         if funcionario.nome.lower() == nome.lower():
#             print("\nFuncionário já cadastrado")
#             return
#
#     novo_funcionario = Funcionario(
#         nome= nome,
#         cargo= cargo,
#         salario= salario,
#         departamento= departamento
#     )
#
#     funcionarios.append(novo_funcionario)
#     print("\nFuncionário cadastrado com sucesso!")
#
#
#
# # Por que precisa de encontrar uncionarios, me respoda por comentário (brevemente)
# def encontrar_funcionario(funcionarios):
#
#     nome = input("\nDigite o nome do funcionário: ")
#
#     for funcionario in funcionarios:
#         if funcionario.nome.lower() == nome.lower():
#             return funcionario
#
#     print("\nFuncionário não encontrado.")
#     return None
#
#
#
# # função criada para exibir cada funcionário -> tenho um array então o for exibe cada objeto dele
# def exibir_funcionarios(funcionarios):
#
#     # se o tamanho for igual a 0
#     if len(funcionarios) == 0:
#         print("\nNenhum funcionário cadastrado.")
#         return
#
#     print("\n===== FUNCIONÁRIOS CADASTRADOS =====")
#
#     for funcionario in funcionarios:
#         print(funcionario.exibir_dados())
#
#
#
# # menu para o cadastrador utilizar
# def menu():
#     funcionarios = []
#     while True:
#         print("1 - Cadastrar Funcionários")
#         print("2 - Dar aumento")
#         print("3 - Mudar departamento")
#         print("4 - Exibir dados")
#         print("5 - Sair")
#
#
#         opcao = input("Qual a opção desejada? ")
#
#         # cadastrar funcionario
#         if opcao == '1':
#             novo_funcionario(funcionarios)
#
#         # dar aumento
#         elif opcao == '2':
#             funcionario = encontrar_funcionario(funcionarios)
#
#             if funcionario is not None:
#                 valor = float(input("Digite a porcentagem do aumento"))
#
#                 funcionario.receber_aumento(valor)
#
#         # mudar departamento
#         elif opcao == '3':
#             funcionario = encontrar_funcionario(funcionarios)
#
#             if funcionario is not None:
#                 funcionario.mudar_departamento()
#         # exibir dados
#         elif opcao == '4':
#             exibir_funcionarios(funcionarios)
#
#         # sair
#         elif opcao == '5':
#             print("\nPrograma finalizado.")
#             break
#
#         else:
#             print("\nopção não encontrada.")
# menu()