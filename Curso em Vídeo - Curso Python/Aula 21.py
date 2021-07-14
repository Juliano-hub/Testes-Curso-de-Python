# Parâmetros opcionais

"""
def somar(a=0, b=0, c=0):
    print(f'A soma é: {a+b+c}')

somar()
somar(1, 2)
somar(c=3, b=4)

# Escopo

def teste():
    print(f'A dentro vale {a}')

a = 5
teste(a)

"""
def notas(*nota, sit=False):
    menor = maior = total_notas = media = 0
    for i in nota:
        total_notas += 1
        media += i
        if i > maior:
            maior = i
        elif i < menor:
            menor = i
    
    media = media / len(nota)
    if media >= 7:
        situacao = 'Bom'
    else:
        situacao = 'Ruim'

    retorno = dict()
    retorno['Total'] = total_notas
    retorno['maior nota'] = maior
    retorno['menor nota'] = menor
    retorno['média'] = media
    if sit == True:
        retorno['situação'] = situacao
    return retorno


valores_de_notas = notas(3.5, 2, 6.5, 2, 7, 4, sit=True)
print(f'{valores_de_notas}')