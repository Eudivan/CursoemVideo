l1 = int(input('lado 1: '))
l2 = int(input('lado 2: '))
l3 = int(input('lado 3: '))
lista = [l1, l2, l3]
meio =(l1 + l2 + l3) - (max(lista) + min(lista))
print('Os valores {}, {} e {}...'.format(min(lista), meio, max(lista)))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l2 + l1:  #minha solução max(lista) - min(lista) < meio < max(lista) + min(lista)
    print('\033[032mFormam um triangulo!')
else:
    print('\033[31mNão formam um triangulo!')
