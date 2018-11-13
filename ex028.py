from random import randint
from time import sleep
numX = randint(0, 5)
print('\033[32m-=-'*20)
print('\033[1;37mestou pensando em um numero 0 a 5, adivinhe qual!\033[m')
print('\033[32m-=-'*20)
n = int(input('\033[1;30mqual o seu palpite? \n'))
print('\033[1;35mProcessando...\033[m')
sleep(1)
if numX == n:
    print('\033[32mUau! Parabens, você acertou.\033[m')
else:
    print('\033[1;31mErrou! tente novamente, eu estava pensando no {} e não no {}.'.format(numX, n))
print('-'*24)
