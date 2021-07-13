KM = int(input('Digite op Km: '))

if KM <= 80:
    preço = KM * 0.50
else:
    preço = KM * 0.45

    print('Maior que 200Km, pagar R$0.45 per Km: R${}' .format(preço) )