def contador(inicio,fim,passo):
    if inicio > fim and passo > 0:
        passo = passo * -1
    if passo == 0:
        if inicio > fim:
            passo = -1
        elif fim > inicio:
            passo = 1
    for y in range(inicio,fim,passo):
        print(y, end=' ')


print('BEM-VINDO AO CONTADOR')
print('A primeira contagem é: 1 até 10 em 1 em 1')
contador(1,11,1)
print('\nA segunda contagem é : 10 até 0 de 2 em 2')
contador(10,-2,-2)
print('\nA terceira é você que escolhe:')
ini = int(input('Informe o inicio da contagem'))
f = int(input('Informe o final da contagem'))
p = int(input('Informe o passo de contagem'))
contador(ini,f,p)
