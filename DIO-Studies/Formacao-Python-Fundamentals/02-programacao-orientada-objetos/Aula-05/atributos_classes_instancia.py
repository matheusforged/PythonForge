

# Atributos do objeto
# Todos os objetos nascem com o mesmo número de atributos
# de classe e de instância. Atributos de instância são diferentes
# para cada objeto (cada objeto tem uma cópia), já os atributos
# de classe são compartilhados entre os objetos.

class estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"{self.nome} - {self.matricula} - {self.escola}"

    
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)


aluno_1 = estudante("Matheus", 1)
aluno_2 = estudante("Arthur", 2) 

mostrar_valores(aluno_1, aluno_2)
mostrar_valores(aluno_1, aluno_2) 

aluno_1.matricula = 3

mostrar_valores(aluno_1, aluno_2) 
