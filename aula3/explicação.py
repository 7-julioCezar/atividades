#para que servem as fiunções
#exemplo de criação de uma função

def saudacao():
    print("Bom Dia!")

saudacao()


# o que são parametros ?
#metodo de inserção de dados em uma determinada função 
def cumprimentar(nome):
    print(f"Olá,{nome}")



nome = str (input("Digite o seu nome: "))

cumprimentar(f"{nome}")