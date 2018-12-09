mat = []
maior = []
par = som3 = 0
li = int(input('Número de linhas: '))
col = int(input('Número de colunas: '))
for lin in range(li):
    mat.append([])
    for c in range(col):
        mat[lin].append(int(input(f'Posição [{lin}x{c}]: ')))
        #somando os pares
        if mat[lin][c] % 2 == 0:
            par += mat[lin][c]
        #somando a ultima coluna
        if c + 1 == col:
            som3 += mat[lin][c]
        #maio na segunda linha
        if lin == 1:
            maior.append(mat[lin][c])
for c in mat:
    print(f'{c}')
print(f'Soma do pares = {par} \nSoma da última coluna coluna = {som3} \nMaior na segunda linha = {max(maior)}\n{maior}')

