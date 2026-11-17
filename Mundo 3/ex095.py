jogadores = list()

while True:
    print('-'*30)
    jogador = dict()
    jogador['nome'] = str(input('Nome do jogador: '))
    totalp = int(input('Quantas partidas jogou? '))
    partidas = list()
    for p in range(1, totalp+1):
        partidas.append(int(input(f'Quantos gols fez na {p}º partida? ')))

    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)

    jogadores.append(jogador.copy())
    partidas.clear()

    continuar = None
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Deseja continuar? [S/N] ')).upper()
    if continuar == 'N':
        break

print('=-'*30)

print(f'{"No.":<6}{"Nome":<15}{"Gols":<23}{"Total":<4}')
for i, jogador in enumerate(jogadores):
    print(f'{i:<6}{jogador["nome"]:<15}{str(jogador["gols"]):<23}{str(jogador["total"]):<4}')

print('=-'*30)
while True:
    mostrar = int(input('Mostrar dados de qual jogador? '))
    if mostrar != 999:
        if 0 > mostrar and mostrar > len(jogadores)-1: 
            print(f'ERRO! Não existe jogador com código {mostrar}')
            break
        print(f'--- LEVANTAMENTO DO JOGADOR {jogadores[mostrar]["nome"]}:')
        for i, j in enumerate(jogadores[mostrar]['gols']):
            print(f'    No jogo {i}, fez {jogadores[mostrar]["gols"][i]} gols.')
        print('-'*30)
    else:
        print(f'<< VOLTE SEMPRE >>')
        break
