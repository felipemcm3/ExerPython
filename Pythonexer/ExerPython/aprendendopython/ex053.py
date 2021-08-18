frase = str(input('Informe a palavra para ser analisada '
                    'se é polindromo')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for y in range(len(junto)-1, -1, -1):
    inverso += junto[y]
print('O inverso da frase {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palindromo')
else:
    print('Não é palindromo')
