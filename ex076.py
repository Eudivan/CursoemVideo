t = 0
tabela = ('Lápis', 1.75,
          'Borracha', 2.00,
          'Mochila', 120,
          'Caderno', 45,
          'estojo', 25,
          'grampeador', 5,
          'Compasso', 9.99,
          'Canetas', 15.90,
          'Livro', 34.90)
print('-' * 40)
print(f'{"Listagem dos produtos": ^40}')
print('-' * 40)
for pos in range(0, len(tabela)):
    if pos % 2 == 0:
        print(f'{tabela[pos]:.<30}R$', end='')
    else:
        print(f'{tabela[pos]:>7.2f}')
        t += tabela[pos]
print(f'TOTAL{"R$":.>27} {t: <7.2f}')
print('-' * 40)



#DOIS CÓDIGOS SEMELHANTES




print('\n\n\n')
produtos = ('pão', 4.40, 'presunto', 6.66, 'mortadela', 3.89, 'calabresa', 24.98, 'oleo', 3.49, 'ovo', 5, 'pizza', 19.8,
            'frango', 7, 'salcicha', 7, 'feijão', 4.4, 'maracuja', 3, 'melancia', 11, 'laranja', 7, 'bisteca', 34,
            'detergente', 1.3, 'sabão', 6, 'farinha', 10, 'arroz', 11, 'fanta', 3.8, 'vassoura', 8)
t2 = 0
print('-' * 40)
print(f'{"SUPERMERCADO EOA": ^40}')
print('-' * 40)
print(f'\n{"COMPRAS": ^40}')
for n in range(0, len(produtos)):
    if n % 2 == 0:
        print(f'{produtos[n]:.<30}R$', end='')
    elif n % 2 == 1:
        print(f'{produtos[n]: >7.2f}')
        t2 += produtos[n]
print(f'TOTAL{"R$":.>27}{t2: > 6.2f}')







