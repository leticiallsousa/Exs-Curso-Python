s = 0
for soma in range(1, 7):
    numero = int(input('Escreva um número inteiro: '))
    if numero % 2 == 0:
        s += numero
print(f'A soma dos valores pares digitados é igual a: {s}')
