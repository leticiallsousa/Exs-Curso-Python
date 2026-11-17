jogador = dict()
partidas = list()

jogador['nome'] = str(input('Nome do jogador: '))
totalp = int(input('Quantas partidas jogou? '))

for partida in range(1, totalp+1):
    partidas.append(int(input(f'Quantos gols fez na {partida}º partida? ')))

jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)

print('=-'*30)
print(jogador)
print('=-'*30)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('=-'*30)
print(f'O jogador {jogador["nome"]} jogou {totalp} partidas.')

for i, v in enumerate(jogador['gols']):
    print(f'    => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
