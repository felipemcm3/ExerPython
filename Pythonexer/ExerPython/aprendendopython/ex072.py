lista = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
         'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')


while True:
    escolha = ' '
    num = int(input('Informe o número entre 0 a 20 para ser escrito por extenso'))
    while num < 0 or num > 20:
        num = int(input('Errado!!Você informou um valor maior que 20 e menor que 0'))
    print(f'O número escolhido foi {lista[num]}')
    while not escolha in 'SsNn':
        escolha = str(input('Informe S/N para continuar')).strip()[0]
    if escolha in 'Nn':
        break
print('Volte sempre!!!')

