import requests
try:
    resp = requests.get('http://pudim.com.br/')

except:
    print('\033[31mNão foi possivel conectar no site\033[m')

else:
    print('\033[32mO site foi conectado\033[m')
