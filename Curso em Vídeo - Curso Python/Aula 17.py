# Listas
""""

num = [2, 5, 9, 1]
num.append(7)
num.insert(10, 0)
num.sort()

print(num)
num.pop( len(num) - 1)
print(num)

for i in num:
    print(i)

"""""
continuar = 'S'
vetor = []

while continuar == 'S':
    num = int( input('Digite um valor: ') )

    if num not in vetor:
        vetor.append(num)

    continuar = input('Continuar?[S/N]')
    if continuar == 'N':
        break

vetor.sort
print(vetor)