from time import sleep
from random import randint
marcador = 20 * '\033[31ms2\033[m'
resul = cont = 0
print(marcador)
print('BEM-VINDO AO JOGO DE PAR OU IMPAR')
while True:
    escolha = str(input('[P]Par\n[I]Impar\nInforme se quer:')).strip()[0]
    if escolha in 'Pp':
        computador = randint(0, 10)
        n = int(input('Escolha seu número'))
        resul = computador + n
        if resul % 2 == 0:
            print(f'Você \033[32mvenceu\033[m!!!O número deu {resul} par!')
            cont +=1
        else:
            print(f'Você \033[31mperdeu\033[m.O número deu {resul} impar')
            break
    elif escolha in 'Ii':
        computador = randint(0, 100)
        n = int(input('Escolha seu número'))
        resul = computador + n
        if resul % 2 != 0:
            print(f'Você \033[32mvenceu\033[m!!!O resultado deu {resul} impar!')
            cont += 1
        else:
            print(f'Você \033[31mperdeu\033[m.O resultado deu {resul} par')
            break
    else:
        print('\033[33mVocê digitou outra coisa tente novamente\033[m')
    sleep(2)
sleep(2)
print(f'Você teve \033[35m{cont}\033[m vitórias')
print(marcador)
