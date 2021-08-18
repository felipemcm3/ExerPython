cidade = str(input('Informe o nome da cidade')).strip()
cidade = cidade.upper()
print('A cidade {} tem {} palavra SANTO no começo'
      .format(cidade, cidade.count('SANTO', 0,5)))
