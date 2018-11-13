from time import sleep
from random import randint
print('\033[1;34;10m=-'*18)
print('Vamos jogar PEDRA, PAPEL, TESOURA!')
print('-=' * 18 + '\033[m')
print('\033[33mEu ja escolhi!\033[m')
n1 = int(input('''\033[33mESCOLHA A SUA OPÇÃO: não se preocupe, garanto que não posso ver!
[1] PEDRA
[2] PAPEL
[3] TESOURA
\033[m'''))
if n1 == 1:
    ppt = 'pedra'           #ppt = pedra papel tesoura
elif n1 == 2:               #ppt2 = pedra papel tesoura da maquina
    ppt = 'papel'
elif n1 == 3:
    ppt ='tesoura'
else:
    print('\033[31;1mOpção inválida\033[m')

n2 = randint(1, 3)
if n2 == 1:
    ppt2 = 'pedra'
elif n2 == 2:
    ppt2 = 'papel'
else:
    ppt2 = 'tesoura'

print('\033[32;1mPedra')
sleep(0.3)
print('Papel')
sleep(0.3)
print('Tesoura\033[m')
sleep(0.5)


print('\033[34m')
if ppt == ppt2:
    print('\033[34mEMPATOU!')
    print('Você escolheu {} e eu também!'.format(ppt, ppt2))
elif ppt == 'pedra' and ppt2 == 'tesoura':
    print('Você venceu!')

elif ppt == 'tesoura' and ppt2 == 'papel':
    print('Você venceu!')

elif ppt == 'papel' and ppt2 == 'pedra':
    print('Você venceu!')
else:
    print('\033[31mEu venci')

print('Eu escolhi {} e você {}'.format(ppt2, ppt))
print('\033[m')
