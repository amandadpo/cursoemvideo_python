def notas(*n,sit=False):
    """
    Função para analisar notas e situações de vários alunos
    :param a: uma ou mais notas dos alunos (aceita várias)
    :param sit: parâmentro opcional, indicando se deve ou não mostrar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    notas_tot = {}
    notas_tot['Total'] = len(n)
    notas_tot['maior'] = max(n)
    notas_tot['menor'] = min(n)
    notas_tot['média'] = sum(n)/len(n)
    if sit == True:
        if notas_tot['média'] < 5:
            notas_tot['situação'] = 'RUIM'
        elif notas_tot['média'] > 7:
            notas_tot['situação'] = 'BOA'
        else:
            notas_tot['situação'] = 'REGULAR'

    return notas_tot


resp = notas(1,10,10,8,sit=True)
print(resp)
help(notas)