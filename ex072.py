num = 21
n = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', \
    'treze', 'quartoze', 'quize', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
c = 'S'
while c in 'S':
    while True:
        num = int(input('Digite um número de 0 a 20: '))
        if 0 <= num <= 20:
            break
        print('\nTente novamente! ', end='')
    print(f'Você digitou: {n[num]}')
    while True:
        c = str(input('\n>>> Quer digitar outro número:[S/N] ')).strip().upper()[0]
        if c in 'SN':
            break

print('\n\n\n\nPrograma encerrado!')











