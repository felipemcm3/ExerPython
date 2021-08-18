from time import sleep
marcador = 30 * '\033[34mx\033[35mx\033[36mx\033[m'
print(marcador)
escolha = int()

print('Bem-Vindo a Calculadora Versatil')
num1 = int(input('Informe o primeiro número'))
num2 = int(input('Informe o segundo número'))

while escolha != 5:

    print('[1]SOMA\n[2]MULTIPLICAR\n[3]MAIOR\n[4]NOVOS NUMEROS\n[5]SAIR DO PROGRAMA')
    escolha = int(input('Informe sua opção'))
    if escolha == 1:
        print('O número {} somado a número {} é {}'.format(num1, num2, num1+num2))
    elif escolha == 2:
        print('O número {} multiplicado pelo número {} é {}'.format(num1, num2, num1 * num2))
    elif escolha == 3:
        maior = 0
        if num1 >= maior:
            maior = num1
        if num2 >= maior:
            maior = num2
        print('Entre o número {} e número {} o maior é {}'.format(num1, num2, maior))
    elif escolha == 4:
        num1 = int(input('Informe o novo primeiro número'))
        num2 = int(input('informe o novo segundo número'))
    else:
        if escolha != 5:
            print('Você digitou outra coisa siga o menu:')
    sleep(3)

print('FIM DO PROGRAMA')
print(marcador)
