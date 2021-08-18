def area(l,c):
    a = l * c
    print(f'A área de {l} de largura e {c} de comprimento é {a}')

print('\033[35mBEM-VINDO AO MEDIDOR DE AREA EM PYTHON\033[m')
lar = float(input('Informe a largura do terreno'))
com = float(input('Informe o comprimento do terreno'))
area(lar,com)
