import random
jogador = None
vit = 0
while True:
    while jogador != 'P' and jogador != 'I':
        jogador = str(input('Você deseja ser Par[P] ou Ímpar[I]? ')).upper()
    if jogador == 'P':
        maquina = 'I'
    else:
        maquina = 'P'
    num_j = int(input('Qual número de 1 a 10 você escolhe? '))
    print('-'*20)
    num_m = random.randint(1, 10)
    print(f'Eu escolhi o número {num_m}')
    print(f'A soma dos nossos números é igual a {num_j + num_m}.', end=' ')
    if (num_m+num_j) % 2 == 0:
        if jogador == 'P':
            print('Como você escolheu par, você ganhou!')
            vit += 1
        if maquina == 'P':
            print('Como eu escolhi par, eu ganhei!')
            print('-' * 20)
            break
    if (num_m+num_j) % 2 != 0:
        if jogador == 'I':
            print('Como você escolheu ímpar, você ganhou!')
            vit += 1
        if maquina == 'I':
            print('Como eu escolhi ímpar, eu ganhei!')
            print('-' * 20)
            break
    print('-' * 20)

print(f'Jogo finalizado! Você ganhou {vit} vezes consecutivas!')

