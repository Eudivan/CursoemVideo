'''from math import factorial
num = int(input('Digite um numero para saber o fatorial: '))
n1 = factorial(num)
n2 = 1
print('{}! = '.format(num), end='')
for c in range(num, 0, -1):
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    n2 *= c

print('{}'.format(n1), end='')
print(n2)'''


'''num = int(input('Digite um número para saber o fatorial: '))
n = num
t = 1
print('{}! = '.format(num), end='')
while n > 0:
    print('{}'.format(n), end='')
    print(' x 'if n > 1 else ' = ', end='')
    t *= n
    n -= 1
print('{}'.format(t), end='')'''

print('-' * 10)
print(' FATORIAL')
print('-' * 10)
cont = 0
s = 's'
fat = 0
while s == 's':
    f = int(input('Digite um número para saber o fatorial: '))
    cont = f
    print('{}! = {} x '.format(f, f), end='')
    while cont != 1:
        cont -= 1
        fat = f * cont
        f = fat
        print('{}'.format(cont), end='')
        if cont == 1:
            print(' = ', end='')
        else:
            print(' x ', end='')
    print(fat)
    s = str(input('Quer ver outro numero? [S/N]: ')).strip().lower()
    while s not in 'sn':
        s = str(input('Quer ver outro número? [S/N]: ')).strip().lower()




