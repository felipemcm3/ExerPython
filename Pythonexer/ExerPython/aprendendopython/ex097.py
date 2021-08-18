def escreva(msg):
    qua = len(msg)
    print('\033[33m-=\033[m'*qua)
    print(f'  {msg}')
    print('\033[32m-=\033[m'*qua)


print('\033[34mPERSONALIZAR MENSAGEM EM PYTHON\033[m')
while True:
    mensagem = str(input('Informe uma mensagem')).strip()
    escreva(mensagem)
    escolha = str(input('Você quer continuar ? S/N')).strip().upper()[0]
    if escolha == 'N':
        break
escreva('Obrigado')
