alunos = {}
sala = []
def notas():
    '''
    Essa funcao perguntará as notas dos alunos e dirá quais são suas
    MENOR NOTA
    MAIOR NOTA
    MEDIA
    SITUAÇÃO
    :return:
    '''
    maior = menor = soma = 0
    global sala
    global alunos
    dados = dict()
    while True:
        alunos['nome'] = str(input('Informe o nome do aluno')).strip()
        alunos['nota'] = float(input('Informe a nota do aluno'))
        sala.append(alunos.copy())
        escolha = str(input('Informe S/N para continuar')).strip()[0]
        if escolha in 'Nn':
            break
    print(f'Lista sala {sala}')
    dados['quant'] = len(sala)
    for y in range(0, len(sala)):
        if y == 0:
            maior = sala[y]['nota']
            menor = sala[y]['nota']
        elif sala[y]['nota'] > maior:
            maior = sala[y]['nota']
        elif sala[y]['nota'] < menor:
            menor = sala[y]['nota']
        soma += sala[y]['nota']
    dados['menor'] = menor
    dados['maior'] = maior
    dados['media'] = soma / len(sala)
    if dados['media'] >= 9:
        dados['situa'] = 'OTIMO'
    elif 7 <= dados['media'] < 9:
        dados['situa'] = 'BOM'
    elif 5 <= dados['media'] < 7:
        dados['situa'] = 'RECUPERAÇÃO'
    elif 5 > dados['media']:
        dados['situa'] = 'REPROVADO'

    print(f'Dicionario dados: {dados}')
    return dados.copy()


resp = dict()
resp = notas()
print(f'Dicionario resp {resp}')
print(f'Foram {resp["quant"]} pessoas cadastradas sendo {resp["menor"]} a menor nota\n'
      f'{resp["maior"]} a maior nota {resp["media"]:.2f} a media da turma sua situação está {resp["situa"]}')
