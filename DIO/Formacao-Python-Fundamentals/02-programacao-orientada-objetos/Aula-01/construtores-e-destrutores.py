#Método construtor
# O método construtor sempre é executado quando uma nova
# instância da classe é criada. Nesse método inicializamos o
# estado do nosso objeto. Para declarar o método construtor da
# classe, criamos um metodo com o nome _init

class cachorro():
    def __init__(self, name, cor, acordado=True):
        print("Inicializando a classe ...")
        self.name = name
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo a instância da classe.")

    def latir(self):
        print("Auau")

c = cachorro("Chappie", "amarelo, ")
c.latir()

print("Ola mundo")

