num1 = int( input('Digite um num: ') )
num2 = int( input('Digite outro num: ') )

op = 99
while op != 5:
    print('1) Soma')
    print('2) Diminuir')
    print('3) Mult')
    print('4) Div')
    print('5) Sair')

    op = int(input('Escolha uma OP: ') )

    if op == 1:
        print('Soma: {}' .format(num1 + num2))
    elif op == 2:
            print('Dim: {}' .format(num1 - num2))
    elif op == 3:
            print('Mult: {}' .format(num1 * num2))
    else:
            print('Div: {}' .format(num1 % num2))