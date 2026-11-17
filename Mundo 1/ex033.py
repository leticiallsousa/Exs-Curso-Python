a = float(input('Digite um número: '))
b = float(input('Digite um número: '))
c = float(input('Digite um número: '))

maior = a
if a < b > c:
    maior = b
if a < c > b:
    maior = c

menor = a
if a > b < c:
    menor = b
if a > c < b:
    menor = c

print(f'O número {menor} é o menor e o número {maior} é o maior')
