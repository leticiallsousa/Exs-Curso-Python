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
