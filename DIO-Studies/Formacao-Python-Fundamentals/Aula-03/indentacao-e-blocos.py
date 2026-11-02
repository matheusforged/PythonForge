#Bloco em Python
# def sacar(self, valor: float): # início do bloco do método

#     if self.saldo >= valor:

#         self.saldo -= valor

# fim do bloco do if

# fim do bloco do método

# inicio do bloco do if

def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("valor sacado!")
        print("retire o seu dinheiro na boca do caixa.")

sacar(100)