import random
tabela = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR', 'Atlético-MG',
          'Fortaleza', 'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá',
          'Cuiabá', 'Ceará', 'Atlético-GO', 'Avaí', 'Juventude')
print('-'*30)
print(f'LISTA DOS TIMES BRASILEIRÃO: {tabela}')
print('-'*30)
print(f'CINCO PRIMEIROS COLOCADOS: {tabela[:5]}')
print('-'*30)
print(f'QUATRO ÚLTIMOS COLOCADOS: {tabela[-4:]}')
print('-'*30)
print(f'OS TIMES EM ORDEM ALFABÉTICA: {sorted(tabela)}')
print('-'*30)
print(f'O TIME DO BOTAFOGO FICOU EM {tabela.index("Botafogo")+1}º LUGAR NA CLASSIFICAÇÃO')
print('-'*30)
