import random

jogadores = dict()

for j in range(1, 5):
    jogadores[f'jogador {j}'] = random.randint(1, 6)

print('Valores Sorteados: ')
for k, v in jogadores.items():
    print(f'    O {k} tirou {v}')

jogadores_ordenado = dict(sorted(jogadores.items(), key=lambda item: item[1]))
# para ordenar o dicionário eu também posso usar:
# from operator import itemgetter
# sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print('Ranking dos Jogadores:')
ranking = 1
for k, v in jogadores_ordenado.items():
    print(f'    {ranking}º lugar: {k} com {v}')
    ranking += 1
