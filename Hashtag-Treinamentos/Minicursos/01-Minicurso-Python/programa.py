
import pandas as pd
import win32com.client as win32
from pathlib import Path


# ==================================================
# 1. CONFIGURAÇÕES
# ==================================================

pasta_projeto = Path(__file__).resolve().parent
arquivo_excel = pasta_projeto / "Vendas.xlsx"

destinatario = "matheus@hadeon.dev.br"
assunto = "Relatório de Vendas por Loja"


# ==================================================
# 2. IMPORTAÇÃO DA BASE DE DADOS
# ==================================================

if not arquivo_excel.exists():
    raise FileNotFoundError(
        f"Arquivo não encontrado: {arquivo_excel}"
    )

tabela_vendas = pd.read_excel(arquivo_excel)

# Configuração para visualização no console
pd.set_option("display.max_columns", None)


# ==================================================
# 3. TRATAMENTO E ANÁLISE DOS DADOS
# ==================================================

# Agrupar as vendas por loja e calcular os indicadores
relatorio = (
    tabela_vendas
    .groupby("ID Loja", as_index=False)
    .agg(
        Faturamento=("Valor Final", "sum"),
        Quantidade=("Quantidade", "sum")
    )
)

# Calcular o ticket médio por unidade vendida
relatorio["Ticket Médio"] = (
    relatorio["Faturamento"] / relatorio["Quantidade"]
)

# Ordenar pelo faturamento, do maior para o menor
relatorio = relatorio.sort_values(
    by="Faturamento",
    ascending=False
)

print(relatorio)


# ==================================================
# 4. FORMATAÇÃO DAS TABELAS HTML
# ==================================================

# Criar cópias para não alterar os dados originais
faturamento = relatorio[["ID Loja", "Faturamento"]].copy()
quantidade = relatorio[["ID Loja", "Quantidade"]].copy()
ticket_medio = relatorio[["ID Loja", "Ticket Médio"]].copy()

# Formatar valores monetários no padrão brasileiro
def formatar_moeda(valor):
    return (
        f"R$ {valor:,.2f}"
        .replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )

faturamento["Faturamento"] = faturamento["Faturamento"].apply(
    formatar_moeda
)

ticket_medio["Ticket Médio"] = ticket_medio["Ticket Médio"].apply(
    formatar_moeda
)

# Converter DataFrames para HTML
faturamento_html = faturamento.to_html(
    index=False,
    border=0,
    justify="center"
)

quantidade_html = quantidade.to_html(
    index=False,
    border=0,
    justify="center"
)

ticket_medio_html = ticket_medio.to_html(
    index=False,
    border=0,
    justify="center"
)


# ==================================================
# 5. CONSTRUÇÃO DO E-MAIL
# ==================================================

html_email = f"""
<html>
<head>
<style>
    body {{
        font-family: Arial, sans-serif;
        color: #333333;
        font-size: 14px;
    }}

    h3 {{
        color: #1F4E78;
        margin-top: 25px;
    }}

    table {{
        border-collapse: collapse;
        width: 80%;
        margin-bottom: 20px;
    }}

    th {{
        background-color: #1F4E78;
        color: white;
        padding: 10px;
        text-align: center;
    }}

    td {{
        border: 1px solid #dddddd;
        padding: 8px;
        text-align: center;
    }}

    tr:nth-child(even) {{
        background-color: #f2f2f2;
    }}
</style>
</head>

<body>

<p>Prezados,</p>

<p>
Segue o relatório de desempenho das vendas por loja.
</p>

<h3>Faturamento por Loja</h3>
{faturamento_html}

<h3>Quantidade Vendida por Loja</h3>
{quantidade_html}

<h3>Ticket Médio por Loja</h3>
{ticket_medio_html}

<br>

<p>Atenciosamente,</p>
<p><b>Matheus</b></p>

</body>
</html>
"""


# ==================================================
# 6. ENVIO DO E-MAIL PELO OUTLOOK
# ==================================================

try:
    outlook = win32.Dispatch("Outlook.Application")

    mail = outlook.CreateItem(0)

    mail.To = destinatario
    mail.Subject = assunto
    mail.HTMLBody = html_email

    mail.Send()

    print("E-mail enviado com sucesso!")

except Exception as erro:
    print(f"Erro ao enviar o e-mail: {erro}")
