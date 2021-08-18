marcador = 30 * '\033[31m¨\033[33m¨\033[32m¨\033[m'
print(marcador)
lista = ['M', 'm', 'F', 'f']

sexo = str(input('Informe o sexo F/M ?'))

while not sexo in lista:
    sexo = str(input('Você digitou errado.\nInforme o sexo F/M ?'))

print('Fim do laço você informou {}'.format(sexo))
