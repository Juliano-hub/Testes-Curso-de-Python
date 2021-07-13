continuar = 1
total = maior_mil = custo_menor = contador_barato = 0

while continuar == 'S':
    nome = str( input('Digite o nome do produto:') )
    preço = float( input('Digite o preço:') )

    total += preço
    contador_barato = 1

    if preço > 1000:
        maior_mil = maior_mil + 1

    if contador_barato == 1:
        custo_menor = preço
        nome_menor = nome
    else:
        if preço < custo_menor:
            custo_menor = preço
            nome_menor = nome           

    continuar = str(input('Continuar?[S/N]'))
    if continuar == 'N':
        break

print(f'O produto mais {nome_menor} é o mais barato com o custo de: {custo_menor}')
print(f'O total da compra é: R${total:.2f}')
print('-----FIM')
    