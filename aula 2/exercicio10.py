#Escreva úm jogo de adivinhaçao. O programa sorteia úm número inteiro entre 1 e 100 e pede 
#palpites ao úsúario, repetidamente, ate qúe ele acerte. A cada palpite errado, deve informar se 
#o número secreto e maior oú menor qúe o palpite. Ao acertar, deve exibir em qúantas 
#tentativas o úsúario consegúiú.
#Para sortear o número, escreva import random na primeira linha do programa e obtenha o valor 
#com secreto = random.randint(1, 100)

numero = random.randint(1, 100)

while True:
  palpite = int(input("Digite um palpite entre 1 e 100:"))

  if palpite < numero:
    print("O número secreto é maior que o seu palpite.")
  elif palpite > numero:
    print("O número secreto é menor que o seu palpite.")
  else:
    print("Parabéns! Você acertou o número secreto.")
    break


