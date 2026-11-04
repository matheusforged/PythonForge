import openpyxl

# Criando uma nova planilha
workbook = openpyxl.Workbook()

# Selecionando a planilha ativa
sheet = workbook.active

# Inserindo dados
sheet["A1"] = "Nome"
sheet["B1"] = "Idade"

sheet["A2"] = "Matheus"
sheet["B2"] = 22

# Salvando o arquivo
workbook.save("teste.xlsx")

print("Planilha criada com sucesso!")