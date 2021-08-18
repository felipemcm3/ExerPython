from random import sample

print('Bem-Vindo ao sorteador de ordem!')
n1 = input('Informe o primeiro nome')
n2 = input('Informe o segundo nome')
n3 = input('Informe o terceiro nome')
n4 = input('Informe o quarto nome')
lista = [n1, n2, n3, n4]
sorteados = sample(lista, 4)
print('Os alunos que apresentaram na seguinte ordem'
      '{}'.format(sorteados))
