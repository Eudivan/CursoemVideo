from random import randint
a = randint(0, 10)
b = randint(0, 10)
c = randint(0, 10)
d = randint(0, 10)
e = randint(0, 10)
n = a, b, c, d, e
print(f'Os números gerados foram: ', end='')
for c in sorted(n):
    print(f'{c} ', end='')

print(f'\n\nO maior valor foi: {max(n)}')
print(f'O menor valor foi: {min(n)}')


