vel = float(input('Informe a velocidade do carro em Km/h'))
if (vel > 80):
    print('Você foi multado')
    vel -= 80
    print('Sua multa é de R${:.2f}'.format(vel * 7.00))
else:
    print('Dirija com segunça')

print('Siga em frente')