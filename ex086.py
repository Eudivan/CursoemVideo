mtx = []
linha = int(input('Numero de linhas: '))
colun = int(input('Número de colunas:'))
print(f'Matrix {linha}x{colun}')
for c in range(linha):
    mtx.append([])
    for x in range(colun):
        mtx[c].append(input(f'Matrix ({c},{x}): '))

for l in range(linha):
    for c in range(colun):
        if c == 0:
            print('[', end='')
        print(f'{mtx[l] [c]:^7}', end='')
        if c + 1 == colun:
            print(']')



