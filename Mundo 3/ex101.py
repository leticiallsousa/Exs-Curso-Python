import datetime
def voto(nasc):
    idade = datetime.date.today().year-nasc
    if 70 > idade >= 18:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    if 16 > idade:
        return f'Com {idade} anos: NÃO VOTA'
    else:
        return f'Com {idade} anos: VOTO OPCIONAL'

ano = int(input('Em que ano você nasceu? '))
print(voto(ano))