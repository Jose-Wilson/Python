from random import randint
from time import sleep
print('Suas Opções:')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')
jogador = int(input('Qual é a sua jogada? '))
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-='*15)
print(f'jogador jogou {itens[jogador]}')
print(f'O computador jogou {itens[computador]}')
print('-='*15)

if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('\033[31mJOGADA INVÁLIDA!\033[m')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('\033[31mJOGADA INVÁLIDA\033[m')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('\033[31mJOGADA INVÁLIDA\033[m')



