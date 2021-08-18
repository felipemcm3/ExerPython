from datetime import date
marcador = 30 * '\033[36m+\033[m'
print(marcador)
sexo = str(input('Informe seu sexo sendo MASCULINO ou FEMININO')).strip()
sexo = sexo.lower()
if sexo == 'masculino':
    nasc = int(input('Informe o ano do nascimento'))
    ano = date.today().year
    idade = ano - nasc
    if idade < 18:
        print('Você ainda vai se alistar. Falta {} anos'.format(18 - idade))
        print('Você se alistará no ano de {}.'.format(nasc + 18))
    elif idade == 18:
        print('Você vai se alistar esse ano !')
    else:
        print('Já passou seu tempo de alistar a {} anos'.format(idade - 18))
        print('Você devia ter se alistado em {}.'.format(nasc + 18))
elif sexo == 'feminino':
    print('Pessoas do sexo feminino não precisam se alistar')
else:
    print('Você digitou outra coisa')
print(marcador)
