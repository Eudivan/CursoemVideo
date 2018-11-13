from time import sleep
sal = float(input('Informe o salário: '))
s2 = sal
if sal > 1250:
    aum = sal * 0.1
    sal = aum + sal
    por = 10
else:
    por = 15
    aum = sal * 0.15
    sal = aum + sal
print('\033[34mO salário R${:.2f} tera aumento de {}%\033[m'.format(s2, por))
sleep(0.6)
print('O sálario teve aumento de \033[1;32mR${:.2f}\033[m \nNovo salário é \033[33mR${:.2f}\033[m!'.format((aum), sal))
