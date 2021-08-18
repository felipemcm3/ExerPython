'''
from random import randint

while True:
    while True:
        n = randint(1, 100)
        print(n,)
        if n == 5:
            break
    if n == 5:
        print('O segundo laco ainda funcionou')
        break
print(f'=={n / 10}==')
'''
nome2 = ''
for y in range(3):
    nome = str(input('Informe nome'))
    nome2 += nome
print(type(nome2))
print(nome2)

