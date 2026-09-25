#Escreva apresentar(nome, cidade, uf="SC"), que devolve "Ana, de Fraiburgo/SC". Chame a
#função três vezes: uma sem informar a UF, uma informando "PR" por posição e uma informando uf="RS"
#pelo nome. 

def apresentar(nome, cidade, uf="SC"):
    return f"{nome}, de {cidade}/{uf}"

print(apresentar("Ana", "Fraiburgo"))
print(apresentar("Carlos", "Curitiba", "PR"))
print(apresentar("Maria", "Porto Alegre", uf="RS"))