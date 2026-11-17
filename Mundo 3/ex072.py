while True:

    extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
               'treze', 'quatorze', 'quinze', 'dezeseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
    numero = int(input('Digite um número entre 0 e 20: '))
    while 0 > numero or numero > 20:
        numero = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {extenso[numero]}')

    continuar = None
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Deseja continuar? [S/N] ')).upper()
    if continuar == 'N':
        break



