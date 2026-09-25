#Exercício 2
#Leia a base e a altura de um retângulo. Calcule e exiba a área e o perímetro, ambos com duas
#casas decimais.

base = float(input("digite a base de um retângulo: "))
altura = float(input("Digite a altura de um retângulo: "))

area = base * altura
perimetro = 2 * (base + altura)

print(f"A area total do retângulo é {area:.2f}")
print(f"O perimetro do retângulo é {perimetro:.2f}")
