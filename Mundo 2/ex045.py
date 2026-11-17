import random

jogada = int(input('Escolha:\n[1] Pedra\n[2] Papel\n[3] Tesoura\n'))
if jogada == 1:
    jogada = 'pedra'
elif jogada == 2:
    jogada = 'papel'
elif jogada == 3:
    jogada = 'tesoura'
else:
    jogada = random.choice(['pedra', 'papel', 'tesoura'])

movimentos = random.choice(['pedra', 'papel', 'tesoura'])

if movimentos == jogada:
    print(f'MAQUINA: {movimentos}\nVOCÊ: {jogada}\nEmpate!')
elif (movimentos == 'pedra' and jogada == 'papel') or (movimentos == 'papel' and jogada == 'tesoura') or \
        (movimentos == 'tesoura' and jogada == 'pedra'):
    print(f'MAQUINA: {movimentos}\nVOCÊ: {jogada}\nVocê ganhou!')
else:
    print(f'MAQUINA: {movimentos}\nVOCÊ: {jogada}\nA máquina ganhou!')
# ou
# elif (movimentos == 'pedra' and jogada == 'tesoura') or (movimentos == 'papel' and jogada == 'pedra') or
# (movimentos == 'tesoura' and jogada == 'papel'):
