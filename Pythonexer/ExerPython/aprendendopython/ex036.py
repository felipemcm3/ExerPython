marcador = 30 * '\033[33m-=-\033[m'
print(marcador)
vacasa = float(input('Qual valor da casa a ser comprada'))
salario = float(input('Qual seu salário ?'))
anos = int(input('Quantos anos pretende pagar ?'))
print(marcador)
anos = anos * 12
vacasa = vacasa / anos
salario = salario * 0.3
if salario < vacasa:
    print('A prestação da casa ficará {:.2f}, 30% do seu salário ficará {:.2f}.\nSua parcela ficará maior que'
          ' 30% do seu salário por isso não podemos permitir o emprestimo.'.format(vacasa, salario))
else:
    print('Seu emprestimo foi aceito ! {:.2f} equivale a 30% do seu salário\nsendo menor que a parcela'
          'do imovel {:.2f}'.format(salario, vacasa))
print(marcador)
