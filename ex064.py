cont = n = total = 0
print('Para sair e mostra o resultado digite 999\n\n')
while n != 999:
    n = int(input('Informe um número: '))
    if n != 999:
        total += n
        cont += 1
if cont != 1:
    print('Você digitou {} números\nA soma é {}'.format(cont, total))
elif cont == 1:
    print('Você digitou apenas o número {}'.format(total))





