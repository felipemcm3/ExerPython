def fatorial(num,r):
    '''
    :param num: o numero que será calculado fatorial
    :param r: resposta da pergunta para exibir ou não a conta
    :return: não a return
    '''
    if r in 'S':
        aux = num - 1
        soma = 0
        while aux != 0:
            if soma == 0:
                soma = num * aux
                print('{}x{}'.format(num, aux), end='')
            elif soma != 0:
                soma *= aux
                print('x{}'.format(aux), end='')
            aux -= 1
        print('={}'.format(soma))
    else:
        from math import factorial
        fator = factorial(num)
        print(fator)
n = int(input('Informe um número para o fatorial'))
resp = str(input('Você quer imprimir o calculo ? S/N')).strip().upper()[0]
while not resp in 'SN':
    resp = str(input('Você deve informar apenas S/N')).strip().upper()[0]
fatorial(n,resp)
help(fatorial)
