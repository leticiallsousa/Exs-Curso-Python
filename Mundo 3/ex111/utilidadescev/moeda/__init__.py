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
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-'*30)
    print(f"{'Preço analisado:':<20}", end='')
    print(f'R${preço}')
    print(f"{'Dobro do preço:':<20}", end='')
    print(f'R${dobro(preço)}')
    print(f"{'Metade do preço:':<20}", end='')
    print(f'R${metade(preço)}')
    print(f"{f'{aumento}% de aumento:':<20}", end='')
    print(f'R${aumentar(preço, aumento)}')
    print(f"{f'{redução}% de redução:':<20}", end='')
    print(f'R${diminuir(preço, redução)}')
    print(f'-'*30)

