numeros = list()
aux = list()
menor = 0
for y in range(5):
    aux.append(int(input(f'Informe um número da lista')))
cont = len(aux)

while True:
    for x in range(0, len(aux)):
        if x==0:
            menor = aux[x]
        elif aux[x] <= menor:
            menor = aux[x]
    aux.remove(menor)
    numeros.append(menor)
    cont -= 1
    menor = 0
    if cont == 0:
        break
print(f'Os valor da lista em ordem é {numeros}')
