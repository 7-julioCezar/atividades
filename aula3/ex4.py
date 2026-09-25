# Escreva maior_de_tres(a, b, c), que devolve o maior dos três números, sem usar a função max.
#Teste com o maior valor em cada uma das três posições.

def maior(a,b,c):
    if a > b and a > c:
        return a
    elif b > c and b > a:
       return b
    else:
        return c



i = int(input("Digite o primeiro numero: "))
x = int(input("Digite o segundo numero: "))
y = int (input("Digite o terceiro numero: "))

print(f"O maior numero é {maior(i,x,y)}")

    