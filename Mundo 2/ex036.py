casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário? '))
anos = int(input('Em quantos anos pretende pagar a casa? '))
if casa/anos/12 > salario/100*30:
    print('Seu empréstimo foi negado!')
else:
    print('Seu empréstimo foi aprovado!')