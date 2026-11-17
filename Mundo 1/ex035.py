num1 = float(input('Digite o comprimento de um lado de um triângulo: '))
num2 = float(input('Digite o comprimento de um lado de um triângulo: '))
num3 = float(input('Digite o comprimento de um lado de um triângulo: '))

if (num2+num3) > num1 and (num1 + num3) > num2 and (num2 + num1) > num3:
    print('Esses comprimentos podem formar um triângulo!')
else:
    print('Esses comprimentos não podem formar um triângulo!')
