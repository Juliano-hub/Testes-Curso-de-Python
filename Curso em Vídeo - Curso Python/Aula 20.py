# funções
# passagem de parâmetro com lista
import random

"""
def soma(num1, num2):
    print(f'{num1 + num2}')

soma(8, 9)

# empacotador em python
# coloca todos os parâmetros que foram dados em uma tupla
def contador( *num ):
    tam = len(num)
    print(f'valores: {num} com um total de {tam}')

contador(2, 1, 7)
contador(1, 2, 3, 5, 4)

def mult(lista):
    for i in range(0, len(lista) ):
        lista[i] *= 2
    print(f'{lista}')

valores = [7, 2, 5, 0, 4]
mult(valores)
mult([9,8,7,6])

#-------------------------------------------------------
def escreva(texto):
    print('~' * len(texto))
    print(f'{texto}')
    print('~' * len(texto))


escreva('Testando')
escreva('É um teste')

#-------------------------------------------

def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1

    if inicio < fim:
        if passo > 0:
            passo *= -1

        i = inicio
        print(f'{inicio}')

        while(i != fim):
            print(f'{i}')
            i += passo

        print(f'{i}')

    else:
        if passo < 0:
            passo *= -1

        i = inicio
        while(i != fim):
            print(f'{i}')
            i -= passo
        
        print(f'{i}')


inicio = int(input('Inicio:'))
fim = int(input('Fim:'))
passo = int(input('Passo:'))    
contador(inicio, fim, passo)

#-------------------------------------------------
def maior(*tupla_nums):
    if len(tupla_nums ) != 0:
        maior = -1
    else:
        maior = 0
    
    for i in range(0, len(tupla_nums) ):
        if tupla_nums[i] > maior:
            maior = tupla_nums[i]
    
    print(f'O maior valor entre os {len(tupla_nums)} num de {tupla_nums} é: {maior}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

#---------------------------------------------------------

def sorteia( lista ):

    for x in range(0, 5):
        lista.append( int( random.randrange(0, 10) ))

def somar_pares( lista ):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f'A soma dos pares é: {soma}')


lista_random = list()
sorteia(lista_random)
print(f'{lista_random}')
somar_pares(lista_random)

"""