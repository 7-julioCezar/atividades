#Escreva ao_contrario(texto), que devolve o texto de trás para frente. Para "Python", deve devolver
#"nohtyP".

def inversor(text):
    invertida = ""
    for letra in text:
        invertida = letra + invertida
    print(f"a palvra invertido, fica igual á {invertida}")


palavra = str(input("Digite uma palavra: "))
inversor(palavra)