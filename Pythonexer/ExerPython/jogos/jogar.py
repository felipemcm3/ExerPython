import adivinhacao
import forca
def escolha():
    print("\n\nOla felipe vamos arrasar no python!!!!!!!")
    print("***********************************************")
    print("Bem-Vindo ao Jogo ")
    print("************************************************")

    print("(1) Jogar adivinhação (2) Jogar forca")
    escolha = int(input("Qual você quer jogar ?"))

    if(escolha == 1):
        adivinhacao.jogar()
    else:
        forca.jogar()
if(__name__ == "__main__"):
    escolha()