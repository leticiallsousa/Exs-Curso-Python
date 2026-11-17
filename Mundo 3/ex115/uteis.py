def cabeçalho(texto, center=False):
    print('-'*42)
    if center:
        print(str(texto).center(42))
    else:
        print(str(texto))
    print('-'*42)

def menu(lista):
    cabeçalho('MENU PRINCIPAL', True)
    global indice
    indice = 0
    for item in lista:
        indice += 1
        print(f'\033[33m{indice} - \033[m\033[34m{item}\033[m')
    print('-'*42)
    opc = leiaOpção('Sua opção: ')
    return opc

def leiaOpção(msg):
    opcao = input(f'\033[33m{msg}\033[m\033[32m')
    print('\033[m', end='')
    while True:
        try:
            if opcao.isdigit() and 1 <= int(opcao) <= indice:
                return int(opcao)
            else:
                print('\033[31mERRO! Digite uma opção válida!\033[m')
                opcao = input(f'\033[33m{msg}\033[m\033[32m')
                print('\033[m', end='')
        except (KeyboardInterrupt):
            print(f'\033[31mERRO! O usuário não informou uma opção\033[m')


def input_colorido(mensagem):
    entrada = input(f'{mensagem}\033[32m')
    print('\033[m', end='')
    return entrada

def cadastro():
    nome = input_colorido('Nome: ')
    while True:
        if not nome.split():
            print('\033[31mERRO! Você precisa digitar um nome!\033[m')
            nome = input_colorido('Nome: ')
            continue

        idade = input_colorido('Idade: ')
        try:
            if idade.isdigit():
                break
            else:
                print('\033[31mERRO! Digite uma opção válida!\033[m')
        except:
            print('\033[31mERRO! Digite uma opção válida!\033[m')
    pessoa = {'nome':nome, 'idade':idade+' anos'}
    return pessoa
    