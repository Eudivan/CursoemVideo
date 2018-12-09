num = [[], []]
for c in range(7):
    n = int(int(input('Digite um valor: ')))
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)





num[0].sort()
num[1].sort()
print(f'Pares {num[0]} \nÍmpares{num[1]}')

