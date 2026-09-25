#Exercício 10
#Escreva um conversor de moedas com menu. O programa deve exibir as opções 1 - Real
#para Dólar e 2 - Dólar para Real e ler a opção escolhida. Se a opção não for 1 nem 2, deve
#exibir Opção inválida. e encerrar. Caso contrário, deve ler o valor e exibir o resultado da
#conversão com duas casas decimais e a moeda correta. Use a cotação fixa 1 dólar = 5,40
#reais, guardada em uma variável no início do programa



cotacao = 5.40

print("1 - Real para Dólar")
print("2 - Dólar para Real")

opcao = int(input("Escolha uma opção: "))

if opcao == 1:
    valor = float(input("Digite o valor em reais: "))
    resultado = valor / cotacao
    print(f"Resultado: ${resultado:.2f}")

elif opcao == 2:
    valor = float(input("Digite o valor em dólares: "))
    resultado = valor * cotacao
    print(f"Resultado: R$ {resultado:.2f}")

else:
    print("Opção inválida.")
