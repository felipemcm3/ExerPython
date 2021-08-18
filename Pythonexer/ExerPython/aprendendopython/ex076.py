marcador = 50 * '\033[33m-\033[m'
print(marcador)
print('Lista de preços')
print(marcador)
produtos = ('macarrão', 3.99, 'arroz', 8.99, 'suco', 3.00, 'carne', 15.00)

for y in range(0,8,2):
    print('{:}{:.>20}'.format(produtos[y], produtos[y+1]))
