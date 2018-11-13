classi = 'Palmeiras', 'Internacional', 'Flamengo', 'São Paulo', 'Gremio', 'Atletico-PR', 'Atlético-MG',\
                'Santos', 'Cruceiro', 'Botafogo', 'Flumeinense', 'Corinthians', 'Bahia', 'Vasco da Gama', 'Ceará SC',\
                'Sport Recife', 'EC Vitória', 'América-MG', 'Chapecoense', 'Paraná'
chap = 0
print('\033[33mOs primeiros colocados')
for c in range(0, 5):
    print(f'{c + 1}º ', end='')
    print(classi[c])

print('\n\n\033[31mO 4 últimos colcados')
for b in classi[-4:]:
    print(f'{classi.index(b) + 1}º ', end='')
    print(b)

chap = classi.index('Chapecoense') + 1
print(f'\n\033[30;1mO Chapecoense está na posição {chap}º')

print(f'\n\nTodos os clubes! {len(classi)}')
for a in (sorted(classi)):
    print(a)
