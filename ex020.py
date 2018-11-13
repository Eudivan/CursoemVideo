from random import shuffle
n1 = input('aluno um: ')
n2 = input('Aluno dois: ')
n3 = input('aluno três: ')
n4 = input('Aluno quatro: ')
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação é')
print(lista)
