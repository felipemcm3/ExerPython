nome = str(input('Informe o nome completo')).strip()
separacao = nome.split()
print('primeiro nome = {}'.format(separacao[0]))
print('ultimo nome = {}'.format(separacao[len(separacao)-1]))
