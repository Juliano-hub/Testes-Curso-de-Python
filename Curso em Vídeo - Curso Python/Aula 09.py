frase = 'Teste do curso em Python'
print(frase[0:7])
print('quant: ', frase.count('o'))

frase = frase.replace('Python', 'C')
print(frase)
print('C' in frase, 'na posição', frase.find('C'))

nome = 'Axes furdado'
maiusculas = format(nome.upper())
print(maiusculas)

print('tam sem espaços:', len(nome) - nome.count(' ') )