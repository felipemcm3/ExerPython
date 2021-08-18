marcador = 40 * '#'
print(marcador)
print('Bem-Vindo !\nVamos calcular a tarifa do aluguel do carro')
d = int(input('Informe o número de dias que o carro ficou alugado'))
km = float(input('Informe os kilometros rodados no carro'))
vd: int = d * 60
vkm: float = km * 0.15
print(marcador)
print('Você alugou o carro sua tarifa será {:.2f}'.format(vd + vkm))
