soma = 0
for c in range(6):
    n = int(input('Informe um número'))
    if n % 2 == 0:
        soma += n
print('A soma dos números pares é {}'.format(soma))
