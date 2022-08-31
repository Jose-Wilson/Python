from random import randint
from time import sleep


def sorteia(lista):
    print(f'Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        sleep(0.5)
        n = randint(1, 10)
        lista.append(n)
        print(f'\033[36m{n}   ', end='\033[m')
    print('PRONTO!')


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de \033[36m{lista}\033[m, temos \033[36m{soma}')


números = []
sorteia(números)
somapar(números)







