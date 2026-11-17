n1 = int(input('Qual o primeiro número? '))
n2 = int(input('Qual o segundo número? '))
if n1 > n2:
    print(f'O número {n1} é o maior número!')
elif n2 > n1:
    print(f'O número {n2} é o maior número!')
else:
    print('Os dois números são iguais!')
