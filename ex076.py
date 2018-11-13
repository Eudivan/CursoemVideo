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
print('-' * 40)


