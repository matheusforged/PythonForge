# O que são funções?

# Função é um bloco de código identificado por um nome e pode
# receber uma lista de parâmetros, esses parâmetros podem ou
# não ter valores padrões. Usar funções torna o código mais
# legível e possibilita o reaproveitamento de código. Programar
# baseado em funções, é o mesmo que dizer que estamos
# programando de maneira estruturada.

def exibir_mensagem():
    print("Olá mundo!")

def exibir_mensagem_2(nome) :
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")

exibir_mensagem()
exibir_mensagem_2(nome="Guilherme")
exibir_mensagem_3()
exibir_mensagem_3(nome="Chappie")

def calcular_total (numeros) :
    return sum(numeros)

def retorna_antecessor_e_sucessor (numero) :
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

calcular_total([10, 20, 34]) # 64
retorna_antecessor_e_sucessor(10) # (9, 11)


def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados ...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
salvar_carro( ** {"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})

# Args e kwargs
# Podemos combinar parâmetros obrigatórios com args e
# kwargs. Quando esses são definidos (*args e ** kwargs), o
# metodo recebe os valores como tupla e dicionario
# respectivamente.

def exibir_poema(data_extenso, *args, ** kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in
kwargs. items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print (mensagem)

exibir_poema("Zen of Python", "Beautiful is better than ugly.", autor="Tim Peters", ano=1999)

################################################

# Position only
# usar o "/" para que seja necessario passar os argumentos por posição

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0",
combustivel="Gasolina") # válido

criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat",
motor="1.0", combustivel="Gasolina") # inválido

#################################################

# Keyword only
# usar o "*" para que seja necessario passar os argumentos por keyword

def criar_carro(*, modelo, ano, placa, marca, motor, combustivel) :
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat",
motor="1.0", combustivel="Gasolina") # válido

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0",
combustivel="Gasolina") # inválido

########################################################################

# Objetos de primeira classe

# Em Python tudo é objeto, dessa forma funções também são
# objetos o que as tornam objetos de primeira classe. Com isso
# podemos atribuir funções a variáveis, passá-las como
# parâmetro para funções, usá-las como valores em estruturas
# de dados (listas, tuplas, dicionários, etc) e usar como valor de
# retorno para uma função (closures).

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")

exibir_resultado(10, 10, somar) # 0 resultado da operação 10 + 10 = 20
exibir_resultado(10, 10, subtrair) # 0 resultado da operação 10 - 10 = 0

#####################################################################

# Escopo local e escopo global
# Python trabalha com escopo local e global, dentro do bloco da
# função o escopo é local. Portanto alterações ali feitas em
# objetos imutáveis serão perdicas quando o método terminar
# de ser executado. Para usar objetos globais utilizamos a
# palavra-chave global, que informa ao interpretador que a
# variável que está sendo manipulada no escopo local é global.
# Essa NÃO é uma boa prática e deve ser evitada.

salario = 2000

def salario_bonus (bonus) :
    global salario
    salario += bonus
    return salario

salario_bonus (500) # 2500