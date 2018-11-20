list = []
s = ' '

while True:
    n = int(input('Digite um valor: '))
    if n in list:
        print('Valor duplicado!... não foi adicionado')
    else:
        list.append(n)
    while s not in 'sn':
        s = str(input('Quer continuar:[s/n] ')).strip().lower()[0]
    if s in 's':
        s = ' '
    if s in 'n':
        break

list.sort()
print(list)




