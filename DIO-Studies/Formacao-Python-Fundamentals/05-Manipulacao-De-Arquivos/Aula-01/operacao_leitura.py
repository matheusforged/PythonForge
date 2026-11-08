arquivo = open(
     r"D:\Git\Repository\PythonForge\DIO-Studies\Formacao-Python-Fundamentals\05-Manipulação-De-Arquivos\Aula-01\lorem.txt"
)
# printa o arquivo inteiro
# print(arquivo.read())

# printa linha a linha do arquivo
# print(arquivo.readline())
# print(arquivo.readline())
# print(arquivo.readline())

# .readline() - Lê o arquivo linha a linha
# .readlines() - Lê o arquivo linha a linha e retorna em lista.

for linha in arquivo.readlines():
    print(linha)

# # tip
# while len(linha := arquivo.readline()):
#     print(linha)

arquivo.close()





