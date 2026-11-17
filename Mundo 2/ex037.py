num = int(input('Digite um número inteiro: '))
conv = int(input('''Escolha uma das bases para conversão:
[1] Binário
[2] Octonal
[3] Hexadecimal\n'''))
if conv == 1:
    print(f'O número {num} convetido para Binário é igual a {bin(num)[2:]}')
elif conv == 2:
    print(f'O número {num} convetido para Octonal é igual a {oct(num)[2:]}')
elif conv == 3:
    print(f'O número {num} convetido para Hexadecimal é igual a {hex(num)[2:]}')
else:
    print('Opção inválida')