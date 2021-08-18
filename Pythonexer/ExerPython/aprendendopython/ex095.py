jog = dict()
gols = list()
jogadores = list()
x = 0
marcador = 30 * '\033[31m#\033[m'
print(marcador)
while True:
    jog['nome'] = str(input('Nome do jogador:'))
    jog['quapar'] = int(input('Quantas partidas jogadas?'))
    for y in range(0, jog['quapar']):
          gols.append(int(input(f'Informe quantos gols na partida {y+1}')))
    jog['gol'] = gols[:]
    jog['total'] = sum(gols)
    gols.clear()
    jogadores.append(jog.copy())
    escolha = str(input('Informe S/N para continuar'))
    if escolha in 'Nn':
        break
print(marcador)

for y in range(0, len(jogadores)):
    print(f'NºJogador{y}\t{jogadores[y]["nome"]}\tGols{jogadores[y]["gol"]}'
          f'\tTotal {jogadores[y]["total"]}')
print(marcador)
while True:
    x = int(input('Qual jogador quer mostrar?(999 para o loop)'))
    if x == 999:
        break
    while x > len(jogadores):
        x = int(input('Você informou o número fora da faixa de jogadores'))
    print(f'O jogador {jogadores[x]["nome"]}')
    for o in range(0, len(jogadores[x]["gol"])):
        print(f'Jogo {o} gols {jogadores[x]["gol"][o]}')
    print(marcador)
