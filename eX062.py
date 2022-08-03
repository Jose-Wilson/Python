print('Gerador de PA')
print('-='*10)
primeiro = int(input('Primeiro Termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} ->', end=' ')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input(f'Quantos termos voçê quer a mais? '))
print(f'Progreção finalizada com {total} termos mostrados.')


