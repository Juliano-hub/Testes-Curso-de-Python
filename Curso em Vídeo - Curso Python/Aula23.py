try:
    a = int(input('Numerador: '))
    b = int(input('Numerador: '))
    r = a/b

# catch
except(ValueError, TypeError):
    print('Algum valor não é válido!!!')
except ZeroDivisionError:
    print('Não tem como dividir por zero!!!')
except KeyboardInterrupt:
    print('Não foi digitado!!!')

else:
    print(f'O resultado é: {r}')
finally:
    print('-----Fim!!!')