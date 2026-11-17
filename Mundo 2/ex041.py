nasc = int(input('Em que ano você nasceu? '))
idade = 2022-nasc
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SENIOR')
elif idade > 20:
    print('MASTER')
