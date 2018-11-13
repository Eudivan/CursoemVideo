sal = float(input('Qual o salário do funcionário? R$'))
por = float(input('quantos por cento de aumento? %'))

sal2 = sal + (sal * (por/100))
print('O salário do funcionário passará de R${:.2f}, com aumento de aproximadamente {:.0f}%, para R${:.2f}'.format(sal, por, sal2))
print('Aumento de R${:.2f}'.format(sal * (por / 100)))
