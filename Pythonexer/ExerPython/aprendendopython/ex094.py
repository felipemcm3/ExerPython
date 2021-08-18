pessoa = {}
grupo = []
media = 0
marcador = 50 * '\033[32m69\033[m'
while True:
    pessoa['nome'] = str(input('Informe o nome'))
    pessoa['sexo'] = str(input('Informe o sexo M/F')).strip()[0]
    while not pessoa['sexo'] in 'FfMm':
        pessoa['sexo'] = str(input('Você informou errado apenas M/F'))
    pessoa['idade'] = int(input('Informe a idade'))
    grupo.append(pessoa.copy())
    escolha = str(input('Informe S/N para continuar'))
    while not escolha in 'SsNn':
        escolha = str(input('Você informou errado apenas S/N'))
    if escolha in 'Nn':
        break
print(marcador)
print(grupo)
print('Foram cadastradas {} pessoas'.format(len(grupo)))
for y in grupo:
    media += y['idade']
media = media / len(grupo)
print(f'A média de idade do grupo é {media:.0f}')
for y in grupo:
    if y['sexo'][0] in 'Ff':
        print(f'{y["nome"]} é uma pessoa do sexo feminino')
for y in grupo:
    if y['idade'] > media:
        print(f'{y["nome"]} tem a idade {y["idade"]} estando acima da media {media}')
print(marcador)
