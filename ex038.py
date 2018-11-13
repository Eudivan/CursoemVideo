n1 = int(input('digite um numero: '))
n2 = int(input('outro: '))
n3 = int(input('mais um: '))
g = 'igual'
m = 'igual'
p = 'igual'

if n1 > n2 > n3:
    g = n1
    m = n2
    p = n3
elif n1 > n3 > n2:
    g = n1
    m = n3
    p = n2
elif n2 > n1 > n3:
    g = n2
    m = n1
    p = n3
elif n2 > n3 > n1:
    g = n2
    m = n3
    p = n1
elif n3 > n1 > n2:
    g = n3
    m = n1
    p = n2
elif n3 > n2 > n1:
    g = n3
    m = n2
    p = n1

if n1 == n2 or n2 == n3 or n3 == n1:
    print('\033[31;1malguns valores digitados são iguais')

print('O maior é {} \nO segundo maior é {} \nO menor é {}'.format(g, m, p))


