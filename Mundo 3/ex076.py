produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso',
                  9.99, 'Mochila', 120.32, 'Caneta', 22.30, 'Livro', 34.90)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for listagem in range(0, len(produtos)):
    if listagem % 2 == 0:
        print(f'{produtos[listagem]:.<30}', end='')
    else:
        print(f'R${produtos[listagem]:>8.2f}')
print('-'*40)


# for listagem in range(0, len(produtos_tupla)):
#     produtos = str(produtos_tupla[listagem])
#     if listagem % 2 == 0:
#         print(produtos, end='')
#         print('R$'.rjust(32-len(produtos), '.'), end='')
#     else:
#         print(produtos.rjust(8))
# print('-'*40)
