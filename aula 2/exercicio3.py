#Exercício 3
#Leia úm número inteiro e faça a contagem regressiva dele ate 1, exibindo úm número por 
#linha. Ao terminar, exiba a palavra Fim

numero = int (input("Digite um numero inteiro:"))

for i in range(numero, 0, -1):
  print(i)
print("Fim")