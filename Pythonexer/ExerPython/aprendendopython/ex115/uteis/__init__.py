def linha(msg):
    print('\033[34m-\033[m' * 30)
    print(msg.center(30))


def menu():
    linha('FAÇA SUA ESCOLHA')
    linha('1-Lista de Nomes\n2-Cadastrar Nomes\n3-Sair')
    resp = int(input('Escolha:'))
    return resp
