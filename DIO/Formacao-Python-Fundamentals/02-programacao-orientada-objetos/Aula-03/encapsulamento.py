# O que é Encapsulamento?

# Protecão de acesso
# O encapsulamento e um dos conceitos fundamentais em
# programação orientada a objetos. Ele descreve a ideia de
# agrupar dados e os métodos que manipulam esses dados em
# uma unidade. Isso impõe restrições ao acesso direto a variáveis
# e métodos e pode evitar a modificação acidental de dados.
# Para evitar alterações acidentais, a variável de um objeto só
# pode ser alterada pelo método desse objeto.

# Modificadores de acesso
# Em linguagens como Java e C++, existem palavras reservadas
# para definir o nível de acesso aos atributos e métodos da
# classe. Em Python não temos palavras reservadas, porém
# usamos convenções no nome do recurso, para definir se a
# variável é pública ou privada.

# Definição
# · Público: Pode ser acessado de fora da classe.
# · Privado: Só pode ser acessado pela classe.

class conta:
    def __init__(self, nro_agencia, saldo=0):
        self.nro_agencia = nro_agencia
        self._saldo = saldo
       

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    def mostrar_saldo(self):
        return self._saldo

Conta = conta("0001", 100)
Conta.depositar(100)

print(Conta.nro_agencia)
print(Conta.mostrar_saldo())

