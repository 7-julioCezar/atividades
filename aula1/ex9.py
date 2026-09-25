#Exercício 9
#Leia um ano e informe se ele é bissexto. Um ano é bissexto quando é divisível por 4, exceto se
#for divisível por 100, a menos que também seja divisível por 400. Escreva a condição em uma
#única linha de if.

ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print("Ano bissexto")
else:
    print("Ano não bissexto")
