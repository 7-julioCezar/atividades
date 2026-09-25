#10.Escreva formatar_telefone(telefone), que devolve "(49) 99999-0001" a partir de 
#"49999990001". A função deve tratar telefones de 11 e de 10 dígitos, reaproveitar somente_digitos do 
#exercício anterior e devolver o telefone sem alteração quando ele não tiver nenhum desses dois 

def somente_digitos(texto):
    return "".join(caractere for caractere in texto if caractere.isdigit())


def formatar_telefone(telefone):
    digitos = somente_digitos(telefone)
   
    if len(digitos) == 11:
        return f"({digitos[:2]}) {digitos[2:7]}-{digitos[7:]}"
    
    elif len(digitos) == 10:
        return f"({digitos[:2]}) {digitos[2:6]}-{digitos[6:]}"
  
    return telefone


print(formatar_telefone("49999990001"))  
print(formatar_telefone("4932460000"))   
print(formatar_telefone("12345"))       