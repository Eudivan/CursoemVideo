s = 's'
cont = total = 0
maior = menor = 0
while s == 's':
    n = int(input('Digite um número: '))
    cont += 1
    if cont == 1:
        maior = n
        menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
    total += n
    s = str(input('Quer continar? [S/N]: ')).strip().lower()[0]
    while s not in 'sn':
        print('\033[31mOpção Inválida!\033[m')
        s = str(input('Quer continuar? [S/N]: ')).strip().lower()[0]
media = total / cont
print('\n\nVocê digitou {} números \nO maior valor = {} \nO menor = {} \nA média é {}'.format(cont, maior, menor, media))

4