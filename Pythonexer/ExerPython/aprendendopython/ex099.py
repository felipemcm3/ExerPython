from random import sample
from time import sleep
def maior(num, x):
    print(f'Foi sorteado {x} numeros sendo o maior {max(num)}')
    sleep(1)

marcador = 40 * '\033[31m#\033[m'
print(marcador)
lista = list()
i = int(input('Informe quantas vezes quer sortear os números'))
for y in range(i, 0, -1):
    lista = sample(range(100), y)
    print('Os numeros sorteados foram:',end=' ')
    for v in lista:
        print(v, end=' ')
        sleep(1)
    maior(lista, y)
    print(marcador)
print('OBRIGADO!')