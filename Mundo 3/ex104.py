
def leiaInt(n=None):
    while not isinstance(n, int):
        numero = input(n)
        if numero.isdigit():
            n = int(numero)
            return n
        else:
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')