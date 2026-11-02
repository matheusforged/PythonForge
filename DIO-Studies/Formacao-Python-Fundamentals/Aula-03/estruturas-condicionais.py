# # IF

# saldo = 2000.0
# saque = float(input("Informe o valor do saque: "))

# if saldo >= saque:
#     print("Realizando saque!")

# if saldo <= saque:
#     print("faldo insuficiente!")

# # IF/ELSE

# saldo = 2000.0
# saque = float(input("Informe o valor do saque: "))

# if saldo >= saque:
#     print("Realizando saque!")
# else:
#     print("Saldo insuficiente!")

# #IF/ELIF/ELSE

# opcao = int(input("Informe uma opçao: [1] Sacar \n[2] Extrato: "))

# if opcao == 1:
#     valor = float(input("Informe a quantia para o saque: "))
# #
# elif opcao == 2:
#     print("Exibindo o extrato ... ")
# else:
#     print("Opção inválida")

MAIOR_IDADE = 18
IDADE_ESPECIAL = 12

idade = int(input("Informa sua idade:"))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CHN.")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH.")

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CHN.")
else:
    print( "Ainda não pode tirar a CNH.")

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CHN.")
elif idade >= IDADE_ESPECIAL:
    print("Pode fazer aulas teoricas, mas não pode fazer aulas praticas.")
else:
    print("Ainda não pode tirar a CNH.")