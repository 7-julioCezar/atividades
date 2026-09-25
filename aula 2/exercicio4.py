#Exercício 4
#Leia úm número inteiro positivo e calcúle a soma de todos os números de 1 ate ele.

numero = int (input("Digite um numero"))

soma = 0
for i in range(1, numero + 1):
    print(f"{soma} + {i} = {soma + i}")
    soma += i
print(soma) 