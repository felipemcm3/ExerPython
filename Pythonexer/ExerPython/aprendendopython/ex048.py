soma:int = 0
for n in range(1 , 501):
    if n % 2 != 0 and n % 3 == 0 :
        soma += n
print('A soma de todos os número impares divisiveis por 3 de 1 a 500 é {}'
      .format(soma))
