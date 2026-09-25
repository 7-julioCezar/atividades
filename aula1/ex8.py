#Exercício 8
#Leia nome, peso em quilogramas e altura em metros. Calcule o IMC pela fórmula peso /
#altura² e exiba-o com duas casas decimais, junto da classificação: abaixo de 18,5 é Abaixo do
#peso; de 18,5 a 24,9 é Peso normal; de 25 a 29,9 é Sobrepeso; 30 ou mais éObesidade.

nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso / (altura ** 2)

print(f"Nome: {nome}")
print(f"IMC: {imc:.2f}")

if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif imc < 25:
    print("Classificação: Peso normal")
elif imc < 30:
    print("Classificação: Sobrepeso")
else:
    print("Classificação: Obesidade")
