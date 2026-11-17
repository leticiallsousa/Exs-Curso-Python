idade = int(input('Qual é a sua idade? '))
if idade > 18:
    print(f'Já passou {idade-18} anos do tempo do alistamento!')
elif idade < 18:
    print(f'Ainda faltam {18-idade} anos para se alistar!')
else:
    print('Está na hora de se alistar!')
