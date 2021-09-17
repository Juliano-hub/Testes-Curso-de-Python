A = []
for i in range(5):
    A.append( [7] * 5 )
    
A[4][1] = 5
A[0][4] = 4

print(f'\nMatriz: {A}')

min0 = min(A[0])
print(f'Minimo do A[0][x]: {min0}')
print(f'Posicao do minimo de A[0][x]: {A[0].index(min0)}')

min4 = min(A[4])
print(f'Minimo do A[4][x]: {min4}')
print(f'Posicao do minimo de A[4][x]: {A[4].index(min4)}')