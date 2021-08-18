numeros = list()
par = list()
impar = list()
escolha = ''
while True:
    numeros.append(int(input('Informe um número')))
    escolha = str(input('Informe S/N para continuar'))
    if escolha in 'Nn':
        break
for y in numeros:
    if y % 2 == 0:
        par.append(y)
    else:
        impar.append(y)
print(f'Você informou esses números: {numeros}')
print(f'São pares {par} ')
print(f'São impares {impar}')
