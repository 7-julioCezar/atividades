#Leia notas repetidamente, ate qúe o úsúario digite -1. Ao encerrar, exiba qúantas notas foram 
#informadas e a media delas, com dúas casas decimais. Se nenhúma nota tiver sido informada, 
#exiba Nenhuma nota informada.

nota = float(input("Digite uma nota ou -1 para encerrar: "))
soma = 0
quantidade = 0

while nota != -1:
    soma += nota
    quantidade += 1
    nota = float(input("Digite uma nota ou -1 para encerrar: "))

if quantidade > 0:
    media = soma / quantidade
    print(f"Quantidade de notas informadas: {quantidade}")
    print(f"Média das notas: {media:.2f}")
else:
    print("Nenhuma nota informada.")