def ficha(nome, gols=0):
    if nome.strip() == '':
        nome = '<desconhecido>'
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')
    
nome = str(input('Qual o nome do jogador? '))
gols = input('O jogador fez quantos gols? ')
ficha(nome, gols)
