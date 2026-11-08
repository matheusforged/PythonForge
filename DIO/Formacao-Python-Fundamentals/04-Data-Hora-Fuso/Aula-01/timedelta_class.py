from datetime import datetime, timedelta, date

tipo_carro = "M" # "P", "M", "G"
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()


if tipo_carro == "P":
    data_estimanda = data_atual + timedelta(minutes=tempo_pequeno)
    print(f"O carro chegou: {data_atual} e ficará pronto ás {data_estimanda}")
elif tipo_carro == "M":
    data_estimanda = data_atual + timedelta(minutes=tempo_medio)
    print(f"O carro chegou: {data_atual} e ficará pronto ás {data_estimanda}")
else:
    data_estimanda = data_atual + timedelta(minutes=tempo_grande)
    print(f"O carro chegou: {data_atual} e ficará pronto ás {data_estimanda}")

print( date.today() - timedelta(days=1))

resultado = datetime(2026, 11, 8, 16, 7, 00) - timedelta(hours=1)
print(resultado)