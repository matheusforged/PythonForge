# Herança múltipla
# Quando uma classe filha herda de várias classes pai, ela é
# chamada de herança múltipla.

#########################################################################################
# Exemplo Herança Múltipla:
#########################################################################################

class animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
            return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class mamifero(animal):
    def __init__(self, cor_pelo, **kw):
            self.cor_pelo = cor_pelo
            super().__init__(**kw)

class ave(animal):
    def __init__(self, cor_bico, **kw):
            self.cor_bico = cor_bico
            super().__init__(**kw)

class cachorro(mamifero):
    pass

class gato(mamifero):
    pass

class leao(mamifero):
    pass

class ornitorrinco(mamifero, ave):
    pass


# gato1 = gato(4, "laranja")
# print(gato1)

ornitorrinco1 = ornitorrinco(nro_patas= 4, cor_pelo= "Marrom", cor_bico="Laranja")
print(ornitorrinco1)