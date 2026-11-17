pessoas = list()
pessoa = dict()
idade = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo [M/F]: '))
    pessoa['idade'] = int(input('Idade: ')) 
    idade += pessoa['idade']
    pessoas.append(pessoa.copy())
    

    continuar = None
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Deseja continuar? [S/N] ')).upper()
    if continuar == 'N':
        break

print('=-'*30)
print(f'- Foram cadastradas {len(pessoas)} pessoas.')
print(f'- A média de idade de pessoas do grupo é {idade/(len(pessoas))}')

mulheres = list()
idade_media = list()
for f in range(0, len(pessoas)):
    if pessoas[f]['sexo'] in 'fF':
        mulheres.append(pessoas[f]['nome'])
    if pessoas[f]['idade'] > idade/(len(pessoas)):
        idade_media.append(pessoas[f]['nome'])

print(f'- Lista com todas as mulheres: {mulheres}')
print(f'- Lista com todos com idade acima da média ({idade/(len(pessoas))}): {idade_media}')
