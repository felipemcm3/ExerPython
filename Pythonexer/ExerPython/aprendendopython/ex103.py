def ficha(jog = "Jogador", gols = 0):
    return f'{jog} fez {gols} gols'


nome = str(input('Informe o nome do jogador (caso não queira aperte enter)')).strip()
pontos = str(input('Informe quantos gols ele fez (caso não queira aperte enter)')).strip()
if pontos.isnumeric():
    pontos = int(pontos)
else:
    pontos = 0
if nome == '':
    print(ficha(gols=pontos))
else:
    print(ficha(nome, pontos))

