def leiaint(msg):
    while True:
        n = input(msg)
        if n.isnumeric():
            n = int(n)
            break
        else:
            print('\033[31mDIGITE APENAS NUMEROS INTEIROS\033[m')
    return  n


n = leiaint('Digite um número')
print(f'O valor digitado foi {n}')