print('''======
  PA3.0
  ======''')

ter = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão: '))
con = 0
v = 10
v2 = 1
while v2 != 0:
    while con < v:
        print('{} => '.format(ter), end='')
        ter += raz
        con += 1
    print('...')
    if con == v:
        v2 = int(input('\nQuer ver mais termos? quantos?\n para encerra digite 0: ', ))
        v += v2

print('\n\nA progressão foi encerrado com {} termos mostrados'.format(con))




