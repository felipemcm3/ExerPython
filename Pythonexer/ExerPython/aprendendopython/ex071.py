marcador = 50 * '\033[32m$\033[m'
val = 0
aux = 0
cin = vin = dez = um = 0
print(marcador)
print('BEM-VINDO AO CAIXA ELETRONICO!')
while True:
    val = input('Informe o valor que queira sacar sendo somente números inteiros')
    if val.isnumeric():
        val = int(val)
        break
aux = val
while True:
    if val >= 50:
        val -= 50
        cin += 1
    elif val >= 20:
        val -= 20
        vin += 1
    elif val >= 10:
        val -= 10
        dez += 1
    elif val >= 1:
        val -= 1
        um += 1
    elif val == 0:
        break

print('Você retirou {},\n[{}] cedulas de cinquenta\n[{}] cedulas de vinte\n[{}] cedulas de dez,\n[{}] cedulas de um'
      .format(aux, cin, vin, dez, um))
print(marcador)
teste = str
