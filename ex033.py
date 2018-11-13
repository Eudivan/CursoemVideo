v1 = int(input('Valor um: '))
v2 = int(input('Valor dois: '))
v3 = int(input('valor três: '))
lista = [v1, v2, v3]
print('O MENOR foi \033[1;32m{}\033[m'.format(min(lista)))
print('O MAIOR foi \033[1;34m{}\033[m'.format(max(lista)))
