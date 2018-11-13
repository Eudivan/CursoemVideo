from time import sleep
from random import randint
print('''\033[32m======================================================
\33[34m  Estou pensando em um número 0 a 10 tente adivinhar!
\033[32m======================================================\033[m''')
vezes = 1
p = int(input('\033[21;1mQual o seu palpite? \033[m'))
pc = randint(0, 10)
print('\033[34mProcessando...\033[m')
sleep(0.6)
while p != pc:
    vezes += 1
    if p > pc:
        print('Menos... ', end='')
    elif p < pc:
        print('Mais... ', end='')
    p = int(input('\033[31mVocê erro!\033[m Tente novamente: '))
print('\033[34mProcessando...\033[m')
sleep(0.5)
print('\033[33mParabéns! Eu estava pensando no {} \nVocê conseguiu acerta na {}ª tentativa!\033[m'.format(pc, vezes))
