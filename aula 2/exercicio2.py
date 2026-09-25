#Exercício 2
#Leia úm número inteiro e exiba a tabúada dele, de 1 a 10, no formato 7 x 3 = 21.

numero = int (input("Digite um numero inteiro:"))

for i in range(1,11):
  resultado = numero * i
  print(f"{numero} x {i} = {resultado}")
