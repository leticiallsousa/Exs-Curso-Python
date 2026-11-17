nome_barato = None
total = mais_mil = cont = 0
while True:
    cont += 1
    simnao = None
    nome = str(input('Digite o nome de um produto: '))
    preco = float(input('Digite o preço do produto: R$'))
    while simnao != 'S' and simnao != 'N':
        simnao = str(input('Deseja continuar? [S/N] ')).upper()
    if cont == 1:
        barato = preco
    total += preco
    if preco > 1000:
        mais_mil += 1
    if preco <= barato:
        nome_barato = nome
        barato = preco
    if simnao == 'N':
        break
print(f'O total da compra foi R${total:.2f}')
print(f'{mais_mil} produtos custam mais que R$1000.00')
print(f'O nome do produto mais barato é {nome_barato}, que custa {barato:.2f}')
