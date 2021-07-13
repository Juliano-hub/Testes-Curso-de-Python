"""
print('Olá Mundo!')
print('7' + '4')
print('Olá', 5)

nome = 'Teste'
idade = 30
print(nome, idade)

nome_input = input('Qual seu nome?')
idade_input = input('Quantos anos vc tem?')
print(nome_input, idade_input)

comentário em várias linhas
"""

# comentário em 1 linha
msg = 'Teste!'
print(msg)

num1 = input('Digite o primeiro número: ') 
num2 = input('Digite o segundo número: ') 

soma = int(num1) + int(num2)
# faz o cast convertendo para int

print('A soma é: ' , soma)
# usa vírgula para poder colocar mais de um tipo de var no print

ler_nome = input('Qual seu nome?')
input('Olá ' + ler_nome)

dia = input('Qual dia que voce nasceu?')
mes = input('Qual mes que voce nasceu?')
ano = input('Qual ano que voce nasceu?')
input(dia + '/' + mes + '/' + ano)
