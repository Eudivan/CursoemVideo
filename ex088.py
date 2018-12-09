from time import sleep
from random import randint
jogo = []
n = 0
num = int(input('\033[30;1mQUANTOS PALPITES QUER GERAR? '))
print('OK!')
print('\033[34;1mAnalisando...')
sleep(1)
print('\nAqui está!\033[m')
for c in range(num):
    jogo.append([])
    while len(jogo[c]) < 6:
        pal = randint(1, 60)
        if pal not in jogo[c]:
            jogo[c].append(pal)
        n += 1
    print(f'\033[30;1mJogo {c + 1}: {sorted(jogo[c])}')
    sleep(0.4)


print(n)

