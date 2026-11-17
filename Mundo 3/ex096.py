print('CONTROLE DE TERRENOS')
print('-'*30)


def area(largura, comprimento):
    area = largura*comprimento
    print(f'A área do terreno {largura}x{comprimento} é de {area}m².')


l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))

area(l, c)
