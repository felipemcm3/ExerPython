n = int(input('Informe quantos termos de Fibonacci quer ver'))
p = 0
s = 1
soma = 0
y = n
if n == 1:
    print(p)
    n -= 1
elif n == 2:
    print(p, s, end = ' ')
    n -= 2
while n != 0:
    if y == n:
        print(p, s, end = ' ')
        n -= 2
    soma = p + s
    print(soma, end = ' ')
    p = s
    s = soma
    n -= 1
