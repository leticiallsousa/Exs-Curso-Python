media = 0
velho = 0
quant = 0
nome_velho = 0
for p in range(1, 5):
    print(f'----- {p}º PESSOA -----')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    media += idade
    if sexo == 'M' and idade > velho:
        velho = idade
        nome_velho = nome
    if sexo == 'F' and idade < 20:
        quant += 1
media /= 4
print(f'A média de idade do grupo é de {media:.1f} anos')
print(f'O homem mais velho tem {velho} anos e se chama {nome_velho}')
print(f'Ao todo tem {quant} mulher(es) com menos de 20 anos')
