#Exercício 5
#Leia uma temperatura em graus Celsius e converta para Fahrenheit, exibindo o resultado com
#uma casa decimal. Fórmula: F = C × 9 / 5 + 32

celsius = float(input("Digite a temperatura em graus Celsius: "))

temp = (celsius * 9 / 5 + 32)

print(f"a temperatura em fahrenheit {temp:.2f}")
