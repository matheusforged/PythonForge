# POLIMORFISMO

# Mesmo método com comportamento diferente
# Na herança, a classe filha herda os métodos da classe pai. No
# entanto, é possível modificar uln método em uma classe filha
# herdada da classe pai. Isso é particularmente útil nos casos em
# que o método herdado da classe pai não se encaixa
# perfeitamente na classe filha.

class Passaro:
    def voar(self):
        print("Voando ....")

class Pardal(Passaro):
    def voar(self):
        super().voar()

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")

class Aviao(Passaro):
    def voar(self):
        print("Avião está decolando ... ")

def plano_voo(obj):
    obj.voar()

plano_voo(Pardal())
plano_voo(Avestruz())
plano_voo(Aviao())
