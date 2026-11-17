valores = []
while True:
    valor = int(input('Digite um valor: '))

    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    continuar = None
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Deseja continuar? [S/N] ')).upper()
    if continuar == 'N':
        break

print('=-'*25)
print(f'Você digitou o valores {sorted(valores)}')
