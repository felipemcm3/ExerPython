from ex111.utilidadesCeV import moeda
marcador = 30 * '\033[33m-=\033[m'
print(marcador)
print('BEM-VINDO')
num = int(input('Informe um valor'))
print(marcador)
moeda.resumo(num)
print(marcador)
