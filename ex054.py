from datetime import date
mai = 0
men = 0
em = 0
en = 0
for c in range(1, 8, 1):
    nasc = int(input('Digite a {}ª data de nascimento: '.format(c)))
    n1 = date.today().year - nasc
    if n1 >= 18:
        mai += 1
        print('\033[34m')

    else:
        men += 1
        print('\033[33m')

if mai == 0:
    em = 'não existe maiores'
    en = 'são menores'
elif men == 0:
    en = 'não existe menores'
    em = 'são maiores'
elif mai > 1 and men > 1:
    en = 'são menores'
    em = 'são maiores'
elif mai < 2:
    em = 'é maior'
    en = 'são menores'
else:
    em = 'são maiores'
    en = 'é menor'
print('\033[1;30m{} {} de idade e {} {} de idade!'.format(mai, em, men, en))
