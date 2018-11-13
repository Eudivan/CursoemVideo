print('--------------------------')
print('  CADASTRO DE PESSOAS')
print('--------------------------')
m18 = hom = mul = 0
while True:
    n = str(input('Nome da pessoa: '))
    i = int(input('Idade: '))

    s = ' '
    while s not in 'fm':
        s = str(input('Sexo [F/M] ')).lower().strip()[0]
    print('--------------------------')
    if i > 18:
        m18 += 1
    if s in 'm':
        hom += 1
    if s in 'f' and i < 20:
        mul += 1
    con = ' '
    while con not in 'sn':
        con = str(input('NOVO CADASTRO? [S/N] ')).strip().lower()[0]
    if con in 'n':
        break

print(f'Foram registrado {hom} homens \n{m18} pessoas têm mais de 18 anos \n{mul} mulheres têm menos de 20 anos')
