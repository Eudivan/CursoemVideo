from time import sleep
n1 = float(input('Nota 01: '))
n2 = float(input('Nota 02: '))
n3 = float(input('Nota 03: '))
m = (n1 + n2 + n3) / 3
print('\033[1;34mO aluno está...\033[m')
sleep(1)
if m >= 7:
    print('\033[33mAPROVADO! Com a media {:.1f}'.format(m))
elif m < 5:
    print('\033[31mREPROVADO! Com média {:.1f}'.format(m))
else:
    print('\033[34mna RECUPERAÇÃO! Com média {:.1f}'.format(m))