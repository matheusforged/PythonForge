# Tuplas são definidas usando parenteses
# Tuplas não podem ser alteradas

frutas = ("laranja", "pera", "uva",)

letras = tuple("python")

numeros = tuple([1, 2, 3,4])

pais =("Brasil",)

#Exemplo
frutas = ("maçã", "laranja", "uva", "pera",)
frutas[0] # maçã
frutas [2] # uva

# Exemplo
frutas = ("maçã", "laranja", "uva", "pera",)
frutas[-1] # pera
frutas [3] # laranja

# Matrizes com tuplas

matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5,"c"),
)

matriz[0][0] # (1, "a", 2)
matriz[0] [-1] # 1
matriz[-1] [-1] # 2
matriz[0] # "c"

# Fatiamento com tupla

tupla = ("p", "y", "t", "h", "o", "n",)

tupla[2: ] # ("t", "h", "o", "n")
tupla[:2] # ("p", "y")
tupla[1:3] # ("y", "t")
tupla[0:3:2] # ("p", "t")
tupla[ : : ] # ("p", "y", "t", "h", "o", "n")
tupla[ ::- 1] # ("n", "o", "h", "t", "y", "p")

carros =("gol", "celta", "palio",)

for carro in carros:
    print(carro)

#Metodos de classe tuple

## ().count
cores = ("vermelho", "azul", "verde", "azul",)

cores.count("vermelho") # 1
cores.count("azul") # 2
cores.count("verde") # 1

## ().index
linguagens = ("python", "js", "c", "java", "csharp",)

linguagens. index("java") # 3
linguagens.index("python") # 0

## len
linguagens = ("python", "js", "c", "java", "csharp",)
len(linguagens) # 5


carros = ("gol") 
print(isinstance(carros, tuple))