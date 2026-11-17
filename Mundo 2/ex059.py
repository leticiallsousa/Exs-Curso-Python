n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opcao = None
while opcao != 5:
    opcao = int(input('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Sair do Programa
Qual é a sua opção? '''))
    if opcao == 1:
        print(f'A soma entre {n1} e {n2} é igual a {n1+n2}.')
    elif opcao == 2:
        print(f'O produto entre {n1} e {n2} é igual a {n1*n2}')
    elif opcao == 3:
        if n1 > n2:
            print(f'O maior número é o {n1}')
        if n2 > n1:
            print(f'O maior número é o {n2}')
        if n1 == n2:
            print(f'Os dois números são iguais: {n1}')
    elif opcao == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('Finalizando programa... ')
    else:
        print('Opção inválida')
print('Fim do programa')