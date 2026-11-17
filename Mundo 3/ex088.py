from random import randint

print('=-' * 20)
print(f' JOGA NA MEGA SENA '.center(40))
print('=-' * 20)

quantidade = int(input('Quantos jogos você quer que eu sorteie? '))

jogos = list()
for q in range(0, quantidade):
    megasena = list()
    while len(megasena) != 6:
        numero = randint(1, 60)
        while numero in megasena:
            numero = randint(1, 60)
        megasena.append(numero)
    jogos.append(megasena)

print(f' SORTEANDO {quantidade} JOGOS '.center(40, '='))

for j in range(0, quantidade):
    print(f'JOGO {j+1}: {sorted(jogos[j])}')

print(f' BOA SORTE '.center(40, '='))
