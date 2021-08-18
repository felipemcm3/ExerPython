numeros = list()
escolha = ''
while True:
    numeros.append(int(input('Informe um valor')))
    escolha = str(input('Informe S/N para continuar')).strip()[0]
    if escolha in 'Nn':
        break
numeros.sort(reverse=True)
print(f'Foram digitados {len(numeros)}')
print(f'Os números ordenados decrescente: {numeros}')
if 5 in numeros:
    print(f'O valor 5 esta na lista na casa {numeros.index(5)}')
else:
    print('O valor 5 \033[31mNÃO\033[m está na lista')
