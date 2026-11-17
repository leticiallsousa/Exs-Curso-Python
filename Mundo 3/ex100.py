import random

numeros = list()

def sorteia():
    print('Sorteando 5 valores na lista:', end=' ')
    for s in range(0, 5):
        sorteado = random.randint(1, 10)
        numeros.append(sorteado)
        print(sorteado, end=' ')
    print('PRONTO!')


def soma():
    soma = 0
    for n in numeros:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {numeros}, temos {soma}')

sorteia()
soma()
# se criar um parâmetro de lista para cada uma das funções, usar ele ao invés da lista 
# "números" e só depois criar a lista números e colocar dentro do parênteses da função, vai
# ficar melhor, depois corrigir

