nota = float(input('Informe a primeira nota'))
nota2 = float(input('Informe a segunda nota'))
media = (nota + nota2) / 2
if media < 5.0:
    print('Sua media é {} você foi \033[31mreprovado'.format(media))
elif 7 > media >= 5:
    print('Sua media é {} você está de \033[33mrecuperação'.format(media))
elif media >= 7:
    print('Sua media é {} você está \033[32maprovado'.format(media))
