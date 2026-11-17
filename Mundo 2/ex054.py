sim = 0
nao = 0
for nasc in range(0, 7):
    ano = int(input('Qual o seu ano de nascimento? '))
    if 2022-ano >= 18:
        sim += 1
    else:
        nao += 1
print(f'{sim} das pessoas já atingiram a maioridade, e {nao} pessoas ainda não atingiram')
