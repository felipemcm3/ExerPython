escolha = 's'
maior = menor = soma = cont = 0

while escolha in 'Ss':
    n = int(input('Informe um número'))
    if cont == 0:
        maior = n
        menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
    soma += n
    cont += 1
    escolha = str(input('Quer continuar informando número S/N ?')).strip()[0]

print('O maior número foi {} e o menor número foi {}'.format(maior, menor))
print('A media dos número informados foi {:.2f}'.format(soma/cont))
