maior_idade = homem = mulher = cont = 0
while True:
    sexo = simnao = None
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Qual o sexo dessa pessoa? [M/F] ')).upper()
    idade = int(input('Qual a idade dessa pessoa? '))
    while simnao != 'S' and simnao != 'N':
        simnao = str(input('Deseja continuar? [S/N] ')).upper()
    if idade > 18:
        maior_idade += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    cont += 1
    if simnao == 'N':
        break
print(f'Foram cadastradas {cont} pessoas.')
print(f'Dentre elas, possuem:')
print(f'{maior_idade} pessoas com mais de 18 anos;')
print(f'{homem} homens;')
print(f'{mulher} mulheres com menos de 20 anos.')
