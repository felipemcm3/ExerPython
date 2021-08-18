'''
distancia = float(input('Informe a distância da viagem em Km'))

if (distancia <= 200):
    print('O valor de sua passagem é {}'.format(distancia * 0.50))
else:
    print('Sua viagem excede 200km,'
          ' o valor de sua passagem é {}'.format(distancia * 0.45))

'''
distancia = float(input('Informe a distancia da viagem em Km'))
print('Valor a ser pago é R${}'.format(distancia * 0.50) if distancia <= 200
      else 'Valor a ser pago é R${}'.format(distancia * 0.45))
