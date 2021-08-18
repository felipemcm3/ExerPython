alunos = list()
nomes = ''
notas = list()
cont = 0
while True:
    nomes = str(input('Informe o nome do aluno')).strip()
    alunos.append(nomes)
    nomes = ''
    for y in range(0, 3):
        if y != 2:
            notas.append(float(input(f'Informe a {y+1}º nota')))
        else:
            alunos.append(notas[:])
            alunos.append((notas[0]+notas[1])/2)
    notas.clear()
    escolha = str(input('Informe S/N para continuar'))
    if escolha in 'Nn':
        break
print(alunos)
print(f'{"Aluno":<10}{"Média":>5}')
for i, x in enumerate(alunos):
    if type(x) == str:
        print(f'{x:<10}',end='')
    if type(x) == float:
        print(f'{x:>5}')




