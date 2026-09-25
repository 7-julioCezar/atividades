#. Escreva celsius_para_fahrenheit(celsius), que devolve a temperatura em graus Fahrenheit. A
#conversão é celsius * 9 / 5 + 32.
def conversor(celsius):
     fahrenheit = celsius * 9 / 5 + 32
     print(f"{celsius}ºC = {fahrenheit:.1f}ºF")


temp = int(input("Digite a temperatura atual: "))
conversor(temp)