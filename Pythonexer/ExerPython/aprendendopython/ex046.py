from time import sleep
marcador = 20 * '\033[31m*\033[32m*\033[33m*\033[m'
print('\033[1;36mBEM-VINDO A QUEIMA DE FOGOS!!!\033[m')
for n in range(10, -1, -1):
    print('Contagem {}!!'.format(n))
    sleep(1)
print('BOOMM!{}'.format(marcador))
