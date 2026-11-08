# INFORMAÇÕES DE CONTEXTO DECORADORES:

def calculadora(operacao):
    def soma(a, b):
        return a + b

    def sub(a, b):
        return a - b

    def mul(a, b):
        return a * b

    def div(a, b):
        return a / b

    match operacao:
        case "+":
            return soma
        case "-":
            return sub
        case "*":
            return mul
        case "/":
            return div

op = calculadora("+")
print(op(2,2))
op = calculadora("-")  
print(op(2,2))
op = calculadora("*")  
print(op(2,2))
op = calculadora("/")
print(op(2,2))


## PASSAGEM PARAMETRO:

def mensagem(nome):
    print("executando mensagem")
    return f"Oi {nome}"

def mensagem_longa(nome):
    print("executando mensagem longa")
    return f"Olá tudo bem com você {nome}?"

def executar(funcao, nome):
    print("executando executar")
    return funcao(nome)

print(executar(mensagem, "Joao"))
print(executar(mensagem_longa, "Joao"))

## FUNÇÃO INTERNA:

def principal():
    print("executando a funcao principal")

    def funcao_interna():
        print("executando a função interna")

    def funcao_2():
        print("executando a função 2")

    funcao_interna()
    funcao_2()

principal()