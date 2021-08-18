aluno = dict()

aluno['nome'] = str(input('Nome do aluno').strip())
aluno['media'] = float(input(f'Média de {aluno["nome"]}'))

print(f'O aluno {aluno["nome"]} tem a média {aluno["media"]}')
if aluno['media'] >= 7.0:
    print(f'{aluno["nome"]} está \033[32mAPROVADO!\033[m')
elif 5.0 <= aluno["media"] < 7.0:
    print(f'{aluno["nome"]} está \033[33mRECUPERAÇÃO!\033[m')
else:
    print(f'{aluno["nome"]} está \033[31mREPROVADO!\033[m')
