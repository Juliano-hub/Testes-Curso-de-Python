# dicionários

# biblioteca para gerar os números aleatórios
import random
from time import sleep
from operator import itemgetter

"""
dados = dict()
dados = {'nome': 'Pedro', 'idade': 30}
print(dados['nome'])
print(dados['idade'])

dados['sexo'] = 'M'

del dados['idade']

filme = {
    'titulo': 'ABC',
    'ano': 7987,
    'diretor': 'CBA'
}

print(filme.values())
print(filme.keys())
print(filme.items())

for k,v in filme.items():
    print(f'O (k) é (v)')

------------------------------------------------------------

pessoas = {'nome': 'Gus', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]}')

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
estado3 = {'uf': 'Rio Grande do Sul', 'sigla': 'RS'}
brasil.append(estado1)
brasil.append(estado2)
brasil.append(estado3)

    #o primeiro campo ele pega o indice dos cadastros em si e no segundo ele pega o atributo desejado
print(brasil[0])
print(brasil[2]['sigla'])

estado_ler = dict()
brasil_ler = list()

for i in range(0, 3):
    estado_ler['uf'] = str(input('Unidade Federativa: '))
    estado_ler['sigla'] = str(input('Sigla do Estado: '))

    # usa o estado_ler.copy pois ele iria preencher o mesmo dado de 0 a 2
    # se não tivesse isto no caso do dicionário
    brasil_ler.append(estado_ler.copy())
    
for j in brasil_ler:
    for v in j.values():
        print(v)


#--------------------------------------
Aluno = dict()
Lista_Alunos = list()

Aluno['Nome'] = str(input('Nome: '))
Aluno['Média'] = int(input('Média: '))

Lista_Alunos.append(Aluno.copy())

    #o primeiro campo ele pega o indice dos cadastros em si e no segundo ele pega o atributo desejado
if Lista_Alunos[0]['Média'] >= 7:
    print('Nota de Aprovação')
else:
    print('Nota de Reprovação')   
"""

Jogador = dict()
Lista_Jogadores = list()

for i in range(0, 5):
                            # utiliza a biblioteca random
    Jogador['Nome'] = str( f'Jogador{i}' )
    Jogador['Valor_Dado'] = int( random.randrange(1, 6) )
                            # adiciona o dado gerado para a lista de jogadores
    Lista_Jogadores.append(Jogador.copy())

# Lista_Jogadores.sort()
print('Valores dos dados:')
for j in range(0, 5):
    print(f'O {Lista_Jogadores[j]["Nome"]} tirou: {Lista_Jogadores[j]["Valor_Dado"]}')

    # usa com o import do sleep
    sleep(1)

#--------------------------------------

jogador_fut = dict()
Partidas = list()

jogador_fut['nome'] = input('Nome: ')
Total_partitas = input(f'Quantodas partidas {jogador_fut["nome"]} jogou?')

for i in range(0, Total_partitas):
    Partidas.append(int(input(f'Quantos gols foram feitos na {i} partida?')))

jogador_fut['Gols'] = Partidas[:]
jogador_fut['total'] = sum(Partidas)

print(f'O jogador {jogador_fut["Nome"]} fez um total de {jogador_fut["total"]} gols')

