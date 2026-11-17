pessoas = list()
maior = menor = 0

while True:
    p = list()
    p.append(str(input('Nome: ')))
    p.append(int(input('Peso: ')))

    if len(pessoas) == 0:
        maior = menor = p[1]
    if p[1] > maior:
        maior = p[1]
    if p[1] < menor:
        menor = p[1]

    pessoas.append(p[:])
    p.clear()

    continuar = None
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Deseja continuar? [S/N] ')).upper()
    if continuar == 'N':
        break

print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')

print(f'O maior peso foi de {maior}kg, peso de: ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')

print(f'\nO menor peso foi de {menor}kg, peso de: ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
