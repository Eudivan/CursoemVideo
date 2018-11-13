pmai = 0
pmen = 0
psma = 0
psme = 0
for c in range(1, 6):
    peso = float(input('{}º peso: '.format(c)))
    if peso > pmai:
        pmai = peso
        psma = c
    if c == 1:
        pmen = peso
    if peso < pmen:
        pmen = peso
        psme = c
print('O maior peso foi da {}ª com {}Kg \nO menor peso da {}ª com {}Kg'.format(psma, pmai, psme, pmen))
