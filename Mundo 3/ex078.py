valores = []
for val in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {val}: ')))
print('=-'*25)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)} nas posições ', end='')
for p, v in enumerate(valores):
    if v == max(valores):
        print(f'{p}... ', end='')
print(f'\nO menor valor digitado foi {min(valores)} nas posições ', end='')
for p, v in enumerate(valores):
    if v == min(valores):
        print(f'{p}... ', end='')
