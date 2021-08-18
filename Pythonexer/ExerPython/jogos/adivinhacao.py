import random
def jogar():


    print("\n\nOla felipe vamos arrasar no python!!!!!!!")
    print("***********************************************")
    print("Bem-Vindo ao Jogo de Adivinhação!")
    print("************************************************")

    print("Nivel de dificuldade\n(1) facil numeros entre 1 a 10\n(2) médio numeros entre 1 a 50\n(3) dificil números entre 1 a 100")
    dificuldade = int(input("Qual o nível ?"))
    vezes = int(input("Informe quantas vezes quer chances"))
    print("Você começará com 1000 pontos e perderá conforme erra")
    pontos = 1000
    if (dificuldade == 1):
        numero_secreto = round(random.randrange(1, 11, 1))
    elif (dificuldade == 2):
        numero_secreto = round(random.randrange(1, 51, 1))
    else:
        numero_secreto = round(random.randrange(1, 101, 1))

    for vezes in range(vezes,0, -1):
        tentativa =int(input("Digite o seu numero entre 1 até 100: "))
        while(tentativa < 1 or tentativa > 100):
            tentativa =int(input("Por favor você deve digitar apenas entre 1 até 100"))


        certo = tentativa == numero_secreto
        maior = tentativa > numero_secreto
        menor = tentativa < numero_secreto


        if (certo):
            print("Parabéns você acertou sua pontuação foi {}".format(pontos))
            break
        else:
            if(maior):
                print("Você errou ! O número que digitou é maior que o número secreto")
                if(vezes != 1):
                    print("Tem mais {} chances".format(vezes-1))
                pontos = round(pontos - abs(numero_secreto - tentativa) / 3)
            elif(menor):
                print("Você errou ! O número que digitou é menor que o número secreto")
                if(vezes != 1):
                    print("Tem mais {} chances".format(vezes-1))
                pontos = round(pontos - abs(numero_secreto - tentativa) / 3)

    if(vezes == 1):
        print("Suas chances acabaram o número secreto é {} sua pontuação foi {}".format(numero_secreto, pontos))

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
