dis = float(input('Qual a distância da viagem em km? '))
if dis <= 200:
    print(f'O preço da passagem é de R${dis*0.5}')
else:
    print(f'O preço da passagem é de R${dis*0.45}')

