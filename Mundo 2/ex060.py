valor = int(input('Digite um valor para saber seu fatorial: '))
print(f'Calculando {valor}! = ', end='')
contagem = valor
multiplicacao = 1
while contagem >= 2:
    print(contagem, end=' x ')
    multiplicacao *= contagem
    contagem -= 1
print(f'1 = {multiplicacao}')