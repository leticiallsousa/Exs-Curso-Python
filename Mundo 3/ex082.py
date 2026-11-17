valores = []
while True:
    valores.append(int(input('Digite um valor: ')))

    continuar = None
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Deseja continuar? [S/N] ')).upper()
    if continuar == 'N':
        break

par = []
impar = []

for v in valores:
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)

print('=-'*30)
print(f'A lista completa é {valores}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')
