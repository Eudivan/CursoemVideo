from random import randint
print('\033[1;30m+-' * 17)
print('     JOGO DO PAR OU ÍMPAR')
print('-+' * 17)
print('\n\n')
cont = j = pc = 0
while True:
    esc = int(input('Digite 1 p/ Ímpar ou 2 p/ Par: '))
    j = int(input('Sua jodada: '))
    print('\033[34m-------------------------------------------------------------------\033[m')
    pc = randint(0, 5)
    soma = pc + j
    if soma % 2 == 0:
        print('Deu Par! ', end='')
    else:
        print('Deu Ímpar! ', end='')

    if esc == 1 and soma % 2 == 0 or esc == 2 and soma % 2 == 1:
        print(f'\033[31mGAME OVER!\nVocê venceu {cont} partidas!', end='')
        print(f' eu joguei {pc} e vc {j} que somado da {soma}')
        break
    else:
        print('\033[33mVocê ganhou! ', end='')
    print(f' eu joguei {pc} e vc {j} que somado da {soma}')
    print('\033[34m-------------------------------------------------------------------\033[m')
    cont += 1
