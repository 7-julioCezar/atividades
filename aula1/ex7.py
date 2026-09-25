#Exercício 7
#Leia três notas. Calcule a média e exiba-a com duas casas decimais. Em seguida, informe a
#situação: média de 7 ou mais é APROVADO; de 4 a 6,9 é RECUPERAÇÃO; abaixo de 4 é REPROVAD

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print(f"Média: {media:.2f}")

if media >= 7:
    print("APROVADO")
elif media >= 4:
    print("RECUPERAÇÃO")
else:
    print("REPROVADO")
