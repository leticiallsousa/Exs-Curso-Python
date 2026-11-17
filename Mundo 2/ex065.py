num = int(input('Digite um número: '))
simnao = str(input('Quer continuar? [S/N] ')).upper()
media = maior = menor = num
c = 1

while simnao == 'S':
    num = int(input('Digite um número: '))
    simnao = str(input('Quer continuar? [S/N] ')).upper()
    if num >= maior:
        maior = num
    if num <= menor:
        menor = num
    media += num
    c += 1
media = media/c
print(f'Você digitou {c} números e a média foi {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')

