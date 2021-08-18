n = int(input('Informe o número para revelar se é primo ou não'))
contador:int = 0
for z in range(1, n+1):
    if n % z == 0:
        print('\033[32m{}\033[m'.format(z), end = ' ')
        contador += 1
    else:
        print('\033[31m{}\033[m'.format(z), end=' ')
if contador == 2 or n == 1:
    print('\nO número {} \033[32mé\033[m primo.'.format(n))
else:
    print('\nO número {} \033[31mnão\033[m é primo'.format(n))
