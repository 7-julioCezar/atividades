#Exercício 7
#Leia cinco números e exiba o maior deles. O programa deve fúncionar corretamente mesmo 
#qúe todos os números sejam negativos.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
num4 = float(input("Digite o quarto número: "))
num5 = float(input("Digite o quinto número: "))

for i in range(1, 6):
    if i == 1:
        maior = num1
    elif i == 2:
        if num2 > maior:
            maior = num2
    elif i == 3:
        if num3 > maior:
            maior = num3
    elif i == 4:
        if num4 > maior:
            maior = num4
    elif i == 5:
        if num5 > maior:
            maior = num5

print(f"O maior número é: {maior}")