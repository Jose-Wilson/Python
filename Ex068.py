from random import randint
print('=-'*15)
print('{:^30}'.format('VAMOS JOGAR PAR OU ÍMPAR'))
print('=-'*15)
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total foi {jogador + computador}')
    print('-'*45)
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar Novamente...')
    print('-'*45)
print(f'GAME OVER! Você venceu {v} vezes.')
print('-'*45)
