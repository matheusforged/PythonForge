while True:
    numero = int(input("Informe um numero: "))

    if numero == 10:
        break

print(numero)

for numero in range(100):
    if numero == 10:
        break

    print(numero, end="")

for numero in range(100):
    if numero == 10:
        continue

    print(numero, end="")
