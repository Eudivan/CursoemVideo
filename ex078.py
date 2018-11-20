valor = []
for cont in range(0, 5):
    valor.append(int(input('Digite um valor: ')))

m = max(valor)
n = min(valor)
print('=+' * 30)
print(f'Você digitou os valores {valor}')


print(f'O maior valor foi {m} nas posições ', end='')
for pos, num in enumerate(valor):
    if num == m:
        print(pos, end='...')


print(f'\nO menor valor foi {n} nas posições ', end='')
for pos, num in enumerate(valor):
    if num == n:
        print(pos, end='...')
print('\n\n')


