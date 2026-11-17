import random

numero = int(input('Escreva um número de 0 a 5: '))
num = random.randint(0, 5)
if numero == num:
    print(f'Parabéns, você acertou! O número escolhido foi {num}.')
else:
    print(f'Infelizmente você errou! O número certo era {num} (Você escolheu {numero}).')
