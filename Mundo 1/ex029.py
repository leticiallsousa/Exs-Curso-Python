vel = float(input('Escreva a velocidade de um carro: '))
if vel > 80:
    print(f'Você foi multado em R${(vel-80)*7} por estar digindo {vel-80}km/h acima do limite de velocidade!')
else:
    print('Você não foi multado!')
