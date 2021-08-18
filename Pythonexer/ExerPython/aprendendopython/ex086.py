linha = list()
coluna = list()

for y in range(0, 3):
    for p in range(0, 3):
        coluna.append(int(input(f'Informe um valor para posição [{y}][{p}]')))
    linha.append(coluna[:])
    coluna.clear()
print('Sua matriz ficará assim:')
for x in range(0, 3):
    for w in range(0, 3):
        print(f'[{linha[x][w]:^5}]', end=' ')
    print()

