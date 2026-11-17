num = int(input('Escreva um número inteiro: '))
print(f'-------------\nTABUADA DO {num}\n-------------')
for mult in range(0, 10):
    print(f'{num} x {mult} = {num*mult}')
print('-------------')
