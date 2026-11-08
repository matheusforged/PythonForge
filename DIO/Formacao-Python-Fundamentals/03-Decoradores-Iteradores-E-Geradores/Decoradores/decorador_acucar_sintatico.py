def meu_decorador(funcao):
    def envelope():
        print("faz algo antes de executar")
        funcao()
        print("faz algo depois de executar")

    return envelope

@meu_decorador # usanndo o decorador apenas com o "@"
def ola_mundo():
    print("Olá mundo!")

ola_mundo()
