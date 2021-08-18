from datetime import date
hoje = date.today().year
fun = dict()
anonasc = 0
fun['nome'] = str(input('Informe o nome'))
anonasc = int(input(('Ano de nascimento')))
fun['idade'] = hoje - anonasc
fun['carteira'] = int(input('Nº da carteira (0 não tem carteira)'))
if fun['carteira'] != 0:
    fun['contratacao'] = int(input('Informe o ano da contratação'))
    fun['salario'] = float(input('Informe o salario'))
    fun['aposentadoria'] = fun['idade'] + ((fun['contratacao'] + 35) - hoje)
for x, y in fun.items():
    print(f'O indice {x} tem o item {y}')
