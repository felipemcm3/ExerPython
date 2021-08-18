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

def resumo(n):
    print(f'O dobro do número {moeda(n)} é {dobro(n, True)}')
    print(f'A metade do número {moeda(n)} é {metade(n, True)}')
    print(f'O valor aumentado em 10% ficará {aumentar(n, True)}')
    print(f'O valor diminuido em 13% ficará {diminuir(n, True)}')
