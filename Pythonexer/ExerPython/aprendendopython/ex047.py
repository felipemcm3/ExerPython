marcador = 40 * '\033[35m#\033[m'
print(marcador)
for n in range(1, 51):
    if n % 2 == 0:
        print('Esse numero {} é par entre 1 a 50'.format(n))
print(marcador)
