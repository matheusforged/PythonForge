nome = "Guilherme"
idade = 28
profissao = "Progamador"
linguagem = "Python"
saldo = 50.50

dados = {"nome": "Guilherme", "idade": 28, "saldo": 50.50}

print("Nome: %s Idade: %d" % (idade, nome))
print("Nome: {} Idade: {}".format(nome, idade))
print("Nome: {1} Idade: {0}".format(idade, nome))
print("Nome: {1} Idade: {o} Nome: {1} ". format(idade, nome))
print("Nome: {nome} Idade: {idade}" . format(nome=nome, idade=idade))
print("Nome: {name} Idade: {age} {name} {name} {age}".format(age=idade, name=nome))
print("Nome: {nome} Idade: {idade}".format( ** dados))

print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")

# Strings triplas

nome = "Matheus"
mensagem = f"""
Olá meu nome é {nome},
EU estou aprendendo Python.

"""

print(
    """
    =================MENU=====================

    [1] Depositar
    [2] Sacar
    [3] Ver extrato da conta
    [0] Sair do sistema

    ==========================================
    
"""

)
