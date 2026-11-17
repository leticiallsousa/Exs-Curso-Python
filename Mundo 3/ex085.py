numeros = [[], []]
for n in range(1, 8):
    val = int(input(f'Digite o {n}° número: '))
    if not val % 2 == 0:
        numeros[0].append(val)
    else:
        numeros[1].append(val)

print(f'Os valores ímpares digitados foram: {sorted(numeros[0])}')
print(f'Os valores pares digitados foram: {sorted(numeros[1])}')
