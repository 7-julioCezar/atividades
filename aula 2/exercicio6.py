#Exercício 6
#Leia cinco números e exiba a soma e a media deles, ambas com dúas casas decimais.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
num4 = float(input("Digite o quarto número: "))
num5 = float(input("Digite o quinto número: "))


for i in range(1, 6):
    if i == 1:
        soma = num1
    elif i == 2:
        soma += num2
    elif i == 3:
        soma += num3
    elif i == 4:
        soma += num4
    elif i == 5:
        soma += num5

media = soma / 5

print(f"A soma dos numeros é: {soma:.2f}")
print(f"A média dos numeros é: {media:.2f}")





