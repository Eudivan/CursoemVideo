lista = []
imp = []
par = []
c = q = 0
qtd = int(input('Quer digite quantos valores? '))
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    c += 1
    if c == qtd:
        print('\33[31m-=\033[m' * 30)
        print('Digite 0 para encerrar!')
        q = int(input('Quer digita mais quantos valores? '))
        print('\033[31m=-\033[m' * 30)
        qtd += q
        if q == 0:
            break
for num in lista:
    if num % 2 == 0:
        par.append(num)
    else:
        imp.append(num)


print(f'PARES  \033[33m{sorted(par)}\033[m')
print(f'ÍMPARES \033[32m{sorted(imp)}\033[m')
print(f'Ao todo foram digitados {len(lista)} elementos \nTodos os valores \033[34m{sorted(lista)}\033[m')


