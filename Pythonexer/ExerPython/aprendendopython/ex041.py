from datetime import date
marcador = 20 * '\033[31m-\033[32m=\033[33m-\033[m'

print(marcador)
nasc = int(input('Informe seu ano de nascimento'))
ano = date.today().year
idade = ano - nasc

if idade <= 9:
    print('Sua idade é {} categoria mirim'.format(idade))
elif idade <= 14:
    print('Sua idade é {} categoria infantil'.format(idade))
elif idade <= 19:
    print('Sua idade é {} categoria junior'.format(idade))
elif idade <= 25:
    print('Sua idade é 20 categoria sênior')
else:
    print('Sua idade é {} categoria master'.format(idade))
print(marcador)
