tupla = tuple()
pares = ''
for c in range(0, 4):
    numero = int(input('Digite um valor: '))
    tupla += numero,
    if numero % 2 == 0:
        pares += f'{numero} '
print(f'O valores digitados foram: {tupla}')

nove = tupla.count(9)
if nove == 0:
    print('O número 9 não foi digitado')
else:
    print(f'O número 9 apareceu {nove} vez{"es" if 0 == nove or nove > 1 else ""}')

if 3 in tupla:
    print(f'A primeira posição em que o número 3 aparece é a {tupla.index(3)+1}º posição')
else:
    print('Você não digitou o número 3')

if pares == '':
    print('Você não digitou números pares')
else:
    print(f'Números pares digitados: {pares}')
