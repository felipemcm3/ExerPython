pessoa = list()
grupo = list()
maior = menor = float(0)

while True:
    pessoa.append(str(input('Informe o nome')).strip())
    pessoa.append(float(input('Informe o peso')))
    if len(grupo) == 0:
        maior = menor = pessoa[1]
    elif pessoa[1] > maior:
        maior = pessoa[1]
    elif pessoa[1] < menor:
        menor = pessoa[1]
    grupo.append(pessoa[:])
    pessoa.clear()
    escolha = str(input('Informe S/N para continuar:')).strip()
    if escolha in 'Nn':
        break
print(f'Foram cadastradas {len(grupo)} pessoas')
print(f'O maior peso foi {maior}.Sendo:', end='')
for o in grupo:
    if o[1] == maior:
         print(f'{o[0]}',end=' ')
print(f'\nO menor peso foi {menor}.Sendo:', end='')
for u in grupo:
    if u[1] == menor:
        print(f'{u[0]}',end=' ')

