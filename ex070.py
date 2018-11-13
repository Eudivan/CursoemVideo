print('ESTATÍSTCA DE PRODUTOS!\n\n')
total = m100 = barato = cont = nome = 0
while True:
    s = ' '
    p = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    if cont == 1 or preco < barato:
        barato = preco
        nome = p

    if preco > 1000:
        m100 += 1
    while s not in 'sn':
        s = str(input('Deseja adicionar outro produto? [S/N]')).lower().strip()[0]
    if s == 'n':
        break

print(f'''\n--------CUPOM FISCAL--------
Total de produtos = {cont}
Total gasto = R${total:.2f}
Produtos que custam mais de R$1000.00 = {m100}
Produto mais barato: {nome} R${barato:.2f}''')

