print('='*30)
print(f'{"BANCO":^30}')
print('='*30)
valor = int(input('Digite o valor a ser sacado: R$'))
cinquenta = vinte = dez = um = 0

while valor >= 50:
    cinquenta += 1
    valor -= 50
while valor >= 20:
    vinte += 1
    valor -= 20
while valor >= 10:
    dez += 1
    valor -= 10
while valor >= 1:
    um += 1
    valor -= 1

valores = [cinquenta, vinte, dez, um]
contador = 0
for v in valores:
    contador += 1
    if contador == 1:
        reais = 50
    if contador == 2:
        reais = 20
    if contador == 3:
        reais = 10
    if contador == 4:
        reais = 1
    if v > 0:
        print(f'Total de {v} cédulas de R${reais}')
print('='*30)
print('Volte sempre ao Banco! Tenha um ótimo dia!')
