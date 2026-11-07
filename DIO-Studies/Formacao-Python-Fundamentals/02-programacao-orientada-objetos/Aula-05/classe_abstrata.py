# ABC
# Por padrão, o Python não fornece classes abstratas. O Python
# vem com um módulo que fornece a base para definir as classes
# abstratas, e o nome do módulo é ABC. O ABC funciona
# decorando métodos da classe base como abstratos e, em
# seguida, registrando classes concretas como implementações
# da base abstrata. Um método se torna abstrato quando
# decorado com @abstractmethod.

from abc import ABC, abstractmethod, abstractproperty

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV ...")
        print("Ligado!")

    def desligar(self):
        print("Desligando a TV ...")
        print("Desligado!")

    @property
    def marca(self):
        return "LG"

class ControleArCondicionado(ControleRemoto):
    def ligar(self):
            print("Ligando o Ar Condicionado ...")
            print("Ligado!")

    def desligar(self):
        print("Desligando o Ar Condicionado ...")
        print("Desligado!")

    @property
    def marca(self):
        return "Philco"

controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)

control = ControleArCondicionado()
control.ligar()
control.desligar()
print(control.marca)