from datetime import date
atual = date.today().year
maior:int = 0
menor:int = 0
for y in range(7):
    nasc = int(input('Informe o ano do nascimento da {} pessoa'.format(y+1)))
    idade = atual - nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('{} pessoas são maiores capazes\n{} pessoas são menores incapazes'
      .format(maior, menor))
