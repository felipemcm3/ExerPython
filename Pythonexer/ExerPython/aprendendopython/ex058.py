from random import randint
marcador = 30 * '\033[31m#\033[32m#\033[33m#\033[m'
print(marcador)
computador = randint(1, 100)
cont:int = 1
num = int(input('Informe um número para adivinhação'))
while not num == computador:
    if computador > num:
        print('Voce errou digite um número maior')
    else:
        print('Você errou digite um número menor')
    num = int(input('Tentei novamente !'))
    cont += 1

print('Parabéns você venceu com {} tentativas'
      ' o computador digitou {} e você {}'.format(cont, computador, num))
print(marcador)
