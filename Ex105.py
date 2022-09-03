def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos {aceita varis}
    :param sit: valor opcional indicando de deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = {}
    r['Total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


resp = notas(5.5, 9.5, sit=True)
print(resp)
help(notas)
