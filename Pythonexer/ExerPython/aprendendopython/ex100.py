from random import sample
def sorteia():
    lista = list()
    lista = sample(range(100), 5)
    print(f'Os números sorteados foram {lista}')
    somapar(lista)


def somapar(num):
    soma = 0
    for y in num:
        if y % 2 == 0:
            print(y, end=' ')
            soma += y
    print(f'A soma dos pares é {soma}')


sorteia()
