def funcao():
    global n
    n = 1
    print(f'N dentro vale {n}')

n = 4
print(f'N vale fora {n}')
funcao()
print(f'N fora dinovo {n}')
