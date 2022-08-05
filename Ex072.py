cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
        'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
        'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
        'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    núm = int(input('Digite um número entre 0 e 20: '))
    print(f'Você digitou o número \033[36m{cont[núm]}\033[m')
    resp = ' '
    while resp not in 'SN':
        print('='*30)
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp not in 'SN':
            print('\033[31mResposta Incorreta! Tente novamente!\033[m')
    if resp == 'N':
        break




