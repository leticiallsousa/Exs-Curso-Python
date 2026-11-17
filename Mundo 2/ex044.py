preco = float(input('Qual o preço normal do produto? '))
metodo = int(input(f'QUAL O MÉTODO DE PAGAMENTO?\n{"-"*27}\n[1] À vista dinheiro/cheque: 10% de desconto\n[2] À '
                   f'vista cartão: 5% de desconto\n[3] Em até 2x no cartão: preço normal\n[4] 3x ou mais: 20% de '
                   f'juros\n'))
if metodo == 1:
    print(f'O valor do produto com desconto de 10% é R$ {preco-(preco/100*10)}')
elif metodo == 2:
    print(f'O valor do produto com desconto de 5% é R$ {preco-(preco/100*5)}')
elif metodo == 3:
    print(f'O valor do produto continua o mesmo! Duas parcelas de R${preco/2} cada, no total R${preco}')
elif metodo == 4:
    parcelas = int(input('Em quantas vezes você quer parcelar? '))
    if parcelas < 3:
        print(f'O valor do produto continua o mesmo! Duas parcelas de R${preco/2} cada, no total R${preco}')
    else:
        print(f'O valor do produto aumentou em 20%! Você vai pagar {parcelas}x de R${(preco+(preco/100*20))/parcelas}'
              f' cada, no total R${(preco+(preco/100*20))}')
else:
    print('Opção inválida!')
