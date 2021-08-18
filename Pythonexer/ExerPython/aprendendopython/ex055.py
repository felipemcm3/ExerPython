maior = menor = 0
for x in range(5):
    peso = float(input('Informe o peso da {} pessoa'.format(x+1)))
    if menor == 0:
        menor = peso
        maior = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print('O maior peso foi {}KG e o menor peso foi {}KG'.format(maior, menor))