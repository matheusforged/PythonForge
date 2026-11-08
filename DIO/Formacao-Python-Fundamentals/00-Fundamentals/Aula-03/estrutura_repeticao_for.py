# O que são estruturas de repetição?
## São estruturas utilizadas para repetir um trecho de código um determinado número de vezes. 
## Esse número pode ser conhecido previamente ou determinado atraves de uma expressão lógica.

# for

texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

print() # adiciona uma quebra de linha

# for/else

texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print() # adiciona uma quebra de linha
    print("Executa")

# função range
## range(stop) -> range object
## range(start, stop[, step]) -> range object

list(range(4))
[0, 1, 2, 3]

for numero in range(0, 11):
    print(numero, end=" ")

# exibindo a tabuada do 5
for numero in range(0, 51, 5):
    print(numero, end=" ")

