print('{:~^40}'.format(' LOJAS OLIVEIRA '))
pre = float(input('Valor da compra: (R$) '))
pag = int(input('Escolha a forma de pagamento: \n[1] DINHEIRO/CHEQUE \n[2] CARTÃO \n'))
jur = 0.00
des = 0.00
tol = 0.00
par = 0
print('Valor da compra R${:.2f}\n'.format(pre))
if pag == 1:
    des = pre * 0.1
    tol = pre - des
    print('Escolheu DINHEIRO/CHEQUE \n\nÀ VISTA TEM DESCONTO DE 10%')
elif pag == 2:
    par = int(input('Escolheu CARTÃO! \nInforme a quantidade de vezes:\n '))
    if par == 1:
        des = pre * 0.05
        tol = pre - des
        print('\nÀ VISTA no cartão tem 5% de desconto!')
    elif par == 2:
        tol = pre
        print('Parcela 2x no cartão.')
    elif par > 2:
        jur = pre * 0.2
        tol = pre + jur
        print('Parcela {}x no cartão. Com 20% de juros'.format(par))
    else:
        tol = pre
        print('\033[31mOPÇÃO INVÁLIDA!\033[m')

else:
    tol = pre
    print('\033[31mOPÇÃO INVÁLIDA!\033[m')


print('''Desconto  \033[34m-R${:.2f}\033[m
Juros  \033[31mR${:.2f}
\033[1;30mTotal = \033[33mR${:.2f}\033[m'''.format(des, jur, tol), end='')


if par > 1:
    print(' dividido em {}x de R${:.2f}'.format(par, tol / par))
