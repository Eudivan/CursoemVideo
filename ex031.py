from time import sleep
print('\033[34m-'*120)
print('Para viagens de até 200km será cobrado R$0,50 por Km percorridos, acima disso, R$0,45! Façam uma boa viagem!')
print('-'*120 +'\033[m')
dis = int(input('Informe a distancia: Km '))
print('Distância informada {}Km!'.format(dis))
sleep(0.5)
if dis <= 200:
    val = dis  * 0.50
    print('\033[1mO valor a ser pago é \033[32mR${:.2f}\033[m!'.format(val))
else:
    val = dis * 0.45
    print('\033[1;10mO valor a ser pago é \033[32mR${:.2f}\033[m!'.format(val, dis))

