cores = {'limpa':'\033[m','vermelho':'\033[31m'}
nome = str(input('Informe seu nome')).strip()
print('Seu nome é {}{}{} parabéns !!!'
      .format(cores['vermelho'], nome, cores['limpa']))
