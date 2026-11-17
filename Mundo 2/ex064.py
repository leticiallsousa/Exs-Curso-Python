num = int(input('Digite um número inteiro: '))
soma = num
while num != 999:
    num = int(input('Digite um número inteiro: '))
    if num == 999:
        break
    soma += num
print(f'A soma dos valores digitados é: {soma}')
