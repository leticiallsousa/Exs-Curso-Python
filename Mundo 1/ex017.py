import math

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
print(f'O valor da hipotenusa é {math.hypot(co, ca):.2f}')
