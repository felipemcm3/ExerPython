def aumentar(n):
    au = n * 0.1
    n = n + au
    return n

def diminuir(n):
    di = n * 0.13
    n = n - di
    return n

def dobro(n):
    return n * 2

def metade(n):
    return n / 2


def moeda(n):
    valor = aumentar(n)
    return f'R${valor:.2f}'
