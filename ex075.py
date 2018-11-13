b = c = d = t = e = 0
for con in range(0, 4):
    a = int(input('Digite um valor!'))
    if con == 0:
        b = a
    if con == 1:
        c = a
    if con == 2:
        d = a
    if con == 3:
        e = a
    t = b, c, d, e
print(f'Valore digitados: {t}')
if 9 in t:
    print(f'O nove apareceu {t.count(9)} vezes!')
else:
    print('Não digitado nenhum número nove!')

if 3 in t:
    print(f'O número três apareceu na posição [{t.index(3)}] pela primeira vez')
else:
    print('Não foi digitado nenhum número três')

print('Os números pares: ', end='')
for n in t:
    if n % 2 == 0:
        print(n, end=' ')




'''if b % 2 == 0:
    print(f'{b} ', end='')
if c % 2 == 0:
    print(f'{c} ', end='')
if d % 2 == 0:
    print(f'{d} ', end='')
if e % 2 == 0:
    print(f'{e} ', end='')'''

