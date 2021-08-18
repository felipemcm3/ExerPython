from random import randint
menor = maior = 0


lista = (randint(-100,100), randint(-100,100), randint(-100,100),
         randint(-100,100), randint(-100,100))

print(f'Os valores da tupla são:', end = ' ')
for u in lista:
 print(f'{u}', end = ' ')

for c in range(5):
    if c == 0 or lista[c] < menor:
        menor = lista[c]
    elif lista[c] > maior:
        maior = lista[c]
print(f'\nO menor valor é {menor} e maior é {maior}')
