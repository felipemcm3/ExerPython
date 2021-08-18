coluna = list()
linha = list()
par = maior = soma = 0
for y in range(0, 3):
    for x in range(0, 3):
        coluna.append(int(input(f'Informe o valor da posição [{y}][{x}]')))
        if coluna[x] % 2 == 0:
            par += coluna[x]
        if y == 1:
            if x == 0:
                maior = coluna[x]
            elif coluna[x] > maior:
                maior = coluna[x]
        if x == 2:
            soma += coluna[x]

    linha.append(coluna[:])
    coluna.clear()
print('Sua matriz ficou assim:')
for y in range(0, 3):
    for x in range(0, 3):
        print(f'[{linha[y][x]:^5}]', end=' ')
    print()
print(f'A soma dos valores pares da matriz é {par}')
print(f'A soma dos valores da terceira coluna é {soma}')
print(f'O maior valor da segunda linha é {maior}')