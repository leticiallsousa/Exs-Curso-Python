completo = list()

while True:
    aluno = list()
    notas = list()

    aluno.append(str(input('Nome: ')))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))

    aluno.append(notas)
    aluno.append(float((notas[0]+notas[1])/2))
    completo.append(aluno)

    continuar = None
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Deseja continuar? [S/N] ')).upper()
    if continuar == 'N':
        break

print('=-'*20)
print('Nº    Aluno               Média')
print('-'*40)

for aluno in range(0, len(completo)):
    print(f'{aluno:<6}{completo[aluno][0]:<20}{completo[aluno][2]}')

print('-'*40)

while True:
    n_individuais = int(input('Mostrar notas de qual aluno? '))
    if n_individuais == 999:
        print('FINALIZANDO...\nVOLTE SEMPRE!')
        break
    print(f'Notas de {completo[n_individuais][0]} são {completo[n_individuais][1]}')
    print('-'*40)
