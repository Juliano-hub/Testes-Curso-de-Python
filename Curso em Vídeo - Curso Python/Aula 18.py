# Lista p 2 

"""
pessoas = [['Pedro', 25], ['Maria', 19], ['João', 17]]

print(pessoas[2][1])
print(pessoas[1])

for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos' )
"""
contador = 0
matriz = []

while contador < 9:
    num = int( input(f'Digite o num {contador}: ') )
    matriz.append(num)
    contador += 1

for i in range(0, 9, +3):
    print(f'[{matriz[i]}] [{matriz[i+1]}] [{matriz[i+2]}]') 

soma_pares = 0
for i in range(0, 9):
    if matriz[i] % 2 == 0:
        soma_pares += matriz[i] 

print(f'A soma dos valores pares é: {soma_pares}')
print(f'Soma da terceira coluna é: {matriz[2] + matriz[5] + matriz[8]}')

if matriz[3] > matriz[4]:
    maior_valor = matriz[3]
else:
    maior_valor = matriz[4]

if matriz[5] > maior_valor:
    maior_valor = matriz[5]

print(f'Maior valor da segunda linha é: {maior_valor}')

