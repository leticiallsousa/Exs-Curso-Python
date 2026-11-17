valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    continuar = None
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Deseja continuar? [S/N] ')).upper()
    if continuar == 'N':
        break

print('=-'*30)
print(f'Você digitou {len(valores)} elementos.')
print(f'Os valores em ordem decrescente são {sorted(valores, reverse=True)}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
