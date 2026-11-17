def moeda(num):
    numero = f'{num:.2f}'.replace('.', ',')
    return numero


def aumentar(num, taxa):
    n = num+(num/100*taxa)
    return n


def diminuir(num, taxa):
    n = num-(num/100*taxa)
    return n

def dobro(num):
    num *= 2
    return num


def metade(num):
    num /= 2
    return num
