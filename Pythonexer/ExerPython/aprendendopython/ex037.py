marcador = 30 * '\033[31m*\033[32m*\033[33m*\033[m'
print(marcador)
num = int(input('Informe o número a ser convertido'))
tipo = int(input('1-Binario\n2-Octal\n3-Hexadecimal\nInforme o tipo de conversão:'))
print(marcador)
if tipo == 1:
    resul = format(num, 'b')
    print('O número {} em binario é {}'.format(num, resul))
elif tipo == 2:
    resul = format(num, 'o')
    print('O número {} em octal é {}'.format(num, resul))
elif tipo == 3:
    resul = format(num, 'x')
    print('O número {} em hexadecimal é {}'.format(num, resul))
else:
    print('Você informou o número errado')
print(marcador)
