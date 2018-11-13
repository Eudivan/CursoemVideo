n1 = int(input('lado 1: '))
n2 = int(input('lado 2: '))
n3 = int(input('Lado 3: '))
print('\033[34;1mOs numeros {}, {} e {}...\033[m'.format(n1, n2, n3))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('\033[1mFormam um Triangulo,', end=' ')
    if n1 == n2 == n3:
        print('Equilátero! Todos os lados são iguais.')
    elif n1 == n2 or n2 == n3 or n3 == n1:
        print('Isósceles! Dois lados são iguais.')
    elif n1 != n2 and n2 != n3 and n3 != n1:
        print('Escaleno! Todos os lados são diferentes.\033[m')
else:
    print('\033[31mNão formam um triangulo!\033[m')
