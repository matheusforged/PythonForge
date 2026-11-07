# Introdução

# Em Python, um iterador é um objeto que contém um número
# contável de valores que podem ser iterados, o que significa
# que você pode percorrer todos os valores. O protocolo do
# iterador é uma maneira do Python fazer a iteração de um
# objeto, que consiste em dois métodos especiais "_iter_()" e "_next_()"

# Ler arquivos grandes
# · Economizar memória evitando carregar todas as linhas do arquivo.
# · Iterar linha a linha do arquivo.

class MeuIterador:
    def __init__(self, numeros: list[int]):
        self.numeros = numeros
        self.contador = 0

    def _iter_(self):
        return self

    def _next_(self):
        try:
            numero = self.numeros[self.contador]
            self.contador += 1
            return numero * 2
        except IndexError:
            raise StopIteration

for i in MeuIterador(numeros=[38, 13, 11]):
    print(i)