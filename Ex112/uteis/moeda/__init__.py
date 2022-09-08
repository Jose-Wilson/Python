def metade(preço=0, formato=False):
    res = preço / 2
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if formato is False else moeda(res)


def aumento(preço=0, taxaa=0, formato=False):
    res = preço + (preço * taxaa / 100)
    return res if formato is False else moeda(res)


def redução(preço=0, taxar=0, formato=False):
    res = preço - (preço * taxar  / 100)
    return res if formato is False else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda:<3}{preço:.2f}'.replace('.', ',')


def resumo(preço=0, taxaa=0, taxar=0):
    print(f'-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'{taxaa}% de aumento: \t{aumento(preço, taxaa, True)}')
    print(f'{taxar}% de redução: \t{redução(preço, taxar, True)}')
    print('-' * 30)
