print('=-'*55)
print('\033[034mA velocidade máxima é 80Km/h, caso ultrapasse a multa é R$ 7,00 por cada quilometro acima do limite!\033[m')
print('=-'*55)
vel = int(input('\nqual a velocidade? \nKM/h '))
multa = (vel - 80) * 7
if vel > 80:
    print('\n\033[31m{}Km/h ACIMA DA VELOCIDADE, multa de \033[1;32mR${:.2f}\033[m'.format((vel - 80), multa))
else:
    print('\n\033[032mNão ultrapassou o limite\033[m')
print('\033[33mTenha um bom dia! Dirija com segurança!\033[m')