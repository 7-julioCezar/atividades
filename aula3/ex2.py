#Escreva area_retangulo(largura, altura), que devolve a área. Teste com três pares de valores
#diferentes

def area(alt, larg):
    a = alt * larg
    print(f"A área total é = {a}")

alt = int(input("Digite a altura: "))
larg = int(input("Digite a largura: "))

area(alt, larg)