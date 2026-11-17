c = ('\033[m',        # sem cor
     '\033[0;37;41m', # vermelho
     '\033[0;37;42m', # verde
     '\033[0;37;43m', # amarelo
     '\033[0;37;44m', # azul
     '\033[0;37;45m', # roxo
     '\033[0;30;47m'  # branco
     )

def escreva(msg, cor=0):
    tamanho = len(msg)+8
    print(f'{c[cor]}', end='')
    print('~'*tamanho)
    print(f'{msg:^{tamanho}}')
    print('~'*tamanho)
    print(f'{c[0]}', end='')

def ajuda(com):
    escreva(f'Acessando o manual do comando "{com}"', 4)
    print(f'{c[6]}', end='')
    help(com)
    print(f'{c[0]}', end='')

while True:
    escreva('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input(f'Função ou Biblioteca > ')).lower()
    if comando == 'fim':
        escreva('ATÉ LOGO!', 1)
        break
    ajuda(comando)
