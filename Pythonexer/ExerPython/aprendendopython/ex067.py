while True:
    n = 0
    aux = 1
    n = int(input('Informe o número para imprimir sua tabuada.\nDigite um valor negativo para parar'))
    if n < 0:
        break
    while True:
        if aux == 11:
            break
        print(f'{n} x {aux} = {n*aux}')
        aux += 1

print('Você digitou um valor negativo o programa parou !')