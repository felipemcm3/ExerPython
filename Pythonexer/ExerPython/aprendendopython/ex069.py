conidad = mas = fem = 0
while True:
    print(30 * '\033[31mx\033[m')
    idade = int(input('Informe sua idade'))
    sexo = str(input('Informe seu sexo M/F ?')).strip()[0]
    while not sexo in 'MmFf':
        sexo= str(input('Você digitou outra coisa informe seu sexo M/F ?'))
    if idade > 18:
        conidad += 1
    if sexo in 'Mm':
        mas += 1
    if sexo in 'Ff' and idade < 20:
        fem += 1
    escolha = str(input('Você quer continuar ? S/N')).strip()[0]
    while not escolha in 'SsNn':
        escolha = str(input('Apenas informe S sim N não deseja continuar ?'))
    if escolha in 'Nn':
        break
print(f'Você saiu do programa:\n[{conidad}] pessoas maiores de 18\n[{mas}] '
      f'homens\n[{fem}] mulheres com menos de 20 anos')