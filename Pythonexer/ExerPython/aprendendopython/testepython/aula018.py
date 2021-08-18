dados = ['felipe', 25, 'maria', 18, 'joao', 22 ]
pessoas = list()
pessoas.append(dados[:])
dados[4] = 'Aurea'
dados[5] = 2
pessoas.append(dados[:])
dados.clear()
print(dados)
