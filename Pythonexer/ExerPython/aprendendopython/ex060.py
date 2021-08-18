#Jeito com funcao
'''
from math import factorial
num = int(input('Informe o número para imprimir o fatorial'))
fator = factorial(num)
print(fator)
'''

#Jeito hard core ;)
num = int(input('Informe o número para mostrar o fatorial'))
print('O fatorial de {}! é:'.format(num), end = ' ')
aux = num -1
soma = 0
while aux != 0:
    if soma == 0:
        soma = num * aux
        print('{}x{}'.format(num,aux), end ='')
    elif soma != 0:
        soma *= aux
        print('x{}'.format(aux), end='')
    aux -= 1
print('={}'.format(soma))

