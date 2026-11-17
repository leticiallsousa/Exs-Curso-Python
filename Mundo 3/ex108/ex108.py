import moeda

preço = float(input('Digite um preço: R$'))

print(f'A metade de R${moeda.moeda(preço)} é R${moeda.moeda(moeda.metade(preço))}')
print(f'O dobro de R${moeda.moeda(preço)} é R${moeda.moeda(moeda.dobro(preço))}')
print(f'Aumentando 10%, temos R${moeda.moeda(moeda.aumentar(preço, 10))}')
