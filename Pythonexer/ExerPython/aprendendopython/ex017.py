from math import hypot
marcador = 50 * '#'
print(marcador)
print('Bem-Vindo ao calculador de hiptenusa')
c1 = float(input('Informe o tamanho do cateto adjacente'))
c2 = float(input('Informe o tamanho do cateto oposto'))

print('A hipotenuza dos catetos informados é {:.2f}'.format(hypot(c1, c2)))
print(marcador)
