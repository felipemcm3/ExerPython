sal = float(input('Informe o salário'))
if (sal > 1250.00):
    print('O salário \033[33;40mR${}\033[m terá o aumento de \033[31;40mR${}\033[m passando a ser \033[32;40mR${}\033[m'
          .format(sal, sal * 0.10, sal + sal * 0.10))
else:
    print('O salário \033[33;40mR${}\033[m terá o aumento de \033[31;40mR${}\033[m passando a ser \033[32;40mR${}\033[m'
          .format(sal, sal * 0.15, sal + sal * 0.15))
