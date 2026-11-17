primeiro = int(input('Qual o primeiro termo da PA? '))
razao = int(input('Qual a razão da PA? '))
quant = 0
termos = 10
while termos != 0:
    while termos >= 1:
        print(primeiro, end=' ')
        primeiro += razao
        termos -= 1
        quant += 1
    termos = int(input('\nQuantos termos deseja mostrar a mais? '))
print(f'Processo finalizado com {quant} termos mostrados!')
