from time import sleep
nota = [[]]
adc = 'a'
num = 0
i = ' '
while True:
    nota[num].append(str(input('Nome do aluno: ')).strip().capitalize())
    nota[num].append(float(input('Nota 1: ')))
    nota[num].append(float(input('Nota 2: ')))
    print('--' * 32)
    while adc not in ' 0':
        adc = input('Tecle ENTER para adicionar um aluno ou digite 0 para encerrar: ')
    print('--' * 32)
    if adc == '0':
        break
    num += 1
    nota.append([])
    adc = 'a'
print('-=' * 32)
print('-' * 26)
print('\033[1;37mID |  ALUNO      | MÉDIA\033[m')
print('-' * 26)
for c in range(len(nota)):
    print(f'{c + 1}   {nota[c][0]: <16}', end='')
    print(f'{(nota[c][1] + nota[c][2]) / 2}')
print('-' * 26)
print()
while True:
    while i not in range(0, len(nota)+1):
        i = int(input('Para ver as notas do aluno digite o ID ou 0 para encerrar: '))
    if i == 0:
        break
    else:
        i -= 1
        print(f'A notas de \033[1;37m{nota[i][0]}\033[m são \033[1;37m{nota[i][1], nota[i][2]}\033[m')
        print('-' * 64)

    i = ' '
for c in range(5):
    print('.')
    sleep(0.4)
print('Programa encerrado!')
















