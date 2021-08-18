lista = ('morango', 'pessego', 'melancia', 'manga', 'uva', 'carro')
vogal = ('a', 'e', 'i', 'o', 'u')

for y in lista:
    print('\nA palavra {} tem vogal '.format(y.upper()), end = ' ')
    for x in vogal:
        try:
            if y.index(x):
                print('{}'.format(x), end = ' ')
        except ValueError:
            continue
