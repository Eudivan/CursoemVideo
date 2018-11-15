print('''Sequência de Fibonacci é uma sucessão de números que obedecem um padrão em que cada elemento subsequente
é a soma dos dois anteriores. 1, 1, 2, 3, 5...\n\n''')

f = int(input('Informe quantos números da sequência de fibonacci quer ver: '))
cont = 2
a = b = 1
print(f'{a}, {b},', end=' ')
while True:
    c = a + b
    print(f'{c},', end=' ')
    b = a
    a = c
    cont += 1
    if cont == f:
        s = int(input('\n>>> Quer ver mais quantos número? digite 0 para encerrar  '))
        if s > 0:
            f += s
        else:
            break

print('\n\n\n\nPrograma encerrado!')

