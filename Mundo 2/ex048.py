s = 0
for impares in range(-1, 500, 2):
    if impares % 3 == 0:
        s += impares
print(f'A soma de todos os números ímpares múltiplos de 3 entre 1 e 500 é igual a: {s}')
