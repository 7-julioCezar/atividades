#7. Escreva media(a, b, c), que devolve a média das três notas, e situacao(nota), que devolve
#"aprovado" para 7 ou mais, "recuperação" para 5 ou mais e "reprovado" abaixo disso. Depois
#imprima a situação de três alunos usando uma função dentro da outra.

def media(a,b,c):
    media = (a + b + c) / 3
    return media

def situacao(nota):
    if nota >= 7:
        return "aprovado"
    elif nota >= 5:
        return "recuperação"
    else:
        return "reprovado"

# Imprimindo a situação de três alunos
print(f"Situação do aluno 1: {situacao(media(10,10,10))}")
print(f"Situação do aluno 2: {situacao(media(6,7,8))}")
print(f"Situação do aluno 3: {situacao(media(4,5,6))}")