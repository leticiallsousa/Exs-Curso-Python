sal = float(input('Qual o valor do seu salário? R$'))
if sal > 1250:
    print(f'Com um aumento de 10% seu salário vai ser R${sal/100*10+sal}')
else:
    print(f'Com um aumento de 15% seu salário vai ser R${sal/100*15+sal}')
