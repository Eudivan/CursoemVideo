dicio = {}
gols = gol = 0
dicio['Nome'] = str(input('Nome do jogador: ')).strip().capitalize()
part = int(input('Numero de partidas jogadas: '))
for c in range(part):
    gol = int(input(f'Quantos gols {dicio["Nome"]} marcou na {c + 1}ª partida: '))
    gols += gol
dicio['Total de partidas'] = part
dicio['Gols'] = gols
dicio['Média de gols/partida'] = gols / part
for k, v in dicio.items():
    print(f' - {k}: {v}')