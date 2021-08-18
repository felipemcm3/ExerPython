from math import radians, cos, sin, tan
ang = float(input('Informe o angulo para calcular sen, cos, tang'))
co = cos(radians(ang))
se = sin(radians(ang))
tan = tan(radians(ang))
print('O conseno de {} é {:.2f}'.format(ang, co))
print('O seno de {} é {:.2f}'.format(ang, se))
print('A tangente de {} é {:.2f}'.format(ang, tan))
