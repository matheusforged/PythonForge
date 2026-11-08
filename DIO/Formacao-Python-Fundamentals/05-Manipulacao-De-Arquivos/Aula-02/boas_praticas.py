from pathlib import Path

ROOT_PATH = Path(__file__).parent

# try:
#     with open(ROOT_PATH / "novo-diretorio" / "1novo.txt", "r") as arquivo:
#         print(arquivo.read())
# except FileNotFoundError as exc:
#     print(f'O arquivo não foi encontrado: {exc}')
# except IOError as exc:
#     print(f'Não foi possivel abrir o arquivo: {exc}')

# try:
#     with open(ROOT_PATH / "arquivo-utf-8.txt", "w", encoding="utf-8") as arquivo:
#         arquivo.write("Aprendendo a manipular arquivos utilizando Python.")
# except IOError as exc:
#     print(f"Erro ao abrir o arquivo {exc}")

try:
    with open(ROOT_PATH / "arquivo-utf-8.txt", "w", encoding="ascii") as arquivo:
        print(arquivo.read())
except UnicodeDecodeError as exc:
    print(exc)
except IOError as exc:
    print(f"Erro ao abrir o arquivo {exc}")






