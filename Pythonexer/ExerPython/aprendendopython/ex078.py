numeros = []
posmai = list()
posmen = list()

for y in range(5):
    numeros.append(int(input('Informe o número na posição {}\t'.format(y))))
maior = max(numeros)
menor = min(numeros)
for x in range(5):
    if numeros[x] == maior:
        posmai.append(x)
    if numeros[x] == menor:
        posmen.append(x)
print(f'Você digitou {numeros}')
print(f'O maior número é {maior} que esta na posição {posmai}')
print(f'O menor número é {menor} que esta na posição {posmen}')
'''
for y in range(5):
    numeros.append(int(input(f'Informe um número na posição {y}:\t')))
    if y == 0 or numeros[y] <= menor:
        if numeros[y] == menor:

        menor = numeros[y]
        posmen = y
    if numeros[y] > maior:
        maior = numeros[y]
        posmai = y

print(f'Sua lista ficou da seguinte forma {numeros}')
print(f'O maior número foi {maior} na posição {posmai} e menor foi {menor} na posicao {posmen}')
'''