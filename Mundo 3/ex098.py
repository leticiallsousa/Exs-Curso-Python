from time import sleep

def contador(inicio, fim, passo):
    print('=-'*30)
    print(f'Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}')
    if passo == 0:
        passo = 1
    for c in range(inicio, fim+1 if inicio < fim else fim-1, passo if inicio < fim or passo < 0 else -passo):
        sleep(0.5)
        print(c, end=' ')
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, -2)
print('=-'*30)
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input(f'{"Início: ":<8}'))
fim = int(input(f'{"Fim: ":<8}'))
passo = int(input(f'{"Passo: ":<8}'))
contador(inicio, fim, passo)
