jog = dict()
gols = list()
marcador = 30 * '\033[31m#\033[m'
jog['nome'] = str(input('Nome do jogador:'))
jog['quapar'] = int(input('Quantas partidas jogadas?'))
for y in range(0, jog['quapar']):
      gols.append(int(input(f'Informe quantos gols na partida {y+1}')))
jog['gol'] = gols[:]
jog['total'] = sum(gols)
print(marcador)
print(jog)
print(marcador)
for x, y in jog.items():
      print(f'Na posicao {x} tem o item {y}')
print(marcador)
print(f'O jogador {jog["nome"]} jogou {jog["quapar"]} partidas')
for x, y in jog.items():
      if x == 'gol':
            for u, o in enumerate(y):
                  print(f'Na partida {u+1} fez {o} gols')
print(f'No total foram {jog["total"]} gols')
'''
print(f'O jogador {jog["nome"]} jogou {jog["quapar"]} partidas')
for x, y in enumerate(gols):
      print(f'\t=>Na partida {x+1} fez {y} gols')
print(f'No total foram {jog["total"]} gols')
'''