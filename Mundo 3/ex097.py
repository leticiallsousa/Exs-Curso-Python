def escreva(texto):
    tamanho = len(texto) + 8
    print('-'*tamanho)
    print(f'{texto:^{tamanho}}')
    print('-'*tamanho)


escreva('alô')
escreva('BOM DIA BOM DIA BOM DIA')
escreva('eu to viciada em pão de mel vegano alguém me ajuda socorro')
