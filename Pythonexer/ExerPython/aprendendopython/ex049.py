marcador = 30 * '\033[31m=\033[32m-\033[33m=\033[m'
print(marcador)
print('BEM-VINDO A TABUADA ELETRONICA')
n = int(input('Informe qual tabuada você quer'))
for c in range(1, 11):
    print('{} x {} = {}'.format(n, c, n*c))
print(marcador)
