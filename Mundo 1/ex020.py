import random

al1 = input('ALUNO 1: ')
al2 = input('ALUNO 2: ')
al3 = input('ALUNO 3: ')
al4 = input('ALUNO 4: ')
alunos = [al1, al2, al3, al4]
random.shuffle(alunos)
print(f'A ordem de apresentação será\n{alunos}')
