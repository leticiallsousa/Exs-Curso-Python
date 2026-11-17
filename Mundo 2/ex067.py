while True:
    print('-'*20)
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*20)
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c} = {num*c}')
print('PROGRAMA TABUADA ENCERRADO!')
