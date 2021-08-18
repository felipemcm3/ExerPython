n = cont = soma = 0
n = int(input('Informe um número digite 999 se quiser sair do loop:\t'))
while not n == 999:
    soma += n
    cont += 1
    n = int(input('Informe um número digite 999 se quiser sair do loop:\t'))
print('Você digitou {} números e sua soma foi {}'.format(cont, soma))
