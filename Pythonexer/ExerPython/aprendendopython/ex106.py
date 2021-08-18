marcador = 50 * '#'
print(f'\33[7:32:40m{marcador}')
print('\033[7:32:40mBEM-VINDO AO SISTEMA DE AJUDA DO PYTHON')
while True:
    variavel = str(input('\033[32:41mInforme o nome da funcao'))
    if variavel == 'FIM' or variavel == 'fim':
        break
    else:
        print(f'\033[7:34:47m{help(variavel)}\033[m')
