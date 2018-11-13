from time import sleep
print('\033[34mProgressão Aritimética!\033[m')
p = 0
termo = int(input('\nDigite o primeiro termo: '))
razao = int(input('Digite a razão: '))
vezes = termo + 11 * razao
for pa in range(termo, vezes, razao):
    print('{}'.format(pa), end=' => ')
    sleep(0.5)
print('fim')
