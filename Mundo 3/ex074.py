from random import randint
numeros = (randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9))
print('Os números sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior número da tupla é: {max(numeros)}')
print(f'O menor número da tupla é: {min(numeros)}')
