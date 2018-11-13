print('''Sequência de Fibonacci é uma sucessão de números que obedecem um padrão em que cada elemento subsequente
é a soma dos dois anteriores. 1, 1, 2, 3, 5...\n\n''')

n = int(input('Infome quantos número da sequencia quer mostra: '))
f1 = 1
f2 = 1
f3 = 0
cont = 3
print('\n{}, {}, '.format(f1, f2), end='')

while cont <= n:
    f3 = f1 + f2
    print('{}, '.format(f3), end='')
    f1 = f2
    f2 = f3
    cont += 1

