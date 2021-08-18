estado = dict()
brasil = list()

for y in range(0, 3):
    estado['uf'] = str(input('Informe o nome do estado'))
    estado['sigla'] = str(input('Informe a sigla'))
    brasil.append(estado.copy())
print(brasil[1]['sigla'])
