media:float = 0
maior:int = 0
nomemaisvelho:str
mul20:int = 0
for x in range(4):
    nome = str(input('Informe seu nome')).strip()
    idade = int(input('Informe sua idade'))
    sexo = str(input('Digite seu sexo (masculino) ou (feminino)')).strip().lower()
    media += idade
    if x == 0 and sexo in 'masculinoMASCULINO':
        maior = idade
        nomemaisvelho = nome
    if idade > maior and sexo in 'masculinoMASCULINO':
        maior = idade
        nomemaisvelho = nome
    if sexo in 'femininoFEMININO' and idade < 20:
       mul20 += 1
print('Idade média do grupo {:.0f}'.format(media / 4))
print('O homem mais velho é {} com {} anos'.format(nomemaisvelho, maior))
print('São {} mulheres com menos de 20 anos'.format(mul20))
