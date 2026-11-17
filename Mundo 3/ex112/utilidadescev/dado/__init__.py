def leiaDinheiro(msg):
    mensagem = input(msg)
    mensagem = mensagem.replace(',', '.')

    while True:
        if mensagem.count('.') <= 1 and mensagem.replace('.', '').isdigit():
            break
        else:
            print(f'\033[1;31mErro! "{mensagem}" é um preço inválido!\033[m')
            mensagem = input(msg)
    return float(mensagem)
