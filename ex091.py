from random import randint
from time import sleep
from operator import itemgetter
jogador = {}
ranking = {}
for c in range(4):
    jogador[c] = randint(1, 6)
print('-' * 30)
for k, v in jogador.items():
    sleep(0.8)
    print(f'Jogador nº{k + 1} jogou o dado!')
    sleep(2)
    print(f'deu {v}')

    print('\033[34m`,´\033[m' * 10)

print('-=' * 30)

ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar foi o jogador{v[0] + 1} com {v[1]} pontos')
