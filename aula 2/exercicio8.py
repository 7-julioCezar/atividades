#Exercício 8
#Leia um número inteiro positivo e conte quantos números pares e quantos números ímpares 
#existem de 1 até ele. Exiba as duas quantidades.

numero = int(input("Digite um número inteiro positivo: "))
pares = 0
ímpares = 0

for i in range(1, numero + 1):
    if i % 2 == 0:
        pares += 1
    else:
        ímpares += 1

print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {ímpares}")