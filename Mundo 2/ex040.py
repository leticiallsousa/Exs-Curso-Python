n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2)/2
if media >= 7:
    print('APROVADO')
elif 6.9 >= media >= 5:
    print('RECUPERAÇÃO')
elif media < 5:
    print('REPROVADO')
