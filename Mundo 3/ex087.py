matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = terceira = maior = 0

for a in range(0, 3):
    for b in range(0, 3):
        matriz[a][b] = int(input(f'Digite um valor para [{a}, {b}]: '))
        if matriz[a][b] % 2 == 0:
            pares += matriz[a][b]

for a in range(0, 3):
    for b in range(0, 3):
        print(f'[{matriz[a][b]:^5}]', end='')
    print()

for a in range(0, 3):
    terceira += matriz[a][2]
for a in matriz[1]:
    if a > maior:
        maior = a

print(f'A soma dos valores pares é {pares}.')
print(f'A soma dos valores da terceira coluna é {terceira}.')
print(f'O maior valor da segunda linha é {maior}.')
