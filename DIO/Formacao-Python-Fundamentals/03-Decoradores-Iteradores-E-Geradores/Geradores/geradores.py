# O que são geradores?

# São tipos especiais de iteradores, ao contrário das listas ou
# outros iteráveis, não armazenam todos os seus valores na
# memória.

# São definidos usando funções regulares, mas, ao invés de
# retornar valores usando "return", utilizam "yield".

def meu_gerador(numeros: list[int]):
    for numero in numeros:
        yield numeros * 2

for i in meu_gerador(numeros=[1, 2, 3]):
    print(i)


