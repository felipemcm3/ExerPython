p = int(input('Informe o primeiro termo da PA'))
r = int(input('Informe a razão da Progressão Aritimetica'))
aux = 0
print('A progressão aritimetica de {} com razão {} é:'.format(p, r))
while aux != 10:
    print(p, end = ' ')
    p += r
    aux += 1