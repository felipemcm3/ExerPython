def voto(nasc):
    from datetime import date
    atual = date.today().year
    idade = atual - nasc
    if idade < 16:
        return 'Sua idade é {} não pode votar'.format(idade)
    elif 16 <= idade < 18 or 65 <= idade:
        return f'Sua idade é {idade} seu voto é opcional'
    else:
        return f'Sua idade é {idade} seu voto é obrigatorio'


ano = int(input('Informe o ano de nascimento'))
resp = voto(ano)
print(resp)
print(type(resp))


