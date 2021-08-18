from random import choices
from time import sleep
marcador = 15 * '\033[31m69\033[32m69\033[33m69\033[m'
print(marcador)
print('\033[34mBEM-VINDO AO JOKENPÔ !!!\033[m')
escolha = str(input('Digite oque você irá jogar\nPedra, papel ou tesoura ?')).strip()
escolha = escolha.lower()
lista = ['pedra','papel','tesoura']
computador = choices(lista)
print('\033[1;31mJON\033[m')
sleep(1)
print('\033[32mKEN\033[m')
sleep(1)
print('\033[33mPON!!!\033[m')
sleep(1)
if escolha == 'pedra':
    if computador == ['tesoura'] :
        print('Você \033[32mGANHOU\033[m o computador escolheu {}'.format(computador))
    elif computador == ['papel']:
        print('Você \033[31mPERDEU\033[m o computador escolheu {}'.format(computador))
    else:
        print('\033[33mEmpate\033[m')
elif escolha == 'papel':
    if computador == ['pedra']:
        print('Você \033[32mGANHOU\033[m o computador escolheu {}'.format(computador))
    elif computador == ['tesoura']:
        print('Você \033[31mPERDEU\033[m o computador escolheu {}'.format(computador))
    else:
        print('\033[33mEmpate\033[m')
elif escolha == 'tesoura':
    if computador == ['papel']:
        print('Você \033[32mGANHOU\033[m o computador escolheu {}'.format(computador))
    elif computador == ['pedra']:
        print('Você \033[31mPERDEU\033[m o computador escolheu {}'.format(computador))
    else:
        print('\033[33mEmpate\033[m')
else:
    print('\033[35mVocê digitou outra coisa\033[35m')
print(marcador)
