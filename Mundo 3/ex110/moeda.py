def moeda(num, format=True):
    if not format:
        return
    num = f'{num:.2f}'.replace('.', ',')
    return num


def aumentar(num, taxa, format=True):
    n = num+(num/100*taxa)
    if format:
        n = f'{n:.2f}'.replace('.', ',')
    return n


def diminuir(num, taxa, format=True):
    n = num-(num/100*taxa)
    if format:
        n = f'{n:.2f}'.replace('.', ',')
    return n

def dobro(num, format=True):
    num *= 2
    if format:
        num = f'{num:.2f}'.replace('.', ',')
    return num


def metade(num, format=True):
    num /= 2
    if format:
        num = f'{num:.2f}'.replace('.', ',')
    return num


def resumo(preço, aumento, redução):
    print('-'*35)
    print('RESUMO DO VALOR'.center(30))
    print('-'*35)
#   print('Preço analisado:'.ljust(20), end=f'R${preço}\n')
#   print('Dobro do preço:'.ljust(20), end=f'R${dobro(preço)}\n')
#   print('Metade do preço:'.ljust(20), end=f'R${metade(preço)}')
#   print(f'{aumento}% de aumento:'.ljust(20), end=f'R${aumentar(preço, aumento)}')
#   print(f'{redução}% de redução:'.ljust(20), end=f'R${diminuir(preço, redução)}')
    print(f'Preço analisado: \tR${preço}')
    print(f'Dobro do preço: \tR${dobro(preço)}')
    print(f'Metade do preço: \tR${metade(preço)}')
    print(f'{aumento}% de aumento: \tR${aumentar(preço, aumento)}')
    print(f'{redução}% de redução: \tR${diminuir(preço, redução)}')
    
    print(f'-'*35)
