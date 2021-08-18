times = ('Palmeiras', 'Atletico-MG', 'Fortaleza', 'Bragantino', 'Atletico-PR', 'Flamengo', 'Ceará',
         'Bahia', 'Fluminense', 'Santos', 'Atletico-GO', 'Corinthias', 'Internacional', 'Juventude',
         'Cuiabá', 'São Paulo', 'Sport', 'América-MG', 'Grêmio', 'Chapecoense', )

print('Os cincos primeiros colocados:')
for c in range(0, 5):
    print(f'{times[c]}')
print('Os quatro ultimos colocados:')
for u in range(16, 20):
    print(f'{times[u]}')
print('Os times em ordem alfabetica:')
print(f'{sorted(times)}')
print('O time Chapecoense está na posição:', end = ' ')
print(times.index('Chapecoense')+1)