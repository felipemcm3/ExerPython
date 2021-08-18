frase = str(input('Informe uma frase')).strip().upper()
print('A frase digitada tem {} letras A'.format(frase.count('A')))
print('A letra A aparece primeiro na posição {}'.format(frase.find('A')+1))
print('A letra A aparece pela ultima vez na posição {}'
      .format(frase.rfind('A')+1))
