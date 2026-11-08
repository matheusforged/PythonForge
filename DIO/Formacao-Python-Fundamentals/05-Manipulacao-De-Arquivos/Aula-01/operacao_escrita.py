arquivo = open(
     r"D:\Git\Repository\PythonForge\DIO-Studies\Formacao-Python-Fundamentals\05-Manipulação-De-Arquivos\Aula-01\write_text.txt",
     "w"
)

arquivo.write("Escrevendo dados em um novo arquivo")
arquivo.writelines(["\n", "Escrevendo", "\n", "um", "\n", "novo", "\n", "texto"]) # .writelines() - lê em formato de lista [].
arquivo.close()