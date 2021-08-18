marcador = 30 * '\033[33m//\033[m'
while True:
    try:
        inteiro = input('Informe um número inteiro')

        if inteiro.isnumeric():
            inteiro = int(inteiro)
        else:
            inteiro = int('y')

    except ValueError:
        print('\033[31mERRO!!Digite o número correto\033[m')
    else:
        break
print(marcador)
while True:
    try:
        real = input('Informe um número real').strip()

        if real == '':
            real = float(0)

        elif not real.isalpha():
            if '.' in real:
                real = float(real)
            else:
                real = float('y')
        else:
            real = float(real)
    except ValueError:
        print('\033[31mERRO!!Digite o número correto\033[m')
    else:
        break
print(marcador)

print(f'O número inteiro digitado foi {inteiro}')
print(f'O número real digitado foi {real}')
