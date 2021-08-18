marcador = 30 * '\033[31m#\033[36m#\033[m'
print(marcador)
peso = float(input('Informe seu peso'))
altura = float(input('Informe sua altura'))
imc = peso / (altura * altura)
if imc < 18.5:
    print('Seu IMC deu {:.2f} estando abaixo do peso'.format(imc))
elif imc <= 25:
    print('Seu IMC deu {:.2f} seu peso está ideal'.format(imc))
elif imc <= 30:
    print('Seu IMC deu {:.2f} você está com sobrepeso'.format(imc))
elif imc <= 40:
    print('Seu IMC deu {:.2f} você está com obesidade'.format(imc))
else:
    print('Seu IMC deu {:.2f} obesidade morbida'.format(imc))
print(marcador)
