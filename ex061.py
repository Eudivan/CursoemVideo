print('PA COM WHILE!\n\n\n')

ter = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão: '))
v = 0
while v < 10:
    print('{} => '.format(ter), end='')
    ter += raz
    v += 1
print('...', end='')

