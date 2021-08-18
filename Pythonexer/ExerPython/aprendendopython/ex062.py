p = int(input('Informe o primeiro termo'))
r = int(input('Informe a razão da progressão aritimetica'))
aux = 10
cont = 0
print('Imprimindo os 10 primeiros termos:')
while aux != 0:
    print(p, end = ' ')
    p += r
    aux -= 1
    cont += 1
    if aux == 0:
        aux = int(input('\nInforme mais quantos termos quer ver:'))
print('Você consultou {} termos.'.format(cont))
