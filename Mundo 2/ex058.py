import random
usuario = int(input('Acabei de pensar em um número entre 0 e 10.\nTente adivinhar qual foi esse número: '))
computador = random.randint(1, 10)
tentativas = 1
while usuario != computador:
    if usuario > computador:
        usuario = int(input('Menos... Tente novamente: '))
        tentativas += 1
    if usuario < computador:
        usuario = int(input('Mais... Tente novamente: '))
        tentativas += 1
print(f'Você acertou com {tentativas} tentativas. Parabéns!')