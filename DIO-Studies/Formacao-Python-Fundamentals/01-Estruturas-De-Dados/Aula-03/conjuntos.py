# set
## Como criar conjuntos?

# O que são conjuntos?
# Um set é uma coleção que não possui objetos repetidos,
# usamos sets para representar conjuntos matemáticos ou
# eliminar itens duplicados de um iterável.

set([1, 2, 3, 1, 3, 4]) # {1, 2, 3, 4}

set("abacaxi") # {"b", "a", "c", "x", "i"}

set(("palio", "gol", "celta", "palio")) #{"gol", "celta", "palio"}

numeros = set([1, 2, 3, 1, 3, 4])
print(numeros) # {1, 2, 3, 4}

letras = set("abacaxi")
print(letras) # {"b", "a", "c", "x", "i"}

carros = set(("palio", "gol", "celta", "palio"))
print(carros) # {"gol", "celta", "palio"}

linguagens = {"python", "java", "python"}
print(linguagens)

# Conjuntos em Python não suportam indexação e nem
# fatiamento, caso queira acessar os seus valores é necessário
# converter o conjunto para lista.

# {}.union
conjunto_a = {1, 2}
conjunto_b = {3, 4}

conjunto_a. union(conjunto_b) # {1, 2, 3, 4}

# {}.intersection
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.intersection(conjunto_b) # {2, 3}

# {}.difference
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a. difference(conjunto_b) # {1}
conjunto_b. difference(conjunto_a) # {4}

# {}.symmetric difference
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.symmetric_difference(conjunto_b) # {1, 4}

# {}.issubset
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

conjunto_a. issubset (conjunto_b) # True
conjunto_b.issubset (conjunto_a) # False

# {}.isdisjoint
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

conjunto_a.isdisjoint(conjunto_b) # True
conjunto_a.isdisjoint(conjunto_c) # False

# {}.add
sorteio = {1, 23}

sorteio.add(25) # {1, 23, 25}
sorteio.add(42) # {1, 23, 25, 42}
sorteio.add(25) # {1, 23, 25, 42}

sorteio

# {}.clear
sorteio = {1, 23}

sorteio # {1,23}
sorteio.clear() 
sorteio # {}

sorteio

# {}.copy
sorteio = {1, 23}

sorteio # {1, 23}
sorteio.copy()
sorteio # {1, 23}

numeros

# {}.discard - Discartar um valor no conjunto
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

numeros # {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
numeros.discard(1)
numeros.discard(45) # {2, 3, 4, 5, 6, 7, 8, 9, 0}

numeros
numeros . pop()
numeros. pop()
numeros

# {}.pop
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

numeros # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
numeros.pop() # 0
numeros.pop() # 1

numeros # {2, 3, 4, 5, 6, 7, 8, 9}

# {}.remove
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

numeros # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
numeros.remove(0) # 0
numeros # {1, 2, 3, 4, 5, 6, 7, 8, 9}

# len
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

len (numeros) # 10

# in
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

1 in numeros # True
10 in numeros # False