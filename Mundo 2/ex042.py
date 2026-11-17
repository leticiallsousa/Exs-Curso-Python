l1 = float(input('Digite a primeira medida: '))
l2 = float(input('Digite a segunda medida: '))
l3 = float(input('Digite a terceira medida: '))

if l1+l2 >= l3 and l2+l3 >= l1 and l3+l1 >= l2:
    print('Essas medidas podem formar um triângulo!')
    if l1 == l2 == l3:
        print('O triângulo será equilátero.')
    elif l1 != l2 != l3:
        print('O triângulo será escaleno')
    else:  # ou elif l1 == l2 != l3 or l2 == l3 != l1 or l3 == l1 != l2:
        print('O triângulo será isóceles')

else:
    print('Essas medidas não podem formar um triângulo!')
