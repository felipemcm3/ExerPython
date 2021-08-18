import moeda
marcador = 30 * '\033[33m-=\033[m'
print(marcador)
print('BEM-VINDO')
num = int(input('Informe um valor'))
print(marcador)
print(f'O dobro do número {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}')
print(f'A metade do número {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}')
print(f'O valor aumentado em 10% ficará {moeda.moeda(moeda.aumentar(num))}')
print(f'O valor diminuido em 13% ficará {moeda.moeda(moeda.diminuir(num))}')
print(marcador)
