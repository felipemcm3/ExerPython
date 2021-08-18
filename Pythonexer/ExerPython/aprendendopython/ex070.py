total = cont = menor = 0
barato = ''
while True:
    produto = str(input('Informe o nome do produto'))
    preco = float(input('Informe o preço do produto'))
    total += preco
    if cont == 0 or preco < menor:
        menor = preco
        barato = produto
    if preco > 1000:
        cont += 1
    escolha = str(input('Você quer continuar cadastrando S/N ?')).strip()[0]
    while not escolha in 'SsNn':
        escolha = str(input('Você deve informar apenas S sim N não deseja continuar ?'))
    if escolha in 'Nn':
        break
print(f'\033[31mSua compras acabaram!!\033[m.\nO total deu {total}.\n'
      f'O total de produtos acima de R$1000,00 foi {cont}\n'
      f'O produto mais barato foi {barato} custando R${menor}')
