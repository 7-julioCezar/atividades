#Exercício 6
#Leia um número inteiro e informe se ele é par ou ímpar. Se for zero, exiba a mensagem O
#número é zero.

num = int(input("Digite um numero"))

if num % 2 == 0:
    print("Numero par")
else:
    print("numero impar")