import uteis, os, json

while True:
    opcao = uteis.menu(['Ver pessoas cadastradas',
                        'Cadastrar nova pessoa',
                        'Sair do sistema'])

    if opcao == 1:
        uteis.cabeçalho('PESSOAS CADASTRADAS', True)
        caminho = r'C:\Users\Windows10\OneDrive\Área de Trabalho\Cursos\Curso em Vídeo - Python\Mundo 3\ex115\pessoas.json'
        if os.path.exists(caminho):
            # abre o arquivo como leitor e identifica o arquivo na variavel
            r5t4444444
                # looping para printar cada pessoa na lista
                for num, pessoa in enumerate(lista_pessoas):
                    print(f'{lista_pessoas[num]["nome"].ljust(30)}{lista_pessoas[num]["idade"]}')
        else:
            print('No momento, não há ninguém cadastrado.'.center(42))

    elif opcao == 2:
        uteis.cabeçalho('NOVO CADASTRO', True)
        caminho = r'C:\Users\Windows10\OneDrive\Área de Trabalho\Cursos\Curso em Vídeo - Python\Mundo 3\ex115\pessoas.json'
        if not os.path.exists(caminho):
            # cria o arquivo, abrindo como escritor e escrevendo nele
            with open(caminho, 'w') as arquivo_json:
                json.dump([], arquivo_json)

        pessoa = uteis.cadastro()
        # abre o arquivo como leitor e identifica o arquivo na variavel
        with open(caminho, 'r') as arquivo_json:
            lista_pessoas = json.load(arquivo_json)
        # Adiciona a pessoa na lista
        lista_pessoas.append(pessoa)
        # Escreve a lista atualizada no arquivo
        with open(caminho, 'w') as arquivo_json:
            json.dump(lista_pessoas, arquivo_json, indent=4)
        
        print(f'Novo registro de {pessoa["nome"]} adicionado.')
        
    elif opcao == 3:
        uteis.cabeçalho('Saindo do sistema... Até logo!', True)
        break
