from random import randint
import os
dados = 0
jogador = dict()
maior = 0
marcador = 30 * '\033[33m*\033[m'

for j in range(1, 5):
    print(marcador)
    print(f'Jogador {j} aperte enter para sortear os dados')
    os.system("pause")
    dados = randint(1, 6)
    jogador[f'jogador{j}'] = dados
    print(f'Jogador{j} fez {dados} pontos')

for i in sorted(jogador, key=jogador.get, reverse=True):
    print(f'Os números foram {jogador[i]}')
    if jogador[i] >= maior:
        maior = jogador[i]
for x, y in jogador.items():
    if y == maior:
        print(f'O jogado {x} ganhou com {y} pontos')
