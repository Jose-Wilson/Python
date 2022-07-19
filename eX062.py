print('Gerador de PA')
print('-='*10)
t = int(input('Primeiro Termo: '))
r = int(input('Razão da PA: '))
term = t
cont = 1
while mais != 0:
    while cont <= 10:
        print(f'{term} ->', end=' ')
        term += r
        cont += 1
    print('PAUSA')
    mais = int(input(f'Quantos termos vocÇe quer a mais? '))
print('FIM')


