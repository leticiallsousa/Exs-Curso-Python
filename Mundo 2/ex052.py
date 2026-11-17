numero = int(input('Digite um número: '))
divisoes = 1
divisivel = 0
for d in range(0, numero):
    # ou
    # for d in range(1, numero+1):
    #   if numero % d == 0:
    if numero % divisoes == 0:
        divisivel += 1
    divisoes += 1

if divisivel > 2:
    print(f'O número {numero} não é um número primo')
else:
    print(f'O número {numero} é um número primo')
