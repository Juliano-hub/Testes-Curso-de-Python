def ler_valor():
    valido = False

    while not valido:
        valor = str(input('Digite o valor R$')).replace(',', '.')
        if valor.isalpha() or valor.strip() == '':
            print('Não foi válido!')
        else:
            valido = True
            return float(valor)