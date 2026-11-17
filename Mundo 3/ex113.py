def leiaInt(n):
    pronto = False
    while not pronto:
        try:
            numero = int(input(n))
        except (TypeError, ValueError):
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[1;31mO usuário preferiu não informar esse numero.\033[m')
            return 0
        else:
            pronto = True
            return numero

def leiaFloat(n):
    pronto = False
    while not pronto:
        try:
            numero = float(input(n))
        except (TypeError, ValueError):
            print('\033[1;31mERRO! Digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[1;31mO usuário preferiu não informar esse número.\033[m')
            return 0
        else:
            pronto = True
            return numero

int = leiaInt('Digite um número inteiro: ')
float = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {int} e o valor real foi {float}')