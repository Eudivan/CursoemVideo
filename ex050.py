s = 0
cont = 0
for soma in range(1, 7, 1):
    n1 = int(input('Digite o {} numero: '.format(soma)))
    n2 = n1 % 2
    if n1 % 2 == 0:
        s = s + n1
        cont += 1


print('\033[32mNúmeros pares digitado = {} \nO total é {}\033[m'.format(cont, s))
