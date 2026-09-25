#Escreva somente_digitos(texto), que devolve apenas os dígitos do texto recebido, e 
#telefone_valido(telefone), que devolve True quando o telefone tem 10 ou 11 dígitos. A segunda 
#deve usar a primeira. Teste com "(49) 99999-0001", "49 3246-0000" e "123".

def somente_digitos(texto):
    return "".join(caractere for caractere in texto if caractere.isdigit())

def telefone_valido(telefone):
    digitos = somente_digitos(telefone)

    return len(digitos) in (10, 11)


print(telefone_valido("(49) 99999-0001"))
print(telefone_valido("49 3246-0000"))  
print(telefone_valido("123"))            