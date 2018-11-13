print('''-------------------
CAIXA ELETRÔNICO
-------------------
Este caixa está abastecido com notas de R$100 R$50, R$20, R$10 e R$1
===============================================================\n''')
v = int(input('Qual o valor deseja sacar? R$'))
total = v
ced = 100
totced = 0
while True:
    while total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'{totced} cédulas de R${ced}')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break

