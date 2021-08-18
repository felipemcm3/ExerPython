'''resposta = 'Ss'
n = 0
par = 0
impar = 0
while resposta in 'Ss':
    n =int(input('Informe o valor'))
    resposta = input('Informe se quer continuar S/N')
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
print('Você digitou {} pares e {} impares'.format(par, impar))
'''
junto = 'FelipeManoel'
print(junto[6:12])