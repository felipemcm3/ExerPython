variavel = input('Informe algo')
if(variavel.isnumeric() == True):
    print('A variavel é {} um número'.format(variavel))
elif(variavel.isalpha() == True):
    print('A variavel é {} um letra ou palavra'.format(variavel))
else:
    print('A variavel {} é alpha númerico'.format(variavel))
