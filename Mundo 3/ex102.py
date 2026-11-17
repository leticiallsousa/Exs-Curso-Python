def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número n.
    """
    print('-'*30)
    f = 1 
    for c in range(n, 0, -1):
        if show == True:
            print(f'{c} ', end='x ' if c>1 else '= ')
        f *= c
    return f


print(fatorial(5, True))
print(fatorial(6, False))
print(fatorial(3))

help(fatorial)
