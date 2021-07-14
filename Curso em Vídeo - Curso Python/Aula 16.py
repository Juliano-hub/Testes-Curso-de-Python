# tupla

Palavras = ('Python', 'Curso', 'Teste', 'C', 'Video', 'Escrever')

for i in range(0, len(Palavras) ):
    print(f'A palavra {Palavras[i]} tem as vogais:')

    if Palavras[i].find('a') == 1:
        print(' a')

    if Palavras[i].find('e') == 1:
        print(' e')

    if Palavras[i].find('i') == 1:
        print(' i')

    if Palavras[i].find('o') == 1:
        print(' o')

    if Palavras[i].find('u') == 1:
        print(' u')