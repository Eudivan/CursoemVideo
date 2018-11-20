lista = []
cont = 0
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    s = ' '
    while s not in 'sn':
        s = str(input('Quer continuar?[s/n] ')).strip().lower()[0]
    if s in 'n':
        break
    elif s in 's':
        s = ' '
lista.sort(reverse=True)
print('~~' * 30)
if 5 not in lista:
    print('\nNenhum número 5 foi digitado!')
else:
    print('O 5 aparaceu nas posições ', end=' ')
    for pos, c in enumerate(lista):
        if c == 5:
            cont += 1
            print(f'[{pos}]', end=' ')




print(f'\nTotal de números {len(lista)}\nOs número na lista são {lista}')



