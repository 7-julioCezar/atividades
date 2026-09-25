#. Escreva contar_vogais(texto), que devolve quantas vogais o texto tem, contando maiúsculas e
#minúsculas. Para "Programação", deve devolver 5.

def contVogais(text):
    contador = 0
    for caractere in text:
        if caractere.lower() in "aeiou":
            contador += 1

    return contador

texto = str(input("Digite uma palavra: "))

print(f"o numero de vogais é igual á {contVogais(texto)}")