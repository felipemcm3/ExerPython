cores = {'limpa':'\033[m','vermelho':'\033[31m','amarelo':'\033[33m', 'verde':'\033[32m'}
n1 = int(input('{}Informe o primeiro número{}'.format(cores['vermelho'],cores['limpa'])))
n2 = int(input('{}Informe o segundo número{}'.format(cores['amarelo'],cores['limpa'])))
n3 = int(input('{}Informe o terceiro número{}'.format(cores['verde'],cores['limpa'])))
maior = menor = n1
if n2 > maior:
    maior = n2
if n2 < menor:
    menor = n2
if n3 > maior:
    maior = n3
if n3 < menor:
    menor = n3
print('O maior número é {} e menor {}'.format(maior, menor))
