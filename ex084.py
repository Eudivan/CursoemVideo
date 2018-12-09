rep = 'a'
lista = []
listacopia = []
lp = []
lle = []
cont = p = le = 0  # p o mais pesado. le o mais leve
while True:
    print('--' * 30)
    nome = str(input('Nome: ')).strip().capitalize()
    peso = float(input('Peso: '))
    print('--' * 30)
    lista.append(nome)
    lista.append(peso)
    listacopia.append(lista[:])
    lista.clear()
    #rep é quantas vezes o laço vai rodas para cadastra pessoas
    while rep not in ' 0':
        rep = str(input('\033[34mPara continuar tecle \033[30;1mENTER\033[m\033[34m ou digite \033[30;1m0\033[m\033[34m para encerrar: \033[m'))
    if rep == '0':
        break
    rep = 'a'

for c in listacopia:
    #PEGANDO O MAIOR E MENOR PESO!
    if cont == 0:
        p = le = c[-1]
    if p < c[-1]:
        p = c[-1]
    if le > c[-1]:
        le = c[-1]
    cont += 1
for c in listacopia:
    if c[-1] == p:
        lp.append(c[0])
    if c[-1] == le:
        lle.append(c[0])
print(f'Foram cadastrados {len(listacopia)} pessoas!')
print(f'O maior peso foi {p}Kg com a(s) pessoa(s) {lp}\nO menor peso foi {le}Kg com a(s) pessoa(s) {lle}')


