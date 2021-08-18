marcador = 30 * '\033[1;34m=\033[m'
print(marcador)
l = float(input('Informe o primeiro lado'))
l2 = float(input('Informe o segundo lado'))
l3 = float(input('Informe o terceiro lado'))
if l + l2 > l3 and l + l3 > l2 and l2 + l3 > l:
    print('As medidas \033[1;32mFORMAM\033[m um triângulo')
    if l == l2 == l3:
        print('Esse é um triângulo \033[1;36mEQUILATERO\033[m')
    elif l == l2 or l == l3 or l2 == l3:
        print('Esse é um triângulo \033[1;36mISOSCELES\033[m')
    else:
        print('Esse é um triângulo \033[1;36mESCALENO\033[m')
else:
    print('As medidas \033[1;31mNÃO\033[m formam um triângulo')
print(marcador)

