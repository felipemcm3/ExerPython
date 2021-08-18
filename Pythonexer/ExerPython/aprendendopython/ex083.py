expressao = str(input('Informe alguma coisa com ()'))
aux = aux2 = 0
for y in expressao:
    if y == '(':
        aux += 1
    elif y == ')':
        aux2 += 1
if aux == aux2:
    print('O uso dos parenteses está \033[32mCORRETO\033[m')
else:
    print('O uso dos parenteses está \033[31mERRADO\033[m')
