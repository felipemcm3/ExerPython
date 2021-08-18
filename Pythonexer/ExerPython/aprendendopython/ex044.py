marcador = 30 * '\033[33m>\033[35m<\033[m'
print(marcador)
preco = float(input('Informe o valor do produto'))
print(marcador)
escolha = int(input('1-A vista dinheiro ou cheque\n2-A vista cartão\n3-Parcelado 2 vezes'
                    '\n4-Parcelado mais vezes\nInforme sua opcão de pagamento.'))
print(marcador)
if escolha == 1:
    print('Você ganhou 10% de desconto pagando {}'.format(preco - (preco * 0.1)))
elif escolha == 2:
    print('Você ganhou 5% de desconto pagando {}'.format(preco - (preco * 0.05)))
elif escolha == 3:
    print('Valor R${} será parcelado em 2 vezes de {:.2f}'.format(preco, preco / 2))
elif escolha == 4:
    parc = int(input('Quantas parcelas gostaria de pagar ?'))
    print('O valor será acrescentado 20% sendo {} parcelas de R${}.\nAumentando o valor total de R${} para R${}.'
          .format(parc, (preco + preco * 0.2) / parc, preco, (preco + preco * 0.2)))
else:
    print('Você deve escolher uma das alternativas')
print(marcador)
