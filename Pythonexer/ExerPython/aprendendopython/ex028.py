from random import randint
marcador = 50 * '-=-'
print(marcador)
num = randint(0, 5)
tentativa = int(input('Tente descobrir o número sorteador!!!\n'
                      'Informe um número inteiro entre 0 e 5'))
print(marcador)
if (tentativa == num):
    print('Parabéns você acertou')
else:
    print('Que pena você errou o número era {}'.format(num))
print(marcador)
