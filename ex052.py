cont = 0
num = int(input('Digite um numero: '))
for p in range(1, num + 1, 1):
    if num % p == 0:
        cont += 1
        print('\033[32;1m{}\033[m'.format(p), end=' ')
    else:
        print('\033[31m{}\033[m'.format(p), end=' ')
print('\nO número {} foi divísivel {}'.format(num, cont), end=' ')
if cont == 2:
    print('vezes!\nPor isso ele é PRIMO!')
elif cont == 1:
    print('vez!\num NÃO É PRIMO, pois é apenas divisível por ele mesmo!')
else:
    print('vezes!\nNÃO É PRIMO!')
