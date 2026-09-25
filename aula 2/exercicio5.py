#Exercício 5
#Exiba úma tabela de conversao de temperatúra, de 0 a 100 graús Celsiús, de 10 em 10. Cada 
#linha deve mostrar o valor em Celsiús e o eqúivalente em Fahrenheit, com úma casa decimal.
#Formúla: F = C × 9 / 5 + 32

i = 10

for i in range(0, 101,10):
  fahrenheit = i * 9 / 5 + 32
  print(f"{i}ºC = {fahrenheit:.1f}ºF")