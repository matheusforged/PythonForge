import os
import shutil
import sys
from pathlib import Path

ROOT_PATH = Path(__file__).parent
diretorio_projeto = "novo-diretorio"

# os.mkdir(ROOT_PATH / diretorio_projeto)

arquivo = open(ROOT_PATH / "novo.txt", "w")
arquivo.close()

# arquivo_path = Path(__file__).parent

# os.rename(ROOT_PATH / "novo.txt", ROOT_PATH / "nome_alterado.txt")

# os.remove(ROOT_PATH / "nome_alterado.txt")

shutil.move(ROOT_PATH / "novo.txt", ROOT_PATH / "novo-diretorio" / "novo.txt")

