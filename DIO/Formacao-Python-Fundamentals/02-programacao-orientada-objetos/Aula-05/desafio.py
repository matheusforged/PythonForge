##################################################################################################
# Desafio 1:
##################################################################################################

# Crie uma classe e método para realizar a soma:
num1 = int(input())
num2 = int(input())

class Calculadora:
  def soma(num1, num2):
    return num1 + num2

resultado = Calculadora.soma(num1, num2)
print(resultado)

##################################################################################################
# Desafio 2:
##################################################################################################

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Crie um método para retornar as informações formatas com Nome e Idade:    
    def informacaoPessoa(self):
      print(f"Nome: {self.nome}, Idade: {self.idade}")

# Entrada do usuário
nome = input()
idade = int(input())

# Crie uma instância da pessoa:
p1 = Pessoa(nome, idade)

# Chame o método para retornar as informações formatadas e imprima o resultado:
p1.informacaoPessoa()

##################################################################################################
# Desafio 3:
##################################################################################################

# Crie uma classe para converter temperaturas de Celsius para Fahrenheit e um método que realiza o cálculo de conversão:
class ConversorTemperatura:
  def __init__(self, celsius):
    self.celsius = celsius

  def celsius_para_fahrenheit(self):
    print((self.celsius * 1.8) + 32)

# Entrada do usuário
celsius = float(input())

# Crie uma instância do conversor:
conversor = ConversorTemperatura(celsius)

fahrenheit = conversor.celsius_para_fahrenheit()
