def aumentar(n, t = False):
    au = n * 0.1
    n = n + au
    return n if t is False else moeda(n)

def diminuir(n, t = False):
    di = n * 0.13
    n = n - di
    return n if not t else moeda(n)

def dobro(n, t = False):
    n = n * 2
    return n if t is False else moeda(n)

def metade(n, t = False):
    n = n / 2
    return n if not t else moeda(n)


def moeda(n, moeda = 'R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')
