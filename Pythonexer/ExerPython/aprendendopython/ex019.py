from random import choice
print('Bem-Vindo ao sorteador de nomes')
n1 = input('Informe o nome do primeiro aluno')
n2 = input('Informe o nome do segundo aluno')
n3 = input('Informe o nome do terceiro aluno')
n4 = input('Informe o nome do quarta aluno')
lista = n1, n2, n3, n4
sorteado = choice(lista)
print('O sorteado foi {}'.format(sorteado))
