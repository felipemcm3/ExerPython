numeros = list()
escolha = ''
while True:
    num = int(input('Informe um número para a lista'))
    if not num in numeros:
        numeros.append(num)
        print('Valor \033[32madicionado\033[m.')
    else:
        print('Já existe esse valor na lista, \033[31mnão\033[m será adicionado.')
    escolha = input('Você quer continuar? S/N')
    if escolha in 'Nn':
        break
numeros.sort()
print(f'Os valores adicionador foram {numeros}')
