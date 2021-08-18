numeros = [[],[]]
valor = 0

for y in range(0, 7):
    valor = int(input('Informe um número'))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)

numeros[0].sort()
numeros[1].sort()
print(f'Os números pares são: {numeros[0]}')
print(f'Os números impares são: {numeros[1]}')
