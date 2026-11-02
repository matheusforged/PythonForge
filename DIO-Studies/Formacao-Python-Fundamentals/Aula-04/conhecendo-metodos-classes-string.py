# Maiúscula, minúscula e título
curso = "pYtHon"

# Maiúcula
print(curso.upper())
# Minuscula
print(curso.lower())
# Todos minusculos menos a primeira letra
print(curso.title())


# Eliminando espaços em branco

curso = "     Python"

print(curso.strip()) # Tirar os espaços (All)
print(curso.lstrip()) # Tirar os espaços da esquerda (Left)
print(curso.rstrip()) # Tirar os espaços da direita (Right)

# Junções e centralização
curso = "Python"

print(curso.center(10, "#")) # Retorna uma string com a quantidade de caracteres informado com o texto no centrot
# resultado: "##Python##"

print(".".join(curso))
# resultado: "P.y.t.h.o.n"

print(curso[::-1])