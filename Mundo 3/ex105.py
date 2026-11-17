def notas(*notas, sit=False):
    """
    -> Função para analisar nota e situação de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação .
    :return: dicionário com várias informações sobre a situação da turma.
    """
    infos = dict()
    infos['total'] = len(notas)
    infos['maior'] = media = 0
    infos['menor'] = 99999

    for n in notas:
        if n >  infos['maior']:
            infos['maior'] = n
        if n < infos['menor']:
            infos['menor'] = n
        media += n

    media /= len(notas)
    if sit == True:
        if media >= 7:
            infos['situação'] = 'BOA'
        if 7 > media > 5:
            infos['situação'] = 'RAZOÁVEL'
        else:
            infos['situação'] = 'RUIM'

    infos['media'] = media
    return infos


resp = notas(3, 6.2, 5, 9.21, 1, sit=True)
print(resp)
