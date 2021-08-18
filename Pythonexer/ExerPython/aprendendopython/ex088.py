from random import sample
from time import sleep
marcador = 30 * '\033[32m#\033[m'
print(marcador)
lista = list()
cont = 1
print('\033[33mMEGA-SENA ACUMULADA!!!\033[m')
print(marcador)
num = int(input('Quantos jogos quer ?'))

for y in range(0, num):
    sorteados = sample(range(1, 60), 6)
    sorteados.sort()
    lista.append(sorteados[:])
    sorteados.clear()
print(f'Os {num} jogos sorteados foram:')
for x in lista:
    print(f'Jogo {cont}: {x}')
    cont+=1
    sleep(1)
print(f'{marcador}BOA-SORTE!!!{marcador}')