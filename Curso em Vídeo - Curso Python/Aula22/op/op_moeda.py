def resumo(valor, aumento, decremento):
    print(f'O aumento de {aumento}% fica: {aumentar(valor, aumento, 1)}')
    print(f'O decremento de {decremento}% fica: {diminuir(valor, decremento, 0)}')
    print(f'A metade é: {metade(valor, 1)}')
    print(f'O dobro é: {dobro(valor, 0)}')


def aumentar(valor, aumento, formatado):
    res = valor + ( (valor * aumento) / 100)
    if formatado:
        return formatando(res)
    return res

def diminuir(valor, decremento, formatado):
    res = valor - ( (valor * decremento) / 100)
    if formatado:
        return formatando(res)
    return res


def dobro(valor, formatado):
    res = 2 * valor
    if formatado:
        return formatando(res)
    return res


def metade(valor, formatado):
    res = valor / 2
    if formatado:
        return formatando(res)
    return res


def formatando(valor):
    return str(f'R${valor}')