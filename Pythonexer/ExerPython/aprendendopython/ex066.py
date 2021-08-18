soma = cont = 0

while True:
    n = int(input('Informe um número (Digite 999 para sair do loop)'))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'A quantidade de números digitados foram {cont} e sua soma foi {soma}')
