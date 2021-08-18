l1 = float(input('Informe o primeiro lado do triangulo'))
l2 = float(input('Informe o segundo lado do triangulo'))
l3 = float(input('Informe o terceiro lado do triangulo'))
if(l2 + l3 < l1):
    print('Os lados \033[31mnão\033[m formam um triangulo')
elif(l2 + l1 < l3):
    print('Os lados \033[31mnão\033[m formam um triangulo')
elif(l1 + l3 < l2):
    print('Os lados \033[31mnão\033[m formam um triangulo')
else:
    print('Os lados \033[32mformam\033[m um triangulo')
