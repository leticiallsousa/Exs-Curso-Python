import moeda

preço = float(input('Digite um preço: R$'))

print(f'A metade de R${moeda.moeda(preço)} é R${moeda.metade(preço, True)}')
print(f'O dobro de R${moeda.moeda(preço)} é R${moeda.dobro(preço)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(preço, 10, False)}')
