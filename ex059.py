from time import sleep
esco = 0
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
print('''[1]SOMAR
[2]MULTIPLICAR
[3]MAIOR
[4]NOVOS NUMEROS
[5] sair: ''')

while esco != 5:
    esco = int(input('>>>>>> Selecione uma opção: '))
    if esco == 1:
        print('{} + {} = {}\n'.format(n1, n2, n1 + n2))
    elif esco == 2:
        print('{} X {} = {}\n'.format(n1, n2, (n1 * n2)))
    elif esco == 3:
        if n1 > n2:
            print('O maior é {}\n'.format(n1))
        elif n2 > n1:
            print('O maior é {}\n'.format(n2))
        else:
            print('O dois são iguais!\n')
    elif esco == 4:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
        print('''[1]SOMAR2
        
[2]MULTIPLICAR
[3]MAIOR
[4]NOVOS NUMEROS
[5] sair: ''')
    elif esco == 5:
        print('Finalizando...')
    else:
        print('Opção inválida!')

for c in range(1, 7):
    print('.')
    sleep(0.2)
print('Obrigado por ultilizar nosso sistema!')
