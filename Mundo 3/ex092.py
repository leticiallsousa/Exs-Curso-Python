dados = dict()
dados['nome'] = str(input('Nome: '))
ano_nascimento = int(input('Ano de nascimento: '))
dados['idade'] = 2023-ano_nascimento
dados['ctps'] = int(input('Carteira de trabalho (0 se não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: '))
ano_aposentadoria = dados['contratação']+35
dados['aposentadoria'] = ano_aposentadoria-ano_nascimento
print('=-'*10)
for k, v in dados.items():
    print(f"'{k}': {v}, ", end='')
print()
for k, v in dados.items():
    print(f"{k} tem o valor {v}")
