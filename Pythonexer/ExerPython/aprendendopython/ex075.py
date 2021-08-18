cont = contpar =0

lista = (int(input('Informe o primeiro valor')), int(input('Informe o segundo valor')),
         int(input('Informe o terceiro valor')), int(input('Informe o quarto valor')))
for y in lista:
    if y == 9:
      cont +=1
    if y % 2 == 0:
        contpar += 1
print(f'O número 9 apareceu {cont} vezes')
try:
    print(f'O número 3 aparece primeiro na posição {lista.index(3)+1}')
except ValueError:
    print('Não existe nenhum valor 3 na lista.')

print(f'Foram {contpar} números pares na lista')
